#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on June 30, 2017, at 21:00
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
expName = 'lossaver_test_del'  # from the Builder filename that created this script
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
    originPath=u'F:\\Lossaver_Information\\lossaver\\lossaver_test_del.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In the following task, you will be presented with images from the previous study session and new previously unseen images.\n\nYour task is to identify whether each image is old or new.\n\n                  1 = Old                        2 = New\n\nWhen you identify an image as old, you will then be asked to \nidentify which side of the screen it was presented on.\n\n                  1 = Left                       2 = Right\n\nPress Return when you are ready to begin.',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=1200, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0);
import pandas as pd
from glob import glob
import numpy.random as nr
prev_data = pd.read_csv(glob('data/{}_lossaver_study_*.csv'.format(expInfo['participant']))[0])
prev_stimuli = prev_data['stimulus'].tolist()
prev_type = prev_data['trialtype'].tolist()
prev_side = prev_data['stimside']
prev_test = pd.read_csv(glob('data/{}_lossaver_test_imm_*.csv'.format(expInfo['participant']))[0])
prev_test_old = prev_test['stim_old'].tolist()
prev_test_old = [x for x in prev_test_old if x != 'None']
prev_test_new = prev_test['stim_new'].tolist()
prev_test_new = [x for x in prev_test_new if x != 'None']

for i, item in enumerate(prev_stimuli):
    if item in prev_test_old:
        prev_type[i] = 'del'

combo_del = zip(prev_type, prev_stimuli, prev_side)
combo_del = sorted(combo_del)

prev_type_del, prev_stim_del, prev_side_del = zip(*combo_del)
prev_type = prev_type_del[72:]
prev_stim = prev_stim_del[72:]
prev_side = prev_side_del[72:]

prev_loss = prev_stim[:48]
prev_loss_side = prev_side[:48]
combo_loss = sorted(zip(prev_loss_side, prev_loss))
_, prev_loss_list = zip(*combo_loss)
prev_loss_left = prev_loss_list[:24]
prev_loss_right = prev_loss_list[24:]

prev_neutral = prev_stim[48:96]
prev_neutral_side = prev_side[48:96]
combo_neutral = sorted(zip(prev_neutral_side, prev_neutral))
_, prev_neutral_list = zip(*combo_neutral)
prev_neutral_left = prev_neutral_list[:24]
prev_neutral_right = prev_neutral_list[24:]

prev_reward = prev_stim[96:]
prev_reward_side = prev_side[96:]
combo_reward = sorted(zip(prev_reward_side, prev_reward))
_, prev_reward_list = zip(*combo_reward)
prev_reward_left = prev_reward_list[:24]
prev_reward_right = prev_reward_list[24:]

new_list = sorted(glob('stimuli/new/*a.jpg'))
new_list = [x[-8:] for x in new_list]
for i, item in enumerate(new_list):
    if item in prev_test_new:
        new_list[i] = 'del'
    else:
        new_list[i] = 'stimuli/new/' + item
new_list = sorted(new_list)
new_list = new_list[72:]
new_list_rand = nr.permutation(new_list).tolist()
prev_loss_left = nr.permutation(prev_loss_left).tolist()
prev_loss_right = nr.permutation(prev_loss_right).tolist()
prev_neutral_left = nr.permutation(prev_neutral_left).tolist()
prev_neutral_right = nr.permutation(prev_neutral_right).tolist()
prev_reward_left = nr.permutation(prev_reward_left).tolist()
prev_reward_right = nr.permutation(prev_reward_right).tolist()

stim_dict = {}
type_dict = {}
side_dict = {}
for run in range(1, 4):
    stim_list = []
    type_list = []
    side_list = []
