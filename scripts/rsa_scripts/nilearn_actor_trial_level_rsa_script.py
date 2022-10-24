import numpy as np
import os
from nilearn.input_data import NiftiMasker
from nilearn import image
from nilearn.masking import apply_mask
import pandas
import glob
from scipy import stats
import re

'''
This script was written by Natalie Saragosa-Harris. It uses representational similarity analysis (RSA) to get correlations between actor-matched trials within a given region of the brain, in a participant's native space.

This script gets single trial, multivoxel estimates of BOLD signal within the a given region of interest.
It creates two csv files for each participant: one raw values csv and one correlation csv.

In the raw values csv, there should be a row for every trial (actor-emotion); should be 99 actors x 3 emotions = 297 trials.
It is essentially just a bunch of arrays saved as individual rows, with the format [Participant ID, trial (actor-emotion), actor, emotion, run, and then just a bunch of values (an array of voxel estimates)].
Because, for every participant, the exact same mask is applied to every trial, the voxels should be aligned, so each "column" across trials refers to the same voxel.

In the correlation csv, there should be a row for every actor. Each column should be the pair for the correlation.
Columns: Participant ID (same one just copied), Actor, AO_SUR_Corr, HO_SUR_Corr, HO_AO_Corr, Region, Hemisphere, Mask_Detail, Number_Voxels.
Rows: Each actor. So there should be 99 rows.
Then save each correlation in the correct column for that actor.
Here, I read in a template csv file that has these rows and columns but they are empty.
Could create within the script instead, but for ease I just have an empty one to use.

If you are creating masks from existing masks created using the Harvard Oxford atlas, set the 'detail' variable to indicate how the atlas was thresholded when making the mask in FSL and make sure this matches the format of your mask file names (e.g., 'Thr25', 'Thr50', etc.).

Example: amygdala_L_Thr50.nii.gz (region = 'amygdala', detail = 'Thr50', hemisphere = 'L').

Note: This script uses Python 3, so make sure that you are using Python 3 and have the correct libraries installed (see requirements.txt).

'''

# Function to mask data.
def setMasker(msk, smth):
    out = NiftiMasker(mask_img=msk, smoothing_fwhm=smth,
                      standardize=False, memory="nilearn_cache", memory_level=1)
    return (out)


# Template file has the list of all of the actors all of the participants should have seen.
templatepath = '/u/home/n/nsaragos/scripts/cts/rsa_python/template_rsa_file.csv'
studydir = '/u/project/silvers/data/CTS' # Where the data are saved.
outputdir = '/u/home/n/nsaragos/scripts/cts/rsa_python/correlations'

template = pandas.read_csv(templatepath, index_col="Actor")
actors = template.index.values

participants = ['P_001','P_002']
region = 'amygdala' # Input mask of interest here. Make sure it matches how your masks are saved (e.g., 'amy' for 'amygdala', etc.).
detail = 'Thr50' # Make sure this matches the format of your mask files (e.g., 'Thr50'; see earlier notes for more information).
hemisphere = 'L' # Usually, 'bilateral', 'R', or 'L'. If you want to make all three, change and run script for each separately.

