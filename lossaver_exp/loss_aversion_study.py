#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on January 30, 2019, at 15:01
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
from __future__ import absolute_import, division
import os  # handy system and path functions
import sys  # to get file system encoding
from psychopy import gui, visual, core, data, event, logging #pylint: disable=E0401
from psychopy.constants import NOT_STARTED, STARTED, STOPPED, FINISHED #pylint: disable=E0401
import numpy as np  # whole numpy lib is available, prepend 'np.'
import pandas as pd
from PIL import Image
#pylint: disable=C0103,E1102,E1101
# Ensure that relative paths start from the same directory as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(SCRIPT_DIR)

# Store info about the experiment session
exp_name = 'lossaver_study'  # from the Builder filename that created this script
exp_info = {u'session': u'001', u'participant': u'', u'scanner': u'1'}
dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name,
                      order=['participant', 'session', 'scanner'])
if not dlg.OK:
    core.quit()  # user pressed cancel
exp_info['date'] = data.getDateStr()  # add a simple timestamp
exp_info['exp_name'] = exp_name

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = \
SCRIPT_DIR + os.sep + u'data/sub-{0}_ses-01_task-{1}'.format(exp_info['participant'],
                                                             exp_info['exp_name'].split('_')[1])

# An ExperimentHandler isn't essential but helps with data saving
this_exp = data.ExperimentHandler(name=exp_name, version='',
                                  extraInfo=exp_info, runtimeInfo=None,
                                  originPath=u'E:\\lossaver_mid\\lossaver_mid_rev.psyexp',
                                  savePickle=True, saveWideText=True,
                                  dataFileName=filename)
# save a log file for detail verbose info
log_file = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

END_EXP_FLAG = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0,
                    allowGUI=False, allowStencil=False,
                    monitor='testMonitor', color=[1.000, 1.000, 1.000],
                    colorSpace='rgb', blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
exp_info['frameRate'] = win.getActualFrameRate()
if exp_info['frameRate']:
    frame_dur = 1.0 / round(exp_info['frameRate'])
else:
    frame_dur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "begin_setup"
begin_setupClock = core.Clock()

x_dim, y_dim = win.size
fix_size = (50/x_dim, 50/y_dim)
cue_size = (850/x_dim, 850/y_dim)
stim_size = (800/x_dim, 800/y_dim)
text_color = 'black'

orig_dict = {'gain' : pd.read_csv('stimulus_lists/gain_list.csv', header=None)[0].tolist(),
             'loss' : pd.read_csv('stimulus_lists/loss_list.csv', header=None)[0].tolist(),
             'neut' : pd.read_csv('stimulus_lists/neut_list.csv', header=None)[0].tolist()}
class_dict = {}
for classification in orig_dict:
    for item in orig_dict[classification]:
        class_dict[item] = classification
stim_count = np.sum([len(orig_dict[type]) for type in orig_dict])

run_count = 3

