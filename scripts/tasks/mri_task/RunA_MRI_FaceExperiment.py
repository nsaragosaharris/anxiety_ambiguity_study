#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v3.2.3),
    on November 15, 2019, at 16:38
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'RunA_MRI_FaceExperiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Initialize"
InitializeClock = core.Clock()
# In this script I use a csv file to define my variables as opposed to explicity defining them in my code. 
# I then use the participant's number and the session number to create personalized order files, in case that would be helpful

import csv
import random 

with open("RunA_Jitter.csv") as f:
    reader = csv.DictReader(f)
    jitters = [row["ISI_duration"] for row in reader]

participant_id = expInfo["participant"]
session_id = expInfo["session"]

random.shuffle(jitters)

# get image names and expressions
condition_input_file = "RunA_ConditionsInputFile.csv"
with open(condition_input_file) as f:
    reader = csv.DictReader(f)
    input_rows = [row["ImageFile"] for row in reader]

output_rows = [(input_row, jitter) for input_row, jitter in zip(input_rows, jitters)]

# write image names, expressions, and jitters
condition_output_file = "RunA_ConditionsFile.csv"
with open(condition_output_file, "w") as f:
    writer = csv.DictWriter(f, ["ImageFile", "jitter"])
    writer.writeheader()
    writer.writerows([{"ImageFile": output_row[0], "jitter": output_row[1]} for output_row in output_rows])