#Creates list of 48 old trials (16 of each type, 4 on each side)
    for i in range(8):
        stim_list.append('stimuli/' + prev_loss_left.pop())
        side_list.append('left')
        stim_list.append('stimuli/' + prev_loss_right.pop())
        side_list.append('right')
        type_list.extend(('loss', 'loss'))
        stim_list.append('stimuli/' + prev_neutral_left.pop())
        side_list.append('left')
        stim_list.append('stimuli/' + prev_neutral_right.pop())
        side_list.append('right')
        type_list.extend(('neutral', 'neutral'))
        stim_list.append('stimuli/' + prev_reward_left.pop())
        side_list.append('left')
        stim_list.append('stimuli/' + prev_reward_right.pop())
        side_list.append('right')
        type_list.extend(('reward', 'reward'))
        stim_list.extend((new_list_rand.pop(), 
                          new_list_rand.pop(), 
                          new_list_rand.pop(),
                          new_list_rand.pop(),
                          new_list_rand.pop(),
                          new_list_rand.pop()))
        type_list.extend(('new', 'new', 'new', 
                          'new','new', 'new'))
        side_list.extend(('new', 'new', 'new',
                          'new', 'new', 'new'))

    combo_stim_type = zip(stim_list, type_list, side_list)
    combo_stim_type = nr.permutation(combo_stim_type)
    stim_list_rand, type_list_rand, side_list_rand = zip(*combo_stim_type)
    stim_dict['{}'.format(run)] = stim_list_rand
    type_dict['{}'.format(run)] = type_list_rand
    side_dict['{}'.format(run)] = side_list_rand
