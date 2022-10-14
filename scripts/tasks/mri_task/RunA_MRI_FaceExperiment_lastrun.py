#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on Tue Nov 19 18:20:04 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'RunA_MRI_FaceExperiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nataliesaragosa-harris/Desktop/Faces Task/MRI Task/RunA_MRI_FaceExperiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

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
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
from psychopy import core
globalClock = core.Clock()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_fixation_OneSecond = visual.TextStim(win=win, name='ISI_fixation_OneSecond',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "facetrial"
facetrialClock = core.Clock()
faceimage = visual.ImageStim(
    win=win,
    name='faceimage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
ghost_response = keyboard.Keyboard()

# Initialize components for Routine "FixationJitter"
FixationJitterClock = core.Clock()
ISI_Fixation_Jitter = visual.TextStim(win=win, name='ISI_Fixation_Jitter',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ghost_response_fixation = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_fixation_OneSecond = visual.TextStim(win=win, name='ISI_fixation_OneSecond',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
EndBlock_TenSecondScreen = visual.TextStim(win=win, name='EndBlock_TenSecondScreen',
    text='End of block.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Initialize"-------
# update component parameters for each repeat
# keep track of which components have finished
InitializeComponents = []
for thisComponent in InitializeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InitializeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Initialize"-------
while continueRoutine:
    # get current time
    t = InitializeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InitializeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitializeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
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
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
onset_triggerwait = globalClock.getTime()
thisExp.addData('WaitforTrigger_GlobalStartTime',onset_triggerwait)

thisExp.nextEntry()
# keep track of which components have finished
wait_for_trigger_2Components = [wait_for_trigger_text, key_resp_2]
for thisComponent in wait_for_trigger_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_for_trigger_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wait_for_trigger_2"-------
while continueRoutine:
    # get current time
    t = wait_for_trigger_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_for_trigger_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_for_trigger_text* updates
    if wait_for_trigger_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_for_trigger_text.frameNStart = frameN  # exact frame index
        wait_for_trigger_text.tStart = t  # local t and not account for scr refresh
        wait_for_trigger_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_for_trigger_text, 'tStartRefresh')  # time at next scr refresh
        wait_for_trigger_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_trigger_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_for_trigger_2"-------
for thisComponent in wait_for_trigger_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wait_for_trigger_text.started', wait_for_trigger_text.tStartRefresh)
thisExp.addData('wait_for_trigger_text.stopped', wait_for_trigger_text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
triggerreceived = globalClock.getTime()
thisExp.addData('GlobalTime_TriggerReceived',triggerreceived)

thisExp.nextEntry()
# the Routine "wait_for_trigger_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISI"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
onset_ISItime = globalClock.getTime()
thisExp.addData('FirstISI_GlobalStart',onset_ISItime)

#thisExp.nextEntry()
# keep track of which components have finished
ISIComponents = [ISI_fixation_OneSecond]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_fixation_OneSecond* updates
    if ISI_fixation_OneSecond.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_fixation_OneSecond.frameNStart = frameN  # exact frame index
        ISI_fixation_OneSecond.tStart = t  # local t and not account for scr refresh
        ISI_fixation_OneSecond.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_fixation_OneSecond, 'tStartRefresh')  # time at next scr refresh
        ISI_fixation_OneSecond.setAutoDraw(True)
    if ISI_fixation_OneSecond.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI_fixation_OneSecond.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            ISI_fixation_OneSecond.tStop = t  # not accounting for scr refresh
            ISI_fixation_OneSecond.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI_fixation_OneSecond, 'tStopRefresh')  # time at next scr refresh
            ISI_fixation_OneSecond.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_fixation_OneSecond.started', ISI_fixation_OneSecond.tStartRefresh)
thisExp.addData('ISI_fixation_OneSecond.stopped', ISI_fixation_OneSecond.tStopRefresh)

# set up handler to look after randomisation of conditions etc
facetrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('RunA_ConditionsFile.csv'),
    seed=None, name='facetrials')
thisExp.addLoop(facetrials)  # add the loop to the experiment
thisFacetrial = facetrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFacetrial.rgb)
if thisFacetrial != None:
    for paramName in thisFacetrial:
        exec('{} = thisFacetrial[paramName]'.format(paramName))

for thisFacetrial in facetrials:
    currentLoop = facetrials
    # abbreviate parameter names if possible (e.g. rgb = thisFacetrial.rgb)
    if thisFacetrial != None:
        for paramName in thisFacetrial:
            exec('{} = thisFacetrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "facetrial"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    trialstarttime = facetrialClock.getTime()
    facetrials.addData('WithinTrial_FaceStart',trialstarttime)
    
    
    global_onset = globalClock.getTime()
    thisExp.addData('Global_FaceStart', global_onset)
    
    #thisExp.nextEntry()
    faceimage.setImage(ImageFile)
    ghost_response.keys = []
    ghost_response.rt = []
    # keep track of which components have finished
    facetrialComponents = [faceimage, ghost_response]
    for thisComponent in facetrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    facetrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "facetrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = facetrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=facetrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *faceimage* updates
        if faceimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            faceimage.frameNStart = frameN  # exact frame index
            faceimage.tStart = t  # local t and not account for scr refresh
            faceimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(faceimage, 'tStartRefresh')  # time at next scr refresh
            faceimage.setAutoDraw(True)
        if faceimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > faceimage.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                faceimage.tStop = t  # not accounting for scr refresh
                faceimage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(faceimage, 'tStopRefresh')  # time at next scr refresh
                faceimage.setAutoDraw(False)
        
        # *ghost_response* updates
        waitOnFlip = False
        if ghost_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ghost_response.frameNStart = frameN  # exact frame index
            ghost_response.tStart = t  # local t and not account for scr refresh
            ghost_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ghost_response, 'tStartRefresh')  # time at next scr refresh
            ghost_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ghost_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ghost_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ghost_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ghost_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ghost_response.tStop = t  # not accounting for scr refresh
                ghost_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ghost_response, 'tStopRefresh')  # time at next scr refresh
                ghost_response.status = FINISHED
        if ghost_response.status == STARTED and not waitOnFlip:
            theseKeys = ghost_response.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                ghost_response.keys = theseKeys.name  # just the last key pressed
                ghost_response.rt = theseKeys.rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in facetrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "facetrial"-------
    for thisComponent in facetrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialendtime = facetrialClock.getTime()
    facetrials.addData('WithinTrial_FaceEnd',trialendtime)
    
    global_offset = globalClock.getTime()
    thisExp.addData('Global_FaceEnd', global_offset)
    
    #thisExp.nextEntry()
    facetrials.addData('faceimage.started', faceimage.tStartRefresh)
    facetrials.addData('faceimage.stopped', faceimage.tStopRefresh)
    # check responses
    if ghost_response.keys in ['', [], None]:  # No response was made
        ghost_response.keys = None
    facetrials.addData('ghost_response.keys',ghost_response.keys)
    if ghost_response.keys != None:  # we had a response
        facetrials.addData('ghost_response.rt', ghost_response.rt)
    facetrials.addData('ghost_response.started', ghost_response.tStartRefresh)
    facetrials.addData('ghost_response.stopped', ghost_response.tStopRefresh)
    
    # ------Prepare to start Routine "FixationJitter"-------
    # update component parameters for each repeat
    jitter_trialstarttime = FixationJitterClock.getTime()
    facetrials.addData('WithinTrial_FixationStart',jitter_trialstarttime)
    
    global_jitter_onset = globalClock.getTime()
    thisExp.addData('Global_FixationStart', global_jitter_onset)
    
    #thisExp.nextEntry()
    ghost_response_fixation.keys = []
    ghost_response_fixation.rt = []
    # keep track of which components have finished
    FixationJitterComponents = [ISI_Fixation_Jitter, ghost_response_fixation]
    for thisComponent in FixationJitterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationJitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "FixationJitter"-------
    while continueRoutine:
        # get current time
        t = FixationJitterClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationJitterClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_Fixation_Jitter* updates
        if ISI_Fixation_Jitter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_Fixation_Jitter.frameNStart = frameN  # exact frame index
            ISI_Fixation_Jitter.tStart = t  # local t and not account for scr refresh
            ISI_Fixation_Jitter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_Fixation_Jitter, 'tStartRefresh')  # time at next scr refresh
            ISI_Fixation_Jitter.setAutoDraw(True)
        if ISI_Fixation_Jitter.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_Fixation_Jitter.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                ISI_Fixation_Jitter.tStop = t  # not accounting for scr refresh
                ISI_Fixation_Jitter.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ISI_Fixation_Jitter, 'tStopRefresh')  # time at next scr refresh
                ISI_Fixation_Jitter.setAutoDraw(False)
        
        # *ghost_response_fixation* updates
        waitOnFlip = False
        if ghost_response_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ghost_response_fixation.frameNStart = frameN  # exact frame index
            ghost_response_fixation.tStart = t  # local t and not account for scr refresh
            ghost_response_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ghost_response_fixation, 'tStartRefresh')  # time at next scr refresh
            ghost_response_fixation.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ghost_response_fixation.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ghost_response_fixation.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ghost_response_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ghost_response_fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ghost_response_fixation.tStop = t  # not accounting for scr refresh
                ghost_response_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ghost_response_fixation, 'tStopRefresh')  # time at next scr refresh
                ghost_response_fixation.status = FINISHED
        if ghost_response_fixation.status == STARTED and not waitOnFlip:
            theseKeys = ghost_response_fixation.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                ghost_response_fixation.keys = theseKeys.name  # just the last key pressed
                ghost_response_fixation.rt = theseKeys.rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationJitterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationJitter"-------
    for thisComponent in FixationJitterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    jitter_trialendtime = FixationJitterClock.getTime()
    facetrials.addData('WithinTrial_FixationEnd',jitter_trialendtime)
    
    global_jitter_offset = globalClock.getTime()
    thisExp.addData('Global_FixationEnd', global_jitter_offset)
    
    #thisExp.nextEntry()
    facetrials.addData('ISI_Fixation_Jitter.started', ISI_Fixation_Jitter.tStartRefresh)
    facetrials.addData('ISI_Fixation_Jitter.stopped', ISI_Fixation_Jitter.tStopRefresh)
    # check responses
    if ghost_response_fixation.keys in ['', [], None]:  # No response was made
        ghost_response_fixation.keys = None
    facetrials.addData('ghost_response_fixation.keys',ghost_response_fixation.keys)
    if ghost_response_fixation.keys != None:  # we had a response
        facetrials.addData('ghost_response_fixation.rt', ghost_response_fixation.rt)
    facetrials.addData('ghost_response_fixation.started', ghost_response_fixation.tStartRefresh)
    facetrials.addData('ghost_response_fixation.stopped', ghost_response_fixation.tStopRefresh)
    # the Routine "FixationJitter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'facetrials'