# Initialize components for Routine "wait_for_trigger_2"
wait_for_trigger_2Clock = core.Clock()
wait_for_trigger_text = visual.TextStim(win=win, name='wait_for_trigger_text',
    text='Get ready!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_fixation_OneSecond = visual.TextStim(win=win, name='ISI_fixation_OneSecond',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "facetrial"
facetrialClock = core.Clock()

faceimage = visual.ImageStim(
    win=win, name='faceimage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "FixationJitter"
FixationJitterClock = core.Clock()

ISI_Fixation_Jitter = visual.TextStim(win=win, name='ISI_Fixation_Jitter',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_fixation_OneSecond = visual.TextStim(win=win, name='ISI_fixation_OneSecond',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
EndBlock_TenSecondScreen = visual.TextStim(win=win, name='EndBlock_TenSecondScreen',
    text='End of block.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Initialize"-------
t = 0
InitializeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
InitializeComponents = []
for thisComponent in InitializeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Initialize"-------
while continueRoutine:
    # get current time
    t = InitializeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitializeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Initialize"-------
for thisComponent in InitializeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Initialize" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wait_for_trigger_2"-------
t = 0
wait_for_trigger_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
wait_for_trigger_2Components = [wait_for_trigger_text, key_resp_2]
for thisComponent in wait_for_trigger_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "wait_for_trigger_2"-------
while continueRoutine:
    # get current time
    t = wait_for_trigger_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_for_trigger_text* updates
    if t >= 0.0 and wait_for_trigger_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        wait_for_trigger_text.tStart = t
        wait_for_trigger_text.frameNStart = frameN  # exact frame index
        wait_for_trigger_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_trigger_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_for_trigger_2"-------
for thisComponent in wait_for_trigger_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "wait_for_trigger_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISI"-------
t = 0
ISIClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ISIComponents = [ISI_fixation_OneSecond]
for thisComponent in ISIComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_fixation_OneSecond* updates
    if t >= 0.0 and ISI_fixation_OneSecond.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_fixation_OneSecond.tStart = t
        ISI_fixation_OneSecond.frameNStart = frameN  # exact frame index
        ISI_fixation_OneSecond.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ISI_fixation_OneSecond.status == STARTED and t >= frameRemains:
        ISI_fixation_OneSecond.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
facetrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('RunA_ConditionsFile.csv'),
    seed=None, name='facetrials')
thisExp.addLoop(facetrials)  # add the loop to the experiment
thisFacetrial = facetrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFacetrial.rgb)
if thisFacetrial != None:
    for paramName in thisFacetrial.keys():
        exec(paramName + '= thisFacetrial.' + paramName)

for thisFacetrial in facetrials:
    currentLoop = facetrials
    # abbreviate parameter names if possible (e.g. rgb = thisFacetrial.rgb)
    if thisFacetrial != None:
        for paramName in thisFacetrial.keys():
            exec(paramName + '= thisFacetrial.' + paramName)
    
    # ------Prepare to start Routine "facetrial"-------
    t = 0
    facetrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    
    faceimage.setImage(ImageFile)
    ghost_response = event.BuilderKeyResponse()
    # keep track of which components have finished
    facetrialComponents = [faceimage, ghost_response]
    for thisComponent in facetrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "facetrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = facetrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *faceimage* updates
        if t >= 0.0 and faceimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            faceimage.tStart = t
            faceimage.frameNStart = frameN  # exact frame index
            faceimage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if faceimage.status == STARTED and t >= frameRemains:
            faceimage.setAutoDraw(False)
        
        # *ghost_response* updates
        if t >= 0.0 and ghost_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            ghost_response.tStart = t
            ghost_response.frameNStart = frameN  # exact frame index
            ghost_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(ghost_response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ghost_response.status == STARTED and t >= frameRemains:
            ghost_response.status = STOPPED
        if ghost_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                ghost_response.keys = theseKeys[-1]  # just the last key pressed
                ghost_response.rt = ghost_response.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in facetrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "facetrial"-------
    for thisComponent in facetrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialendtime = facetrialClock.getTime()
    facetrials.addData('FaceTrialStartTime',faceimage.tStart)
    facetrials.addData('FaceTrialEndTime',trialendtime)
    # check responses
    if ghost_response.keys in ['', [], None]:  # No response was made
        ghost_response.keys=None
    facetrials.addData('ghost_response.keys',ghost_response.keys)
    if ghost_response.keys != None:  # we had a response
        facetrials.addData('ghost_response.rt', ghost_response.rt)
    
    # ------Prepare to start Routine "FixationJitter"-------
    t = 0
    FixationJitterClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    ghost_response_fixation = event.BuilderKeyResponse()
    # keep track of which components have finished
    FixationJitterComponents = [ISI_Fixation_Jitter, ghost_response_fixation]
    for thisComponent in FixationJitterComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "FixationJitter"-------
    while continueRoutine:
        # get current time
        t = FixationJitterClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *ISI_Fixation_Jitter* updates
        if t >= 0.0 and ISI_Fixation_Jitter.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_Fixation_Jitter.tStart = t
            ISI_Fixation_Jitter.frameNStart = frameN  # exact frame index
            ISI_Fixation_Jitter.setAutoDraw(True)
        frameRemains = 0.0 + jitter- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISI_Fixation_Jitter.status == STARTED and t >= frameRemains:
            ISI_Fixation_Jitter.setAutoDraw(False)
        
        # *ghost_response_fixation* updates
        if t >= 0.0 and ghost_response_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            ghost_response_fixation.tStart = t
            ghost_response_fixation.frameNStart = frameN  # exact frame index
            ghost_response_fixation.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(ghost_response_fixation.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ghost_response_fixation.status == STARTED and t >= frameRemains:
            ghost_response_fixation.status = STOPPED
        if ghost_response_fixation.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                ghost_response_fixation.keys = theseKeys[-1]  # just the last key pressed
                ghost_response_fixation.rt = ghost_response_fixation.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationJitterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationJitter"-------
    for thisComponent in FixationJitterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if ghost_response_fixation.keys in ['', [], None]:  # No response was made
        ghost_response_fixation.keys=None
    facetrials.addData('ghost_response_fixation.keys',ghost_response_fixation.keys)
    if ghost_response_fixation.keys != None:  # we had a response
        facetrials.addData('ghost_response_fixation.rt', ghost_response_fixation.rt)
    # the Routine "FixationJitter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'facetrials'


# ------Prepare to start Routine "ISI"-------
t = 0
ISIClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ISIComponents = [ISI_fixation_OneSecond]
for thisComponent in ISIComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_fixation_OneSecond* updates
    if t >= 0.0 and ISI_fixation_OneSecond.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_fixation_OneSecond.tStart = t
        ISI_fixation_OneSecond.frameNStart = frameN  # exact frame index
        ISI_fixation_OneSecond.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ISI_fixation_OneSecond.status == STARTED and t >= frameRemains:
        ISI_fixation_OneSecond.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "EndScreen"-------
t = 0
EndScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [EndBlock_TenSecondScreen]
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndBlock_TenSecondScreen* updates
    if t >= 0.0 and EndBlock_TenSecondScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndBlock_TenSecondScreen.tStart = t
        EndBlock_TenSecondScreen.frameNStart = frameN  # exact frame index
        EndBlock_TenSecondScreen.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if EndBlock_TenSecondScreen.status == STARTED and t >= frameRemains:
        EndBlock_TenSecondScreen.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