'''
Loop 1: Go through every participant.
From their model folder, save the mask that only includes (1) the voxels from all three runs and (2) gray matter.
'''
for p in participants:
    print(p)
    pfile = template  # Start by using the empty template (with column and row names already specified) for their correlation file.
 # Save the participant ID, region, hemisphere, and threshold into their respective columns (values will be repeated in the column).
    pfile = pfile.assign(Participant_ID = p, Region = region, Hemisphere = hemisphere, Mask_Detail = detail)

    # The mask we are using here is the union of the three masks (one for each run),
    # specific to each participant. That is, it only includes voxels that were in all three run's masks.
    mask = glob.glob(f'{studydir}/{p}/model/masks/masks_from_conditionlevel_models/unsmoothed/allruns_{region}_{hemisphere}_{detail}_functional_GMONLY.nii.gz')
    # Create empty dataframe for their raw voxel values and another for their correlation values.
    # Need to give the dataframe column names for every voxel (for merging and appending purposes).
    # To do this, need to get the size of the mask, and then make that many columns.
    colnames = ['Participant_ID','Actor-Emotion', 'Actor', 'Emotion','Run']
    num_voxels = os.popen(f'fslstats {mask[0]} -V').read() # Get size of the mask (how many voxels) using fslstats.
    num_voxels = num_voxels.split(' ')[0] # Get value before the space (FSL prints as voxel, then space, then weird dimension thing that is not useful).
    num_voxels = int(num_voxels)
    pfile = pfile.assign(Number_Voxels = num_voxels) # Save the number of voxels to the file.
    # Create a column for every voxel (e.g., V1, V2, V3, etc.).
    voxel_columns = list(range(1,num_voxels+1))
    voxel_column_names = ["V" + str(x) for x in voxel_columns]
    colnames.extend(voxel_column_names) # Add these new column names.
    p_voxel_file = pandas.DataFrame(columns = colnames) # Create empty dataframe with these columns.

    # Using the file names, load the mask as an image.
    mask_image = image.load_img(mask)

    # It will give a warning because smoothing is set to 0, which is fine because we do not want to smooth in order to keep the small scale spatial information of each voxel.
    masker = setMasker(mask_image, 0) # Note: Could make this smoothing parameter a variable that is defined at the top of the script (and also included as a column in the csv file and in the title of the csv file) as well.


    '''
    Loop 2: Go through every actor. Go to each run and find the actor (should be once per run).
    To do this, find the three .feat directories that match the actor name.
    (if there are not exactly three, print an error message).
    Search the name of the file to figure out which run (1, 2, or 3) and emotion type it is (AO, HO, or SUR).
    Remember, each actor should appear once per run (three times total), with a different emotion each type.
    '''
    for act in actors:  # go through every row (corresponds to an actor).
        # act = 'HF10'
        print(f'Loading actor: {act}.')
        # There should be three trials (feat directories), all in different runs, that match this actor.
        trials = glob.glob(f'{studydir}/{p}/model/run*_lev1_lss-rsa_{act}*.feat/stats/zstat1.nii.gz')

        if len(trials) != 3: # Check that there are three trials.
            print("Error: This actor does not have three zstat trials.")
            continue

        # zstat1 should be the one to use for every trial.
        # I am looping through each run, which corresponds to each trial with that actor.
        allruns = ['run1','run2','run3']

        for run in allruns:
            curr_trial = glob.glob(f'{studydir}/{p}/model/{run}_lev1_lss-rsa_{act}*.feat/stats/zstat1.nii.gz')
            #print(f'Current trial: {curr_trial[0]}.')
            # Figure out what kind of trial we are on (get actor-emotion from file path).
            actor_emotion = (re.search('lss-rsa_(.*).feat',curr_trial[0])).group(1)
            print(f'Loading run: {run} ({actor_emotion}).')
            emotion = actor_emotion[5:] # All actor names are four characters long and followed by the '-' before the emotion.
            # Load in zstat image for each trial (within each run).
            curr_trial_img = image.load_img(curr_trial)

            # Using the masks created before with the masker function, transform the image to only
            # have the values within that mask.

            curr_trial_z = masker.fit_transform(curr_trial_img)
            
            # From https://nilearn.github.io/auto_examples/01_plotting/plot_visualization.html.
            masked_data = apply_mask(curr_trial_img, mask_image)
            # Look at the length of the array to make sure it matches the number of voxels for that participant's functional mask.
            #len(masked_data[0] 
            # It is a 2D array because this function applies the mask for each time point, but there is only one timepoint, so just index the 'first' (0th) array.
            # Save this list of values and relevant information to an array, and then it to their raw values dataframe.
            trial_list = [p, actor_emotion, act, emotion,run]
            trial_list.extend(masked_data[0])
            p_voxel_file.loc[len(p_voxel_file)] = trial_list

            # Now, we want to know what face type is in this trial.
            if emotion == 'SUR':
                SUR_face_z = curr_trial_z
            elif emotion == 'AO':
                AO_face_z = curr_trial_z
            elif emotion == 'HO':
                HO_face_z = curr_trial_z
            else:
                print("Error: Could not find any of the substrings.")

        # Now, for the current actor, there should be a surprised, angry, and happy face array (masks's z statistic values).
	# Based on Lila Davachi's slides, let's z score within the ROI to account for mean activation.
        AO_face_z_score = stats.zscore(AO_face_z[0,], ddof = 1)
        SUR_face_z_score= stats.zscore(SUR_face_z[0,], ddof = 1)  
        HO_face_z_score= stats.zscore(HO_face_z[0,], ddof = 1)

        AO_SUR_corr_zscore = np.corrcoef(AO_face_z_score, SUR_face_z_score)[0, 1]
        HO_SUR_corr_zscore = np.corrcoef(HO_face_z_score, SUR_face_z_score)[0, 1]
        AO_HO_corr_zscore =  np.corrcoef(AO_face_z_score, HO_face_z_score)[0, 1]

        # Find that actor's row, then add correlations to correct column in pfile.
        pfile.loc[act, "AO_SUR"] = AO_SUR_corr_zscore
        pfile.loc[act, "HO_SUR"] = HO_SUR_corr_zscore
        pfile.loc[act, "AO_HO"] = AO_HO_corr_zscore

    pfile.to_csv(f'{outputdir}/ROI_zscored_correlations/{p}_{region}_{hemisphere}_correlations_ROIzscored.csv')
    p_voxel_file.to_csv(f'{outputdir}/raw_voxel_values/{p}_raw_{region}_{hemisphere}_voxel_values.csv')