stim_opa = 0
trial_opa = 0

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_image = visual.ImageStim(
    win=win, name='trial_image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(400, 400),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
color_1 = color_2 = 'white'
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
poly_left_trial = visual.Rect(
    win=win, name='poly_left_trial',units='pix', 
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(-250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
poly_right_trial = visual.Rect(
    win=win, name='poly_right_trial',units='pix', 
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
fixation_cue = visual.Polygon(
    win=win, name='fixation_cue',units='pix', 
    edges=90, size=(25, 25),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "trial_response"
trial_responseClock = core.Clock()
polygon_left = visual.Rect(
    win=win, name='polygon_left',units='pix', 
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(-250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon_right = visual.Rect(
    win=win, name='polygon_right',units='pix', 
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

resp_text = visual.TextStim(win=win, name='resp_text',
    text='\n\n          Left or Right?\n\n\n\n1 = Left                 2 = Right',
    font='Arial',
    units='pix', pos=(0, 0), height=1.0, wrapWidth=1200, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0);
resp_image = visual.ImageStim(
    win=win, name='resp_image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(400, 400),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "followup"
followupClock = core.Clock()
time_waste = visual.Polygon(
    win=win, name='time_waste',units='pix', 
    edges=90, size=(25,25),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

followup_text = visual.TextStim(win=win, name='followup_text',
    text='\n\n          Left or Right?\n\n\n\n1 = Left                 2 = Right',
    font='Arial',
    units='pix', pos=(0, 0), height=60, wrapWidth=1200, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
poly_left_followup = visual.Rect(
    win=win, name='poly_left_followup',units='pix', 
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(-250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
poly_right_followup = visual.Rect(
    win=win, name='poly_right_followup',units='pix', 
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "trial_response"
trial_responseClock = core.Clock()
polygon_left = visual.Rect(
    win=win, name='polygon_left',units='pix', 
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(-250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon_right = visual.Rect(
    win=win, name='polygon_right',units='pix', 
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

resp_text = visual.TextStim(win=win, name='resp_text',
    text='\n\n          Left or Right?\n\n\n\n1 = Left                 2 = Right',
    font='Arial',
    units='pix', pos=(0, 0), height=1.0, wrapWidth=1200, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0);
resp_image = visual.ImageStim(
    win=win, name='resp_image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(400, 400),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
t = 0
introductionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
intro_resp = event.BuilderKeyResponse()

# keep track of which components have finished
introductionComponents = [text, intro_resp]
for thisComponent in introductionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *intro_resp* updates
    if t >= 0.0 and intro_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_resp.tStart = t
        intro_resp.frameNStart = frameN  # exact frame index
        intro_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if intro_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
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

# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('runs_test.xlsx'),
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
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('test_trial_del.xlsx'),
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
        stim = stim_dict['{}'.format(run_index)][trial_index]
        
        if type_dict['{}'.format(run_index)][trial_index] in ['reward', 'loss', 'neutral']:
            stimans = 1
        else:
            stimans = 2
        trial_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [trial_image, ISI, trial_resp, poly_left_trial, poly_right_trial, fixation_cue]
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
            if t >= 0.5 and trial_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_image.tStart = t
                trial_image.frameNStart = frameN  # exact frame index
                trial_image.setAutoDraw(True)
            
            
            # *trial_resp* updates
            if t >= 0.5 and trial_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_resp.tStart = t
                trial_resp.frameNStart = frameN  # exact frame index
                trial_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if trial_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if trial_resp.keys == []:  # then this was the first keypress
                        trial_resp.keys = theseKeys[0]  # just the first key pressed
                        trial_resp.rt = trial_resp.clock.getTime()
                        # was this 'correct'?
                        if (trial_resp.keys == str(stimans)) or (trial_resp.keys == stimans):
                            trial_resp.corr = 1
                        else:
                            trial_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *poly_left_trial* updates
            if t >= 0.5 and poly_left_trial.status == NOT_STARTED:
                # keep track of start time/frame for later
                poly_left_trial.tStart = t
                poly_left_trial.frameNStart = frameN  # exact frame index
                poly_left_trial.setAutoDraw(True)
            if poly_left_trial.status == STARTED:  # only update if drawing
                poly_left_trial.setFillColor(color_1, log=False)
            
            # *poly_right_trial* updates
            if t >= 0.5 and poly_right_trial.status == NOT_STARTED:
                # keep track of start time/frame for later
                poly_right_trial.tStart = t
                poly_right_trial.frameNStart = frameN  # exact frame index
                poly_right_trial.setAutoDraw(True)
            if poly_right_trial.status == STARTED:  # only update if drawing
                poly_right_trial.setFillColor(color_2, log=False)
            
            # *fixation_cue* updates
            if t >= 0.0 and fixation_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_cue.tStart = t
                fixation_cue.frameNStart = frameN  # exact frame index
                fixation_cue.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_cue.status == STARTED and t >= frameRemains:
                fixation_cue.setAutoDraw(False)
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(0.5)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                # updating other components during *ISI*
                trial_image.setImage(stim)
                # component updates done
                ISI.complete()  # finish the static period
            
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
        type_response = ''
        followup_dur = 0
        follow_waste = 2.5
        color_1 = color_2 = 'white'
        
        corr_side = None
        if side_dict['{}'.format(run_index)][trial_index] == 'left':
            corr_side = 1
        elif side_dict['{}'.format(run_index)][trial_index] == 'right':
            corr_side = 2
        trials.addData('oldvsnew', type_response)
        if type_dict['{}'.format(run_index)][trial_index] != 'new':
            stim_old = stim[-8:]
            stim_new = None
        elif type_dict['{}'.format(run_index)][trial_index] == 'new':
            stim_new = stim[-8:]
            stim_old = None
        
        if len(trial_resp.keys) != 0:
            if int(trial_resp.keys[-1]) == 1:
                type_response = 'old'
                followup_dur = 15
                follow_waste = 0
                followup_ans = corr_side
            elif int(trial_resp.keys[-1]) == 2:
                type_response = 'new'
                followup_dur = 0
                follow_waste = 2.5
                followup_ans = None
        else:
            type_response = 'none'
            followup_dur = 2.5
        
        trials.addData('stim', stim)
        trials.addData('stim_old', stim_old)
        trials.addData('stim_new', stim_new)
        trials.addData('trial_type', type_dict['{}'.format(run_index)][trial_index])
        trials.addData('stim_side' , side_dict['{}'.format(run_index)][trial_index])
        
        if len(trial_resp.keys) != 0:
            # Save the corresponding box as which_box
            which_box = trial_resp.keys[0]
            # Execute the format function for the color fill of the selected box
            exec_run = True
            exec('color_{0} = "yellow"'.format(which_box))
        stim_opa = 1
        text_size = 1
        trial_resp_dur = 0.5
        # check responses
        if trial_resp.keys in ['', [], None]:  # No response was made
            trial_resp.keys=None
            # was no response the correct answer?!
            if str(stimans).lower() == 'none':
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
        
        # ------Prepare to start Routine "trial_response"-------
        t = 0
        trial_responseClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        polygon_left.setFillColor(color_1)
        polygon_right.setFillColor(color_2)
        
        
        resp_text.setHeight(text_size)
        resp_image.setOpacity(stim_opa)
        resp_image.setImage(stim)
        # keep track of which components have finished
        trial_responseComponents = [polygon_left, polygon_right, resp_text, resp_image]
        for thisComponent in trial_responseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial_response"-------
        while continueRoutine:
            # get current time
            t = trial_responseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_left* updates
            if t >= 0.0 and polygon_left.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_left.tStart = t
                polygon_left.frameNStart = frameN  # exact frame index
                polygon_left.setAutoDraw(True)
            frameRemains = 0.0 + trial_resp_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_left.status == STARTED and t >= frameRemains:
                polygon_left.setAutoDraw(False)
            
            # *polygon_right* updates
            if t >= 0.0 and polygon_right.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_right.tStart = t
                polygon_right.frameNStart = frameN  # exact frame index
                polygon_right.setAutoDraw(True)
            frameRemains = 0.0 + trial_resp_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_right.status == STARTED and t >= frameRemains:
                polygon_right.setAutoDraw(False)
            
            
            # *resp_text* updates
            if t >= 0.0 and resp_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_text.tStart = t
                resp_text.frameNStart = frameN  # exact frame index
                resp_text.setAutoDraw(True)
            frameRemains = 0.0 + trial_resp_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp_text.status == STARTED and t >= frameRemains:
                resp_text.setAutoDraw(False)
            
            # *resp_image* updates
            if t >= 0.0 and resp_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_image.tStart = t
                resp_image.frameNStart = frameN  # exact frame index
                resp_image.setAutoDraw(True)
            frameRemains = 0.0 + trial_resp_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp_image.status == STARTED and t >= frameRemains:
                resp_image.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_response"-------
        for thisComponent in trial_responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        color_1 = color_2 = 'white'
        # the Routine "trial_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "followup"-------
        t = 0
        followupClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        followup_resp = event.BuilderKeyResponse()
        poly_left_followup.setFillColor(color_1)
        poly_right_followup.setFillColor(color_2)
        # keep track of which components have finished
        followupComponents = [time_waste, followup_text, followup_resp, poly_left_followup, poly_right_followup]
        for thisComponent in followupComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "followup"-------
        while continueRoutine:
            # get current time
            t = followupClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *time_waste* updates
            if t >= 0.0 and time_waste.status == NOT_STARTED:
                # keep track of start time/frame for later
                time_waste.tStart = t
                time_waste.frameNStart = frameN  # exact frame index
                time_waste.setAutoDraw(True)
            frameRemains = 0.0 + follow_waste- win.monitorFramePeriod * 0.75  # most of one frame period left
            if time_waste.status == STARTED and t >= frameRemains:
                time_waste.setAutoDraw(False)
            
            
            # *followup_text* updates
            if t >= 0.0 and followup_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                followup_text.tStart = t
                followup_text.frameNStart = frameN  # exact frame index
                followup_text.setAutoDraw(True)
            frameRemains = 0.0 + followup_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if followup_text.status == STARTED and t >= frameRemains:
                followup_text.setAutoDraw(False)
            
            # *followup_resp* updates
            if t >= 0.0 and followup_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                followup_resp.tStart = t
                followup_resp.frameNStart = frameN  # exact frame index
                followup_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(followup_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + followup_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if followup_resp.status == STARTED and t >= frameRemains:
                followup_resp.status = STOPPED
            if followup_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if followup_resp.keys == []:  # then this was the first keypress
                        followup_resp.keys = theseKeys[0]  # just the first key pressed
                        followup_resp.rt = followup_resp.clock.getTime()
                        # was this 'correct'?
                        if (followup_resp.keys == str(followup_ans)) or (followup_resp.keys == followup_ans):
                            followup_resp.corr = 1
                        else:
                            followup_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *poly_left_followup* updates
            if t >= 0.0 and poly_left_followup.status == NOT_STARTED:
                # keep track of start time/frame for later
                poly_left_followup.tStart = t
                poly_left_followup.frameNStart = frameN  # exact frame index
                poly_left_followup.setAutoDraw(True)
            frameRemains = 0.0 + followup_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if poly_left_followup.status == STARTED and t >= frameRemains:
                poly_left_followup.setAutoDraw(False)
            
            # *poly_right_followup* updates
            if t >= 0.0 and poly_right_followup.status == NOT_STARTED:
                # keep track of start time/frame for later
                poly_right_followup.tStart = t
                poly_right_followup.frameNStart = frameN  # exact frame index
                poly_right_followup.setAutoDraw(True)
            frameRemains = 0.0 + followup_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if poly_right_followup.status == STARTED and t >= frameRemains:
                poly_right_followup.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in followupComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "followup"-------
        for thisComponent in followupComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        color_1 = color_2 = 'white'
        if followup_resp.corr == 1:
            corr_loc = 'correct'
        elif followup_resp.corr == 0:
            corr_loc = 'incorrect'
        trials.addData('corr_location', corr_loc)
        trial_resp_dur = 0.5
        if len(followup_resp.keys) != 0:
            # Save the corresponding box as which_box
            which_box = followup_resp.keys[0]
            # Execute the format function for the color fill of the selected box
            exec_run = True
            exec('color_{0} = "yellow"'.format(which_box))
            trial_resp_dur = 0.5
        elif len(followup_resp.keys) == 0:
            trial_resp_dur = 0
        stim_opa = 0
        text_size = 60 
        
        # check responses
        if followup_resp.keys in ['', [], None]:  # No response was made
            followup_resp.keys=None
            # was no response the correct answer?!
            if str(followup_ans).lower() == 'none':
               followup_resp.corr = 1  # correct non-response
            else:
               followup_resp.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('followup_resp.keys',followup_resp.keys)
        trials.addData('followup_resp.corr', followup_resp.corr)
        if followup_resp.keys != None:  # we had a response
            trials.addData('followup_resp.rt', followup_resp.rt)
        # the Routine "followup" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial_response"-------
        t = 0
        trial_responseClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        polygon_left.setFillColor(color_1)
        polygon_right.setFillColor(color_2)
        
        
        resp_text.setHeight(text_size)
        resp_image.setOpacity(stim_opa)
        resp_image.setImage(stim)
        # keep track of which components have finished
        trial_responseComponents = [polygon_left, polygon_right, resp_text, resp_image]
        for thisComponent in trial_responseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial_response"-------
        while continueRoutine:
            # get current time
            t = trial_responseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_left* updates
            if t >= 0.0 and polygon_left.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_left.tStart = t
                polygon_left.frameNStart = frameN  # exact frame index
                polygon_left.setAutoDraw(True)
            frameRemains = 0.0 + trial_resp_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_left.status == STARTED and t >= frameRemains:
                polygon_left.setAutoDraw(False)
            
            # *polygon_right* updates
            if t >= 0.0 and polygon_right.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_right.tStart = t
                polygon_right.frameNStart = frameN  # exact frame index
                polygon_right.setAutoDraw(True)
            frameRemains = 0.0 + trial_resp_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_right.status == STARTED and t >= frameRemains:
                polygon_right.setAutoDraw(False)
            
            
            # *resp_text* updates
            if t >= 0.0 and resp_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_text.tStart = t
                resp_text.frameNStart = frameN  # exact frame index
                resp_text.setAutoDraw(True)
            frameRemains = 0.0 + trial_resp_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp_text.status == STARTED and t >= frameRemains:
                resp_text.setAutoDraw(False)
            
            # *resp_image* updates
            if t >= 0.0 and resp_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_image.tStart = t
                resp_image.frameNStart = frameN  # exact frame index
                resp_image.setAutoDraw(True)
            frameRemains = 0.0 + trial_resp_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp_image.status == STARTED and t >= frameRemains:
                resp_image.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_response"-------
        for thisComponent in trial_responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        color_1 = color_2 = 'white'
        # the Routine "trial_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
# completed 1 repeats of 'runs'






# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
