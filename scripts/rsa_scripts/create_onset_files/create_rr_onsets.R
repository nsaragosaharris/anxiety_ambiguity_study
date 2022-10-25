# Written by JGM July 2020.
# Edited by NSH July 20, 2020.

# This script creates the "rr" (nuisance regressor) onset files for the LSS analysis.
# It assumes that every participant already has the 300 onset files (created by singletrial_onsets_nsh.r).
# Those 300 files correspond to single trials.

# In this script, we are creating the other regressors.
# For every trial (300 of them), there will be one file corresponding to that trial (already exists) and one text file that corresponds to the remaining trials (in the same run as that trial) of the same emotion type.
# The three other text files will be the rest of the images, organized by emotion type (happy, angry, surprised, and superimposed).
# The resulting text files will automatically be saved into the Scan_Session/Onsets/nsh_onsets.


library(filesstrings)


# Get paths to single trial onsets for those with imaging data.
work_dir <- "/Volumes/Users/SANDLab"
data_path <- paste(work_dir,"/College_transition_study_(CTS)/Data/Behavioral_data/", sep = "", collapse = NULL) # In this directory, there should be a folder for each participant.
setwd(data_path)
subs = Sys.glob(paste(data_path,"CTS*/Scan_session/Onsets/nsh_onsets",sep = "", collapse = NULL))

#subs = Sys.glob(file.path("P:", "College_transition_study_(CTS)", "Data", "Behavioral_data", "CTS*", "Scan_session", "Onsets", "nsh_onsets"))

# This takes a while (about thirty minutes per participant) so I would recommend only doing a small amount at a time.
for (i in 1:length(subs)) {
  sub = subs[i]  
  
  onset_files = Sys.glob(sprintf("%s/CTS*_events_nsh.txt", sub))  # Should be 300 of these.

  temp = strsplit(onset_files, "onsets/")
  mask = stringr::str_detect(unlist(temp), 'CTS[0-1][0-9][0-9]_Run') # Get all of the file names (without the directory in the title).
  filenames = unlist(temp)[mask]
  
  # First, go into "ghost" folder and copy over the files that have all of the trials organized by emotion type.
  # There will be one happy, one for angry, and one for surprised in each run.
  # Note that the one for superimposed faces already exists here so don't need to copy that over.
  participant = unlist(strsplit(sub, "/Scan_session"))[1] # Get participant ID.
  participant = substr(participant,str_length(participant)-5,str_length(participant))
  grouped_emotion_trials  = Sys.glob(paste(data_path,participant,"/Scan_session/Onsets/ghost/*.txt",sep = "", collapse = NULL))
  grouped_emotion_trials  = grouped_emotion_trials[stringr::str_detect(grouped_emotion_trials, "Ghost",negate=TRUE)] # Keep all except for superimposed (already exists).

  singletrial_path = paste(data_path,participant,"/Scan_session/Onsets/nsh_onsets",sep = "", collapse = NULL)
  file.copy(grouped_emotion_trials, singletrial_path)  
  # Rename and replace "MRIFaces" with "All" in the file name.
  copied_files = Sys.glob(paste(data_path,participant,"/Scan_session/Onsets/nsh_onsets/*MRIFaces*.txt",sep = "", collapse = NULL))
  sapply(copied_files,FUN=function(eachPath){
    file.rename(from=eachPath,to=sub(pattern="MRIFaces",replacement="All",eachPath))
  })
  
  
  # Now, for each single trial onset (already exists in this directory), create a corresponding "rr" file.
  # This "rr" file should have all of the onsets for the rest of the trials of that same emotion type in the same run.
  # So if we are looking at AF01_HO trial from run 1, we want to get all other HO (happy) trials from run 1 and save in one text file.
  
  for (f in 1:length(filenames)) {
    
    file = filenames[f]
    
    if ("superimposed" %in% unlist(strsplit(file, "_"))) {
      
      next
      
    } else {
      # Each file (except superimposed) is saved as [ParticipantID]_Run[RunNumber]_[Actor]_[Emotion]_events_nsh.txt.
      act_emo = unlist(strsplit(file, "_"))[3:4] # Separate each part of file name by splitting the string every time '_' appears; third and fourth parts of file name are actor and emotion).
      act_emo = paste(act_emo, collapse="_") # Put actor and emotion together.
      emotion = unlist(strsplit(file, "_"))[4] 
      subid = unlist(strsplit(file, "_"))[1] # Get participant ID.
      run = unlist(strsplit(file, "_"))[2] # Get run number.
      
      other_files = filenames[-f] # All other files that are not this one.
      other_files = other_files[stringr::str_detect(other_files, run)] # Only keep the ones from the same run  as this file (should be 99 files).
      other_files = other_files[stringr::str_detect(other_files, emotion)] # From that list, only keep the ones with the same emotion type as this file (should be 32 files).
      
      other_files_onsets = lapply(paste(sub, other_files, sep="/"), read.table) # Read in all the other files with the same emotion type from this run.
      other_files_onsets = do.call("rbind", other_files_onsets) # Put all of them into one file.
      other_files_onsets = other_files_onsets[order(other_files_onsets[,1]),] # Order them by onset time.
      other_files_onsets = unique(other_files_onsets[,c(1:3)])
      length(other_files_onsets$V1) # Should be 32.
      
      
      
     write.table(other_files_onsets, sprintf("%s/%s_%s_%s_events_%s_rr_nsh.txt", sub, subid, run, act_emo,emotion), row.names=FALSE, col.names = FALSE)
      
      
      # For each run, there should be 99 unique trial files + 99 corresponding "rr" files + 4 summary files (angry, happy, surprised, superimposed) = 202 files.
      # So in the folder, each participant should have 606 total files.
     
     
      # # We want to organize them by emotion type (angry, happy, surprised, or superimposed).
      # other_happy_files = other_files[stringr::str_detect(other_files, "HO")]
      # other_angry_files = other_files[stringr::str_detect(other_files, "AO")]
      # other_surprised_files = other_files[stringr::str_detect(other_files, "SUR")]
      # other_superimposed_files = other_files[stringr::str_detect(other_files, "superimposed")] # Note: if the trial type is "superimposed", this will be empty.
      # 
      # # Now put the directory back into the file names and read them in.
      # other_happy_files_onsets = lapply(paste(sub, other_happy_files, sep="/"), read.table)
      # other_happy_files_onsets = do.call("rbind", other_happy_files_onsets) # Put all of them into one file.
      # other_happy_files_onsets = other_happy_files_onsets[order(other_happy_files_onsets[,1]),] # Order them by onset time.
      # other_happy_files_onsets = unique(other_happy_files_onsets[,c(1:3)])
      # # length(other_happy_files_onsets$V1)

      
      
    }
    
  }
  
}

# Check to make sure each person now has 606 text files in their onset folder.
# Each person (except CTS026) should have 606; CTS026 has 582 because their first run was short.
for (j in 1:length(subs)) {
  
  sub = subs[j]
  total_onset_files = Sys.glob(sprintf("%s/CTS*.txt", sub))
  print(length(total_onset_files))
}
