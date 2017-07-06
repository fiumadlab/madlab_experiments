#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on June 28, 2017, at 21:47
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
expName = 'lossaver_study'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'F:\\Lossaver_Information\\lossaver\\lossaver_study.psyexp',
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
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "cond_instr"
cond_instrClock = core.Clock()
instr_text = visual.TextStim(win=win, name='instr_text',
    text='In the following task, you will be presented with a cue followed by \nan image. If the cue was green, correctly identifying that image \nas indoor or outdoor will reward you with 50 cents. If the cue is red, \nfailing to correctly identify that image will cause you to lose 50 cents.\n\nWhen an object image is presented, your task is to classify that image as\nan indoor or outdoor object.\n\n                             1 = Indoor                  2 = Outdoor\n\nPress Return when you are ready to begin.',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=1200, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
import numpy as np
import os
import numpy.random as nr
from glob import glob
from copy import deepcopy
#Create randomized list of stimuli with their correct classification
stimbase = sorted(glob('stimuli/*a.jpg'))

stimclass = np.genfromtxt('stimclass.csv',
                           delimiter=',').tolist()
combo = zip(stimbase, stimclass)

combo = nr.permutation(combo).tolist()
stimbase_rand, stimclass_rand = zip(*combo)
stimbase_rand = list(stimbase_rand)
stimclass_rand = list(stimclass_rand)
#Creates dictionary for each variable
stim_dict = {}
corr_dict = {}
trial_dict = {}
side_dict = {}
amt_dict = {}
isi_dict = {}
fisi_dict = {}
for run in range(1,5):
    #Create stimulus and classification list
    stim_list = []
    class_list = []
    for i in range(54):
        stim_list.append(stimbase_rand.pop())
        class_list.append(stimclass_rand.pop())
    stim_dict['{}'.format(run)] = stim_list
    corr_dict['{}'.format(run)] = class_list
    #Create Trial Type List
    flatten = lambda l: [item for sublist in l for item in sublist]
    list_tuple = (1,1)
    reward_loss_list = []
    rew_list = []
    loss_list = []
    neu_list = []
    for i in range(9):
        rew_list.append(1)
        loss_list.append(2)
        neu_list.append(3)
    reward_loss_list = deepcopy(rew_list) + deepcopy(loss_list) + deepcopy(neu_list)
    trial_type_list = []
    for item in reward_loss_list:
        new_item = np.array(list_tuple) * item
        trial_type_list.append(new_item.tolist())
    trial_type_list = nr.permutation(trial_type_list)
    trial_type_list = flatten(trial_type_list)    
    #Creates list of side to present on
    side_seed_dict = {}
    side_seed_list = np.ones(9).tolist() + (np.ones(9) * 2).tolist()
    for i, item in enumerate(side_seed_list):
        if item == 1:
            side_seed_list[i] = 'left'
        elif item ==2: 
            side_seed_list[i] = 'right'
    side_seed_dict['1'] = nr.permutation(deepcopy(side_seed_list)).tolist()
    side_seed_dict['2'] = nr.permutation(deepcopy(side_seed_list)).tolist()
    side_seed_dict['3'] = nr.permutation(deepcopy(side_seed_list)).tolist()
    side_list = []
    for item in trial_type_list:
        side_list.append(side_seed_dict['{}'.format(item)].pop())
    side_dict['{}'.format(run)] = side_list
    #Creates List of awarded amounts
    amt_seed_dict = {}
    amt_seed_list = (np.ones(9) * 0.50).tolist()
    amt_seed_dict['1_left'] = nr.permutation(deepcopy(amt_seed_list)).tolist()
    amt_seed_dict['1_right'] = nr.permutation(deepcopy(amt_seed_list)).tolist()
    amt_seed_dict['2_left'] = nr.permutation(deepcopy(amt_seed_list)).tolist()
    amt_seed_dict['2_right'] = nr.permutation(deepcopy(amt_seed_list)).tolist()
    amt_seed_dict['3_left'] = np.zeros(9).tolist()
    amt_seed_dict['3_right'] = np.zeros(9).tolist()
    amt_list = []
    for i, item in enumerate(trial_type_list):
        if side_list[i] == 'left':
            amt_list.append(amt_seed_dict['{}_{}'.format(item, side_list[i])].pop())
        elif side_list[i] == 'right':
            amt_list.append(amt_seed_dict['{}_{}'.format(item, side_list[i])].pop())
    amt_dict['{}'.format(run)] = amt_list
    for i, item in enumerate(trial_type_list):
        if item == 1:
            trial_type_list[i] = 'reward'
        elif item == 2:
            trial_type_list[i] = 'loss'
        elif item == 3:
            trial_type_list[i] = 'neutral'
    trial_dict['{}'.format(run)] = trial_type_list
    #creates list of interstimulus durations
    isi_list = []
    fisi_list = []
    for i in range(18):
        isi_list.extend((4,5,6))
    isi_list = nr.permutation(isi_list).tolist()
    fisi_list = nr.permutation(isi_list).tolist()
    isi_dict['{}'.format(run)] = isi_list
    fisi_dict['{}'.format(run)] = fisi_list
earn_amt = 10.00
earn_txt = format(earn_amt, '.2f')

# Initialize components for Routine "cue"
cueClock = core.Clock()
cue_box = visual.Rect(
    win=win, name='cue_box',units='pix', 
    width=(420, 420)[0], height=(420, 420)[1],
    ori=0, pos=[0,0],
    lineWidth=40, lineColor=1.0, lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
cuecolor = 'grey'
cueamt = None
cuepres = None
cuepos = ''


fixation_cue = visual.Polygon(
    win=win, name='fixation_cue',units='pix', 
    edges=90, size=(25, 25),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
cue_money_count = visual.TextStim(win=win, name='cue_money_count',
    text='default text',
    font='Arial',
    pos=(0, -300), height=60, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "intercue"
intercueClock = core.Clock()
fixation_intercue = visual.Polygon(
    win=win, name='fixation_intercue',units='pix', 
    edges=90, size=(25, 25),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
intercue_money_amt = visual.TextStim(win=win, name='intercue_money_amt',
    text='default text',
    font='Arial',
    pos=(0, -300), height=60, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
from random import choice
color_1 = color_2 = 'white'
polyopa_1 = polyopa_2 = 0
stimans = ''

poly_left = visual.Rect(
    win=win, name='poly_left',
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(-250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
poly_right = visual.Rect(
    win=win, name='poly_right',
    width=(100, 100)[0], height=(100, 100)[1],
    ori=0, pos=(250, -300),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
cue_box_trial = visual.Rect(
    win=win, name='cue_box_trial',units='pix', 
    width=(420, 420)[0], height=(420, 420)[1],
    ori=0, pos=[0,0],
    lineWidth=40, lineColor=1.0, lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
stimulus_image = visual.ImageStim(
    win=win, name='stimulus_image',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(400, 400),
    color=1.0, colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trial_money_amt = visual.TextStim(win=win, name='trial_money_amt',
    text='default text',
    font='Arial',
    pos=(0, -300), height=60, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=60, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
feedback_money_count = visual.TextStim(win=win, name='feedback_money_count',
    text='default text',
    font='Arial',
    pos=(0, -300), height=60, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
run = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('runs_study.xlsx'),
    seed=None, name='run')
thisExp.addLoop(run)  # add the loop to the experiment
thisRun = run.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun.keys():
        exec(paramName + '= thisRun.' + paramName)

for thisRun in run:
    currentLoop = run
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun.keys():
            exec(paramName + '= thisRun.' + paramName)
    
    # ------Prepare to start Routine "cond_instr"-------
    t = 0
    cond_instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3 = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    cond_instrComponents = [instr_text, key_resp_3]
    for thisComponent in cond_instrComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cond_instr"-------
    while continueRoutine:
        # get current time
        t = cond_instrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_text* updates
        if t >= 0.0 and instr_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr_text.tStart = t
            instr_text.frameNStart = frameN  # exact frame index
            instr_text.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
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
        for thisComponent in cond_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cond_instr"-------
    for thisComponent in cond_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_clock = core.MonotonicClock()
    
    # the Routine "cond_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials_study.xlsx'),
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
        
        # ------Prepare to start Routine "cue"-------
        t = 0
        cueClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        trial_id = '{}'.format(run_index)
        stim = stim_dict[trial_id][trial_index]
        stimans = int(float(corr_dict[trial_id][trial_index]))
        trial_type = trial_dict[trial_id][trial_index]
        if trial_type == 'neutral':
            cuecolor = 'grey'
        elif trial_type == 'reward':
            cuecolor = 'green'
        elif trial_type == 'loss':
            cuecolor = 'red'
        if side_dict[trial_id][trial_index] == 'left':
            cuepos = -300
        elif side_dict[trial_id][trial_index] == 'right':
            cuepos = 300
        
        rew_amt = amt_dict[trial_id][trial_index]
        isidur = isi_dict[trial_id][trial_index]
        fisidur = fisi_dict[trial_id][trial_index]
        cue_money_count.setText(earn_txt
)
        # keep track of which components have finished
        cueComponents = [cue_box, ISI, fixation_cue, cue_money_count]
        for thisComponent in cueComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cue"-------
        while continueRoutine:
            # get current time
            t = cueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cue_box* updates
            if t >= fisidur and cue_box.status == NOT_STARTED:
                # keep track of start time/frame for later
                cue_box.tStart = t
                cue_box.frameNStart = frameN  # exact frame index
                cue_box.setAutoDraw(True)
            frameRemains = fisidur + .500- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cue_box.status == STARTED and t >= frameRemains:
                cue_box.setAutoDraw(False)
            
            
            # *fixation_cue* updates
            if t >= 0.0 and fixation_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_cue.tStart = t
                fixation_cue.frameNStart = frameN  # exact frame index
                fixation_cue.setAutoDraw(True)
            frameRemains = 0.0 + fisidur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_cue.status == STARTED and t >= frameRemains:
                fixation_cue.setAutoDraw(False)
            
            # *cue_money_count* updates
            if t >= 0.0 and cue_money_count.status == NOT_STARTED:
                # keep track of start time/frame for later
                cue_money_count.tStart = t
                cue_money_count.frameNStart = frameN  # exact frame index
                cue_money_count.setAutoDraw(True)
            frameRemains = 0.0 + fisidur + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cue_money_count.status == STARTED and t >= frameRemains:
                cue_money_count.setAutoDraw(False)
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(0.5)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                # updating other components during *ISI*
                cue_box.setPos((cuepos, 0))
                cue_box.setLineColor(cuecolor)
                # component updates done
                ISI.complete()  # finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cue"-------
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('cue_time', float(trial_clock.getTime()) - 0.500)
        trials.addData('stimside', side_dict[trial_id][trial_index])
        trials.addData('fisi_dur', fisidur)
        # the Routine "cue" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "intercue"-------
        t = 0
        intercueClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        intercue_money_amt.setText(earn_txt)
        # keep track of which components have finished
        intercueComponents = [fixation_intercue, intercue_money_amt]
        for thisComponent in intercueComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "intercue"-------
        while continueRoutine:
            # get current time
            t = intercueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_intercue* updates
            if t >= 0.0 and fixation_intercue.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_intercue.tStart = t
                fixation_intercue.frameNStart = frameN  # exact frame index
                fixation_intercue.setAutoDraw(True)
            frameRemains = 0.0 + isidur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_intercue.status == STARTED and t >= frameRemains:
                fixation_intercue.setAutoDraw(False)
            
            # *intercue_money_amt* updates
            if t >= 0.0 and intercue_money_amt.status == NOT_STARTED:
                # keep track of start time/frame for later
                intercue_money_amt.tStart = t
                intercue_money_amt.frameNStart = frameN  # exact frame index
                intercue_money_amt.setAutoDraw(True)
            frameRemains = 0.0 + isidur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if intercue_money_amt.status == STARTED and t >= frameRemains:
                intercue_money_amt.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intercueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "intercue"-------
        for thisComponent in intercueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "intercue" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        color_1 = color_2 = 'white'
        poly_left.setOpacity(polyopa_1)
        poly_right.setOpacity(polyopa_2)
        trial_resp = event.BuilderKeyResponse()
        cue_box_trial.setPos((cuepos, 0))
        cue_box_trial.setLineColor(cuecolor)
        stimulus_image.setOpacity(1)
        stimulus_image.setColor([1.000,1.000,1.000], colorSpace='rgb')
        stimulus_image.setPos((cuepos, 0))
        stimulus_image.setImage(stim)
        trial_money_amt.setText(earn_txt
)
        # keep track of which components have finished
        trialComponents = [poly_left, poly_right, trial_resp, cue_box_trial, stimulus_image, trial_money_amt]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if len(trial_resp.keys) != 0:
                # Save the corresponding box as which_box
                which_box = trial_resp.keys[0]
                # Execute the format function for the color fill of the selected box
                exec_run = True
                exec('color_{0} = "yellow"'.format(which_box))
            
            # *poly_left* updates
            if t >= 0 and poly_left.status == NOT_STARTED:
                # keep track of start time/frame for later
                poly_left.tStart = t
                poly_left.frameNStart = frameN  # exact frame index
                poly_left.setAutoDraw(True)
            frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if poly_left.status == STARTED and t >= frameRemains:
                poly_left.setAutoDraw(False)
            if poly_left.status == STARTED:  # only update if drawing
                poly_left.setFillColor(color_1, log=False)
            
            # *poly_right* updates
            if t >= 0 and poly_right.status == NOT_STARTED:
                # keep track of start time/frame for later
                poly_right.tStart = t
                poly_right.frameNStart = frameN  # exact frame index
                poly_right.setAutoDraw(True)
            frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if poly_right.status == STARTED and t >= frameRemains:
                poly_right.setAutoDraw(False)
            if poly_right.status == STARTED:  # only update if drawing
                poly_right.setFillColor(color_2, log=False)
            
            # *trial_resp* updates
            if t >= 0 and trial_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_resp.tStart = t
                trial_resp.frameNStart = frameN  # exact frame index
                trial_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trial_resp.status == STARTED and t >= frameRemains:
                trial_resp.status = STOPPED
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
            
            # *cue_box_trial* updates
            if t >= 0.0 and cue_box_trial.status == NOT_STARTED:
                # keep track of start time/frame for later
                cue_box_trial.tStart = t
                cue_box_trial.frameNStart = frameN  # exact frame index
                cue_box_trial.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cue_box_trial.status == STARTED and t >= frameRemains:
                cue_box_trial.setAutoDraw(False)
            
            # *stimulus_image* updates
            if t >= 0 and stimulus_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus_image.tStart = t
                stimulus_image.frameNStart = frameN  # exact frame index
                stimulus_image.setAutoDraw(True)
            frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stimulus_image.status == STARTED and t >= frameRemains:
                stimulus_image.setAutoDraw(False)
            
            # *trial_money_amt* updates
            if t >= 0.0 and trial_money_amt.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_money_amt.tStart = t
                trial_money_amt.frameNStart = frameN  # exact frame index
                trial_money_amt.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trial_money_amt.status == STARTED and t >= frameRemains:
                trial_money_amt.setAutoDraw(False)
            
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
        trials.addData('stimulus', stim[-8:])
        trials.addData('stimans', stimans)
        trials.addData('rwd_amt', rew_amt)
        trials.addData('isidur', isidur)
        trials.addData('trialtype', trial_type)
        rewd_amt = format(rew_amt, '.2f')
        if trial_resp.corr == 1 and trial_type =='reward':
            fdbck_txt = 'Correct \n +{}'.format(rewd_amt)
            fdbck_color = 'Green'
            earn_amt += float(rew_amt)
        elif trial_resp.corr == 1 and trial_type != 'reward':
            fdbck_txt = 'Correct'
            fdbck_color = 'Green'
        elif trial_resp.corr == 0 and trial_type == 'loss':
            fdbck_txt = 'Incorrect \n -{}'.format(rewd_amt)
            fdbck_color = 'Red'
            earn_amt -= float(rew_amt)
        elif trial_resp.corr == 0 and trial_type != 'loss':
            fdbck_txt = 'Incorrect'
            fdbck_color = 'Red'
        earn_txt = format(earn_amt, '.2f')
        trials.addData('trial_clock', float(trial_clock.getTime()) - 1.000)
        trials.addData('earn_amt', earn_txt)
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
        
        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        feedback_text.setColor(fdbck_color, colorSpace='rgb')
        feedback_text.setText(fdbck_txt)
        feedback_money_count.setText(earn_txt
)
        
        # keep track of which components have finished
        feedbackComponents = [feedback_text, feedback_money_count]
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            if t >= 0 and feedback_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_text.tStart = t
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.setAutoDraw(True)
            frameRemains = 0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedback_text.status == STARTED and t >= frameRemains:
                feedback_text.setAutoDraw(False)
            
            # *feedback_money_count* updates
            if t >= 0.0 and feedback_money_count.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_money_count.tStart = t
                feedback_money_count.frameNStart = frameN  # exact frame index
                feedback_money_count.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedback_money_count.status == STARTED and t >= frameRemains:
                feedback_money_count.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('feedback_clock', float(trial_clock.getTime()) - 0.500)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
# completed 1 repeats of 'run'





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
