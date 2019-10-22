#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on December 13, 2018, at 13:37
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
import psychopy.visual
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
from PIL import Image
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'lossaver_test'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
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
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "setup"
setupClock = core.Clock()
import psychopy.visual
import pandas as pd
from glob import glob
import numpy.random as nr
n_runs = 4
n_trials = 81

test_list = pd.read_csv('stimulus_lists/test_list.csv', header=None)[0].tolist()
nr.shuffle(test_list)
stim_opa = 0
trial_opa = 0
x_dim, y_dim = win.size
fix_size = (25/x_dim, 25/y_dim)

stim_size = (600/x_dim, 600/y_dim)

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
intro_text = visual.TextStim(win=win, name='intro_text',
    text='In the following task, you will be presented with images from the previous study session and new previously unseen images.\n\nYour task is to identify whether each image is old or new.\n\n                  1 = Old     2=Similar     3 = New\n\n',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=1200, ori=0,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0);



# Initialize components for Routine "begin_fix"
begin_fixClock = core.Clock()
begin_fix_dot = visual.Polygon(
    win=win, name='begin_fix_dot',
    edges=99, size=fix_size,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()

trial_image = visual.ImageStim(
    win=win, name='trial_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial_isi"
trial_isiClock = core.Clock()
trial_fix_poly = visual.Polygon(
    win=win, name='trial_fix_poly',
    edges=99, size=fix_size,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "end_fix"
end_fixClock = core.Clock()
end_fix_dot = visual.Polygon(
    win=win, name='end_fix_dot',
    edges=99, size=fix_size,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "setup"-------
t = 0
setupClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame


    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=n_runs, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun.keys():
        exec(paramName + '= thisRun.' + paramName)

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun.keys():
            exec(paramName + '= thisRun.' + paramName)

    # ------Prepare to start Routine "introduction"-------
    t = 0
    introductionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    intro_resp = event.BuilderKeyResponse()
    run_images = test_list[runs.thisN * 81: (runs.thisN + 1) * 81]
    # keep track of which components have finished
    introductionComponents = [intro_text, intro_resp]
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "introduction"-------
    while continueRoutine:
        # get current time
        t = introductionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *intro_text* updates
        if t >= 0.0 and intro_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_text.tStart = t
            intro_text.frameNStart = frameN  # exact frame index
            intro_text.setAutoDraw(True)

        # *intro_resp* updates
        if t >= 0.0 and intro_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_resp.tStart = t
            intro_resp.frameNStart = frameN  # exact frame index
            intro_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if intro_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False


        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "introduction"-------
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_clock = core.MonotonicClock()
    stim = ''
    # the Routine "introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "begin_fix"-------
    t = 0
    begin_fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    begin_fixComponents = [begin_fix_dot]
    for thisComponent in begin_fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "begin_fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = begin_fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *begin_fix_dot* updates
        if t >= 0.0 and begin_fix_dot.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin_fix_dot.tStart = t
            begin_fix_dot.frameNStart = frameN  # exact frame index
            begin_fix_dot.setAutoDraw(True)
        frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if begin_fix_dot.status == STARTED and t >= frameRemains:
            begin_fix_dot.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in begin_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "begin_fix"-------
    for thisComponent in begin_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=n_trials, method='sequential',
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)

    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)

        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        stim = run_images[trials.thisN]
        stim_x, stim_y = Image.open('stimuli/' + stim.split('\\')[-1]).size
        if stim_x > stim_y:
            stim_size = (800/x_dim, (800/ stim_x) * stim_y / y_dim)
        elif stim_x < stim_y:
            stim_size = ((800 / stim_y) * stim_x / x_dim, 800/y_dim)
        else:
            stim_size = (800/x_dim, 800/y_dim)
        trial_onset = trial_clock.getTime()
        trial_image.setImage('stimuli/' + stim.split('\\')[-1])
        trial_image.setSize(stim_size)
        trial_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [trial_image, trial_resp]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame


            # *trial_image* updates
            if t >= 0 and trial_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_image.tStart = t
                trial_image.frameNStart = frameN  # exact frame index
                trial_image.setAutoDraw(True)

            # *trial_resp* updates
            if t >= 0 and trial_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_resp.tStart = t
                trial_resp.frameNStart = frameN  # exact frame index
                trial_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if trial_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if trial_resp.keys == []:  # then this was the first keypress
                        trial_resp.keys = theseKeys[0]  # just the first key pressed
                        trial_resp.rt = trial_resp.clock.getTime()
                        # was this 'correct'?
                        if (trial_resp.keys == str('')) or (trial_resp.keys == ''):
                            trial_resp.corr = 1
                        else:
                            trial_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('trial_onset', trial_onset)
        trials.addData('stim_onset', trial_onset + 0.5)
        trials.addData('stim', stim)
        # check responses
        if trial_resp.keys in ['', [], None]:  # No response was made
            trial_resp.keys=None
            # was no response the correct answer?!
            if str('').lower() == 'none':
               trial_resp.corr = 1  # correct non-response
            else:
               trial_resp.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('trial_resp.keys',trial_resp.keys)
        trials.addData('trial_resp.corr', trial_resp.corr)
        if trial_resp.keys != None:  # we had a response
            trials.addData('trial_resp.rt', trial_resp.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # ------Prepare to start Routine "trial_isi"-------
        t = 0
        trial_isiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        trial_isiComponents = [trial_fix_poly]
        for thisComponent in trial_isiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "trial_isi"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_isiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *trial_fix_poly* updates
            if t >= 0.0 and trial_fix_poly.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_fix_poly.tStart = t
                trial_fix_poly.frameNStart = frameN  # exact frame index
                trial_fix_poly.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trial_fix_poly.status == STARTED and t >= frameRemains:
                trial_fix_poly.setAutoDraw(False)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial_isi"-------
        for thisComponent in trial_isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()

    # completed n_trials repeats of 'trials'


    # ------Prepare to start Routine "end_fix"-------
    t = 0
    end_fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    end_fixComponents = [end_fix_dot]
    for thisComponent in end_fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "end_fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *end_fix_dot* updates
        if t >= 0.0 and end_fix_dot.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_fix_dot.tStart = t
            end_fix_dot.frameNStart = frameN  # exact frame index
            end_fix_dot.setAutoDraw(True)
        frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if end_fix_dot.status == STARTED and t >= frameRemains:
            end_fix_dot.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "end_fix"-------
    for thisComponent in end_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed n_runs repeats of 'runs'




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
