# Adapted from Natalie Saragosa-Harris's create_eventfiles_facestask.r script and Yael Waizman and Joao Guassi Moreira's SB_create_ev_files_all_MRI_tasks_Server_version script.
# Directory script adapted from Yael Waizman's SB_create_ev_files_all_MRI_tasks_Server_version.rmd script.
# Written by Natalie Saragosa-Harris.
# Last edited March 2020.

# This script saves a different text file for every trial (because every trial is unique and we are doing trial by trial estimates).
# Saves an FSL style three column onset file.
# Column One: Onset of trial.
# Column Two: Duration of trial.
# Duration should be 0.5. If want to be super precise, can look at end of trial - beginning of trial. Otherwise, 0.5 is fine because that is what it should be.
# Column Three: Parametric modulator (will just be 1). Only change if you expect the activation to vary by some variable (e.g., for a reward task, if one block has $1 and the other has $100). Will not use in this case.
# Each text file will only have one row (because it corresponds to a single trial). This is true except for the ghost (superimposed) images, which are shown a total of 27 times (9 times in each run).
# So every participant should have 300 total text files.
# This is 99 unique images per run (3 runs) = 297 unique trials + 3 text files with all of the ghost images in each run (should have 9 rows each).
# This is modeled separately for each run, which is why there are going to be 3 text files with the ghost images.

# The resulting text files will automatically be saved into the Scan_Session/Onsets/nsh_onsets.

require(readr)
require(dplyr)
require(tidyverse)

work_dir <- "/Volumes/Users/SANDLab"
#data_path <- "/Volumes/SANDlab/College_transition_study_(CTS)/Data/Behavioral_data/"
data_path <- paste(work_dir,"/College_transition_study_(CTS)/Data/Behavioral_data/", sep = "", collapse = NULL) # In this directory, there should be a folder for each participant.
setwd(data_path)
#path for those participants that participated in the lab session (all participants).
data_folders <- Sys.glob(paste(data_path,"CTS*/Scan_session/Raw",sep = "", collapse = NULL)) # Get list of folders in this directory.
#path for the data for the scan task.
data_files <- Sys.glob(paste(data_path,"CTS*/Scan_session/Raw/*Run*.csv",sep = "", collapse = NULL))  # Note this is defining "completed task" by "did they do any of the runs of the task"; will check that they did three in next section.
#path for participants that already have onset files created.
onsets_created <- Sys.glob(paste(data_path,"CTS*/Scan_session/Onsets/nsh_onsets",sep = "", collapse = NULL)) # Check if they have the folder that corresponds to this version of onsets (does not check if they have all 300 onset files, just the folder).
#create new dataframe that will have all of the participant IDs for people who completed the task.
subs_compl_task <- rep(NA, length(data_folders))
#create new dataframe that will have all of the participant IDs for people who already have onset files.
subs_compl_onsets <- rep(NA, length(onsets_created)) #Might be able to not use this if use the "next" command (later in script).

for (i in 1:length(data_folders)){   # Each folder should correspond to a unique participant.
  
  # Get participant's ID.
  current_folder <- data_folders[i]
  index <- str_locate(current_folder, "data/CTS") # Get their ID by looking for "CTS" (but had to do "data/CTS" so that it doesn't just go to whole CTS folder).
  begin <- index[1]
  end <- index[2]
  participant <- substr(current_folder,end-2,end+3) # Keep only the part of the string that has their ID (the last three characters in 'data/CTS' + three more characters).
  
  # First check if they have 300 total onset files.
  # If they do not, it is most likely zero (meaning they have no onset files.)
  onsets_files <- Sys.glob(paste(data_path, participant,"/Scan_session/Onsets/nsh_onsets/*_nsh.txt",sep = "", collapse = NULL)) 
  if(length(onsets_files)==300){ 
    # If so, add to both subs_compl_task and subs_compl_onsets and go to next person.
    subs_compl_onsets[i] <- participant
    subs_compl_task[i] <- participant
  }
  else{
    # If not, check if they have three runs (the three tasks). If they do, add to subs_compl_task. If not, skip to next person.
    run_files <- Sys.glob(paste(data_folders[i],"/*Run*.csv",sep = "", collapse = NULL))
    if(length(run_files)==3){ 
      # add to subs_compl_task.
      subs_compl_task[i] <- participant
    }else{
      #skip to next person because this participant probably has not done the MRI session yet.
      next
    } 
  }
}
# Now, there should be a final list of subjects who completed the task and a list of subjects who already have four onset files created.
# Find all of the subject IDs that are in the subs_compl_task dataframe but not in the subs_compl_onsets dataframe (all of the subject's that need to have onset files created).
participant_list <- subs_compl_task[!(subs_compl_task %in% subs_compl_onsets)]
# Remove NAs from subs_compl_task and subs_compl_onsets (so that it should only have people completed it).
participant_list <- na.omit(participant_list) 
participant_list <- participant_list[participant_list!="CTS026"] # Remove CTS026 because they have 288 onsets already (run 1 was shorter for them because the scan sequence was incorrect).