# ------Prepare to start Routine "ISI"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
onset_ISItime = globalClock.getTime()
thisExp.addData('FirstISI_GlobalStart',onset_ISItime)

#thisExp.nextEntry()
# keep track of which components have finished
ISIComponents = [ISI_fixation_OneSecond]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_fixation_OneSecond* updates
    if ISI_fixation_OneSecond.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_fixation_OneSecond.frameNStart = frameN  # exact frame index
        ISI_fixation_OneSecond.tStart = t  # local t and not account for scr refresh
        ISI_fixation_OneSecond.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_fixation_OneSecond, 'tStartRefresh')  # time at next scr refresh
        ISI_fixation_OneSecond.setAutoDraw(True)
    if ISI_fixation_OneSecond.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI_fixation_OneSecond.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            ISI_fixation_OneSecond.tStop = t  # not accounting for scr refresh
            ISI_fixation_OneSecond.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI_fixation_OneSecond, 'tStopRefresh')  # time at next scr refresh
            ISI_fixation_OneSecond.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_fixation_OneSecond.started', ISI_fixation_OneSecond.tStartRefresh)
thisExp.addData('ISI_fixation_OneSecond.stopped', ISI_fixation_OneSecond.tStopRefresh)

# ------Prepare to start Routine "EndScreen"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [EndBlock_TenSecondScreen]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndBlock_TenSecondScreen* updates
    if EndBlock_TenSecondScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndBlock_TenSecondScreen.frameNStart = frameN  # exact frame index
        EndBlock_TenSecondScreen.tStart = t  # local t and not account for scr refresh
        EndBlock_TenSecondScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndBlock_TenSecondScreen, 'tStartRefresh')  # time at next scr refresh
        EndBlock_TenSecondScreen.setAutoDraw(True)
    if EndBlock_TenSecondScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndBlock_TenSecondScreen.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            EndBlock_TenSecondScreen.tStop = t  # not accounting for scr refresh
            EndBlock_TenSecondScreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(EndBlock_TenSecondScreen, 'tStopRefresh')  # time at next scr refresh
            EndBlock_TenSecondScreen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndBlock_TenSecondScreen.started', EndBlock_TenSecondScreen.tStartRefresh)
thisExp.addData('EndBlock_TenSecondScreen.stopped', EndBlock_TenSecondScreen.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
