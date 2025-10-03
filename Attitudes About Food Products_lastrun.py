#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Fri Oct  3 17:43:06 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from experiment_info_code
# === SET UP STIMULI CHARACTERISTICS ===

image_size = [0.3,0.3]
left_image_position = [-0.25, 0]
right_image_position = [0.25, 0]

similarity_left_image_position = [-0.25, -0.25]
similarity_right_image_position = [0.25, -0.25]
reference_image_position = [0, 0.15]

choice_position = [0,-1]
border_color = "white"

# === FUNCTION TO GENERATE PAIRS ===

def generate_pairs(items):
    pairs = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            pairs.append([items[i], items[j]])
    return pairs

# === SETTING UP PRACTICE TRIALS ===

# identify list of practice stimuli
practice_path = str("images/practice/comparison/")

# create list of practice stimuli
# === CHANGE PATH HERE ===
# enter directory where your practice stimuli are located
practice_stimuli = [s for s in os.listdir('/Users/mohammadhamdan/Documents/GitHub/Comparative_Judgement/images/practice/comparison') if s.endswith('.png')]

# create all pairs
practice_stimuli = generate_pairs(practice_stimuli)

# shuffle within pairs (so that the same pictures are not more likely to be presented on the same side)
for pair in range(0,len(practice_stimuli)):
    shuffle(practice_stimuli[pair])

# shuffle order
shuffle(practice_stimuli[pair])

# how many trials
length_of_practice_trials = len(practice_stimuli)

# === SETTING UP EXPERIMENTAL TRIALS ===
# identify path
experimental_path = str("images/trials/comparison/")

# === CHANGE PATH HERE ===
# enter directory where your experimental stimuli are located
experimental_stimuli = [s for s in os.listdir('/Users/mohammadhamdan/Documents/GitHub/Comparative_Judgement/images/trials/comparison') if s.endswith('.png')]

# create all pairs
experimental_stimuli = generate_pairs(experimental_stimuli)

# shuffle order
shuffle(experimental_stimuli)

# shuffle within pairs (so that the same pictures are not more likely to be presented on the same side)
for pair in range(0,len(experimental_stimuli)):
    shuffle(experimental_stimuli[pair])

# how many trials
length_of_experimental_trials = len(experimental_stimuli)

# === ATTENTION CHECKS ===
attention_checks_failed = 0

#random stimuli for attention checks
# === CHANGE PATH HERE ===
options = [s for s in os.listdir('/Users/mohammadhamdan/Documents/GitHub/Comparative_Judgement/images/trials/comparison') if s.endswith('.png')]
practice_attention_random_choice = np.random.choice(options)
practice_attention_check_image = 'images/practice/comparison/' + practice_attention_random_choice

# === CHANGE PATH HERE ===
options = [s for s in os.listdir('/Users/mohammadhamdan/Documents/GitHub/Comparative_Judgement/images/trials/comparison') if s.endswith('.png')]
liking_attention_random_choice = np.random.choice(options)
liking_attention_check_image = 'images/trials/comparison/' + liking_attention_random_choice

# === DIET ===
# only flexitarians and omnivores were shown the red meat question, so if 
# one of those was answered in the diet question,
# this value changes to true
omniflex = False



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Attitudes about food products'  # from the Builder filename that created this script
expInfo = {
    'participant': '001',
}
# --- Show participant info dialog --
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
    originPath='/Users/mohammadhamdan/Documents/GitHub/Comparative_Judgement/Attitudes About Food Products_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "routine_0_experiment_conditions" ---
