# Adapted from Joao Guassi Moreira's create_ev_files_coinflip.r script.
# Directory script adapted from Yael Waizman's SB_create_ev_files_all_MRI_tasks_Server_version.rmd script.
# Written by Natalie Saragosa-Harris.
# Last edited November 2019.
# This script creates onset files for each type of trial in the Faces MRI task.
# It saves four onset text files (one for each type of trial; angry, surprised, superimposed "ghost", and happy) for each run (so twelve total).

# Done to save as an FSL style three column onset file.
# Column One: Onset of trial.
# Column Two: Duration of trial. Will be 0.5 because trials are 500 ms long.
  #If want to be super precise, can look at end of trial - beginning of trial. Otherwise, 0.5 is fine because that is what it should be.
# Column Three: Parametric modulator (will just be 1). Only change if you expect the activation to vary by some variable (e.g., for a reward task, if one block has $1 and the other has $100). Will probably not use in this case.

#The resulting text files will automatically be saved into the Scan Session/Onsets/ghost.

library(readr)
library(dplyr)

#Check if script is being run on a Mac or a PC.
if(Sys.info()["sysname"]== "Darwin"){
  work_dir <- "/Volumes/Users/SANDLab"
}else{
  work_dir <- "\\\\pythia.psych.ucla.edu/users/SANDLab"
}

data_path <- paste(work_dir,"/College_transition_study_(CTS)/Tasks/Scan Session/Faces Task/MRI Task/data", sep = "", collapse = NULL)
setwd(data_path)
# All files in the folder; should be three text files (that start with CTS) for each subject.
file_list <- intersect(list.files(data_path,pattern = "CTS"), list.files(data_path,pattern = ".csv"))
print("Files:")
print(file_list)
output_path <- paste(work_dir,"/College_transition_study_(CTS)/Tasks/Scan Session/Onsets/ghost", sep = "", collapse = NULL)

subj_list <- substr(file_list,1,6) # ID part of the file names.
subj_list <- subj_list[!duplicated(subj_list)] # Get unique IDs (instead of listed three times for each person).

for (i in 1:length(subj_list)) {
  
  if(length(list.files(output_path,pattern = subj_list[i]))==12)next # For this participant, if the onset files already exist in data folder, go to next participant.
 
   inFiles <- intersect(list.files(data_path,pattern = subj_list[i]), list.files(data_path,pattern = ".csv")) # In data file, find this participant's files. There should be three of them.
 
   for (f in 1:length(inFiles)) { # This loop is each subject's file (should be three times).
     print(inFiles[f])
     current_data <- read_csv(inFiles[f])
 
      attach(current_data)

      global_start <- current_data$GlobalTime_TriggerReceived[complete.cases(current_data$GlobalTime_TriggerReceived)] #Seconds since task started, when trigger is received (will work as the zero point).

      current_data$TrialType <- ifelse(grepl('AO', current_data$ImageFile, ignore.case = T), 'Angry',
                            ifelse(grepl('SUR', current_data$ImageFile, ignore.case = T), 'Surprised',
                                   ifelse(grepl('superimposed', current_data$ImageFile, ignore.case = T), 'Ghost',
                                   ifelse(grepl('HO',current_data$ImageFile, ignore.case = T),'Happy','None'))))

      conditions_list=split(current_data,current_data$TrialType)
      Angry = as.data.frame(conditions_list$Angry)
      Surprised = as.data.frame(conditions_list$Surprised)
      Ghost = as.data.frame(conditions_list$Ghost)
      Happy = as.data.frame(conditions_list$Happy)
      
      Angry_Start <-  Angry$Global_FaceStart[complete.cases(Angry$Global_FaceStart)]
      Surprised_Start <-  Surprised$Global_FaceStart[complete.cases(Surprised$Global_FaceStart)]
      Ghost_Start <- Ghost$Global_FaceStart[complete.cases(Ghost$Global_FaceStart)]
      Happy_Start<- Happy$Global_FaceStart[complete.cases(Happy$Global_FaceStart)]
      
      AngryOnsets = Angry_Start- global_start
      SurprisedOnsets = Surprised_Start - global_start
      GhostOnsets = Ghost_Start - global_start
      HappyOnsets = Happy_Start - global_start
      
      AngryFace_Events = cbind(AngryOnsets, c(rep(0.5, length(AngryOnsets))), c(rep(1, length(AngryOnsets)))) 
      SurprisedFace_Events = cbind(SurprisedOnsets, c(rep(0.5, length(SurprisedOnsets))), c(rep(1, length(SurprisedOnsets)))) 
      GhostFace_Events = cbind(GhostOnsets, c(rep(0.5, length(GhostOnsets))), c(rep(1, length(GhostOnsets))))
      HappyFace_Events = cbind(HappyOnsets, c(rep(0.5, length(HappyOnsets))), c(rep(1, length(HappyOnsets))))
      
      RunLetter = toString(substring(inFiles[f], regexpr("Run", inFiles[f])+3, regexpr("Run", inFiles[f])+3)) # Should be A, B, or C.
      
      setwd(output_path)
      
      angry_filename= paste(subj_list[i],"_",sprintf("MRIFaces_Run%s_Angry_events.txt",RunLetter),sep="")
      surprised_filename= paste(subj_list[i],"_",sprintf("MRIFaces_Run%s_Surprised_events.txt",RunLetter),sep="")
      ghost_filename= paste(subj_list[i],"_",sprintf("MRIFaces_Run%s_Ghost_events.txt",RunLetter),sep="")
      happy_filename= paste(subj_list[i],"_",sprintf("MRIFaces_Run%s_Happy_events.txt",RunLetter),sep="")
        
      write.table(AngryFace_Events, file=angry_filename, col.names = FALSE, row.names = FALSE)
      write.table(SurprisedFace_Events, file=surprised_filename, col.names = FALSE, row.names = FALSE)
      write.table(GhostFace_Events, file=ghost_filename, col.names = FALSE, row.names = FALSE)
      write.table(HappyFace_Events, file=happy_filename, col.names = FALSE, row.names = FALSE)
      
      setwd(data_path)
      detach(current_data)
  }
  
}