stim_list = {x: [] for x in range(run_count)}
for i in range(stim_count // (run_count ** 2)):
    for run in range(run_count):
        stim_list[run].extend((orig_dict['gain'].pop(),
                               orig_dict['loss'].pop(),
                               orig_dict['neut'].pop()))
post_stim_interval = {x: [2, 4, 6] * 24 for x in range(run_count)}
post_fdbk_interval = {x: [2, 4, 6] * 24 for x in range(run_count)}

for key in stim_list:
    np.random.shuffle(stim_list[key]) #pylint: disable=E1101
    np.random.shuffle(post_stim_interval[key])
    np.random.shuffle(post_fdbk_interval[key])
# Initialize components for Routine "instruc"
instruct_clock = core.Clock()
point_count = 0
point_count_txt = ''
run_clock = core.Clock()
prob_type = {'gain': ['perf'] * 16 + ['corr'] * 4 + ['inco'] * 4,
             'loss': ['perf'] * 16 + ['corr'] * 4 + ['inco'] * 4,
             'neut': ['perf'] * 16 + ['corr'] * 4 + ['inco'] * 4}
instruc_text = visual.TextStim(win=win, name='instruc_text',
                               text='default text',
                               font='Arial',
                               pos=(0, 0), height=0.1, wrapWidth=2, ori=0,
                               color=text_color, colorSpace='rgb', opacity=1,
                               depth=-1.0)

# Initialize components for Routine "begin_fix"
begin_fix_clock = core.Clock()
fix = visual.Polygon(win=win, name='fix',
                     edges=99, size=fix_size,
                     ori=0, pos=(0, 0),
                     lineWidth=1, lineColor=[-1.000, -1.000, -1.000],
                     lineColorSpace='rgb', fillColor=text_color,
                     fillColorSpace='rgb', opacity=1,
                     depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trial_clock = core.Clock()
cue_color = 'Green'
stim_pos = (0, 0)
resp_list = []
begin_fix = 6
feedback_txt = ''
stim = None
cue_image = visual.Rect(win=win, name='cue_image',
                        width=cue_size[0], height=cue_size[1],
                        ori=0, pos=[0, 0],
                        lineWidth=20, lineColor=1.0, lineColorSpace='rgb',
                        fillColor=[1.000, 1.000, 1.000], fillColorSpace='rgb',
                        opacity=1, depth=-1.0, interpolate=True)
fixation = visual.Polygon(win=win, name='fixation',
                          edges=99, size=fix_size,
                          ori=0, pos=(0, 0),
                          lineWidth=1, lineColor=[1, 1, 1],
                          lineColorSpace='rgb', fillColor=text_color,
                          fillColorSpace='rgb', opacity=1,
                          depth=-2.0, interpolate=True)
stim_cue = visual.Rect(win=win, name='stim_cue',
                       width=[1.0, 1.0][0], height=[1.0, 1.0][1],
                       ori=0, pos=[0, 0],
                       lineWidth=20, lineColor=1.0,
                       lineColorSpace='rgb', fillColor=[1.000, 1.000, 1.000],
                       fillColorSpace='rgb', opacity=1,
                       depth=-3.0, interpolate=True)
stimulus_image = visual.ImageStim(win=win, name='stimulus_image',
                                  image='sin', mask=None,
                                  ori=0, pos=[0, 0], size=1.0,
                                  color=[1.000, 1.000, 1.000], colorSpace='rgb',
                                  opacity=1, flipHoriz=False,
                                  flipVert=False, texRes=128,
                                  interpolate=True, depth=-4.0)
resp_window_text = visual.TextStim(win=win, name='resp_window_text',
                                   text='Go!', font='Arial',
                                   pos=(0, 0), height=0.1, wrapWidth=None,
                                   ori=0, color=text_color,
                                   colorSpace='rgb', opacity=1, depth=-6.0)
point_count_box = visual.TextStim(win=win, name='point_count_box',
                                  text='default text', font='Arial',
                                  pos=(0, 0.75), height=0.1, wrapWidth=None,
                                  ori=0, color=text_color, colorSpace='rgb',
                                  opacity=1, depth=-8.0)

# Initialize components for Routine "feedback"
feedback_clock = core.Clock()
feedback_text_box = visual.TextStim(win=win, name='feedback_text_box',
                                    text='default text', font='Arial',
                                    pos=(0, 0), height=0.1,
                                    wrapWidth=None, ori=0,
                                    color=text_color, colorSpace='rgb',
                                    opacity=1, depth=0.0)

point_count_feedback = visual.TextStim(win=win, name='point_count_feedback',
                                       text='default text', font='Arial',
                                       pos=(0, 0.75), height=0.1,
                                       wrapWidth=None, ori=0,
                                       color=text_color, colorSpace='rgb',
                                       opacity=1, depth=-2.0)
update_box = visual.TextStim(win=win, name='update_box',
                             text='default text', font='Arial',
                             pos=(0, -0.5), height=0.1,
                             wrapWidth=None, ori=0,
                             color=text_color, colorSpace='rgb',
                             opacity=1, depth=-3.0)
trial_end_fix = visual.Polygon(win=win, name='trial_end_fix',
                               edges=99, size=fix_size,
                               ori=0, pos=(0, 0),
                               lineWidth=1, lineColor=[1, 1, 1],
                               lineColorSpace='rgb', fillColor=text_color,
                               fillColorSpace='rgb', opacity=1,
                               depth=-4.0, interpolate=True)

# Initialize components for Routine "end_fix"
end_fix_clock = core.Clock()
end_fix_circle = visual.Polygon(win=win, name='end_fix_circle',
                                edges=99, size=fix_size,
                                ori=0, pos=(0, 0),
                                lineWidth=1, lineColor=[1, 1, 1],
                                lineColorSpace='rgb', fillColor=text_color,
                                fillColorSpace='rgb', opacity=1,
                                depth=0.0, interpolate=True)

# Initialize components for Routine "thank_you"
thank_you_clock = core.Clock()
ty_text = visual.TextStim(win=win, name='ty_text',
                          text='The game is now complete!\n', font='Arial',
                          pos=(0, 0), height=0.1,
                          wrapWidth=None, ori=0,
                          color=text_color, colorSpace='rgb',
                          opacity=1, depth=0.0)

# Create some handy timers
global_clock = core.Clock()  # to track the time since experiment started
routine_timer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "begin_setup"-------
t = 0
begin_setupClock.reset()  # clock
frameN = -1
CONTINUE_ROUTINE_FLAG = True
# update component parameters for each repeat

# keep track of which components have finished
begin_setup_components = []
for thisComponent in begin_setup_components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "begin_setup"-------
while CONTINUE_ROUTINE_FLAG:
    # get current time
    t = begin_setupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame


    # check if all components have finished
    if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
        break
    CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
    for thisComponent in begin_setup_components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            CONTINUE_ROUTINE_FLAG = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin_setup"-------
for thisComponent in begin_setup_components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "begin_setup" was not non-slip safe, so reset the non-slip timer
routine_timer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=3, method='sequential',
                         extraInfo=exp_info, originPath=-1,
                         trialList=[None], seed=None, name='runs')
this_exp.addLoop(runs)  # add the loop to the experiment
this_run = runs.trialList[0]  # so we can initialise stimuli with some values


for this_run in runs:
    prob_type = {'gain': ['perf'] * 16 + ['corr'] * 4 + ['inco'] * 4,
                 'loss': ['perf'] * 16 + ['corr'] * 4 + ['inco'] * 4,
                 'neut': ['perf'] * 16 + ['corr'] * 4 + ['inco'] * 4}
    for _type in prob_type:
        np.random.shuffle(prob_type[_type])
    currentLoop = runs

    # ------Prepare to start Routine "instruc"-------
    t = 0
    instruct_clock.reset()  # clock
    frameN = -1
    CONTINUE_ROUTINE_FLAG = True
    # update component parameters for each repeat
    run_images = stim_list[runs.thisN]

    inst_text = \
    '\
    Congratulations! You have been gifted 10 points.\n\
    In the following task, you will lose points for \n\
    every image you fail to correctly identify \n\
    within the time window. \n\n\
            1 = Indoor                2 = Outdoor\n\n\
                  Wait for Researcher to Begin'

    instruc_text.setText(inst_text)
    instruc_end = event.BuilderKeyResponse()
    # keep track of which components have finished
    instrucComponents = [instruc_text, instruc_end]
    for thisComponent in instrucComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "instruc"-------
    while CONTINUE_ROUTINE_FLAG:
        # get current time
        t = instruct_clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame


        # *instruc_text* updates
        if t >= 0.0 and instruc_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruc_text.tStart = t
            instruc_text.frameNStart = frameN  # exact frame index
            instruc_text.setAutoDraw(True)

        # *instruc_end* updates
        if t >= 0.0 and instruc_end.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruc_end.tStart = t
            instruc_end.frameNStart = frameN  # exact frame index
            instruc_end.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instruc_end.status == STARTED:
            these_keys = event.getKeys(keyList=['5', 'space'])

            # check for quit:
            if "escape" in these_keys:
                END_EXP_FLAG = True
            if these_keys:  # at least one key was pressed
                # a response ends the routine
                CONTINUE_ROUTINE_FLAG = False

        # check if all components have finished
        if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
            break
        CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
        for thisComponent in instrucComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                CONTINUE_ROUTINE_FLAG = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instruc"-------
    for thisComponent in instrucComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    point_count_txt = '{0}'.format(point_count)
    run_clock.reset()
    with open('data/sub-{0}_ses-01_task-{1}_run-0{2}.tsv'.format(exp_info['participant'],
                                                                 exp_name.split('_')[1],
                                                                 runs.thisN + 1),
              'a') as datFile:
        datFile.write('\t'.join(['run', 'trial', 'response', 'stimulus_name',
                                 'onset', 'duration', 'response_time',
                                 'trial_type', 'point_total', 'prob_type']) + '\n')
    # the Routine "instruc" was not non-slip safe, so reset the non-slip timer
    routine_timer.reset()

    # ------Prepare to start Routine "begin_fix"-------
    t = 0
    begin_fix_clock.reset()  # clock
    frameN = -1
    CONTINUE_ROUTINE_FLAG = True
    routine_timer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    begin_fixComponents = [fix]
    for thisComponent in begin_fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "begin_fix"-------
    while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
        # get current time
        t = begin_fix_clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix.status == STARTED and t >= frameRemains:
            fix.setAutoDraw(False)

        # check if all components have finished
        if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
            break
        CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
        for thisComponent in begin_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                CONTINUE_ROUTINE_FLAG = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "begin_fix"-------
    for thisComponent in begin_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=72, method='sequential',
                               extraInfo=exp_info, originPath=-1,
                               trialList=[None], seed=None, name='trials')
    this_exp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

    for thisTrial in trials:
        currentLoop = trials

        # ------Prepare to start Routine "trial"-------
        t = 0
        trial_clock.reset()  # clock
        frameN = -1
        CONTINUE_ROUTINE_FLAG = True
        routine_timer.add(3 + post_stim_interval[runs.thisN][trials.thisN])
        # update component parameters for each repeat
        list_pop = [(0.0, 0.0), (-0.0, 0.0)]
        stim_pos = list_pop.pop(np.random.randint(0, 2)) #pylint: disable=E1101

        feedback_txt = ''
        stim = run_images[trials.thisN]
        stim_corr = os.path.basename(stim)[0]
        stim_x, stim_y = Image.open(stim).size
        if stim_x > stim_y:
            stim_size = (800/x_dim, (800/ stim_x) * stim_y / y_dim)
        elif stim_x < stim_y:
            stim_size = ((800 / stim_y) * stim_x / x_dim, 800/y_dim)
        else:
            stim_size = (800/x_dim, 800/y_dim)
        print(class_dict[stim])
        if class_dict[stim] == 'gain':
            cue_color = 'green'
        if class_dict[stim] == 'loss':
            cue_color = 'red'
        if class_dict[stim] == 'neut':
            cue_color = 'grey'
        cue_image.setPos(stim_pos)
        cue_image.setLineColor(cue_color)
        stim_cue.setPos(stim_pos)
        stim_cue.setLineColor(cue_color)
        stim_cue.setSize(cue_size)
        stimulus_image.setPos(stim_pos)
        stimulus_image.setImage(stim)
        stimulus_image.setSize(stim_size)
        trial_resp = event.BuilderKeyResponse()
        false_start_resp = event.BuilderKeyResponse()
        point_count_box.setText(point_count_txt)
        # keep track of which components have finished
        trialComponents = [cue_image, fixation, stim_cue, stimulus_image,
                           resp_window_text, trial_resp, point_count_box]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "trial"-------
        while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
            # get current time
            t = trial_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame
            # *stim_cue* updates
            if t >= 0 and stim_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                stim_cue.tStart = t
                stim_cue.frameNStart = frameN  # exact frame index
                stim_cue.setAutoDraw(True)
            frameRemains = 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if stim_cue.status == STARTED and t >= frameRemains:
                stim_cue.setAutoDraw(False)
            # *stimulus_image* updates
            if t >= 0 and stimulus_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus_image.tStart = t
                stimulus_image.frameNStart = frameN  # exact frame index
                stim_onset = run_clock.getTime()
                stimulus_image.setAutoDraw(True)
            frameRemains = 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if stimulus_image.status == STARTED and t >= frameRemains:
                stimulus_image.setAutoDraw(False)
            # *fixation* updates
            if t >= 2.0 and fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation.tStart = t
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            frameRemains = (2 + post_stim_interval[runs.thisN][trials.thisN]
                            - win.monitorFramePeriod * 0.75)
            if fixation.status == STARTED and t >= frameRemains:
                fixation.setAutoDraw(False)
            # *false_start_resp* updates
            if t >= 2.0 and false_start_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                false_start_resp.tStart = t
                false_start_resp.frameNStart = frameN  # exact frame index
                false_start_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(false_start_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = (2 + post_stim_interval[runs.thisN][trials.thisN]
                            - win.monitorFramePeriod * 0.75)
            if false_start_resp.status == STARTED and t >= frameRemains:
                false_start_resp.status = STOPPED
            if false_start_resp.status == STARTED:
                these_keys = event.getKeys(keyList=['1', '2'])
                # check for quit:
                if "escape" in these_keys:
                    END_EXP_FLAG = True
                if these_keys:  # at least one key was pressed
                    false_start_resp.keys = these_keys[-1]  # just the last key pressed
                    false_start_resp.rt = false_start_resp.clock.getTime()
            resp_window_text.setText('Go!')
            if false_start_resp.keys:
                resp_window_text.setText('False Start!')
            # *resp_window_text* updates
            if t >= 2 + post_stim_interval[runs.thisN][trials.thisN] \
            and resp_window_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_window_text.tStart = t
                resp_window_text.frameNStart = frameN  # exact frame index
                resp_window_text.setAutoDraw(True)
            frameRemains = (2.5 + post_stim_interval[runs.thisN][trials.thisN]
                            - win.monitorFramePeriod * 0.75)
            if resp_window_text.status == STARTED and t >= frameRemains:
                resp_window_text.setAutoDraw(False)

            # *trial_resp* updates
            if t >= 2 + post_stim_interval[runs.thisN][trials.thisN] \
            and trial_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_resp.tStart = t
                trial_resp.frameNStart = frameN  # exact frame index
                trial_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = (2.5 + post_stim_interval[runs.thisN][trials.thisN]
                            - win.monitorFramePeriod * 0.75)
            if false_start_resp.keys:
                frameRemains = 0
            if trial_resp.status == STARTED and t >= frameRemains:
                trial_resp.status = STOPPED
            if trial_resp.status == STARTED:
                these_keys = event.getKeys(keyList=['1', '2'])
                # check for quit:
                if "escape" in these_keys:
                    END_EXP_FLAG = True
                if these_keys:  # at least one key was pressed
                    trial_resp.keys = these_keys[-1]  # just the last key pressed
                    trial_resp.rt = trial_resp.clock.getTime()
            # *fixation* updates
            if t >= 2.5 + post_stim_interval[runs.thisN][trials.thisN] \
            and fixation.status == STOPPED:
                # keep track of start time/frame for later
                fixation.tStart = t
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            frameRemains = (3 + post_stim_interval[runs.thisN][trials.thisN]
                            - win.monitorFramePeriod * 0.75)
            if fixation.status == STARTED and t >= frameRemains:
                fixation.setAutoDraw(False)
            # *point_count_box* updates
            if t >= 0.0 and point_count_box.status == NOT_STARTED:
                # keep track of start time/frame for later
                point_count_box.tStart = t
                point_count_box.frameNStart = frameN  # exact frame index
                point_count_box.setAutoDraw(True)
            frameRemains = (3.0 + post_stim_interval[runs.thisN][trials.thisN]
                            - win.monitorFramePeriod * 0.75)
            if point_count_box.status == STARTED and t >= frameRemains:
                point_count_box.setAutoDraw(False)

            # check if all components have finished
            if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
                break
            CONTINUE_ROUTINE_FLAG = False
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    CONTINUE_ROUTINE_FLAG = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:
                win.flip()
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        this_prob_type = prob_type[class_dict[stim]].pop()
        if this_prob_type == 'perf':
            CORR_STATUS = (trial_resp.keys == os.path.basename(stimulus_image.image)[0])
            if CORR_STATUS and not false_start_resp.keys:
                feedback_txt = 'Correct!'
            elif not CORR_STATUS and not false_start_resp.keys:
                feedback_txt = 'Incorrect!'
        elif this_prob_type == 'corr' and not false_start_resp.keys:
            feedback_txt = 'Correct!'
        elif this_prob_type == 'inco' and not false_start_resp.keys:
            feedback_txt = 'Incorrect!'

        if 'Incorrect!' in feedback_txt and class_dict[stim] == 'loss':
            update_text = '-1'
            point_count -= 1
        elif 'Correct!' in feedback_txt and class_dict[stim] == 'gain':
            update_text = '+1'
            point_count += 1
        elif class_dict[stim] == 'neut':
            update_text = '##'
        else:
            update_text = u'\u00B1' + '0'
        if false_start_resp.keys:
            feedback_txt = 'False Start!'
            if class_dict[stim] == 'loss':
                update_text = '-1'
                point_count -= 1
            elif class_dict[stim] == 'gain':
                update_text = u'\u00B1' + '0'

        # check responses
        if trial_resp.keys in ['', [], None]:  # No response was made
            trial_resp.keys = None
        trials.addData('trial_resp.keys', trial_resp.keys)
        if trial_resp.keys:  # we had a response
            trials.addData('trial_resp.rt', trial_resp.rt)

        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedback_clock.reset()  # clock
        frameN = -1
        CONTINUE_ROUTINE_FLAG = True
        # update component parameters for each repeat
        feedback_text_box.setText(feedback_txt)
        point_count_txt = '{0}'.format(point_count)

        point_count_feedback.setText(point_count_txt)
        update_box.setText(update_text)

        # keep track of which components have finished
        feedbackComponents = [feedback_text_box, point_count_feedback, update_box, trial_end_fix]
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "feedback"-------
        while CONTINUE_ROUTINE_FLAG:
            # get current time
            t = feedback_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # *feedback_text_box* updates
            if t >= 0.0 and feedback_text_box.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_text_box.tStart = t
                feedback_text_box.frameNStart = frameN  # exact frame index
                feedback_text_box.setAutoDraw(True)
            frameRemains = (0.0 + .5 - win.monitorFramePeriod * 0.75)
            if feedback_text_box.status == STARTED and t >= frameRemains:
                feedback_text_box.setAutoDraw(False)
            # *point_count_feedback* updates
            if t >= 0.0 and point_count_feedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                point_count_feedback.tStart = t
                point_count_feedback.frameNStart = frameN  # exact frame index
                point_count_feedback.setAutoDraw(True)
            frameRemains = (post_fdbk_interval[runs.thisN][trials.thisN]
                            + 0.5 - win.monitorFramePeriod * 0.75)
            if point_count_feedback.status == STARTED and t >= frameRemains:
                point_count_feedback.setAutoDraw(False)
            # *update_box* updates
            if t >= 0.0 and update_box.status == NOT_STARTED:
                # keep track of start time/frame for later
                update_box.tStart = t
                update_box.frameNStart = frameN  # exact frame index
                update_box.setAutoDraw(True)
            frameRemains = 0.0 + 0.5 - win.monitorFramePeriod * 0.75
            if update_box.status == STARTED and t >= frameRemains:
                update_box.setAutoDraw(False)
            # *trial_end_fix* updates
            if t >= 0.5 and trial_end_fix.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_end_fix.tStart = t
                trial_end_fix.frameNStart = frameN  # exact frame index
                trial_end_fix.setAutoDraw(True)
            frameRemains = (0.5 + post_fdbk_interval[runs.thisN][trials.thisN]
                            - win.monitorFramePeriod * 0.75)
            if trial_end_fix.status == STARTED and t >= frameRemains:
                trial_end_fix.setAutoDraw(False)

            # check if all components have finished
            if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
                break
            CONTINUE_ROUTINE_FLAG = False
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    CONTINUE_ROUTINE_FLAG = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:
                win.flip()

        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if false_start_resp.keys:
            prob_trial = 'false_start'
        with open('data/sub-{0}_ses-01_task-{1}_run-0{2}.tsv'.format(exp_info['participant'],
                                                                     exp_name.split('_')[1],
                                                                     runs.thisN + 1),
                  'a') \
        as datFile:
            datFile.write('\t'.join([str(x) for x in [runs.thisN + 1, trials.thisN + 1,
                                                      trial_resp.keys, stim,
                                                      stim_onset, 2.0, trial_resp.rt,
                                                      class_dict[stim], point_count,
                                                      this_prob_type]]) + '\n')
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routine_timer.reset()
        this_exp.nextEntry()

    # completed 72 repeats of 'trials'

    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop

    # ------Prepare to start Routine "end_fix"-------
    t = 0
    end_fix_clock.reset()  # clock
    frameN = -1
    CONTINUE_ROUTINE_FLAG = True
    routine_timer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    end_fixComponents = [end_fix_circle]
    for thisComponent in end_fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "end_fix"-------
    while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
        # get current time
        t = end_fix_clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # *end_fix_circle* updates
        if t >= 0.0 and end_fix_circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_fix_circle.tStart = t
            end_fix_circle.frameNStart = frameN  # exact frame index
            end_fix_circle.setAutoDraw(True)
        frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if end_fix_circle.status == STARTED and t >= frameRemains:
            end_fix_circle.setAutoDraw(False)

        # check if all components have finished
        if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
            break
        CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
        for thisComponent in end_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                CONTINUE_ROUTINE_FLAG = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
            core.quit()
        # refresh the screen
        if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "end_fix"-------
    for thisComponent in end_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 3 repeats of 'runs'


# ------Prepare to start Routine "thank_you"-------
t = 0
thank_you_clock.reset()  # clock
frameN = -1
CONTINUE_ROUTINE_FLAG = True
# update component parameters for each repeat
ty_resp = event.BuilderKeyResponse()
# keep track of which components have finished
thank_you_components = [ty_text, ty_resp]
for thisComponent in thank_you_components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thank_you"-------
while CONTINUE_ROUTINE_FLAG:
    # get current time
    t = thank_you_clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # *ty_text* updates
    if t >= 0.0 and ty_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        ty_text.tStart = t
        ty_text.frameNStart = frameN  # exact frame index
        ty_text.setAutoDraw(True)

    # *ty_resp* updates
    if t >= 0.0 and ty_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        ty_resp.tStart = t
        ty_resp.frameNStart = frameN  # exact frame index
        ty_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ty_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ty_resp.status == STARTED:
        these_keys = event.getKeys(keyList=['space'])
        # check for quit:
        if "escape" in these_keys:
            END_EXP_FLAG = True
        if these_keys:  # at least one key was pressed
            ty_resp.keys = these_keys[-1]  # just the last key pressed
            ty_resp.rt = ty_resp.clock.getTime()
            # a response ends the routine
            CONTINUE_ROUTINE_FLAG = False

    # check if all components have finished
    if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
        break
    CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
    for thisComponent in thank_you_components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            CONTINUE_ROUTINE_FLAG = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thank_you"-------
for thisComponent in thank_you_components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ty_resp.keys in ['', [], None]:  # No response was made
    ty_resp.keys = None
this_exp.addData('ty_resp.keys', ty_resp.keys)
if ty_resp.keys:  # we had a response
    this_exp.addData('ty_resp.rt', ty_resp.rt)
this_exp.nextEntry()
# the Routine "thank_you" was not non-slip safe, so reset the non-slip timer
routine_timer.reset()

# these shouldn't be strictly necessary (should auto-save)
this_exp.saveAsWideText(filename+'.csv')
this_exp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
this_exp.abort()  # or data files will save again on exit
win.close()
core.quit()
