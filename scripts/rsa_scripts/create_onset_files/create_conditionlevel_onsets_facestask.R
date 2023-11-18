# Written by Natalie Saragosa-Harris.
# Last edited November 2019.
# This script creates onset files for each type of trial in the Faces MRI task.
# It saves four onset text files (one for each type of trial; angry, surprised, superimposed "ghost", and happy) for each run (so twelve total).

# Done to save as an FSL style three column onset file.
# Column One: Onset of trial.
# Column Two: Duration of trial. Will be 0.5 because trials are 500 ms long.
# If want to be super precise, can look at end of trial - beginning of trial. Otherwise, 0.5 is fine because that is what it should be.
# Column Three: Parametric modulator (will just be 1). Only change if you expect the activation to vary by some variable (e.g., for a reward task, if one block has $1 and the other has $100). Will probably not use in this case.

library(readr)
library(dplyr)
library(glue)

data_path <- ' ' # Path to where the  behavioral data for the MRI task (just button presses for attentional control) is saved.
setwd(data_path)
# All files in the folder; should be three text files (that start with P_) for each subject.
file_list <- intersect(list.files(data_path,pattern = "P_"), list.files(data_path,pattern = ".csv")) # This assumes the files are saved in one folder.
print("Files:")
print(file_list)
output_path <- '' # Where to save output files.

participant_list <- substr(file_list,1,5) # Participant ID part of the file names. This assumes the files are saved with participant ID (p_ followed by three numbers) at the beginning.
participant_list <- participant_list[!duplicated(participant_list)] # Get unique IDs (instead of listed three times for each person).

for (i in 1:length(participant_list)) {
  
  if(length(list.files(output_path,pattern = participant_list[i]))==12)next # For this participant, if the onset files already exist in data folder, go to next participant.
 
   inFiles <- intersect(list.files(data_path,pattern = participant_list[i]), list.files(data_path,pattern = ".csv")) # In data file, find this participant's files. There should be three of them.
 
   for (f in 1:length(inFiles)) { # This loop is each participant's file (should be three times).
     print(inFiles[f])
     current_data <- read_csv(inFiles[f])
 
      #attach(current_data)

      global_start <- current_data$GlobalTime_TriggerReceived[complete.cases(current_data$GlobalTime_TriggerReceived)] # Seconds since task started, when trigger is received (will work as the zero point).

      current_data <- current_data %>% mutate(TrialType = case_when(grepl('AO', ImageFile, ignore.case = T) ~ 'Angry',
                                              grepl('SUR', ImageFile, ignore.case = T) ~ 'Surprised',
                                              grepl('superimposed', ImageFile, ignore.case = T) ~ 'Ghost',
                                              grepl('HO', ImageFile, ignore.case = T) ~ 'Happy'))
      
      Angry = current_data %>% filter(TrialType == "Angry")
      Surprised = current_data %>% filter(TrialType == "Surprised")
      Ghost = current_data %>% filter(TrialType == "Ghost")
      Happy = current_data %>% filter(TrialType == "Happy")
      
      Angry_Start <-  Angry$Global_FaceStart[complete.cases(Angry$Global_FaceStart)]
      Surprised_Start <-  Surprised$Global_FaceStart[complete.cases(Surprised$Global_FaceStart)]
      Ghost_Start <- Ghost$Global_FaceStart[complete.cases(Ghost$Global_FaceStart)]
      Happy_Start<- Happy$Global_FaceStart[complete.cases(Happy$Global_FaceStart)]
      
      AngryOnsets = Angry_Start - global_start # Save the onset time relative to when the trigger from scanner was received.
      SurprisedOnsets = Surprised_Start - global_start
      GhostOnsets = Ghost_Start - global_start
      HappyOnsets = Happy_Start - global_start
      
      AngryFace_Events = cbind(AngryOnsets, c(rep(0.5, length(AngryOnsets))), c(rep(1, length(AngryOnsets)))) 
      SurprisedFace_Events = cbind(SurprisedOnsets, c(rep(0.5, length(SurprisedOnsets))), c(rep(1, length(SurprisedOnsets)))) 
      GhostFace_Events = cbind(GhostOnsets, c(rep(0.5, length(GhostOnsets))), c(rep(1, length(GhostOnsets))))
      HappyFace_Events = cbind(HappyOnsets, c(rep(0.5, length(HappyOnsets))), c(rep(1, length(HappyOnsets))))
      
      RunLetter = toString(substring(inFiles[f], regexpr("Run", inFiles[f])+3, regexpr("Run", inFiles[f])+3)) # Should be A, B, or C.
      
      setwd(output_path)
      
      angry_filename = glue('{participant_list[i]}_MRIFaces_Run{RunLetter}_Angry_events.txt')
      surprised_filename = glue('{participant_list[i]}_MRIFaces_Run{RunLetter}_Surprised_events.txt')
      ghost_filename= glue('{participant_list[i]}_MRIFaces_Run{RunLetter}_Ghost_events.txt')
      happy_filename= glue('{participant_list[i]}_MRIFaces_Run{RunLetter}_Happy_events.txt')
        
      write.table(AngryFace_Events, file = angry_filename, col.names = FALSE, row.names = FALSE)
      write.table(SurprisedFace_Events, file = surprised_filename, col.names = FALSE, row.names = FALSE)
      write.table(GhostFace_Events, file = ghost_filename, col.names = FALSE, row.names = FALSE)
      write.table(HappyFace_Events, file = happy_filename, col.names = FALSE, row.names = FALSE)
      
      setwd(data_path)
      #detach(current_data)
  }
  
}