for (i in 1:length(participant_list)) {

  current_participant <- participant_list[i]
  output_path <- paste(data_path,current_participant, "/Scan_session/Onsets/nsh_onsets", sep = "", collapse = NULL) # Where to save the onset files.
  # If this folder does not exist yet, create it.
  if (!file.exists(output_path)){
    dir.create(output_path)}
  # From before, data_files has the list of all of the run files for all of the participants.
  # So look through data_files for this participant's file.
  inFiles <-grep(current_participant,data_files,value=TRUE) # There should be three files (one for each run).
  runIndex <- str_locate(inFiles[1], ".csv") # Get times for each run in order to create run order label; since all file names have same naming scheme, only need to use first file (the end of the file has the time stamp).
  runBegin <- runIndex[1]
  runEnd <- runIndex[2]
  runTimes <- substr(inFiles,runBegin-4,runEnd-4)
  runTimes <- sort(runTimes)
  
  
  for (f in 1:length(inFiles)) { # This loop is each subject's file (should be three times).
    
    print("Current participant:")
    print(current_participant)
    print("Current participant file:")
    print(inFiles[f])
    current_data <- read_csv(inFiles[f]) # load in data for a given run
    
    #attach(current_data) #attach the dataframe to make it easier to work with (but important to detach below!!)
    
    global_start <- current_data$GlobalTime_TriggerReceived[complete.cases(current_data$GlobalTime_TriggerReceived)] #Seconds since task started, when trigger is received (will work as the zero point).
    
    
    # Check to make sure this would do the same thing as what it has been doing:
    # Save the global_start time as before (using GlobalTime_TriggerReceived, which only has a single value).
    # Create a new data column in current_data, call it global_start_repeated, and save that value in that column (to repeat for every row).
    # Create another column (onset_time). In that, save Global_FaceStart - global_start_repeated to get onset time for every trial.
    current_data$global_start_repeated <- global_start
    current_data$onset_time <- current_data$Global_FaceStart - current_data$global_start_repeated
    
    
    conditions_list=split(current_data,current_data$ImageFile) # split dataframe based on TrialType.
    
    for(c in 1:length(conditions_list))  # There will be 100 dataframes; 99 unique faces + 1 superimposed ghost face, which is shown 9 times).
    {
      
      current_condition_file= as.data.frame(conditions_list[[c]]) 
      current_face_type <- unique(current_condition_file$ImageFile) # This should give you the image they saw on these trials.
      # If it's Null, do nothing and go to the next one.
      if(current_face_type != "NULL") # If it is any of the other ones, figure out what image type it is and create dataframe with the onset times.
      {
        # find the string in between "/Stimuli" and ".jpg"
        # For example, one is "Stimuli/AF01_HO.jpg" but another might be "Stimuli/superimposed.jpg", so cannot hard code the length of substring of interest.
        stimuli_position <- regexpr("Stimuli/", current_face_type) # Find position of "Stimuli/" in the image file name.
        substring_startpoint <- stimuli_position[1]+7 # Where "Stimuli/" ends (8 characters including first character) is where the image filename starts.
        
        jpg_position <- regexpr(".jpg", current_face_type) # Find position of ".jpg" in the image file name.
        substring_endpoint  <- jpg_position[1] # Where ".jpg" starts is where the image filename ends.
        
        image_type <- substr(current_face_type,substring_startpoint+1,substring_endpoint-1) # Get image type by extracting the AF01_HO (or whatever pattern) part of the image file name.
        # We will use "image_type" to now name the file.
        print(image_type) # This should print AF01_HO, superimposed, etc.
      } 
      
      
      current_event <- cbind(as.double(current_condition_file$onset_time), c(rep(.5, length(current_condition_file$onset_time))),c(rep(1, length(current_condition_file$onset_time))))
      # Define path where to put this.
      
      RunTime = substr(inFiles[f],str_locate(inFiles[f], ".csv")[1]-4,str_locate(inFiles[f], ".csv")[2]-4) #Get timestamp from file name.
      RunNum = which(runTimes == RunTime) #Compare filestamp from file name to that in runTimes vector from above to get run number.
      current_event_filepath <- paste(output_path, "/", current_participant,"_Run",RunNum,"_",image_type,"_events_nsh.txt",sep = "", collapse = NULL)
      
      
      write.table(current_event, current_event_filepath, col.names = FALSE, row.names = FALSE)
      #detach(current_data)
      setwd(data_path)
    }
  }
    
}