experiment_conditions_text = visual.ImageStim(
    win=win,
    name='experiment_conditions_text', units='height', 
    image='texts/0_experiment_conditions.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
experiment_conditions_key_resp = keyboard.Keyboard()
experiment_conditions_press_space_to_continue = visual.TextStim(win=win, name='experiment_conditions_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "routine_0_experiment_info" ---
experiment_info_text = visual.ImageStim(
    win=win,
    name='experiment_info_text', units='height', 
    image='texts/0_experiment_info.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
experiment_info_key_resp = keyboard.Keyboard()
experiment_info_press_space_to_continue = visual.TextStim(win=win, name='experiment_info_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "routine_1_informed_consent" ---
informed_conset_key_resp = keyboard.Keyboard()
informed_consent_text = visual.TextStim(win=win, name='informed_consent_text',
    text='By proceeding with the experiment, you agree that you have read and understood the consent form on the previous page. \n\nIf you do not wish to participate, you can press ESC twice to exit and return the study on Connect Research.',
    font='Times New Roman',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
informed_consent_press_space_to_continue = visual.TextStim(win=win, name='informed_consent_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "diet_question" ---
diet_prompt = visual.TextStim(win=win, name='diet_prompt',
    text='How would you describe your diet?',
    font='Times New Roman',
    pos=(0, 0.35), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
diet_options = visual.TextStim(win=win, name='diet_options',
    text='1. Omnivore (I eat meat, fish and/or dairy daily/almost daily)\n\n2. Pescatarian (I eat fish and diary, but not meat)\n\n3. Flexitarian (I eat meat and fish occasionally, but I also eat vegetarian)\n\n4. Vegetarian (I do not eat meat nor fish, but I eat dairy products)\n\n5. Vegan (I do not eat meat, fish nor dairy products)\n\n6. Other\n\nPlease type the number in the box below.',
    font='Times New Roman',
    pos=(0, 0.1), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
diet_response = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.2),     letterHeight=0.025,
     size=(0.1, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='diet_response',
     autoLog=True,
)
diet_key_resp = keyboard.Keyboard()
diet_press_enter_to_continue = visual.TextStim(win=win, name='diet_press_enter_to_continue',
    text='Press ENTER to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "additional_diet_question" ---
additional_diet_prompt = visual.TextStim(win=win, name='additional_diet_prompt',
    text='How long have you been following this diet?',
    font='Times New Roman',
    pos=(0, 0.35), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
additional_diet_options = visual.TextStim(win=win, name='additional_diet_options',
    text="1. Less than a year\n\n2. Within the last 1-3 years\n\n3. Within the last 3 and 5 years\n\n4. Within the last 5 and 10 years\n\n5. For over 10 years\n\n6. I've always followed this diet\n\nPlease type the number in the box below.",
    font='Times New Roman',
    pos=(0, 0.1), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
additional_diet_response = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.2),     letterHeight=0.025,
     size=(0.1, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='additional_diet_response',
     autoLog=True,
)
additional_diet_key_resp = keyboard.Keyboard()
additional_diet_press_enter_to_continue = visual.TextStim(win=win, name='additional_diet_press_enter_to_continue',
    text='Press ENTER to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "red_meat_question" ---
red_meat_prompt = visual.TextStim(win=win, name='red_meat_prompt',
    text='Do you eat red meat (beef, veal, pork and/or lamb)?',
    font='Times New Roman',
    pos=(0, 0.35), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
red_meat_options = visual.TextStim(win=win, name='red_meat_options',
    text='1. Yes\n\n2. No\n\nPlease type the number in the box below.',
    font='Times New Roman',
    pos=(0, 0.1), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
red_meat_response = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.2),     letterHeight=0.025,
     size=(0.1, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='red_meat_response',
     autoLog=True,
)
red_meat_key_resp = keyboard.Keyboard()
red_meat_press_enter_to_continue = visual.TextStim(win=win, name='red_meat_press_enter_to_continue',
    text='Press ENTER to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "routine_3_pre_instructions" ---
key_resp_pre_instructions = keyboard.Keyboard()
pre_instructions_press_space_to_continue = visual.TextStim(win=win, name='pre_instructions_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
pre_instructions_text = visual.ImageStim(
    win=win,
    name='pre_instructions_text', units='height', 
    image='texts/3_pre_instructions.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "routine_4_practice_instructions" ---
practice_instructions_image = visual.ImageStim(
    win=win,
    name='practice_instructions_image', 
    image='texts/4_practice_instructions.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practice_instructions_end = keyboard.Keyboard()
practice_instructions_press_space_to_continue = visual.TextStim(win=win, name='practice_instructions_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "practice_trial" ---
practice_trial_question = visual.TextStim(win=win, name='practice_trial_question',
    text='Which of the two citrus fruits do you LIKE MORE?',
    font='Times New Roman',
    pos=(0, 0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from practice_trial_code
# index
practice_index = 0
practice_trial_left_image = visual.ImageStim(
    win=win,
    name='practice_trial_left_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=left_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
practice_trial_right_image = visual.ImageStim(
    win=win,
    name='practice_trial_right_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=right_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
practice_trial_choice = keyboard.Keyboard()
practice_trial_fruit_A = visual.TextStim(win=win, name='practice_trial_fruit_A',
    text='CITRUS FRUIT A',
    font='Times New Roman',
    pos=(-0.25, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
practice_trial_fruit_B = visual.TextStim(win=win, name='practice_trial_fruit_B',
    text='CITRUS FRUIT B',
    font='Times New Roman',
    pos=(0.25, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
practice_trial_highlighted_choice = visual.Rect(
    win=win, name='practice_trial_highlighted_choice',
    width=image_size[0], height=image_size[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1.0, depth=-7.0, interpolate=True)
practice_trial_missed_trial_text = visual.TextStim(win=win, name='practice_trial_missed_trial_text',
    text='You have not yet responsed, we really care about your response!\n\n\n\nReminder: press "k" if you LIKE the right plant-based steak more, or "d" if you LIKE the left plant-based steak more.',
    font='Times New Roman',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
practice_trial_end_missed_trial_resp = keyboard.Keyboard()
practice_trial_missed_trial_press_space_to_continue = visual.TextStim(win=win, name='practice_trial_missed_trial_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "practice_trial_attention_check" ---
practice_trial_attention_check_question = visual.TextStim(win=win, name='practice_trial_attention_check_question',
    text='This is an attention check. Press Q on your keyboard to continue',
    font='Times New Roman',
    pos=(0, 0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice_trial_attention_check_left_image = visual.ImageStim(
    win=win,
    name='practice_trial_attention_check_left_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=left_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
practice_trial_attention_check_right_image = visual.ImageStim(
    win=win,
    name='practice_trial_attention_check_right_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=right_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
practice_trial_attention_check_choice = keyboard.Keyboard()
practice_trial_attention_check_fruit_A = visual.TextStim(win=win, name='practice_trial_attention_check_fruit_A',
    text='CITRUS FRUIT A',
    font='Times New Roman',
    pos=(-0.25, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
practice_trial_attention_check_fruit_B = visual.TextStim(win=win, name='practice_trial_attention_check_fruit_B',
    text='CITRUS FRUIT B',
    font='Times New Roman',
    pos=(0.25, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "failed_attention_check" ---
missed_attention_check_text = visual.TextStim(win=win, name='missed_attention_check_text',
    text='You just failed an attention check. Please pay full attention to the task.',
    font='Times New Roman',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
missed_attention_check_resp = keyboard.Keyboard()
missed_attention_check_press_space_to_continue = visual.TextStim(win=win, name='missed_attention_check_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "routine_4_practice_aftermath" ---
practice_aftermath_press_space_to_continue = visual.TextStim(win=win, name='practice_aftermath_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice_aftermath_end = keyboard.Keyboard()
practice_aftermath_text = visual.ImageStim(
    win=win,
    name='practice_aftermath_text', units='height', 
    image='texts/4_practice_aftermath.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "routine_6_liking_instructions" ---
liking_instructions_space = keyboard.Keyboard()
# Run 'Begin Experiment' code from liking_instructions_code
# identify list of instructions png files
liking_instructions = ["6_trial_instructions_liking.png", "6_trial_instructions_liking_visual.png"]

# index
liking_instructions_index = 0
liking_instructions_image = visual.ImageStim(
    win=win,
    name='liking_instructions_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
liking_instructions_press_space_to_continue = visual.TextStim(win=win, name='liking_instructions_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "liking_trial" ---
liking_trial_question = visual.TextStim(win=win, name='liking_trial_question',
    text='Which of the two plant-based steaks do you LIKE MORE?',
    font='Times New Roman',
    pos=(0, 0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from liking_trial_code
# index
stimulus_index_liking = 0
liking_trial_left_image = visual.ImageStim(
    win=win,
    name='liking_trial_left_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=left_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
liking_trial_right_image = visual.ImageStim(
    win=win,
    name='liking_trial_right_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=right_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
liking_trial_choice = keyboard.Keyboard()
liking_trial_steak_A_title = visual.TextStim(win=win, name='liking_trial_steak_A_title',
    text='PLANT-BASED STEAK A',
    font='Times New Roman',
    pos=(-0.25, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
liking_trial_steak_B_title = visual.TextStim(win=win, name='liking_trial_steak_B_title',
    text='PLANT-BASED STEAK B',
    font='Times New Roman',
    pos=(0.25, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
liking_trial_missed_trial_text = visual.TextStim(win=win, name='liking_trial_missed_trial_text',
    text='You have not yet responsed, we really care about your response!\n\n\n\nReminder: press "k" if you LIKE the right plant-based steak more, or "d" if you LIKE the left plant-based steak more.',
    font='Times New Roman',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
liking_trial_highlighted_choice = visual.Rect(
    win=win, name='liking_trial_highlighted_choice',
    width=image_size[0], height=image_size[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1.0, depth=-8.0, interpolate=True)
liking_trial_end_missed_trial_resp = keyboard.Keyboard()
liking_trial_missed_trial_press_space_to_continue = visual.TextStim(win=win, name='liking_trial_missed_trial_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "liking_trial_attention_check" ---
liking_trial_attention_check_question = visual.TextStim(win=win, name='liking_trial_attention_check_question',
    text='This is an attention check. Press Q on your keyboard to continue',
    font='Times New Roman',
    pos=(0, 0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
liking_trial_attention_check_left_image = visual.ImageStim(
    win=win,
    name='liking_trial_attention_check_left_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=left_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
liking_trial_attention_check_right_image = visual.ImageStim(
    win=win,
    name='liking_trial_attention_check_right_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=right_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
liking_trial_attention_check_choice = keyboard.Keyboard()
liking_trial_attention_check_steak_A = visual.TextStim(win=win, name='liking_trial_attention_check_steak_A',
    text='PLANT-BASED STEAK A',
    font='Times New Roman',
    pos=(-0.25, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
liking_trial_attention_check_steak_B = visual.TextStim(win=win, name='liking_trial_attention_check_steak_B',
    text='PLANT-BASED STEAK B',
    font='Times New Roman',
    pos=(0.25, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "failed_attention_check" ---
missed_attention_check_text = visual.TextStim(win=win, name='missed_attention_check_text',
    text='You just failed an attention check. Please pay full attention to the task.',
    font='Times New Roman',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
missed_attention_check_resp = keyboard.Keyboard()
missed_attention_check_press_space_to_continue = visual.TextStim(win=win, name='missed_attention_check_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "routine_6_similarity_instructions" ---
similarity_instructions_space = keyboard.Keyboard()
# Run 'Begin Experiment' code from similarity_instructions_code
# identify list of instructions png files
similarity_instructions = ["5_liking_aftermath.png", "5_trial_instructions_sim.png", "5_trial_instructions_sim_visual.png"]

# index
similarity_instructions_index = 0
similarity_instructions_image = visual.ImageStim(
    win=win,
    name='similarity_instructions_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
similarity_instructions_press_space_to_continue = visual.TextStim(win=win, name='similarity_instructions_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "similarity_trial" ---
similarity_trial_question = visual.TextStim(win=win, name='similarity_trial_question',
    text='Which of the two plant-based steaks is MORE SIMILAR to a prototypical BEEF STEAK?',
    font='Times New Roman',
    pos=(0, 0.4), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from similarity_trial_code
# index
stimulus_index_similarity = 0
similarity_trial_left_image = visual.ImageStim(
    win=win,
    name='similarity_trial_left_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=similarity_left_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
similarity_trial_right_image = visual.ImageStim(
    win=win,
    name='similarity_trial_right_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=similarity_right_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
similarity_trial_choice = keyboard.Keyboard()
similarity_trial_steak_A_title = visual.TextStim(win=win, name='similarity_trial_steak_A_title',
    text='PLANT-BASED STEAK A',
    font='Times New Roman',
    pos=(-0.25, -0.05), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
similarity_trial_steak_B_title = visual.TextStim(win=win, name='similarity_trial_steak_B_title',
    text='PLANT-BASED STEAK B',
    font='Times New Roman',
    pos=(0.25, -0.05), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
similarity_trial_missed_trial_text = visual.TextStim(win=win, name='similarity_trial_missed_trial_text',
    text='You have not yet responsed, we really care about your response!\n\n\n\nReminder: press "k" if the right plant-based steak is MORE SIMILAR to a prototypical BEEF STEAK, or "d" if the left plant-based steak is.',
    font='Times New Roman',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
similarity_trial_highlighted_choice = visual.Rect(
    win=win, name='similarity_trial_highlighted_choice',
    width=image_size[0], height=image_size[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1.0, depth=-8.0, interpolate=True)
similarity_trial_end_missed_trial = keyboard.Keyboard()
similarity_reference_title = visual.TextStim(win=win, name='similarity_reference_title',
    text='BEEF STEAK',
    font='Times New Roman',
    pos=(0, 0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
similarity_trial_reference_image = visual.ImageStim(
    win=win,
    name='similarity_trial_reference_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=reference_image_position, size=image_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
similarity_trial_missed_trial_press_space_to_continue = visual.TextStim(win=win, name='similarity_trial_missed_trial_press_space_to_continue',
    text='Press SPACE to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# --- Initialize components for Routine "age_question" ---
age_prompt = visual.TextStim(win=win, name='age_prompt',
    text='What is your age?',
    font='Times New Roman',
    pos=(0, 0.05), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
age_response = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.05),     letterHeight=0.025,
     size=(0.1, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='age_response',
     autoLog=True,
)
age_key_resp = keyboard.Keyboard()
age_press_enter_to_continue = visual.TextStim(win=win, name='age_press_enter_to_continue',
    text='Press ENTER to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "gender_question" ---
gender_prompt = visual.TextStim(win=win, name='gender_prompt',
    text='What is your gender?',
    font='Times New Roman',
    pos=(0, 0.3), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
gender_options = visual.TextStim(win=win, name='gender_options',
    text='1. Male\n\n2. Female\n\n3. Non-binary\n\n4. Prefer not to say\n\n\nPlease type the number in the box below.',
    font='Times New Roman',
    pos=(0, 0.1), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
gender_response = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.15),     letterHeight=0.025,
     size=(0.1, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='gender_response',
     autoLog=True,
)
gender_key_resp = keyboard.Keyboard()
gender_press_enter_to_continue = visual.TextStim(win=win, name='gender_press_enter_to_continue',
    text='Press ENTER to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "frequency_question" ---
frequency_prompt = visual.TextStim(win=win, name='frequency_prompt',
    text='How often do you eat plant-based meat alternatives?',
    font='Times New Roman',
    pos=(0, 0.35), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
frequency_options = visual.TextStim(win=win, name='frequency_options',
    text='1. Never\n\n2. Once every three months\n\n3. Once a month\n\n4. Once a week\n\n5. A couple of times per week\n\n6. Every day\n\nPlease type the number in the box below.',
    font='Times New Roman',
    pos=(0, 0.1), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
frequency_response = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.2),     letterHeight=0.025,
     size=(0.1, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='frequency_response',
     autoLog=True,
)
frequency_key_resp = keyboard.Keyboard()
frequency_press_enter_to_continue = visual.TextStim(win=win, name='frequency_press_enter_to_continue',
    text='Press ENTER to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "feedback_question" ---
feedback_prompt = visual.TextStim(win=win, name='feedback_prompt',
    text='Thank you, the study is almost over. Do you have any feedback for us?',
    font='Times New Roman',
    pos=(0, 0.15), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedback_response = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.2),     letterHeight=0.025,
     size=(0.8, 0.4), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='feedback_response',
     autoLog=True,
)
feedback_key_resp = keyboard.Keyboard()
feedback_press_enter_to_continue = visual.TextStim(win=win, name='feedback_press_enter_to_continue',
    text='Press THE RIGHT ARROW KEY to continue',
    font='Times New Roman',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "end" ---
end_text = visual.TextStim(win=win, name='end_text',
    text='Thank you for your participation!',
    font='Times New Roman',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_experiment = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "routine_0_experiment_conditions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
experiment_conditions_key_resp.keys = []
experiment_conditions_key_resp.rt = []
_experiment_conditions_key_resp_allKeys = []
# keep track of which components have finished
routine_0_experiment_conditionsComponents = [experiment_conditions_text, experiment_conditions_key_resp, experiment_conditions_press_space_to_continue]
for thisComponent in routine_0_experiment_conditionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "routine_0_experiment_conditions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *experiment_conditions_text* updates
    if experiment_conditions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_conditions_text.frameNStart = frameN  # exact frame index
        experiment_conditions_text.tStart = t  # local t and not account for scr refresh
        experiment_conditions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_conditions_text, 'tStartRefresh')  # time at next scr refresh
        experiment_conditions_text.setAutoDraw(True)
    
    # *experiment_conditions_key_resp* updates
    waitOnFlip = False
    if experiment_conditions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_conditions_key_resp.frameNStart = frameN  # exact frame index
        experiment_conditions_key_resp.tStart = t  # local t and not account for scr refresh
        experiment_conditions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_conditions_key_resp, 'tStartRefresh')  # time at next scr refresh
        experiment_conditions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(experiment_conditions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(experiment_conditions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if experiment_conditions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = experiment_conditions_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _experiment_conditions_key_resp_allKeys.extend(theseKeys)
        if len(_experiment_conditions_key_resp_allKeys):
            experiment_conditions_key_resp.keys = _experiment_conditions_key_resp_allKeys[-1].name  # just the last key pressed
            experiment_conditions_key_resp.rt = _experiment_conditions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *experiment_conditions_press_space_to_continue* updates
    if experiment_conditions_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_conditions_press_space_to_continue.frameNStart = frameN  # exact frame index
        experiment_conditions_press_space_to_continue.tStart = t  # local t and not account for scr refresh
        experiment_conditions_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_conditions_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
        experiment_conditions_press_space_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_0_experiment_conditionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "routine_0_experiment_conditions" ---
for thisComponent in routine_0_experiment_conditionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "routine_0_experiment_conditions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "routine_0_experiment_info" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
experiment_info_key_resp.keys = []
experiment_info_key_resp.rt = []
_experiment_info_key_resp_allKeys = []
# keep track of which components have finished
routine_0_experiment_infoComponents = [experiment_info_text, experiment_info_key_resp, experiment_info_press_space_to_continue]
for thisComponent in routine_0_experiment_infoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "routine_0_experiment_info" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *experiment_info_text* updates
    if experiment_info_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_info_text.frameNStart = frameN  # exact frame index
        experiment_info_text.tStart = t  # local t and not account for scr refresh
        experiment_info_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_info_text, 'tStartRefresh')  # time at next scr refresh
        experiment_info_text.setAutoDraw(True)
    
    # *experiment_info_key_resp* updates
    waitOnFlip = False
    if experiment_info_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_info_key_resp.frameNStart = frameN  # exact frame index
        experiment_info_key_resp.tStart = t  # local t and not account for scr refresh
        experiment_info_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_info_key_resp, 'tStartRefresh')  # time at next scr refresh
        experiment_info_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(experiment_info_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(experiment_info_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if experiment_info_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = experiment_info_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _experiment_info_key_resp_allKeys.extend(theseKeys)
        if len(_experiment_info_key_resp_allKeys):
            experiment_info_key_resp.keys = _experiment_info_key_resp_allKeys[-1].name  # just the last key pressed
            experiment_info_key_resp.rt = _experiment_info_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *experiment_info_press_space_to_continue* updates
    if experiment_info_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_info_press_space_to_continue.frameNStart = frameN  # exact frame index
        experiment_info_press_space_to_continue.tStart = t  # local t and not account for scr refresh
        experiment_info_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_info_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
        experiment_info_press_space_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_0_experiment_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "routine_0_experiment_info" ---
for thisComponent in routine_0_experiment_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from experiment_info_code
# recording screen size
thisExp.addData('screen_size', win.size)
# the Routine "routine_0_experiment_info" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "routine_1_informed_consent" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
informed_conset_key_resp.keys = []
informed_conset_key_resp.rt = []
_informed_conset_key_resp_allKeys = []
# Run 'Begin Routine' code from informed_consent_code
# aligning text to the left
informed_consent_text.alignHoriz = "left"
# keep track of which components have finished
routine_1_informed_consentComponents = [informed_conset_key_resp, informed_consent_text, informed_consent_press_space_to_continue]
for thisComponent in routine_1_informed_consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "routine_1_informed_consent" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *informed_conset_key_resp* updates
    waitOnFlip = False
    if informed_conset_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informed_conset_key_resp.frameNStart = frameN  # exact frame index
        informed_conset_key_resp.tStart = t  # local t and not account for scr refresh
        informed_conset_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informed_conset_key_resp, 'tStartRefresh')  # time at next scr refresh
        informed_conset_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(informed_conset_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(informed_conset_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if informed_conset_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = informed_conset_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _informed_conset_key_resp_allKeys.extend(theseKeys)
        if len(_informed_conset_key_resp_allKeys):
            informed_conset_key_resp.keys = _informed_conset_key_resp_allKeys[-1].name  # just the last key pressed
            informed_conset_key_resp.rt = _informed_conset_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *informed_consent_text* updates
    if informed_consent_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informed_consent_text.frameNStart = frameN  # exact frame index
        informed_consent_text.tStart = t  # local t and not account for scr refresh
        informed_consent_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informed_consent_text, 'tStartRefresh')  # time at next scr refresh
        informed_consent_text.setAutoDraw(True)
    
    # *informed_consent_press_space_to_continue* updates
    if informed_consent_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informed_consent_press_space_to_continue.frameNStart = frameN  # exact frame index
        informed_consent_press_space_to_continue.tStart = t  # local t and not account for scr refresh
        informed_consent_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informed_consent_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
        informed_consent_press_space_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_1_informed_consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "routine_1_informed_consent" ---
for thisComponent in routine_1_informed_consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "routine_1_informed_consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "diet_question" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from diet_code
# aligning text to the left
diet_options.alignText = "left"

# only allowing answers from an accepted list
diet_correctKeys = [f"{i}" for i in range(0, 7)]


diet_response.reset()
diet_key_resp.keys = []
diet_key_resp.rt = []
_diet_key_resp_allKeys = []
# keep track of which components have finished
diet_questionComponents = [diet_prompt, diet_options, diet_response, diet_key_resp, diet_press_enter_to_continue]
for thisComponent in diet_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "diet_question" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from diet_code
    # what keys have been pressed this frame?
    keys = diet_response.text
    
    # if any, check that they're the right keys
    if keys:
        if keys not in diet_correctKeys:
            # if they're not valid, remove the last inputted character from the textbox
            diet_response.text = diet_response.text[0:-1]
    
    # if an acceptable answer is given AND return is pressed, continue to next question
    if diet_key_resp.keys == "return" and keys in diet_correctKeys:
        continueRoutine = False
    
    
    # *diet_prompt* updates
    if diet_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        diet_prompt.frameNStart = frameN  # exact frame index
        diet_prompt.tStart = t  # local t and not account for scr refresh
        diet_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(diet_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'diet_prompt.started')
        diet_prompt.setAutoDraw(True)
    
    # *diet_options* updates
    if diet_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        diet_options.frameNStart = frameN  # exact frame index
        diet_options.tStart = t  # local t and not account for scr refresh
        diet_options.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(diet_options, 'tStartRefresh')  # time at next scr refresh
        diet_options.setAutoDraw(True)
    
    # *diet_response* updates
    if diet_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        diet_response.frameNStart = frameN  # exact frame index
        diet_response.tStart = t  # local t and not account for scr refresh
        diet_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(diet_response, 'tStartRefresh')  # time at next scr refresh
        diet_response.setAutoDraw(True)
    
    # *diet_key_resp* updates
    waitOnFlip = False
    if diet_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        diet_key_resp.frameNStart = frameN  # exact frame index
        diet_key_resp.tStart = t  # local t and not account for scr refresh
        diet_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(diet_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'diet_key_resp.started')
        diet_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(diet_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(diet_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if diet_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = diet_key_resp.getKeys(keyList=['return'], waitRelease=False)
        _diet_key_resp_allKeys.extend(theseKeys)
        if len(_diet_key_resp_allKeys):
            diet_key_resp.keys = _diet_key_resp_allKeys[-1].name  # just the last key pressed
            diet_key_resp.rt = _diet_key_resp_allKeys[-1].rt
    
    # *diet_press_enter_to_continue* updates
    if diet_press_enter_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        diet_press_enter_to_continue.frameNStart = frameN  # exact frame index
        diet_press_enter_to_continue.tStart = t  # local t and not account for scr refresh
        diet_press_enter_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(diet_press_enter_to_continue, 'tStartRefresh')  # time at next scr refresh
        diet_press_enter_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in diet_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "diet_question" ---
for thisComponent in diet_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from diet_code
if keys[-1] in ["1", "3"]: # omnivore or flexitarian; for red meat question
    omniflex = True
thisExp.addData('diet_response.text',diet_response.text)
# check responses
if diet_key_resp.keys in ['', [], None]:  # No response was made
    diet_key_resp.keys = None
thisExp.addData('diet_key_resp.keys',diet_key_resp.keys)
if diet_key_resp.keys != None:  # we had a response
    thisExp.addData('diet_key_resp.rt', diet_key_resp.rt)
thisExp.nextEntry()
# the Routine "diet_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "additional_diet_question" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from additional_diet_code
# aligning text to the left
additional_diet_options.alignText = "left"

# only allowing answers from an accepted list
additional_diet_correctKeys = [f"{i}" for i in range(0, 7)]


additional_diet_response.reset()
additional_diet_key_resp.keys = []
additional_diet_key_resp.rt = []
_additional_diet_key_resp_allKeys = []
# keep track of which components have finished
additional_diet_questionComponents = [additional_diet_prompt, additional_diet_options, additional_diet_response, additional_diet_key_resp, additional_diet_press_enter_to_continue]
for thisComponent in additional_diet_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "additional_diet_question" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from additional_diet_code
    # what keys have been pressed this frame?
    keys = additional_diet_response.text
    
    # if any, check that they're the right keys
    if keys:
        if keys not in additional_diet_correctKeys:
            # if they're not valid, remove the last inputted character from the textbox
            additional_diet_response.text = additional_diet_response.text[0:-1]
    
    # if an acceptable answer is given AND return is pressed, continue to next question
    if additional_diet_key_resp.keys == "return" and keys in additional_diet_correctKeys:
        continueRoutine = False
    
    
    # *additional_diet_prompt* updates
    if additional_diet_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        additional_diet_prompt.frameNStart = frameN  # exact frame index
        additional_diet_prompt.tStart = t  # local t and not account for scr refresh
        additional_diet_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(additional_diet_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'additional_diet_prompt.started')
        additional_diet_prompt.setAutoDraw(True)
    
    # *additional_diet_options* updates
    if additional_diet_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        additional_diet_options.frameNStart = frameN  # exact frame index
        additional_diet_options.tStart = t  # local t and not account for scr refresh
        additional_diet_options.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(additional_diet_options, 'tStartRefresh')  # time at next scr refresh
        additional_diet_options.setAutoDraw(True)
    
    # *additional_diet_response* updates
    if additional_diet_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        additional_diet_response.frameNStart = frameN  # exact frame index
        additional_diet_response.tStart = t  # local t and not account for scr refresh
        additional_diet_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(additional_diet_response, 'tStartRefresh')  # time at next scr refresh
        additional_diet_response.setAutoDraw(True)
    
    # *additional_diet_key_resp* updates
    waitOnFlip = False
    if additional_diet_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        additional_diet_key_resp.frameNStart = frameN  # exact frame index
        additional_diet_key_resp.tStart = t  # local t and not account for scr refresh
        additional_diet_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(additional_diet_key_resp, 'tStartRefresh')  # time at next scr refresh
        additional_diet_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(additional_diet_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(additional_diet_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if additional_diet_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = additional_diet_key_resp.getKeys(keyList=['return'], waitRelease=False)
        _additional_diet_key_resp_allKeys.extend(theseKeys)
        if len(_additional_diet_key_resp_allKeys):
            additional_diet_key_resp.keys = _additional_diet_key_resp_allKeys[-1].name  # just the last key pressed
            additional_diet_key_resp.rt = _additional_diet_key_resp_allKeys[-1].rt
    
    # *additional_diet_press_enter_to_continue* updates
    if additional_diet_press_enter_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        additional_diet_press_enter_to_continue.frameNStart = frameN  # exact frame index
        additional_diet_press_enter_to_continue.tStart = t  # local t and not account for scr refresh
        additional_diet_press_enter_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(additional_diet_press_enter_to_continue, 'tStartRefresh')  # time at next scr refresh
        additional_diet_press_enter_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in additional_diet_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "additional_diet_question" ---
for thisComponent in additional_diet_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('additional_diet_response.text',additional_diet_response.text)
# the Routine "additional_diet_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "red_meat_question" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from red_meat_code
#aligning text to the left
red_meat_options.alignText = "left"

# only allowing answers from an accepted list
red_meat_correctKeys = list(["1", "2"])


red_meat_response.reset()
red_meat_key_resp.keys = []
red_meat_key_resp.rt = []
_red_meat_key_resp_allKeys = []
# keep track of which components have finished
red_meat_questionComponents = [red_meat_prompt, red_meat_options, red_meat_response, red_meat_key_resp, red_meat_press_enter_to_continue]
for thisComponent in red_meat_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "red_meat_question" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from red_meat_code
    # what keys have been pressed this frame?
    keys = red_meat_response.text
    
    # if any, check that they're the right keys
    if keys:
        if keys not in red_meat_correctKeys:
            # if they're not valid, remove the last inputted character from the textbox
            red_meat_response.text = red_meat_response.text[0:-1]
    
    # if an acceptable answer is given AND return is pressed, continue to next question
    if red_meat_key_resp.keys == "return" and keys in red_meat_correctKeys:
        continueRoutine = False
    
    
    # *red_meat_prompt* updates
    if red_meat_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_meat_prompt.frameNStart = frameN  # exact frame index
        red_meat_prompt.tStart = t  # local t and not account for scr refresh
        red_meat_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_meat_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'red_meat_prompt.started')
        red_meat_prompt.setAutoDraw(True)
    
    # *red_meat_options* updates
    if red_meat_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_meat_options.frameNStart = frameN  # exact frame index
        red_meat_options.tStart = t  # local t and not account for scr refresh
        red_meat_options.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_meat_options, 'tStartRefresh')  # time at next scr refresh
        red_meat_options.setAutoDraw(True)
    
    # *red_meat_response* updates
    if red_meat_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_meat_response.frameNStart = frameN  # exact frame index
        red_meat_response.tStart = t  # local t and not account for scr refresh
        red_meat_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_meat_response, 'tStartRefresh')  # time at next scr refresh
        red_meat_response.setAutoDraw(True)
    
    # *red_meat_key_resp* updates
    waitOnFlip = False
    if red_meat_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_meat_key_resp.frameNStart = frameN  # exact frame index
        red_meat_key_resp.tStart = t  # local t and not account for scr refresh
        red_meat_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_meat_key_resp, 'tStartRefresh')  # time at next scr refresh
        red_meat_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(red_meat_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(red_meat_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if red_meat_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = red_meat_key_resp.getKeys(keyList=['return'], waitRelease=False)
        _red_meat_key_resp_allKeys.extend(theseKeys)
        if len(_red_meat_key_resp_allKeys):
            red_meat_key_resp.keys = _red_meat_key_resp_allKeys[-1].name  # just the last key pressed
            red_meat_key_resp.rt = _red_meat_key_resp_allKeys[-1].rt
    
    # *red_meat_press_enter_to_continue* updates
    if red_meat_press_enter_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_meat_press_enter_to_continue.frameNStart = frameN  # exact frame index
        red_meat_press_enter_to_continue.tStart = t  # local t and not account for scr refresh
        red_meat_press_enter_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_meat_press_enter_to_continue, 'tStartRefresh')  # time at next scr refresh
        red_meat_press_enter_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in red_meat_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "red_meat_question" ---
for thisComponent in red_meat_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('red_meat_response.text',red_meat_response.text)
# the Routine "red_meat_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "routine_3_pre_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_pre_instructions.keys = []
key_resp_pre_instructions.rt = []
_key_resp_pre_instructions_allKeys = []
# keep track of which components have finished
routine_3_pre_instructionsComponents = [key_resp_pre_instructions, pre_instructions_press_space_to_continue, pre_instructions_text]
for thisComponent in routine_3_pre_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "routine_3_pre_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_pre_instructions* updates
    waitOnFlip = False
    if key_resp_pre_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_pre_instructions.frameNStart = frameN  # exact frame index
        key_resp_pre_instructions.tStart = t  # local t and not account for scr refresh
        key_resp_pre_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_pre_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_pre_instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_pre_instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_pre_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_pre_instructions.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_pre_instructions.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_pre_instructions_allKeys.extend(theseKeys)
        if len(_key_resp_pre_instructions_allKeys):
            key_resp_pre_instructions.keys = _key_resp_pre_instructions_allKeys[-1].name  # just the last key pressed
            key_resp_pre_instructions.rt = _key_resp_pre_instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *pre_instructions_press_space_to_continue* updates
    if pre_instructions_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre_instructions_press_space_to_continue.frameNStart = frameN  # exact frame index
        pre_instructions_press_space_to_continue.tStart = t  # local t and not account for scr refresh
        pre_instructions_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre_instructions_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
        pre_instructions_press_space_to_continue.setAutoDraw(True)
    
    # *pre_instructions_text* updates
    if pre_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre_instructions_text.frameNStart = frameN  # exact frame index
        pre_instructions_text.tStart = t  # local t and not account for scr refresh
        pre_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre_instructions_text, 'tStartRefresh')  # time at next scr refresh
        pre_instructions_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_3_pre_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "routine_3_pre_instructions" ---
for thisComponent in routine_3_pre_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "routine_3_pre_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "routine_4_practice_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
practice_instructions_end.keys = []
practice_instructions_end.rt = []
_practice_instructions_end_allKeys = []
# keep track of which components have finished
routine_4_practice_instructionsComponents = [practice_instructions_image, practice_instructions_end, practice_instructions_press_space_to_continue]
for thisComponent in routine_4_practice_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "routine_4_practice_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_instructions_image* updates
    if practice_instructions_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_instructions_image.frameNStart = frameN  # exact frame index
        practice_instructions_image.tStart = t  # local t and not account for scr refresh
        practice_instructions_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_instructions_image, 'tStartRefresh')  # time at next scr refresh
        practice_instructions_image.setAutoDraw(True)
    
    # *practice_instructions_end* updates
    waitOnFlip = False
    if practice_instructions_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_instructions_end.frameNStart = frameN  # exact frame index
        practice_instructions_end.tStart = t  # local t and not account for scr refresh
        practice_instructions_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_instructions_end, 'tStartRefresh')  # time at next scr refresh
        practice_instructions_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practice_instructions_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practice_instructions_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice_instructions_end.status == STARTED and not waitOnFlip:
        theseKeys = practice_instructions_end.getKeys(keyList=['space'], waitRelease=False)
        _practice_instructions_end_allKeys.extend(theseKeys)
        if len(_practice_instructions_end_allKeys):
            practice_instructions_end.keys = _practice_instructions_end_allKeys[-1].name  # just the last key pressed
            practice_instructions_end.rt = _practice_instructions_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *practice_instructions_press_space_to_continue* updates
    if practice_instructions_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_instructions_press_space_to_continue.frameNStart = frameN  # exact frame index
        practice_instructions_press_space_to_continue.tStart = t  # local t and not account for scr refresh
        practice_instructions_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_instructions_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
        practice_instructions_press_space_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_4_practice_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "routine_4_practice_instructions" ---
for thisComponent in routine_4_practice_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "routine_4_practice_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_practice = data.TrialHandler(nReps=length_of_practice_trials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_practice')
thisExp.addLoop(trials_practice)  # add the loop to the experiment
thisTrials_practice = trials_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
if thisTrials_practice != None:
    for paramName in thisTrials_practice:
        exec('{} = thisTrials_practice[paramName]'.format(paramName))

for thisTrials_practice in trials_practice:
    currentLoop = trials_practice
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
    if thisTrials_practice != None:
        for paramName in thisTrials_practice:
            exec('{} = thisTrials_practice[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "practice_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from practice_trial_code
    # start characteristics for choice square
    # once a choice is given, square turns blue and surrounds chosen image
    choice_position = [0,-1]
    border_color = "white"
    practice_trial_highlighted_choice.fillColor = None
    
    # aligning text to the left
    practice_trial_missed_trial_text.alignText = "left"
    
    # setting images for this trial
    practice_trial_left_img = practice_path + practice_stimuli[practice_index][0]
    practice_trial_right_img = practice_path + practice_stimuli[practice_index][1]
    
    # recording response time
    response_time = None
    practice_trial_left_image.setImage(practice_trial_left_img)
    practice_trial_right_image.setImage(practice_trial_right_img)
    practice_trial_choice.keys = []
    practice_trial_choice.rt = []
    _practice_trial_choice_allKeys = []
    practice_trial_end_missed_trial_resp.keys = []
    practice_trial_end_missed_trial_resp.rt = []
    _practice_trial_end_missed_trial_resp_allKeys = []
    # keep track of which components have finished
    practice_trialComponents = [practice_trial_question, practice_trial_left_image, practice_trial_right_image, practice_trial_choice, practice_trial_fruit_A, practice_trial_fruit_B, practice_trial_highlighted_choice, practice_trial_missed_trial_text, practice_trial_end_missed_trial_resp, practice_trial_missed_trial_press_space_to_continue]
    for thisComponent in practice_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_trial_question* updates
        if practice_trial_question.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_question.frameNStart = frameN  # exact frame index
            practice_trial_question.tStart = t  # local t and not account for scr refresh
            practice_trial_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_question.started')
            practice_trial_question.setAutoDraw(True)
        if practice_trial_question.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_trial_question.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                practice_trial_question.tStop = t  # not accounting for scr refresh
                practice_trial_question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_trial_question.stopped')
                practice_trial_question.setAutoDraw(False)
        # Run 'Each Frame' code from practice_trial_code
        # setting where choice square should move to
        if practice_trial_choice.keys:
            if practice_trial_choice.keys[0] == "d":
                border_color = "blue"
                choice_position = left_image_position
                
            elif practice_trial_choice.keys[0] == "k":
                border_color = "blue"
                choice_position = right_image_position
            
        # Check if a key was pressed and record time
        if practice_trial_choice.keys and response_time is None:
            response_time = t  # `t` is the current time in the routine
        
        # Check if 1 second has passed since response
        if response_time is not None and t - response_time >= 0.5:
            border_color = "white"
            continueRoutine = False
        
        # *practice_trial_left_image* updates
        if practice_trial_left_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_left_image.frameNStart = frameN  # exact frame index
            practice_trial_left_image.tStart = t  # local t and not account for scr refresh
            practice_trial_left_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_left_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_left_image.started')
            practice_trial_left_image.setAutoDraw(True)
        if practice_trial_left_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_trial_left_image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                practice_trial_left_image.tStop = t  # not accounting for scr refresh
                practice_trial_left_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_trial_left_image.stopped')
                practice_trial_left_image.setAutoDraw(False)
        
        # *practice_trial_right_image* updates
        if practice_trial_right_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_right_image.frameNStart = frameN  # exact frame index
            practice_trial_right_image.tStart = t  # local t and not account for scr refresh
            practice_trial_right_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_right_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_right_image.started')
            practice_trial_right_image.setAutoDraw(True)
        if practice_trial_right_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_trial_right_image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                practice_trial_right_image.tStop = t  # not accounting for scr refresh
                practice_trial_right_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_trial_right_image.stopped')
                practice_trial_right_image.setAutoDraw(False)
        
        # *practice_trial_choice* updates
        waitOnFlip = False
        if practice_trial_choice.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_choice.frameNStart = frameN  # exact frame index
            practice_trial_choice.tStart = t  # local t and not account for scr refresh
            practice_trial_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_choice.started')
            practice_trial_choice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practice_trial_choice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practice_trial_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_trial_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_trial_choice.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                practice_trial_choice.tStop = t  # not accounting for scr refresh
                practice_trial_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_trial_choice.stopped')
                practice_trial_choice.status = FINISHED
        if practice_trial_choice.status == STARTED and not waitOnFlip:
            theseKeys = practice_trial_choice.getKeys(keyList=['d','k'], waitRelease=False)
            _practice_trial_choice_allKeys.extend(theseKeys)
            if len(_practice_trial_choice_allKeys):
                practice_trial_choice.keys = _practice_trial_choice_allKeys[0].name  # just the first key pressed
                practice_trial_choice.rt = _practice_trial_choice_allKeys[0].rt
        
        # *practice_trial_fruit_A* updates
        if practice_trial_fruit_A.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_fruit_A.frameNStart = frameN  # exact frame index
            practice_trial_fruit_A.tStart = t  # local t and not account for scr refresh
            practice_trial_fruit_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_fruit_A, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_fruit_A.started')
            practice_trial_fruit_A.setAutoDraw(True)
        if practice_trial_fruit_A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_trial_fruit_A.tStartRefresh + 4.25-frameTolerance:
                # keep track of stop time/frame for later
                practice_trial_fruit_A.tStop = t  # not accounting for scr refresh
                practice_trial_fruit_A.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_trial_fruit_A.stopped')
                practice_trial_fruit_A.setAutoDraw(False)
        
        # *practice_trial_fruit_B* updates
        if practice_trial_fruit_B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_fruit_B.frameNStart = frameN  # exact frame index
            practice_trial_fruit_B.tStart = t  # local t and not account for scr refresh
            practice_trial_fruit_B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_fruit_B, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_fruit_B.started')
            practice_trial_fruit_B.setAutoDraw(True)
        if practice_trial_fruit_B.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_trial_fruit_B.tStartRefresh + 4.25-frameTolerance:
                # keep track of stop time/frame for later
                practice_trial_fruit_B.tStop = t  # not accounting for scr refresh
                practice_trial_fruit_B.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_trial_fruit_B.stopped')
                practice_trial_fruit_B.setAutoDraw(False)
        
        # *practice_trial_highlighted_choice* updates
        if practice_trial_highlighted_choice.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_highlighted_choice.frameNStart = frameN  # exact frame index
            practice_trial_highlighted_choice.tStart = t  # local t and not account for scr refresh
            practice_trial_highlighted_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_highlighted_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_highlighted_choice.started')
            practice_trial_highlighted_choice.setAutoDraw(True)
        if practice_trial_highlighted_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_trial_highlighted_choice.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                practice_trial_highlighted_choice.tStop = t  # not accounting for scr refresh
                practice_trial_highlighted_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_trial_highlighted_choice.stopped')
                practice_trial_highlighted_choice.setAutoDraw(False)
        if practice_trial_highlighted_choice.status == STARTED:  # only update if drawing
            practice_trial_highlighted_choice.setPos(choice_position, log=False)
            practice_trial_highlighted_choice.setLineColor(border_color, log=False)
        
        # *practice_trial_missed_trial_text* updates
        if practice_trial_missed_trial_text.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_missed_trial_text.frameNStart = frameN  # exact frame index
            practice_trial_missed_trial_text.tStart = t  # local t and not account for scr refresh
            practice_trial_missed_trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_missed_trial_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_missed_trial_text.started')
            practice_trial_missed_trial_text.setAutoDraw(True)
        
        # *practice_trial_end_missed_trial_resp* updates
        waitOnFlip = False
        if practice_trial_end_missed_trial_resp.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_end_missed_trial_resp.frameNStart = frameN  # exact frame index
            practice_trial_end_missed_trial_resp.tStart = t  # local t and not account for scr refresh
            practice_trial_end_missed_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_end_missed_trial_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_trial_end_missed_trial_resp.started')
            practice_trial_end_missed_trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practice_trial_end_missed_trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practice_trial_end_missed_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_trial_end_missed_trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = practice_trial_end_missed_trial_resp.getKeys(keyList=['space'], waitRelease=False)
            _practice_trial_end_missed_trial_resp_allKeys.extend(theseKeys)
            if len(_practice_trial_end_missed_trial_resp_allKeys):
                practice_trial_end_missed_trial_resp.keys = _practice_trial_end_missed_trial_resp_allKeys[-1].name  # just the last key pressed
                practice_trial_end_missed_trial_resp.rt = _practice_trial_end_missed_trial_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *practice_trial_missed_trial_press_space_to_continue* updates
        if practice_trial_missed_trial_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            practice_trial_missed_trial_press_space_to_continue.frameNStart = frameN  # exact frame index
            practice_trial_missed_trial_press_space_to_continue.tStart = t  # local t and not account for scr refresh
            practice_trial_missed_trial_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_trial_missed_trial_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
            practice_trial_missed_trial_press_space_to_continue.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial" ---
    for thisComponent in practice_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from practice_trial_code
    #Data logging
    # if response is not given, record as missed trial
    if practice_trial_choice.keys == "":
        trial_type = "practice-missed"
    
    else:
        trial_type = "practice"
        
    thisExp.addData("Trial Type", trial_type)
    thisExp.addData("Left Image", practice_stimuli[practice_index][0])
    thisExp.addData("Right Image", practice_stimuli[practice_index][1])
    
    # move onto next pair
    if practice_trial_choice or practice_trial_end_missed_trial:
        practice_index += 1
    
    
    # check responses
    if practice_trial_choice.keys in ['', [], None]:  # No response was made
        practice_trial_choice.keys = None
    trials_practice.addData('practice_trial_choice.keys',practice_trial_choice.keys)
    if practice_trial_choice.keys != None:  # we had a response
        trials_practice.addData('practice_trial_choice.rt', practice_trial_choice.rt)
    # check responses
    if practice_trial_end_missed_trial_resp.keys in ['', [], None]:  # No response was made
        practice_trial_end_missed_trial_resp.keys = None
    trials_practice.addData('practice_trial_end_missed_trial_resp.keys',practice_trial_end_missed_trial_resp.keys)
    if practice_trial_end_missed_trial_resp.keys != None:  # we had a response
        trials_practice.addData('practice_trial_end_missed_trial_resp.rt', practice_trial_end_missed_trial_resp.rt)
    # the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed length_of_practice_trials repeats of 'trials_practice'


# --- Prepare to start Routine "practice_trial_attention_check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from practice_trial_attention_check_code
# recording response time
response_time = None

# check is not failed 
this_check_failed = False

practice_trial_attention_check_left_image.setImage(practice_attention_check_image)
practice_trial_attention_check_right_image.setImage(practice_attention_check_image)
practice_trial_attention_check_choice.keys = []
practice_trial_attention_check_choice.rt = []
_practice_trial_attention_check_choice_allKeys = []
# keep track of which components have finished
practice_trial_attention_checkComponents = [practice_trial_attention_check_question, practice_trial_attention_check_left_image, practice_trial_attention_check_right_image, practice_trial_attention_check_choice, practice_trial_attention_check_fruit_A, practice_trial_attention_check_fruit_B]
for thisComponent in practice_trial_attention_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "practice_trial_attention_check" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_trial_attention_check_question* updates
    if practice_trial_attention_check_question.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        practice_trial_attention_check_question.frameNStart = frameN  # exact frame index
        practice_trial_attention_check_question.tStart = t  # local t and not account for scr refresh
        practice_trial_attention_check_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_trial_attention_check_question, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'practice_trial_attention_check_question.started')
        practice_trial_attention_check_question.setAutoDraw(True)
    # Run 'Each Frame' code from practice_trial_attention_check_code
    # Check if a key was pressed and record time
    if practice_trial_attention_check_choice.keys and response_time is None:
        response_time = t  # `t` is the current time in the routine
    
    # Check if 1 second has passed since response
    if practice_trial_attention_check_choice.keys:
        #if practice_trial_attention_check_choice.keys[0] == "q":
        if response_time is not None and t - response_time >= 1:
            continueRoutine = False
    
    # *practice_trial_attention_check_left_image* updates
    if practice_trial_attention_check_left_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        practice_trial_attention_check_left_image.frameNStart = frameN  # exact frame index
        practice_trial_attention_check_left_image.tStart = t  # local t and not account for scr refresh
        practice_trial_attention_check_left_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_trial_attention_check_left_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'practice_trial_attention_check_left_image.started')
        practice_trial_attention_check_left_image.setAutoDraw(True)
    
    # *practice_trial_attention_check_right_image* updates
    if practice_trial_attention_check_right_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        practice_trial_attention_check_right_image.frameNStart = frameN  # exact frame index
        practice_trial_attention_check_right_image.tStart = t  # local t and not account for scr refresh
        practice_trial_attention_check_right_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_trial_attention_check_right_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'practice_trial_attention_check_right_image.started')
        practice_trial_attention_check_right_image.setAutoDraw(True)
    
    # *practice_trial_attention_check_choice* updates
    waitOnFlip = False
    if practice_trial_attention_check_choice.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        practice_trial_attention_check_choice.frameNStart = frameN  # exact frame index
        practice_trial_attention_check_choice.tStart = t  # local t and not account for scr refresh
        practice_trial_attention_check_choice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_trial_attention_check_choice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'practice_trial_attention_check_choice.started')
        practice_trial_attention_check_choice.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practice_trial_attention_check_choice.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practice_trial_attention_check_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice_trial_attention_check_choice.status == STARTED and not waitOnFlip:
        theseKeys = practice_trial_attention_check_choice.getKeys(keyList=None, waitRelease=False)
        _practice_trial_attention_check_choice_allKeys.extend(theseKeys)
        if len(_practice_trial_attention_check_choice_allKeys):
            practice_trial_attention_check_choice.keys = [key.name for key in _practice_trial_attention_check_choice_allKeys]  # storing all keys
            practice_trial_attention_check_choice.rt = [key.rt for key in _practice_trial_attention_check_choice_allKeys]
    
    # *practice_trial_attention_check_fruit_A* updates
    if practice_trial_attention_check_fruit_A.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        practice_trial_attention_check_fruit_A.frameNStart = frameN  # exact frame index
        practice_trial_attention_check_fruit_A.tStart = t  # local t and not account for scr refresh
        practice_trial_attention_check_fruit_A.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_trial_attention_check_fruit_A, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'practice_trial_attention_check_fruit_A.started')
        practice_trial_attention_check_fruit_A.setAutoDraw(True)
    
    # *practice_trial_attention_check_fruit_B* updates
    if practice_trial_attention_check_fruit_B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        practice_trial_attention_check_fruit_B.frameNStart = frameN  # exact frame index
        practice_trial_attention_check_fruit_B.tStart = t  # local t and not account for scr refresh
        practice_trial_attention_check_fruit_B.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_trial_attention_check_fruit_B, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'practice_trial_attention_check_fruit_B.started')
        practice_trial_attention_check_fruit_B.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_trial_attention_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practice_trial_attention_check" ---
for thisComponent in practice_trial_attention_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from practice_trial_attention_check_code
#Data logging

thisExp.addData("Left Image", practice_attention_random_choice)
thisExp.addData("Right Image", practice_attention_random_choice)
thisExp.addData("Trial Type", "attention-check")

#if continueRoutine == True:
if practice_trial_attention_check_choice.keys:
    if practice_trial_attention_check_choice.keys[0] != "q":
        # this is a practice attention check, so even if missed, does not count
        #attention_checks_failed += 1
        this_check_failed = True

#else:
#    attention_checks_failed += 1

thisExp.addData("checks failed", attention_checks_failed)
thisExp.addData("this check failed", this_check_failed)

# check responses
if practice_trial_attention_check_choice.keys in ['', [], None]:  # No response was made
    practice_trial_attention_check_choice.keys = None
thisExp.addData('practice_trial_attention_check_choice.keys',practice_trial_attention_check_choice.keys)
if practice_trial_attention_check_choice.keys != None:  # we had a response
    thisExp.addData('practice_trial_attention_check_choice.rt', practice_trial_attention_check_choice.rt)
thisExp.nextEntry()
# the Routine "practice_trial_attention_check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "failed_attention_check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from missed_attention_check_code
# show this screen only if attention check was failed
if this_check_failed == False:
    continueRoutine = False

elif this_check_failed == True and attention_checks_failed > 1:
    continueRoutine = False

# aligning text to the left
missed_attention_check_text.alignText = "left"

# recording response time
response_time = None
missed_attention_check_resp.keys = []
missed_attention_check_resp.rt = []
_missed_attention_check_resp_allKeys = []
# keep track of which components have finished
failed_attention_checkComponents = [missed_attention_check_text, missed_attention_check_resp, missed_attention_check_press_space_to_continue]
for thisComponent in failed_attention_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "failed_attention_check" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *missed_attention_check_text* updates
    if missed_attention_check_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        missed_attention_check_text.frameNStart = frameN  # exact frame index
        missed_attention_check_text.tStart = t  # local t and not account for scr refresh
        missed_attention_check_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(missed_attention_check_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'missed_attention_check_text.started')
        missed_attention_check_text.setAutoDraw(True)
    
    # *missed_attention_check_resp* updates
    waitOnFlip = False
    if missed_attention_check_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        missed_attention_check_resp.frameNStart = frameN  # exact frame index
        missed_attention_check_resp.tStart = t  # local t and not account for scr refresh
        missed_attention_check_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(missed_attention_check_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'missed_attention_check_resp.started')
        missed_attention_check_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(missed_attention_check_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(missed_attention_check_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if missed_attention_check_resp.status == STARTED and not waitOnFlip:
        theseKeys = missed_attention_check_resp.getKeys(keyList=['space'], waitRelease=False)
        _missed_attention_check_resp_allKeys.extend(theseKeys)
        if len(_missed_attention_check_resp_allKeys):
            missed_attention_check_resp.keys = _missed_attention_check_resp_allKeys[-1].name  # just the last key pressed
            missed_attention_check_resp.rt = _missed_attention_check_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *missed_attention_check_press_space_to_continue* updates
    if missed_attention_check_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        missed_attention_check_press_space_to_continue.frameNStart = frameN  # exact frame index
        missed_attention_check_press_space_to_continue.tStart = t  # local t and not account for scr refresh
        missed_attention_check_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(missed_attention_check_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
        missed_attention_check_press_space_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in failed_attention_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "failed_attention_check" ---
for thisComponent in failed_attention_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from missed_attention_check_code
#Data logging
thisExp.addData("checks failed", attention_checks_failed)

# check responses
if missed_attention_check_resp.keys in ['', [], None]:  # No response was made
    missed_attention_check_resp.keys = None
thisExp.addData('missed_attention_check_resp.keys',missed_attention_check_resp.keys)
if missed_attention_check_resp.keys != None:  # we had a response
    thisExp.addData('missed_attention_check_resp.rt', missed_attention_check_resp.rt)
thisExp.nextEntry()
# the Routine "failed_attention_check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "routine_4_practice_aftermath" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
practice_aftermath_end.keys = []
practice_aftermath_end.rt = []
_practice_aftermath_end_allKeys = []
# Run 'Begin Routine' code from practice_aftermath_code
# aligning text to the left
practice_aftermath_text.alignText = "left"
# keep track of which components have finished
routine_4_practice_aftermathComponents = [practice_aftermath_press_space_to_continue, practice_aftermath_end, practice_aftermath_text]
for thisComponent in routine_4_practice_aftermathComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "routine_4_practice_aftermath" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_aftermath_press_space_to_continue* updates
    if practice_aftermath_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_aftermath_press_space_to_continue.frameNStart = frameN  # exact frame index
        practice_aftermath_press_space_to_continue.tStart = t  # local t and not account for scr refresh
        practice_aftermath_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_aftermath_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
        practice_aftermath_press_space_to_continue.setAutoDraw(True)
    
    # *practice_aftermath_end* updates
    waitOnFlip = False
    if practice_aftermath_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_aftermath_end.frameNStart = frameN  # exact frame index
        practice_aftermath_end.tStart = t  # local t and not account for scr refresh
        practice_aftermath_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_aftermath_end, 'tStartRefresh')  # time at next scr refresh
        practice_aftermath_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practice_aftermath_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practice_aftermath_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice_aftermath_end.status == STARTED and not waitOnFlip:
        theseKeys = practice_aftermath_end.getKeys(keyList=['space'], waitRelease=False)
        _practice_aftermath_end_allKeys.extend(theseKeys)
        if len(_practice_aftermath_end_allKeys):
            practice_aftermath_end.keys = _practice_aftermath_end_allKeys[-1].name  # just the last key pressed
            practice_aftermath_end.rt = _practice_aftermath_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *practice_aftermath_text* updates
    if practice_aftermath_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_aftermath_text.frameNStart = frameN  # exact frame index
        practice_aftermath_text.tStart = t  # local t and not account for scr refresh
        practice_aftermath_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_aftermath_text, 'tStartRefresh')  # time at next scr refresh
        practice_aftermath_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_4_practice_aftermathComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "routine_4_practice_aftermath" ---
for thisComponent in routine_4_practice_aftermathComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "routine_4_practice_aftermath" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_liking_instructions = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_liking_instructions')
thisExp.addLoop(trials_liking_instructions)  # add the loop to the experiment
thisTrials_liking_instruction = trials_liking_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_liking_instruction.rgb)
if thisTrials_liking_instruction != None:
    for paramName in thisTrials_liking_instruction:
        exec('{} = thisTrials_liking_instruction[paramName]'.format(paramName))

for thisTrials_liking_instruction in trials_liking_instructions:
    currentLoop = trials_liking_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_liking_instruction.rgb)
    if thisTrials_liking_instruction != None:
        for paramName in thisTrials_liking_instruction:
            exec('{} = thisTrials_liking_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "routine_6_liking_instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    liking_instructions_space.keys = []
    liking_instructions_space.rt = []
    _liking_instructions_space_allKeys = []
    # Run 'Begin Routine' code from liking_instructions_code
    liking_instructions_img = "texts/" + str(liking_instructions[liking_instructions_index])
    
    if liking_instructions_space:
        liking_instructions_index += 1
    liking_instructions_image.setImage(liking_instructions_img)
    # keep track of which components have finished
    routine_6_liking_instructionsComponents = [liking_instructions_space, liking_instructions_image, liking_instructions_press_space_to_continue]
    for thisComponent in routine_6_liking_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_6_liking_instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *liking_instructions_space* updates
        waitOnFlip = False
        if liking_instructions_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            liking_instructions_space.frameNStart = frameN  # exact frame index
            liking_instructions_space.tStart = t  # local t and not account for scr refresh
            liking_instructions_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_instructions_space, 'tStartRefresh')  # time at next scr refresh
            liking_instructions_space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(liking_instructions_space.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(liking_instructions_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if liking_instructions_space.status == STARTED and not waitOnFlip:
            theseKeys = liking_instructions_space.getKeys(keyList=['space'], waitRelease=False)
            _liking_instructions_space_allKeys.extend(theseKeys)
            if len(_liking_instructions_space_allKeys):
                liking_instructions_space.keys = _liking_instructions_space_allKeys[-1].name  # just the last key pressed
                liking_instructions_space.rt = _liking_instructions_space_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *liking_instructions_image* updates
        if liking_instructions_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            liking_instructions_image.frameNStart = frameN  # exact frame index
            liking_instructions_image.tStart = t  # local t and not account for scr refresh
            liking_instructions_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_instructions_image, 'tStartRefresh')  # time at next scr refresh
            liking_instructions_image.setAutoDraw(True)
        
        # *liking_instructions_press_space_to_continue* updates
        if liking_instructions_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            liking_instructions_press_space_to_continue.frameNStart = frameN  # exact frame index
            liking_instructions_press_space_to_continue.tStart = t  # local t and not account for scr refresh
            liking_instructions_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_instructions_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
            liking_instructions_press_space_to_continue.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_6_liking_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_6_liking_instructions" ---
    for thisComponent in routine_6_liking_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "routine_6_liking_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_liking_instructions'


# set up handler to look after randomisation of conditions etc
trials_liking = data.TrialHandler(nReps=length_of_experimental_trials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_liking')
thisExp.addLoop(trials_liking)  # add the loop to the experiment
thisTrials_liking = trials_liking.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_liking.rgb)
if thisTrials_liking != None:
    for paramName in thisTrials_liking:
        exec('{} = thisTrials_liking[paramName]'.format(paramName))

for thisTrials_liking in trials_liking:
    currentLoop = trials_liking
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_liking.rgb)
    if thisTrials_liking != None:
        for paramName in thisTrials_liking:
            exec('{} = thisTrials_liking[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "liking_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from liking_trial_code
    # start characteristics for choice square
    # once a choice is given, square turns blue and surrounds chosen image
    border_color = "white"
    choice_position = [0,-1]
    liking_trial_highlighted_choice.fillColor = None
    
    # aligning text to the left
    liking_trial_missed_trial_text.alignText = "left"
    
    # setting images for this trial
    liking_trial_left_img = experimental_path + experimental_stimuli[stimulus_index_liking][0]
    liking_trial_right_img = experimental_path + experimental_stimuli[stimulus_index_liking][1]
    
    # recording response time
    response_time = None
    liking_trial_left_image.setImage(liking_trial_left_img)
    liking_trial_right_image.setImage(liking_trial_right_img)
    liking_trial_choice.keys = []
    liking_trial_choice.rt = []
    _liking_trial_choice_allKeys = []
    liking_trial_end_missed_trial_resp.keys = []
    liking_trial_end_missed_trial_resp.rt = []
    _liking_trial_end_missed_trial_resp_allKeys = []
    # keep track of which components have finished
    liking_trialComponents = [liking_trial_question, liking_trial_left_image, liking_trial_right_image, liking_trial_choice, liking_trial_steak_A_title, liking_trial_steak_B_title, liking_trial_missed_trial_text, liking_trial_highlighted_choice, liking_trial_end_missed_trial_resp, liking_trial_missed_trial_press_space_to_continue]
    for thisComponent in liking_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "liking_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *liking_trial_question* updates
        if liking_trial_question.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_question.frameNStart = frameN  # exact frame index
            liking_trial_question.tStart = t  # local t and not account for scr refresh
            liking_trial_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_question.started')
            liking_trial_question.setAutoDraw(True)
        if liking_trial_question.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > liking_trial_question.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                liking_trial_question.tStop = t  # not accounting for scr refresh
                liking_trial_question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'liking_trial_question.stopped')
                liking_trial_question.setAutoDraw(False)
        # Run 'Each Frame' code from liking_trial_code
        # start characteristics for choice square
        # once a choice is given, square turns blue and surrounds chosen image
        if liking_trial_choice.keys:
            if liking_trial_choice.keys[0] == "d":
                border_color = "blue"
                choice_position = left_image_position
                
            elif liking_trial_choice.keys[0] == "k":
                border_color = "blue"
                choice_position = right_image_position
            
        # Check if a key was pressed and record time
        if liking_trial_choice.keys and response_time is None:
            response_time = t  # `t` is the current time in the routine
        
        # Check if 1 second has passed since response
        if response_time is not None and t - response_time >= 0.5:
            border_color = "white"
            continueRoutine = False
        
        # *liking_trial_left_image* updates
        if liking_trial_left_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_left_image.frameNStart = frameN  # exact frame index
            liking_trial_left_image.tStart = t  # local t and not account for scr refresh
            liking_trial_left_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_left_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_left_image.started')
            liking_trial_left_image.setAutoDraw(True)
        if liking_trial_left_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > liking_trial_left_image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                liking_trial_left_image.tStop = t  # not accounting for scr refresh
                liking_trial_left_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'liking_trial_left_image.stopped')
                liking_trial_left_image.setAutoDraw(False)
        
        # *liking_trial_right_image* updates
        if liking_trial_right_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_right_image.frameNStart = frameN  # exact frame index
            liking_trial_right_image.tStart = t  # local t and not account for scr refresh
            liking_trial_right_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_right_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_right_image.started')
            liking_trial_right_image.setAutoDraw(True)
        if liking_trial_right_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > liking_trial_right_image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                liking_trial_right_image.tStop = t  # not accounting for scr refresh
                liking_trial_right_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'liking_trial_right_image.stopped')
                liking_trial_right_image.setAutoDraw(False)
        
        # *liking_trial_choice* updates
        waitOnFlip = False
        if liking_trial_choice.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_choice.frameNStart = frameN  # exact frame index
            liking_trial_choice.tStart = t  # local t and not account for scr refresh
            liking_trial_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_choice.started')
            liking_trial_choice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(liking_trial_choice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(liking_trial_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if liking_trial_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > liking_trial_choice.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                liking_trial_choice.tStop = t  # not accounting for scr refresh
                liking_trial_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'liking_trial_choice.stopped')
                liking_trial_choice.status = FINISHED
        if liking_trial_choice.status == STARTED and not waitOnFlip:
            theseKeys = liking_trial_choice.getKeys(keyList=['d','k'], waitRelease=False)
            _liking_trial_choice_allKeys.extend(theseKeys)
            if len(_liking_trial_choice_allKeys):
                liking_trial_choice.keys = _liking_trial_choice_allKeys[0].name  # just the first key pressed
                liking_trial_choice.rt = _liking_trial_choice_allKeys[0].rt
        
        # *liking_trial_steak_A_title* updates
        if liking_trial_steak_A_title.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_steak_A_title.frameNStart = frameN  # exact frame index
            liking_trial_steak_A_title.tStart = t  # local t and not account for scr refresh
            liking_trial_steak_A_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_steak_A_title, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_steak_A_title.started')
            liking_trial_steak_A_title.setAutoDraw(True)
        if liking_trial_steak_A_title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > liking_trial_steak_A_title.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                liking_trial_steak_A_title.tStop = t  # not accounting for scr refresh
                liking_trial_steak_A_title.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'liking_trial_steak_A_title.stopped')
                liking_trial_steak_A_title.setAutoDraw(False)
        
        # *liking_trial_steak_B_title* updates
        if liking_trial_steak_B_title.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_steak_B_title.frameNStart = frameN  # exact frame index
            liking_trial_steak_B_title.tStart = t  # local t and not account for scr refresh
            liking_trial_steak_B_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_steak_B_title, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_steak_B_title.started')
            liking_trial_steak_B_title.setAutoDraw(True)
        if liking_trial_steak_B_title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > liking_trial_steak_B_title.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                liking_trial_steak_B_title.tStop = t  # not accounting for scr refresh
                liking_trial_steak_B_title.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'liking_trial_steak_B_title.stopped')
                liking_trial_steak_B_title.setAutoDraw(False)
        
        # *liking_trial_missed_trial_text* updates
        if liking_trial_missed_trial_text.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_missed_trial_text.frameNStart = frameN  # exact frame index
            liking_trial_missed_trial_text.tStart = t  # local t and not account for scr refresh
            liking_trial_missed_trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_missed_trial_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_missed_trial_text.started')
            liking_trial_missed_trial_text.setAutoDraw(True)
        
        # *liking_trial_highlighted_choice* updates
        if liking_trial_highlighted_choice.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_highlighted_choice.frameNStart = frameN  # exact frame index
            liking_trial_highlighted_choice.tStart = t  # local t and not account for scr refresh
            liking_trial_highlighted_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_highlighted_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_highlighted_choice.started')
            liking_trial_highlighted_choice.setAutoDraw(True)
        if liking_trial_highlighted_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > liking_trial_highlighted_choice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                liking_trial_highlighted_choice.tStop = t  # not accounting for scr refresh
                liking_trial_highlighted_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'liking_trial_highlighted_choice.stopped')
                liking_trial_highlighted_choice.setAutoDraw(False)
        if liking_trial_highlighted_choice.status == STARTED:  # only update if drawing
            liking_trial_highlighted_choice.setPos(choice_position, log=False)
            liking_trial_highlighted_choice.setLineColor(border_color, log=False)
        
        # *liking_trial_end_missed_trial_resp* updates
        waitOnFlip = False
        if liking_trial_end_missed_trial_resp.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_end_missed_trial_resp.frameNStart = frameN  # exact frame index
            liking_trial_end_missed_trial_resp.tStart = t  # local t and not account for scr refresh
            liking_trial_end_missed_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_end_missed_trial_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'liking_trial_end_missed_trial_resp.started')
            liking_trial_end_missed_trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(liking_trial_end_missed_trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(liking_trial_end_missed_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if liking_trial_end_missed_trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = liking_trial_end_missed_trial_resp.getKeys(keyList=['space'], waitRelease=False)
            _liking_trial_end_missed_trial_resp_allKeys.extend(theseKeys)
            if len(_liking_trial_end_missed_trial_resp_allKeys):
                liking_trial_end_missed_trial_resp.keys = _liking_trial_end_missed_trial_resp_allKeys[-1].name  # just the last key pressed
                liking_trial_end_missed_trial_resp.rt = _liking_trial_end_missed_trial_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *liking_trial_missed_trial_press_space_to_continue* updates
        if liking_trial_missed_trial_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            liking_trial_missed_trial_press_space_to_continue.frameNStart = frameN  # exact frame index
            liking_trial_missed_trial_press_space_to_continue.tStart = t  # local t and not account for scr refresh
            liking_trial_missed_trial_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(liking_trial_missed_trial_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
            liking_trial_missed_trial_press_space_to_continue.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in liking_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "liking_trial" ---
    for thisComponent in liking_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from liking_trial_code
    #Data logging
    # if response is not given, record as missed trial
    if liking_trial_choice.keys == "":
        trial_type = "liking-missed"
    
    else:
        trial_type = "liking"
        
    thisExp.addData("Trial Type", trial_type)
    thisExp.addData("Left Image", experimental_stimuli[stimulus_index_liking][0])
    thisExp.addData("Right Image", experimental_stimuli[stimulus_index_liking][1])
    
    # move onto next pair
    if liking_trial_choice or liking_trial_end_missed_trial:
        stimulus_index_liking += 1
    # check responses
    if liking_trial_choice.keys in ['', [], None]:  # No response was made
        liking_trial_choice.keys = None
    trials_liking.addData('liking_trial_choice.keys',liking_trial_choice.keys)
    if liking_trial_choice.keys != None:  # we had a response
        trials_liking.addData('liking_trial_choice.rt', liking_trial_choice.rt)
    # check responses
    if liking_trial_end_missed_trial_resp.keys in ['', [], None]:  # No response was made
        liking_trial_end_missed_trial_resp.keys = None
    trials_liking.addData('liking_trial_end_missed_trial_resp.keys',liking_trial_end_missed_trial_resp.keys)
    if liking_trial_end_missed_trial_resp.keys != None:  # we had a response
        trials_liking.addData('liking_trial_end_missed_trial_resp.rt', liking_trial_end_missed_trial_resp.rt)
    # the Routine "liking_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed length_of_experimental_trials repeats of 'trials_liking'


# --- Prepare to start Routine "liking_trial_attention_check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from liking_trial_attention_check_code
#liking_trial_missed_attention_check_text.alignHoriz = "left"

response_time = None

this_check_failed = False
liking_trial_attention_check_left_image.setImage(liking_attention_check_image)
liking_trial_attention_check_right_image.setImage(liking_attention_check_image)
liking_trial_attention_check_choice.keys = []
liking_trial_attention_check_choice.rt = []
_liking_trial_attention_check_choice_allKeys = []
# keep track of which components have finished
liking_trial_attention_checkComponents = [liking_trial_attention_check_question, liking_trial_attention_check_left_image, liking_trial_attention_check_right_image, liking_trial_attention_check_choice, liking_trial_attention_check_steak_A, liking_trial_attention_check_steak_B]
for thisComponent in liking_trial_attention_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "liking_trial_attention_check" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *liking_trial_attention_check_question* updates
    if liking_trial_attention_check_question.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        liking_trial_attention_check_question.frameNStart = frameN  # exact frame index
        liking_trial_attention_check_question.tStart = t  # local t and not account for scr refresh
        liking_trial_attention_check_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(liking_trial_attention_check_question, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'liking_trial_attention_check_question.started')
        liking_trial_attention_check_question.setAutoDraw(True)
    # Run 'Each Frame' code from liking_trial_attention_check_code
    # Check if a key was pressed and record time
    if liking_trial_attention_check_choice.keys and response_time is None:
        response_time = t  # `t` is the current time in the routine
    
    # Check if 1 second has passed since response
    if liking_trial_attention_check_choice.keys:
        #if liking_trial_attention_check_choice.keys[0] == "q":
        if response_time is not None and t - response_time >= 1:
            continueRoutine = False
        
        
        
        
    
    # *liking_trial_attention_check_left_image* updates
    if liking_trial_attention_check_left_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        liking_trial_attention_check_left_image.frameNStart = frameN  # exact frame index
        liking_trial_attention_check_left_image.tStart = t  # local t and not account for scr refresh
        liking_trial_attention_check_left_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(liking_trial_attention_check_left_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'liking_trial_attention_check_left_image.started')
        liking_trial_attention_check_left_image.setAutoDraw(True)
    
    # *liking_trial_attention_check_right_image* updates
    if liking_trial_attention_check_right_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        liking_trial_attention_check_right_image.frameNStart = frameN  # exact frame index
        liking_trial_attention_check_right_image.tStart = t  # local t and not account for scr refresh
        liking_trial_attention_check_right_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(liking_trial_attention_check_right_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'liking_trial_attention_check_right_image.started')
        liking_trial_attention_check_right_image.setAutoDraw(True)
    
    # *liking_trial_attention_check_choice* updates
    waitOnFlip = False
    if liking_trial_attention_check_choice.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        liking_trial_attention_check_choice.frameNStart = frameN  # exact frame index
        liking_trial_attention_check_choice.tStart = t  # local t and not account for scr refresh
        liking_trial_attention_check_choice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(liking_trial_attention_check_choice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'liking_trial_attention_check_choice.started')
        liking_trial_attention_check_choice.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(liking_trial_attention_check_choice.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(liking_trial_attention_check_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if liking_trial_attention_check_choice.status == STARTED and not waitOnFlip:
        theseKeys = liking_trial_attention_check_choice.getKeys(keyList=None, waitRelease=False)
        _liking_trial_attention_check_choice_allKeys.extend(theseKeys)
        if len(_liking_trial_attention_check_choice_allKeys):
            liking_trial_attention_check_choice.keys = [key.name for key in _liking_trial_attention_check_choice_allKeys]  # storing all keys
            liking_trial_attention_check_choice.rt = [key.rt for key in _liking_trial_attention_check_choice_allKeys]
    
    # *liking_trial_attention_check_steak_A* updates
    if liking_trial_attention_check_steak_A.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        liking_trial_attention_check_steak_A.frameNStart = frameN  # exact frame index
        liking_trial_attention_check_steak_A.tStart = t  # local t and not account for scr refresh
        liking_trial_attention_check_steak_A.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(liking_trial_attention_check_steak_A, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'liking_trial_attention_check_steak_A.started')
        liking_trial_attention_check_steak_A.setAutoDraw(True)
    
    # *liking_trial_attention_check_steak_B* updates
    if liking_trial_attention_check_steak_B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        liking_trial_attention_check_steak_B.frameNStart = frameN  # exact frame index
        liking_trial_attention_check_steak_B.tStart = t  # local t and not account for scr refresh
        liking_trial_attention_check_steak_B.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(liking_trial_attention_check_steak_B, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'liking_trial_attention_check_steak_B.started')
        liking_trial_attention_check_steak_B.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in liking_trial_attention_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "liking_trial_attention_check" ---
for thisComponent in liking_trial_attention_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from liking_trial_attention_check_code
#Data logging

thisExp.addData("Left Image", liking_attention_random_choice)
thisExp.addData("Right Image", liking_attention_random_choice)
thisExp.addData("Trial Type", "attention-check")

#if abort == False:
if liking_trial_attention_check_choice.keys:
    if liking_trial_attention_check_choice.keys[0] != "q" or len(liking_trial_attention_check_choice.keys) < 1:
        attention_checks_failed += 1
        this_check_failed = True

elif not liking_trial_attention_check_choice.keys:
    attention_checks_failed += 1
    this_check_failed = True

thisExp.addData("checks failed", attention_checks_failed)
thisExp.addData("this check failed", this_check_failed)

# check responses
if liking_trial_attention_check_choice.keys in ['', [], None]:  # No response was made
    liking_trial_attention_check_choice.keys = None
thisExp.addData('liking_trial_attention_check_choice.keys',liking_trial_attention_check_choice.keys)
if liking_trial_attention_check_choice.keys != None:  # we had a response
    thisExp.addData('liking_trial_attention_check_choice.rt', liking_trial_attention_check_choice.rt)
thisExp.nextEntry()
# the Routine "liking_trial_attention_check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "failed_attention_check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from missed_attention_check_code
# show this screen only if attention check was failed
if this_check_failed == False:
    continueRoutine = False

elif this_check_failed == True and attention_checks_failed > 1:
    continueRoutine = False

# aligning text to the left
missed_attention_check_text.alignText = "left"

# recording response time
response_time = None
missed_attention_check_resp.keys = []
missed_attention_check_resp.rt = []
_missed_attention_check_resp_allKeys = []
# keep track of which components have finished
failed_attention_checkComponents = [missed_attention_check_text, missed_attention_check_resp, missed_attention_check_press_space_to_continue]
for thisComponent in failed_attention_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "failed_attention_check" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *missed_attention_check_text* updates
    if missed_attention_check_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        missed_attention_check_text.frameNStart = frameN  # exact frame index
        missed_attention_check_text.tStart = t  # local t and not account for scr refresh
        missed_attention_check_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(missed_attention_check_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'missed_attention_check_text.started')
        missed_attention_check_text.setAutoDraw(True)
    
    # *missed_attention_check_resp* updates
    waitOnFlip = False
    if missed_attention_check_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        missed_attention_check_resp.frameNStart = frameN  # exact frame index
        missed_attention_check_resp.tStart = t  # local t and not account for scr refresh
        missed_attention_check_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(missed_attention_check_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'missed_attention_check_resp.started')
        missed_attention_check_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(missed_attention_check_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(missed_attention_check_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if missed_attention_check_resp.status == STARTED and not waitOnFlip:
        theseKeys = missed_attention_check_resp.getKeys(keyList=['space'], waitRelease=False)
        _missed_attention_check_resp_allKeys.extend(theseKeys)
        if len(_missed_attention_check_resp_allKeys):
            missed_attention_check_resp.keys = _missed_attention_check_resp_allKeys[-1].name  # just the last key pressed
            missed_attention_check_resp.rt = _missed_attention_check_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *missed_attention_check_press_space_to_continue* updates
    if missed_attention_check_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        missed_attention_check_press_space_to_continue.frameNStart = frameN  # exact frame index
        missed_attention_check_press_space_to_continue.tStart = t  # local t and not account for scr refresh
        missed_attention_check_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(missed_attention_check_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
        missed_attention_check_press_space_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in failed_attention_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "failed_attention_check" ---
for thisComponent in failed_attention_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from missed_attention_check_code
#Data logging
thisExp.addData("checks failed", attention_checks_failed)

# check responses
if missed_attention_check_resp.keys in ['', [], None]:  # No response was made
    missed_attention_check_resp.keys = None
thisExp.addData('missed_attention_check_resp.keys',missed_attention_check_resp.keys)
if missed_attention_check_resp.keys != None:  # we had a response
    thisExp.addData('missed_attention_check_resp.rt', missed_attention_check_resp.rt)
thisExp.nextEntry()
# the Routine "failed_attention_check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_similarity_instructions = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_similarity_instructions')
thisExp.addLoop(trials_similarity_instructions)  # add the loop to the experiment
thisTrials_similarity_instruction = trials_similarity_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_similarity_instruction.rgb)
if thisTrials_similarity_instruction != None:
    for paramName in thisTrials_similarity_instruction:
        exec('{} = thisTrials_similarity_instruction[paramName]'.format(paramName))

for thisTrials_similarity_instruction in trials_similarity_instructions:
    currentLoop = trials_similarity_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_similarity_instruction.rgb)
    if thisTrials_similarity_instruction != None:
        for paramName in thisTrials_similarity_instruction:
            exec('{} = thisTrials_similarity_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "routine_6_similarity_instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    similarity_instructions_space.keys = []
    similarity_instructions_space.rt = []
    _similarity_instructions_space_allKeys = []
    # Run 'Begin Routine' code from similarity_instructions_code
    if attention_checks_failed == 2:
        continueRoutine = False
    
    similarity_instructions_img = "texts/" + str(similarity_instructions[similarity_instructions_index])
    
    if similarity_instructions_space:
        similarity_instructions_index += 1
    similarity_instructions_image.setImage(similarity_instructions_img)
    # keep track of which components have finished
    routine_6_similarity_instructionsComponents = [similarity_instructions_space, similarity_instructions_image, similarity_instructions_press_space_to_continue]
    for thisComponent in routine_6_similarity_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_6_similarity_instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *similarity_instructions_space* updates
        waitOnFlip = False
        if similarity_instructions_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            similarity_instructions_space.frameNStart = frameN  # exact frame index
            similarity_instructions_space.tStart = t  # local t and not account for scr refresh
            similarity_instructions_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_instructions_space, 'tStartRefresh')  # time at next scr refresh
            similarity_instructions_space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(similarity_instructions_space.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(similarity_instructions_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if similarity_instructions_space.status == STARTED and not waitOnFlip:
            theseKeys = similarity_instructions_space.getKeys(keyList=['space'], waitRelease=False)
            _similarity_instructions_space_allKeys.extend(theseKeys)
            if len(_similarity_instructions_space_allKeys):
                similarity_instructions_space.keys = _similarity_instructions_space_allKeys[-1].name  # just the last key pressed
                similarity_instructions_space.rt = _similarity_instructions_space_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *similarity_instructions_image* updates
        if similarity_instructions_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            similarity_instructions_image.frameNStart = frameN  # exact frame index
            similarity_instructions_image.tStart = t  # local t and not account for scr refresh
            similarity_instructions_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_instructions_image, 'tStartRefresh')  # time at next scr refresh
            similarity_instructions_image.setAutoDraw(True)
        
        # *similarity_instructions_press_space_to_continue* updates
        if similarity_instructions_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            similarity_instructions_press_space_to_continue.frameNStart = frameN  # exact frame index
            similarity_instructions_press_space_to_continue.tStart = t  # local t and not account for scr refresh
            similarity_instructions_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_instructions_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
            similarity_instructions_press_space_to_continue.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_6_similarity_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_6_similarity_instructions" ---
    for thisComponent in routine_6_similarity_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "routine_6_similarity_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials_similarity_instructions'


# set up handler to look after randomisation of conditions etc
trials_similarity = data.TrialHandler(nReps=length_of_experimental_trials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_similarity')
thisExp.addLoop(trials_similarity)  # add the loop to the experiment
thisTrials_similarity = trials_similarity.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_similarity.rgb)
if thisTrials_similarity != None:
    for paramName in thisTrials_similarity:
        exec('{} = thisTrials_similarity[paramName]'.format(paramName))

for thisTrials_similarity in trials_similarity:
    currentLoop = trials_similarity
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_similarity.rgb)
    if thisTrials_similarity != None:
        for paramName in thisTrials_similarity:
            exec('{} = thisTrials_similarity[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "similarity_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from similarity_trial_code
    if attention_checks_failed == 2:
        continueRoutine = False
    
    # start characteristics for choice square
    # once a choice is given, square turns blue and surrounds chosen image
    border_color = "white"
    choice_position = reference_image_position
    similarity_trial_highlighted_choice.fillColor = None
    
    # aligning text to the left
    similarity_trial_missed_trial_text.alignHoriz = "left"
    
    # setting images for this trial
    similarity_trial_left_img = experimental_path + str(experimental_stimuli[stimulus_index_similarity][0])
    similarity_trial_right_img = experimental_path + str(experimental_stimuli[stimulus_index_similarity][1])
    
    # recording response time
    response_time = None
    similarity_trial_left_image.setImage(similarity_trial_left_img)
    similarity_trial_right_image.setImage(similarity_trial_right_img)
    similarity_trial_choice.keys = []
    similarity_trial_choice.rt = []
    _similarity_trial_choice_allKeys = []
    similarity_trial_end_missed_trial.keys = []
    similarity_trial_end_missed_trial.rt = []
    _similarity_trial_end_missed_trial_allKeys = []
    similarity_trial_reference_image.setImage('images/trials/reference/referent.png')
    # keep track of which components have finished
    similarity_trialComponents = [similarity_trial_question, similarity_trial_left_image, similarity_trial_right_image, similarity_trial_choice, similarity_trial_steak_A_title, similarity_trial_steak_B_title, similarity_trial_missed_trial_text, similarity_trial_highlighted_choice, similarity_trial_end_missed_trial, similarity_reference_title, similarity_trial_reference_image, similarity_trial_missed_trial_press_space_to_continue]
    for thisComponent in similarity_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "similarity_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *similarity_trial_question* updates
        if similarity_trial_question.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_question.frameNStart = frameN  # exact frame index
            similarity_trial_question.tStart = t  # local t and not account for scr refresh
            similarity_trial_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_question.started')
            similarity_trial_question.setAutoDraw(True)
        if similarity_trial_question.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_trial_question.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                similarity_trial_question.tStop = t  # not accounting for scr refresh
                similarity_trial_question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_trial_question.stopped')
                similarity_trial_question.setAutoDraw(False)
        # Run 'Each Frame' code from similarity_trial_code
        # start characteristics for choice square
        # once a choice is given, square turns blue and surrounds chosen image
        if similarity_trial_choice.keys:
            if similarity_trial_choice.keys[0] == "d":
                border_color = "blue"
                choice_position = similarity_left_image_position
                
            elif similarity_trial_choice.keys[0] == "k":
                border_color = "blue"
                choice_position = similarity_right_image_position
                
        # Check if a key was pressed and record time
        if similarity_trial_choice.keys and response_time is None:
            response_time = t  # `t` is the current time in the routine
        
        # Check if 1 second has passed since response
        if response_time is not None and t - response_time >= 0.5:
            border_color = "white"
            continueRoutine = False
        
        # *similarity_trial_left_image* updates
        if similarity_trial_left_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_left_image.frameNStart = frameN  # exact frame index
            similarity_trial_left_image.tStart = t  # local t and not account for scr refresh
            similarity_trial_left_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_left_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_left_image.started')
            similarity_trial_left_image.setAutoDraw(True)
        if similarity_trial_left_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_trial_left_image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                similarity_trial_left_image.tStop = t  # not accounting for scr refresh
                similarity_trial_left_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_trial_left_image.stopped')
                similarity_trial_left_image.setAutoDraw(False)
        
        # *similarity_trial_right_image* updates
        if similarity_trial_right_image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_right_image.frameNStart = frameN  # exact frame index
            similarity_trial_right_image.tStart = t  # local t and not account for scr refresh
            similarity_trial_right_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_right_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_right_image.started')
            similarity_trial_right_image.setAutoDraw(True)
        if similarity_trial_right_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_trial_right_image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                similarity_trial_right_image.tStop = t  # not accounting for scr refresh
                similarity_trial_right_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_trial_right_image.stopped')
                similarity_trial_right_image.setAutoDraw(False)
        
        # *similarity_trial_choice* updates
        waitOnFlip = False
        if similarity_trial_choice.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_choice.frameNStart = frameN  # exact frame index
            similarity_trial_choice.tStart = t  # local t and not account for scr refresh
            similarity_trial_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_choice.started')
            similarity_trial_choice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(similarity_trial_choice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(similarity_trial_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if similarity_trial_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_trial_choice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                similarity_trial_choice.tStop = t  # not accounting for scr refresh
                similarity_trial_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_trial_choice.stopped')
                similarity_trial_choice.status = FINISHED
        if similarity_trial_choice.status == STARTED and not waitOnFlip:
            theseKeys = similarity_trial_choice.getKeys(keyList=['d','k'], waitRelease=False)
            _similarity_trial_choice_allKeys.extend(theseKeys)
            if len(_similarity_trial_choice_allKeys):
                similarity_trial_choice.keys = _similarity_trial_choice_allKeys[0].name  # just the first key pressed
                similarity_trial_choice.rt = _similarity_trial_choice_allKeys[0].rt
        
        # *similarity_trial_steak_A_title* updates
        if similarity_trial_steak_A_title.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_steak_A_title.frameNStart = frameN  # exact frame index
            similarity_trial_steak_A_title.tStart = t  # local t and not account for scr refresh
            similarity_trial_steak_A_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_steak_A_title, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_steak_A_title.started')
            similarity_trial_steak_A_title.setAutoDraw(True)
        if similarity_trial_steak_A_title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_trial_steak_A_title.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                similarity_trial_steak_A_title.tStop = t  # not accounting for scr refresh
                similarity_trial_steak_A_title.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_trial_steak_A_title.stopped')
                similarity_trial_steak_A_title.setAutoDraw(False)
        
        # *similarity_trial_steak_B_title* updates
        if similarity_trial_steak_B_title.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_steak_B_title.frameNStart = frameN  # exact frame index
            similarity_trial_steak_B_title.tStart = t  # local t and not account for scr refresh
            similarity_trial_steak_B_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_steak_B_title, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_steak_B_title.started')
            similarity_trial_steak_B_title.setAutoDraw(True)
        if similarity_trial_steak_B_title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_trial_steak_B_title.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                similarity_trial_steak_B_title.tStop = t  # not accounting for scr refresh
                similarity_trial_steak_B_title.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_trial_steak_B_title.stopped')
                similarity_trial_steak_B_title.setAutoDraw(False)
        
        # *similarity_trial_missed_trial_text* updates
        if similarity_trial_missed_trial_text.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_missed_trial_text.frameNStart = frameN  # exact frame index
            similarity_trial_missed_trial_text.tStart = t  # local t and not account for scr refresh
            similarity_trial_missed_trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_missed_trial_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_missed_trial_text.started')
            similarity_trial_missed_trial_text.setAutoDraw(True)
        
        # *similarity_trial_highlighted_choice* updates
        if similarity_trial_highlighted_choice.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_highlighted_choice.frameNStart = frameN  # exact frame index
            similarity_trial_highlighted_choice.tStart = t  # local t and not account for scr refresh
            similarity_trial_highlighted_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_highlighted_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_highlighted_choice.started')
            similarity_trial_highlighted_choice.setAutoDraw(True)
        if similarity_trial_highlighted_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_trial_highlighted_choice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                similarity_trial_highlighted_choice.tStop = t  # not accounting for scr refresh
                similarity_trial_highlighted_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_trial_highlighted_choice.stopped')
                similarity_trial_highlighted_choice.setAutoDraw(False)
        if similarity_trial_highlighted_choice.status == STARTED:  # only update if drawing
            similarity_trial_highlighted_choice.setPos(choice_position, log=False)
            similarity_trial_highlighted_choice.setLineColor(border_color, log=False)
        
        # *similarity_trial_end_missed_trial* updates
        waitOnFlip = False
        if similarity_trial_end_missed_trial.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_end_missed_trial.frameNStart = frameN  # exact frame index
            similarity_trial_end_missed_trial.tStart = t  # local t and not account for scr refresh
            similarity_trial_end_missed_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_end_missed_trial, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_end_missed_trial.started')
            similarity_trial_end_missed_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(similarity_trial_end_missed_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(similarity_trial_end_missed_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if similarity_trial_end_missed_trial.status == STARTED and not waitOnFlip:
            theseKeys = similarity_trial_end_missed_trial.getKeys(keyList=['space'], waitRelease=False)
            _similarity_trial_end_missed_trial_allKeys.extend(theseKeys)
            if len(_similarity_trial_end_missed_trial_allKeys):
                similarity_trial_end_missed_trial.keys = _similarity_trial_end_missed_trial_allKeys[-1].name  # just the last key pressed
                similarity_trial_end_missed_trial.rt = _similarity_trial_end_missed_trial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *similarity_reference_title* updates
        if similarity_reference_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            similarity_reference_title.frameNStart = frameN  # exact frame index
            similarity_reference_title.tStart = t  # local t and not account for scr refresh
            similarity_reference_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_reference_title, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_reference_title.started')
            similarity_reference_title.setAutoDraw(True)
        if similarity_reference_title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_reference_title.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                similarity_reference_title.tStop = t  # not accounting for scr refresh
                similarity_reference_title.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_reference_title.stopped')
                similarity_reference_title.setAutoDraw(False)
        
        # *similarity_trial_reference_image* updates
        if similarity_trial_reference_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_reference_image.frameNStart = frameN  # exact frame index
            similarity_trial_reference_image.tStart = t  # local t and not account for scr refresh
            similarity_trial_reference_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_reference_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'similarity_trial_reference_image.started')
            similarity_trial_reference_image.setAutoDraw(True)
        if similarity_trial_reference_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > similarity_trial_reference_image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                similarity_trial_reference_image.tStop = t  # not accounting for scr refresh
                similarity_trial_reference_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'similarity_trial_reference_image.stopped')
                similarity_trial_reference_image.setAutoDraw(False)
        
        # *similarity_trial_missed_trial_press_space_to_continue* updates
        if similarity_trial_missed_trial_press_space_to_continue.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            similarity_trial_missed_trial_press_space_to_continue.frameNStart = frameN  # exact frame index
            similarity_trial_missed_trial_press_space_to_continue.tStart = t  # local t and not account for scr refresh
            similarity_trial_missed_trial_press_space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(similarity_trial_missed_trial_press_space_to_continue, 'tStartRefresh')  # time at next scr refresh
            similarity_trial_missed_trial_press_space_to_continue.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in similarity_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "similarity_trial" ---
    for thisComponent in similarity_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from similarity_trial_code
    #Data logging
    # if response is not given, record as missed trial
    if similarity_trial_choice.keys == "":
        trial_type = "similarity-missed"
    
    else:
        trial_type = "similarity"
        
    thisExp.addData("Trial Type", trial_type)
    thisExp.addData("Left Image", experimental_stimuli[stimulus_index_similarity][0])
    thisExp.addData("Right Image", experimental_stimuli[stimulus_index_similarity][1])
    
    # move onto next trial
    if similarity_trial_choice or similarity_trial_end_missed_trial:
        stimulus_index_similarity += 1
    # check responses
    if similarity_trial_choice.keys in ['', [], None]:  # No response was made
        similarity_trial_choice.keys = None
    trials_similarity.addData('similarity_trial_choice.keys',similarity_trial_choice.keys)
    if similarity_trial_choice.keys != None:  # we had a response
        trials_similarity.addData('similarity_trial_choice.rt', similarity_trial_choice.rt)
    # check responses
    if similarity_trial_end_missed_trial.keys in ['', [], None]:  # No response was made
        similarity_trial_end_missed_trial.keys = None
    trials_similarity.addData('similarity_trial_end_missed_trial.keys',similarity_trial_end_missed_trial.keys)
    if similarity_trial_end_missed_trial.keys != None:  # we had a response
        trials_similarity.addData('similarity_trial_end_missed_trial.rt', similarity_trial_end_missed_trial.rt)
    # the Routine "similarity_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed length_of_experimental_trials repeats of 'trials_similarity'


# --- Prepare to start Routine "age_question" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
age_response.reset()
age_key_resp.keys = []
age_key_resp.rt = []
_age_key_resp_allKeys = []
# Run 'Begin Routine' code from age_question_code
if attention_checks_failed == 2:
    continueRoutine = False

# only allowing answers from an accepted list
age_correctKeys = [f"{i}" for i in range(0, 100)]
# keep track of which components have finished
age_questionComponents = [age_prompt, age_response, age_key_resp, age_press_enter_to_continue]
for thisComponent in age_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "age_question" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *age_prompt* updates
    if age_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age_prompt.frameNStart = frameN  # exact frame index
        age_prompt.tStart = t  # local t and not account for scr refresh
        age_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'age_prompt.started')
        age_prompt.setAutoDraw(True)
    
    # *age_response* updates
    if age_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age_response.frameNStart = frameN  # exact frame index
        age_response.tStart = t  # local t and not account for scr refresh
        age_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age_response, 'tStartRefresh')  # time at next scr refresh
        age_response.setAutoDraw(True)
    
    # *age_key_resp* updates
    waitOnFlip = False
    if age_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age_key_resp.frameNStart = frameN  # exact frame index
        age_key_resp.tStart = t  # local t and not account for scr refresh
        age_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age_key_resp, 'tStartRefresh')  # time at next scr refresh
        age_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(age_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(age_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if age_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = age_key_resp.getKeys(keyList=['return'], waitRelease=False)
        _age_key_resp_allKeys.extend(theseKeys)
        if len(_age_key_resp_allKeys):
            age_key_resp.keys = _age_key_resp_allKeys[-1].name  # just the last key pressed
            age_key_resp.rt = _age_key_resp_allKeys[-1].rt
    
    # *age_press_enter_to_continue* updates
    if age_press_enter_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age_press_enter_to_continue.frameNStart = frameN  # exact frame index
        age_press_enter_to_continue.tStart = t  # local t and not account for scr refresh
        age_press_enter_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age_press_enter_to_continue, 'tStartRefresh')  # time at next scr refresh
        age_press_enter_to_continue.setAutoDraw(True)
    # Run 'Each Frame' code from age_question_code
    # what keys have been pressed this frame?
    keys = age_response.text
    
    # if any, check that they're the right keys
    if keys:
        if keys not in age_correctKeys:
            # if they're not valid, remove the last inputted character from the textbox
            age_response.text = age_response.text[0:-1]
        if len(keys) > 2:
            age_response.text = age_response.text[0:-1]
    
    # if an acceptable answer is given AND return is pressed, continue to next question
    if age_key_resp.keys == "return" and keys in age_correctKeys:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in age_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "age_question" ---
for thisComponent in age_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('age_response.text',age_response.text)
# the Routine "age_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "gender_question" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from gender_code
if attention_checks_failed == 2:
    continueRoutine = False

# aligning text to the left
gender_options.alignText = "left"

# only allowing answers from an accepted list
gender_correctKeys = [f"{i}" for i in range(0, 5)]
gender_response.reset()
gender_key_resp.keys = []
gender_key_resp.rt = []
_gender_key_resp_allKeys = []
# keep track of which components have finished
gender_questionComponents = [gender_prompt, gender_options, gender_response, gender_key_resp, gender_press_enter_to_continue]
for thisComponent in gender_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "gender_question" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from gender_code
    # what keys have been pressed this frame?
    keys = gender_response.text
    
    # if any, check that they're the right keys
    if keys:
        if keys not in gender_correctKeys:
            # if they're not valid, remove the last inputted character from the textbox
            gender_response.text = gender_response.text[0:-1]
    
    # if an acceptable answer is given AND return is pressed, continue to next question
    if gender_key_resp.keys == "return" and keys in gender_correctKeys:
        continueRoutine = False
    
    # *gender_prompt* updates
    if gender_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gender_prompt.frameNStart = frameN  # exact frame index
        gender_prompt.tStart = t  # local t and not account for scr refresh
        gender_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gender_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'gender_prompt.started')
        gender_prompt.setAutoDraw(True)
    
    # *gender_options* updates
    if gender_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gender_options.frameNStart = frameN  # exact frame index
        gender_options.tStart = t  # local t and not account for scr refresh
        gender_options.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gender_options, 'tStartRefresh')  # time at next scr refresh
        gender_options.setAutoDraw(True)
    
    # *gender_response* updates
    if gender_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gender_response.frameNStart = frameN  # exact frame index
        gender_response.tStart = t  # local t and not account for scr refresh
        gender_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gender_response, 'tStartRefresh')  # time at next scr refresh
        gender_response.setAutoDraw(True)
    
    # *gender_key_resp* updates
    waitOnFlip = False
    if gender_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gender_key_resp.frameNStart = frameN  # exact frame index
        gender_key_resp.tStart = t  # local t and not account for scr refresh
        gender_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gender_key_resp, 'tStartRefresh')  # time at next scr refresh
        gender_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(gender_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(gender_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if gender_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = gender_key_resp.getKeys(keyList=['return'], waitRelease=False)
        _gender_key_resp_allKeys.extend(theseKeys)
        if len(_gender_key_resp_allKeys):
            gender_key_resp.keys = _gender_key_resp_allKeys[-1].name  # just the last key pressed
            gender_key_resp.rt = _gender_key_resp_allKeys[-1].rt
    
    # *gender_press_enter_to_continue* updates
    if gender_press_enter_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gender_press_enter_to_continue.frameNStart = frameN  # exact frame index
        gender_press_enter_to_continue.tStart = t  # local t and not account for scr refresh
        gender_press_enter_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gender_press_enter_to_continue, 'tStartRefresh')  # time at next scr refresh
        gender_press_enter_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gender_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "gender_question" ---
for thisComponent in gender_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gender_response.text',gender_response.text)
# the Routine "gender_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "frequency_question" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from frequency_code
if attention_checks_failed == 2:
    continueRoutine = False

# aligning text to the left
frequency_options.alignText = "left"

# only allowing answers from an accepted list
frequency_correctKeys = [f"{i}" for i in range(0, 7)]
frequency_response.reset()
frequency_key_resp.keys = []
frequency_key_resp.rt = []
_frequency_key_resp_allKeys = []
# keep track of which components have finished
frequency_questionComponents = [frequency_prompt, frequency_options, frequency_response, frequency_key_resp, frequency_press_enter_to_continue]
for thisComponent in frequency_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "frequency_question" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from frequency_code
    # what keys have been pressed this frame?
    keys = frequency_response.text
    
    # if any, check that they're the right keys
    if keys:
        if keys not in frequency_correctKeys:
            # if they're not valid, remove the last inputted character from the textbox
            frequency_response.text = frequency_response.text[0:-1]
    
    # if an acceptable answer is given AND return is pressed, continue to next question
    if frequency_key_resp.keys == "return" and keys in frequency_correctKeys:
        continueRoutine = False
    
    # *frequency_prompt* updates
    if frequency_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        frequency_prompt.frameNStart = frameN  # exact frame index
        frequency_prompt.tStart = t  # local t and not account for scr refresh
        frequency_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(frequency_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'frequency_prompt.started')
        frequency_prompt.setAutoDraw(True)
    
    # *frequency_options* updates
    if frequency_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        frequency_options.frameNStart = frameN  # exact frame index
        frequency_options.tStart = t  # local t and not account for scr refresh
        frequency_options.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(frequency_options, 'tStartRefresh')  # time at next scr refresh
        frequency_options.setAutoDraw(True)
    
    # *frequency_response* updates
    if frequency_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        frequency_response.frameNStart = frameN  # exact frame index
        frequency_response.tStart = t  # local t and not account for scr refresh
        frequency_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(frequency_response, 'tStartRefresh')  # time at next scr refresh
        frequency_response.setAutoDraw(True)
    
    # *frequency_key_resp* updates
    waitOnFlip = False
    if frequency_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        frequency_key_resp.frameNStart = frameN  # exact frame index
        frequency_key_resp.tStart = t  # local t and not account for scr refresh
        frequency_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(frequency_key_resp, 'tStartRefresh')  # time at next scr refresh
        frequency_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(frequency_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(frequency_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if frequency_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = frequency_key_resp.getKeys(keyList=['return'], waitRelease=False)
        _frequency_key_resp_allKeys.extend(theseKeys)
        if len(_frequency_key_resp_allKeys):
            frequency_key_resp.keys = _frequency_key_resp_allKeys[-1].name  # just the last key pressed
            frequency_key_resp.rt = _frequency_key_resp_allKeys[-1].rt
    
    # *frequency_press_enter_to_continue* updates
    if frequency_press_enter_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        frequency_press_enter_to_continue.frameNStart = frameN  # exact frame index
        frequency_press_enter_to_continue.tStart = t  # local t and not account for scr refresh
        frequency_press_enter_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(frequency_press_enter_to_continue, 'tStartRefresh')  # time at next scr refresh
        frequency_press_enter_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in frequency_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "frequency_question" ---
for thisComponent in frequency_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('frequency_response.text',frequency_response.text)
# the Routine "frequency_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "feedback_question" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from feedback_code
if attention_checks_failed == 2:
    continueRoutine = False

# aligning text to the left
frequency_prompt.alignText = "left"
feedback_response.reset()
feedback_key_resp.keys = []
feedback_key_resp.rt = []
_feedback_key_resp_allKeys = []
# keep track of which components have finished
feedback_questionComponents = [feedback_prompt, feedback_response, feedback_key_resp, feedback_press_enter_to_continue]
for thisComponent in feedback_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "feedback_question" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedback_prompt* updates
    if feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_prompt.frameNStart = frameN  # exact frame index
        feedback_prompt.tStart = t  # local t and not account for scr refresh
        feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_prompt.started')
        feedback_prompt.setAutoDraw(True)
    
    # *feedback_response* updates
    if feedback_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_response.frameNStart = frameN  # exact frame index
        feedback_response.tStart = t  # local t and not account for scr refresh
        feedback_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_response.started')
        feedback_response.setAutoDraw(True)
    
    # *feedback_key_resp* updates
    waitOnFlip = False
    if feedback_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_key_resp.frameNStart = frameN  # exact frame index
        feedback_key_resp.tStart = t  # local t and not account for scr refresh
        feedback_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_key_resp.started')
        feedback_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(feedback_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(feedback_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if feedback_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = feedback_key_resp.getKeys(keyList=['right'], waitRelease=False)
        _feedback_key_resp_allKeys.extend(theseKeys)
        if len(_feedback_key_resp_allKeys):
            feedback_key_resp.keys = _feedback_key_resp_allKeys[-1].name  # just the last key pressed
            feedback_key_resp.rt = _feedback_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *feedback_press_enter_to_continue* updates
    if feedback_press_enter_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_press_enter_to_continue.frameNStart = frameN  # exact frame index
        feedback_press_enter_to_continue.tStart = t  # local t and not account for scr refresh
        feedback_press_enter_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_press_enter_to_continue, 'tStartRefresh')  # time at next scr refresh
        feedback_press_enter_to_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "feedback_question" ---
for thisComponent in feedback_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('feedback_response.text',feedback_response.text)
# check responses
if feedback_key_resp.keys in ['', [], None]:  # No response was made
    feedback_key_resp.keys = None
thisExp.addData('feedback_key_resp.keys',feedback_key_resp.keys)
if feedback_key_resp.keys != None:  # we had a response
    thisExp.addData('feedback_key_resp.rt', feedback_key_resp.rt)
thisExp.nextEntry()
# the Routine "feedback_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_experiment.keys = []
end_experiment.rt = []
_end_experiment_allKeys = []
# Run 'Begin Routine' code from end_code
if attention_checks_failed == 2:
    continueRoutine = False

#end_text.alignHoriz = "left"
# keep track of which components have finished
endComponents = [end_text, end_experiment]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
while continueRoutine and routineTimer.getTime() < 8.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            end_text.setAutoDraw(False)
    
    # *end_experiment* updates
    waitOnFlip = False
    if end_experiment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_experiment.frameNStart = frameN  # exact frame index
        end_experiment.tStart = t  # local t and not account for scr refresh
        end_experiment.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_experiment, 'tStartRefresh')  # time at next scr refresh
        end_experiment.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_experiment.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_experiment.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_experiment.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_experiment.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            end_experiment.tStop = t  # not accounting for scr refresh
            end_experiment.frameNStop = frameN  # exact frame index
            end_experiment.status = FINISHED
    if end_experiment.status == STARTED and not waitOnFlip:
        theseKeys = end_experiment.getKeys(keyList=['space'], waitRelease=False)
        _end_experiment_allKeys.extend(theseKeys)
        if len(_end_experiment_allKeys):
            end_experiment.keys = _end_experiment_allKeys[-1].name  # just the last key pressed
            end_experiment.rt = _end_experiment_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-8.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
