#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Mon Nov 18 20:34:54 2019
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
expName = 'V1_Behavioral_FaceExperiment'  # from the Builder filename that created this script
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
    originPath=u'/Users/nataliesaragosaharris/Desktop/Ambiguous Faces Task/Behavioral Task/V1_Behavioral_FaceExperiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
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

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
textwelcome = visual.TextStim(win=win, name='textwelcome',
    text='In this task, you will be looking at faces.\n\nPress the spacebar to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions_1 = visual.TextStim(win=win, name='instructions_1',
    text='After each face, you will indicate whether the person in the picture FEELS GOOD or FEELS BAD.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instructions_2"
Instructions_2Clock = core.Clock()
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text="If you think the person FEELS GOOD, press '1'.\n\nIf you think the person FEELS BAD, press '0'.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instructions_3"
Instructions_3Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text="Make your response quickly, as soon as you see 'FEELS GOOD' and 'FEELS BAD' on the screen.\n\nYou will have 1 second to make your response.\n\nPress the spacebar to begin a practice round.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practicetrial"
practicetrialClock = core.Clock()
practiceimage = visual.ImageStim(
    win=win, name='practiceimage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "practiceresponse"
practiceresponseClock = core.Clock()
good_or_bad_rating_practice = visual.ImageStim(
    win=win, name='good_or_bad_rating_practice',
    image='Stimuli/good_or_bad.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.5,1.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "practice_timingfeedback"
practice_timingfeedbackClock = core.Clock()
#msg='blank message'#if this shows on the screen, we forgot to update the msg!
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ISI_2"
ISI_2Clock = core.Clock()
ISI_fixation = visual.TextStim(win=win, name='ISI_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instructions_4"
Instructions_4Clock = core.Clock()
afterpractice_text = visual.TextStim(win=win, name='afterpractice_text',
    text='You are done with the practice.\n\nYou will not get feedback on whether you responded quickly enough during the actual task.\n\nPress the spacebar when you are ready to begin.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ISI_NoResponse"
ISI_NoResponseClock = core.Clock()
ISI_NoResponse_Fixation = visual.TextStim(win=win, name='ISI_NoResponse_Fixation',
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
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "response"
responseClock = core.Clock()
good_or_bad_rating = visual.ImageStim(
    win=win, name='good_or_bad_rating',
    image='Stimuli/good_or_bad.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.5,1.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ISI_2"
ISI_2Clock = core.Clock()
ISI_fixation = visual.TextStim(win=win, name='ISI_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ISI_NoResponse"
ISI_NoResponseClock = core.Clock()
ISI_NoResponse_Fixation = visual.TextStim(win=win, name='ISI_NoResponse_Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='End of experiment.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
t = 0
WelcomeScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
wait_for_spacebar = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeScreenComponents = [textwelcome, wait_for_spacebar]
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textwelcome* updates
    if t >= 0.0 and textwelcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        textwelcome.tStart = t
        textwelcome.frameNStart = frameN  # exact frame index
        textwelcome.setAutoDraw(True)
    
    # *wait_for_spacebar* updates
    if t >= 0.0 and wait_for_spacebar.status == NOT_STARTED:
        # keep track of start time/frame for later
        wait_for_spacebar.tStart = t
        wait_for_spacebar.frameNStart = frameN  # exact frame index
        wait_for_spacebar.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(wait_for_spacebar.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if wait_for_spacebar.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            wait_for_spacebar.keys = theseKeys[-1]  # just the last key pressed
            wait_for_spacebar.rt = wait_for_spacebar.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if wait_for_spacebar.keys in ['', [], None]:  # No response was made
    wait_for_spacebar.keys=None
thisExp.addData('wait_for_spacebar.keys',wait_for_spacebar.keys)
if wait_for_spacebar.keys != None:  # we had a response
    thisExp.addData('wait_for_spacebar.rt', wait_for_spacebar.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
space_instructions_1 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [instructions_1, space_instructions_1]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_1* updates
    if t >= 0.0 and instructions_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_1.tStart = t
        instructions_1.frameNStart = frameN  # exact frame index
        instructions_1.setAutoDraw(True)
    
    # *space_instructions_1* updates
    if t >= 0.0 and space_instructions_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        space_instructions_1.tStart = t
        space_instructions_1.frameNStart = frameN  # exact frame index
        space_instructions_1.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(space_instructions_1.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if space_instructions_1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            space_instructions_1.keys = theseKeys[-1]  # just the last key pressed
            space_instructions_1.rt = space_instructions_1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_instructions_1.keys in ['', [], None]:  # No response was made
    space_instructions_1.keys=None
thisExp.addData('space_instructions_1.keys',space_instructions_1.keys)
if space_instructions_1.keys != None:  # we had a response
    thisExp.addData('space_instructions_1.rt', space_instructions_1.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_2"-------
t = 0
Instructions_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
spacebar_instructions_2 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_2Components = [instructions_2, spacebar_instructions_2]
for thisComponent in Instructions_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_2"-------
while continueRoutine:
    # get current time
    t = Instructions_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_2* updates
    if t >= 0.0 and instructions_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_2.tStart = t
        instructions_2.frameNStart = frameN  # exact frame index
        instructions_2.setAutoDraw(True)
    
    # *spacebar_instructions_2* updates
    if t >= 0.0 and spacebar_instructions_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        spacebar_instructions_2.tStart = t
        spacebar_instructions_2.frameNStart = frameN  # exact frame index
        spacebar_instructions_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spacebar_instructions_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if spacebar_instructions_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            spacebar_instructions_2.keys = theseKeys[-1]  # just the last key pressed
            spacebar_instructions_2.rt = spacebar_instructions_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_2"-------
for thisComponent in Instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if spacebar_instructions_2.keys in ['', [], None]:  # No response was made
    spacebar_instructions_2.keys=None
thisExp.addData('spacebar_instructions_2.keys',spacebar_instructions_2.keys)
if spacebar_instructions_2.keys != None:  # we had a response
    thisExp.addData('spacebar_instructions_2.rt', spacebar_instructions_2.rt)
thisExp.nextEntry()
# the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_3"-------
t = 0
Instructions_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
spacebar_instructions_3 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_3Components = [instructions_3, spacebar_instructions_3]
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_3"-------
while continueRoutine:
    # get current time
    t = Instructions_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_3* updates
    if t >= 0.0 and instructions_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_3.tStart = t
        instructions_3.frameNStart = frameN  # exact frame index
        instructions_3.setAutoDraw(True)
    
    # *spacebar_instructions_3* updates
    if t >= 0.0 and spacebar_instructions_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        spacebar_instructions_3.tStart = t
        spacebar_instructions_3.frameNStart = frameN  # exact frame index
        spacebar_instructions_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spacebar_instructions_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if spacebar_instructions_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            spacebar_instructions_3.keys = theseKeys[-1]  # just the last key pressed
            spacebar_instructions_3.rt = spacebar_instructions_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_3"-------
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if spacebar_instructions_3.keys in ['', [], None]:  # No response was made
    spacebar_instructions_3.keys=None
thisExp.addData('spacebar_instructions_3.keys',spacebar_instructions_3.keys)
if spacebar_instructions_3.keys != None:  # we had a response
    thisExp.addData('spacebar_instructions_3.rt', spacebar_instructions_3.rt)
thisExp.nextEntry()
# the Routine "Instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticeTrials.csv'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice.keys():
        exec(paramName + '= thisPractice.' + paramName)

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice.keys():
            exec(paramName + '= thisPractice.' + paramName)
    
    # ------Prepare to start Routine "practicetrial"-------
    t = 0
    practicetrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    practiceimage.setImage(PracticeImageFile)
    practice_good_or_bad_response_early = event.BuilderKeyResponse()
    # keep track of which components have finished
    practicetrialComponents = [practiceimage, practice_good_or_bad_response_early]
    for thisComponent in practicetrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practicetrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practicetrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practiceimage* updates
        if t >= 0.0 and practiceimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            practiceimage.tStart = t
            practiceimage.frameNStart = frameN  # exact frame index
            practiceimage.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practiceimage.status == STARTED and t >= frameRemains:
            practiceimage.setAutoDraw(False)
        
        # *practice_good_or_bad_response_early* updates
        if t >= 0.0 and practice_good_or_bad_response_early.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_good_or_bad_response_early.tStart = t
            practice_good_or_bad_response_early.frameNStart = frameN  # exact frame index
            practice_good_or_bad_response_early.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(practice_good_or_bad_response_early.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practice_good_or_bad_response_early.status == STARTED and t >= frameRemains:
            practice_good_or_bad_response_early.status = STOPPED
        if practice_good_or_bad_response_early.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '0'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practice_good_or_bad_response_early.keys = theseKeys[-1]  # just the last key pressed
                practice_good_or_bad_response_early.rt = practice_good_or_bad_response_early.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practicetrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practicetrial"-------
    for thisComponent in practicetrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if practice_good_or_bad_response_early.keys in ['', [], None]:  # No response was made
        practice_good_or_bad_response_early.keys=None
    practice.addData('practice_good_or_bad_response_early.keys',practice_good_or_bad_response_early.keys)
    if practice_good_or_bad_response_early.keys != None:  # we had a response
        practice.addData('practice_good_or_bad_response_early.rt', practice_good_or_bad_response_early.rt)
    
    # ------Prepare to start Routine "practiceresponse"-------
    t = 0
    practiceresponseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    practice_good_or_bad_response = event.BuilderKeyResponse()
    # keep track of which components have finished
    practiceresponseComponents = [good_or_bad_rating_practice, practice_good_or_bad_response]
    for thisComponent in practiceresponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practiceresponse"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceresponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *good_or_bad_rating_practice* updates
        if t >= 0.0 and good_or_bad_rating_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            good_or_bad_rating_practice.tStart = t
            good_or_bad_rating_practice.frameNStart = frameN  # exact frame index
            good_or_bad_rating_practice.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if good_or_bad_rating_practice.status == STARTED and t >= frameRemains:
            good_or_bad_rating_practice.setAutoDraw(False)
        
        # *practice_good_or_bad_response* updates
        if t >= 0.0 and practice_good_or_bad_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_good_or_bad_response.tStart = t
            practice_good_or_bad_response.frameNStart = frameN  # exact frame index
            practice_good_or_bad_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(practice_good_or_bad_response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practice_good_or_bad_response.status == STARTED and t >= frameRemains:
            practice_good_or_bad_response.status = STOPPED
        if practice_good_or_bad_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '0'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practice_good_or_bad_response.keys = theseKeys[-1]  # just the last key pressed
                practice_good_or_bad_response.rt = practice_good_or_bad_response.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceresponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceresponse"-------
    for thisComponent in practiceresponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if practice_good_or_bad_response.keys in ['', [], None]:  # No response was made
        practice_good_or_bad_response.keys=None
    practice.addData('practice_good_or_bad_response.keys',practice_good_or_bad_response.keys)
    if practice_good_or_bad_response.keys != None:  # we had a response
        practice.addData('practice_good_or_bad_response.rt', practice_good_or_bad_response.rt)
    
    # ------Prepare to start Routine "practice_timingfeedback"-------
    t = 0
    practice_timingfeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if not practice_good_or_bad_response.keys and not practice_good_or_bad_response_early.keys  :
        msg="Too slow!"
        
    else:
        msg=""
    feedback_text.setText(msg)
    # keep track of which components have finished
    practice_timingfeedbackComponents = [feedback_text]
    for thisComponent in practice_timingfeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice_timingfeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_timingfeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback_text* updates
        if t >= 0.0 and feedback_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_text.tStart = t
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_text.status == STARTED and t >= frameRemains:
            feedback_text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_timingfeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_timingfeedback"-------
    for thisComponent in practice_timingfeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "ISI_2"-------
    t = 0
    ISI_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISI_2Components = [ISI_fixation]
    for thisComponent in ISI_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISI_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_fixation* updates
        if t >= 0.0 and ISI_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_fixation.tStart = t
            ISI_fixation.frameNStart = frameN  # exact frame index
            ISI_fixation.setAutoDraw(True)
        frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISI_fixation.status == STARTED and t >= frameRemains:
            ISI_fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI_2"-------
    for thisComponent in ISI_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice'


# ------Prepare to start Routine "Instructions_4"-------
t = 0
Instructions_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_4Components = [afterpractice_text, key_resp_2]
for thisComponent in Instructions_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_4"-------
while continueRoutine:
    # get current time
    t = Instructions_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *afterpractice_text* updates
    if t >= 0.0 and afterpractice_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        afterpractice_text.tStart = t
        afterpractice_text.frameNStart = frameN  # exact frame index
        afterpractice_text.setAutoDraw(True)
    
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
        theseKeys = event.getKeys(keyList=['space'])
        
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
    for thisComponent in Instructions_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_4"-------
for thisComponent in Instructions_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Instructions_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ChooseBlock = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BlockFileList.csv'),
    seed=None, name='ChooseBlock')
thisExp.addLoop(ChooseBlock)  # add the loop to the experiment
thisChooseBlock = ChooseBlock.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChooseBlock.rgb)
if thisChooseBlock != None:
    for paramName in thisChooseBlock.keys():
        exec(paramName + '= thisChooseBlock.' + paramName)

for thisChooseBlock in ChooseBlock:
    currentLoop = ChooseBlock
    # abbreviate parameter names if possible (e.g. rgb = thisChooseBlock.rgb)
    if thisChooseBlock != None:
        for paramName in thisChooseBlock.keys():
            exec(paramName + '= thisChooseBlock.' + paramName)
    
    # ------Prepare to start Routine "ISI_NoResponse"-------
    t = 0
    ISI_NoResponseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISI_NoResponseComponents = [ISI_NoResponse_Fixation]
    for thisComponent in ISI_NoResponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI_NoResponse"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISI_NoResponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_NoResponse_Fixation* updates
        if t >= 0.0 and ISI_NoResponse_Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_NoResponse_Fixation.tStart = t
            ISI_NoResponse_Fixation.frameNStart = frameN  # exact frame index
            ISI_NoResponse_Fixation.setAutoDraw(True)
        frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISI_NoResponse_Fixation.status == STARTED and t >= frameRemains:
            ISI_NoResponse_Fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_NoResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI_NoResponse"-------
    for thisComponent in ISI_NoResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    facetrials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(BlockFileName),
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
        good_or_bad_response_early = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        facetrialComponents = [faceimage, good_or_bad_response_early]
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
            
            # *good_or_bad_response_early* updates
            if t >= 0.0 and good_or_bad_response_early.status == NOT_STARTED:
                # keep track of start time/frame for later
                good_or_bad_response_early.tStart = t
                good_or_bad_response_early.frameNStart = frameN  # exact frame index
                good_or_bad_response_early.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(good_or_bad_response_early.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if good_or_bad_response_early.status == STARTED and t >= frameRemains:
                good_or_bad_response_early.status = STOPPED
            if good_or_bad_response_early.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '0'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    good_or_bad_response_early.keys = theseKeys[-1]  # just the last key pressed
                    good_or_bad_response_early.rt = good_or_bad_response_early.clock.getTime()
            
            
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
        # check responses
        if good_or_bad_response_early.keys in ['', [], None]:  # No response was made
            good_or_bad_response_early.keys=None
        facetrials.addData('good_or_bad_response_early.keys',good_or_bad_response_early.keys)
        if good_or_bad_response_early.keys != None:  # we had a response
            facetrials.addData('good_or_bad_response_early.rt', good_or_bad_response_early.rt)
        for thisComponent in facetrialComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                    if good_or_bad_response_early.keys in ['', [], None]:  # No response was made
                        good_or_bad_response_early.keys=None
                        good_or_bad_response_early.rt=None
                        facetrials.addData('good_or_bad_response_early.rt', good_or_bad_response_early.rt)
                    facetrials.addData('good_or_bad_response_early.keys',good_or_bad_response_early.keys)
                    if good_or_bad_response_early.keys != None:  # we had a response
                        facetrials.addData('good_or_bad_response_early.rt', good_or_bad_response_early.rt)
        
        # ------Prepare to start Routine "response"-------
        t = 0
        responseClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        good_or_bad_response = event.BuilderKeyResponse()
        # keep track of which components have finished
        responseComponents = [good_or_bad_rating, good_or_bad_response]
        for thisComponent in responseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "response"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = responseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *good_or_bad_rating* updates
            if t >= 0.0 and good_or_bad_rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                good_or_bad_rating.tStart = t
                good_or_bad_rating.frameNStart = frameN  # exact frame index
                good_or_bad_rating.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if good_or_bad_rating.status == STARTED and t >= frameRemains:
                good_or_bad_rating.setAutoDraw(False)
            
            # *good_or_bad_response* updates
            if t >= 0.0 and good_or_bad_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                good_or_bad_response.tStart = t
                good_or_bad_response.frameNStart = frameN  # exact frame index
                good_or_bad_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(good_or_bad_response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if good_or_bad_response.status == STARTED and t >= frameRemains:
                good_or_bad_response.status = STOPPED
            if good_or_bad_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '0'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    good_or_bad_response.keys = theseKeys[-1]  # just the last key pressed
                    good_or_bad_response.rt = good_or_bad_response.clock.getTime()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response"-------
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if good_or_bad_response.keys in ['', [], None]:  # No response was made
            good_or_bad_response.keys=None
        facetrials.addData('good_or_bad_response.keys',good_or_bad_response.keys)
        if good_or_bad_response.keys != None:  # we had a response
            facetrials.addData('good_or_bad_response.rt', good_or_bad_response.rt)
        
        # ------Prepare to start Routine "ISI_2"-------
        t = 0
        ISI_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISI_2Components = [ISI_fixation]
        for thisComponent in ISI_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISI_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI_fixation* updates
            if t >= 0.0 and ISI_fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_fixation.tStart = t
                ISI_fixation.frameNStart = frameN  # exact frame index
                ISI_fixation.setAutoDraw(True)
            frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if ISI_fixation.status == STARTED and t >= frameRemains:
                ISI_fixation.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI_2"-------
        for thisComponent in ISI_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'facetrials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'ChooseBlock'


# ------Prepare to start Routine "ISI_NoResponse"-------
t = 0
ISI_NoResponseClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
ISI_NoResponseComponents = [ISI_NoResponse_Fixation]
for thisComponent in ISI_NoResponseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ISI_NoResponse"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_NoResponseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_NoResponse_Fixation* updates
    if t >= 0.0 and ISI_NoResponse_Fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_NoResponse_Fixation.tStart = t
        ISI_NoResponse_Fixation.frameNStart = frameN  # exact frame index
        ISI_NoResponse_Fixation.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ISI_NoResponse_Fixation.status == STARTED and t >= frameRemains:
        ISI_NoResponse_Fixation.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_NoResponseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_NoResponse"-------
for thisComponent in ISI_NoResponseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "EndScreen"-------
t = 0
EndScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [text]
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
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
