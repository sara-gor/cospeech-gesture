#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Thu Nov 13 18:08:30 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
#import nidaqmx

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'exp_cospeech_congruency'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

## Specify output port for trigger
## Change channel if needed
#trigger_task = nidaqmx.Task()
#trigger_task.do_channels.add_do_chan("Dev1/port0/line0")

## trigger function
#def send_trigger():
  #  trigger_task.write(True)
  #  core.wait(0.002)  # 2 milliseconds
   # trigger_task.write(False)

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/sara-sofiagorriz/Library/CloudStorage/OneDrive-Chalmers/Experiments/CoSpeech_congruency/exp_cospeech_congruency.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('keyWelcomeResponse') is None:
        # initialise keyWelcomeResponse
        keyWelcomeResponse = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyWelcomeResponse',
        )
    if deviceManager.getDevice('keyEplanation') is None:
        # initialise keyEplanation
        keyEplanation = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyEplanation',
        )
    if deviceManager.getDevice('keyInstructSpeak_continue') is None:
        # initialise keyInstructSpeak_continue
        keyInstructSpeak_continue = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyInstructSpeak_continue',
        )
    if deviceManager.getDevice('keyInstructHand') is None:
        # initialise keyInstructHand
        keyInstructHand = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyInstructHand',
        )
    if deviceManager.getDevice('keyResponseInstructBoth') is None:
        # initialise keyResponseInstructBoth
        keyResponseInstructBoth = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyResponseInstructBoth',
        )
    if deviceManager.getDevice('keyBlockResponseTraining') is None:
        # initialise keyBlockResponseTraining
        keyBlockResponseTraining = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyBlockResponseTraining',
        )
    # create speaker 'audioStim_Training'
    deviceManager.addDevice(
        deviceName='audioStim_Training',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index = '-1',
        #index=None,
        #name="SAMSUNG (NVIDIA High Definition Audio)",
        resample='True',
        latencyClass=1,
    )
    # create speaker 'audioGoCue_Training'
    deviceManager.addDevice(
        deviceName='audioGoCue_Training',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index = '-1',
        #index=None,
        #name="SAMSUNG (NVIDIA High Definition Audio)",
        resample='True',
        latencyClass=1,
    )
    if deviceManager.getDevice('keyBlockResponse') is None:
        # initialise keyBlockResponse
        keyBlockResponse = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyBlockResponse',
        )
    # create speaker 'audioStimuli'
    deviceManager.addDevice(
        deviceName='audioStimuli',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index = '-1',
      #  index=None,
       # name="SAMSUNG (NVIDIA High Definition Audio)",
        resample='True',
        latencyClass=1,
    )
    # create speaker 'audioGoCue'
    deviceManager.addDevice(
        deviceName='audioGoCue',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index = '-1',
     #   index=None,
       # name="SAMSUNG (NVIDIA High Definition Audio)",
        resample='True',
        latencyClass=1,
    )
    if deviceManager.getDevice('keyRespPause') is None:
        # initialise keyRespPause
        keyRespPause = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyRespPause',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcomeScreen" ---
    # Run 'Begin Experiment' code from codeBeginning
    from psychopy import visual, core, event
    import pandas as pd 
    import numpy as np
    import random
    from PIL import Image  # Python Imaging Library (included with PsychoPy)
    
    # Try to open a small non-fullscreen window for the experimenter
    #try:
    #    expWin = visual.Window(
    #        size=(400, 200),
    #        screen=2,          # 0 = primary display (change if needed)
    #        fullscr=False,
    #        color='grey',
    #        units='pix'
    #    )
    #    expWinOK = True
    #except Exception as e:
     #   print(f"⚠️ Could not open experimenter window: {e}")
      #  expWinOK = False
    
    ## specifiy current Block number
    nBlock = 0
    
    ## load stimuli
    # load go trials
    go_trials = pd.read_excel('stimuli_go_congruency.xlsx')
    
    # repeat go trials 3 times
    go_trials_rep = pd.concat([go_trials]*3, ignore_index = True)
    
    # load nogo trials
    nogo_trials = pd.read_excel('stimuli_nogo_congruency.xlsx')
    subset_nogo_trials = nogo_trials.sample(n=5).reset_index(drop=True)  # select 5 random rows
    
    # Combine Go and NoGo trials
    all_trials = pd.concat([go_trials_rep, subset_nogo_trials], ignore_index = True)
    
    # shuffle 
    all_trials = all_trials.sample(frac=1).reset_index(drop=True)
    
    # temporary csv
    all_trials.to_csv('block_trials.csv', index = False)
    
    
    # choose subset from go-trials for training block
    # we want to show each gesture once during training, choose instruciton type randomly 
    
    # choose subset in go_trials
    samples = []
    for i in range(0, len(go_trials), 3):
        block = go_trials.iloc[i:i+3]  # block of 3 rows of excel
        if len(block) > 0:
            chosen = block.sample(n=2)  # random instruction
            samples.append(chosen)
    
    # 16 Samples 
    samples = pd.concat(samples).head(16)
    nogo_samples = nogo_trials.sample(n=2).reset_index(drop=True)
    trainingTrials = pd.concat([samples, nogo_samples], ignore_index = True)
    trainingTrials = trainingTrials.sample(frac=1).reset_index(drop=True)
    trainingTrials.to_csv('trainingTrials.csv', index = False)
    
    # adjust video size to screen window size
    screen_width = win.size[0]
    screen_height = win.size[1]
    
    print("Screen window size: ", screen_width, screen_height)
    
    video_width = int(screen_height * 0.8 * (16/9))
    video_height = int(screen_height * 0.8)
    sizeVideo = [video_width, video_height]
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='Welcome!\n\nIf you want to continue to the explanation of this task, please press SPACEBAR.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keyWelcomeResponse = keyboard.Keyboard(deviceName='keyWelcomeResponse')
    
    # --- Initialize components for Routine "explanationScreen" ---
    textExplanation = visual.TextStim(win=win, name='textExplanation',
        text="In the following task, each trial will begin with a word played over the speakers, accompanied by a video showing a gesture on the screen in front of you. \n\nAfter this, you'll be asked to do one of the following - repeat the word, perform the gesture, or do both at the same time — depending on the trial.\n\nYou'll know when to respond by a GO cue, which will appear as a green circle. If instead a red circle appears, it's a No-Go trial - in that case, simply relax and do nothing. Please attempt to perform the gesture with only your right hand to the best of your abilities. Even if you cannot physically produce the gesture, please give it your best try.\n\nNote: The word you hear and the gesture you see on the screen may not always match.\n\nPress SPACEBAR to continue.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyEplanation = keyboard.Keyboard(deviceName='keyEplanation')
    
    # --- Initialize components for Routine "explInstructSpeak" ---
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='images/speak.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    textInstructSpeak = visual.TextStim(win=win, name='textInstructSpeak',
        text='The shown symbol is the image you will see when you are asked to repeat the word. ',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keyInstructSpeak_continue = keyboard.Keyboard(deviceName='keyInstructSpeak_continue')
    textInstructSpeak_continue = visual.TextStim(win=win, name='textInstructSpeak_continue',
        text='Press SPACEBAR to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "explInstructHand" ---
    textInstructHand = visual.TextStim(win=win, name='textInstructHand',
        text='The shown symbol is the image you will see when you are asked to repeat the gesture. ',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageInstructHand = visual.ImageStim(
        win=win,
        name='imageInstructHand', 
        image='images/hand.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    keyInstructHand = keyboard.Keyboard(deviceName='keyInstructHand')
    textInstructHand_continue = visual.TextStim(win=win, name='textInstructHand_continue',
        text='Press SPACEBAR to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "explInstructBoth" ---
    imageInstructBoth = visual.ImageStim(
        win=win,
        name='imageInstructBoth', 
        image='images/speak_gesture1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    textInstructBoth = visual.TextStim(win=win, name='textInstructBoth',
        text='The shown symbol is the image you will see when you are asked to repeat the word and the gesture simultaneously. ',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    keyResponseInstructBoth = keyboard.Keyboard(deviceName='keyResponseInstructBoth')
    textInstructBoth_continue = visual.TextStim(win=win, name='textInstructBoth_continue',
        text='Press SPACEBAR to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "blockTraining" ---
    textBlockTraining = visual.TextStim(win=win, name='textBlockTraining',
        text='This is the beginning of the training. If you want to start, please press SPACEBAR.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyBlockResponseTraining = keyboard.Keyboard(deviceName='keyBlockResponseTraining')
    
    # --- Initialize components for Routine "trialTraining" ---
    iti_Training = visual.Rect(
        win=win, name='iti_Training',
        width=(2, 2)[0], height=(2, 2)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    textStart_Training = visual.TextStim(win=win, name='textStart_Training',
        text='START',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    movieGesture_Training = visual.MovieStim(
        win, name='movieGesture_Training',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=True,
        pos=(0, 0), size=sizeVideo, units='pix',
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=-3
    )
    audioStim_Training = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='audioStim_Training',    name='audioStim_Training'
    )
    audioStim_Training.setVolume(1.0)
    instructionImage_Training = visual.ImageStim(
        win=win,
        name='instructionImage_Training', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    actionCue_Training = visual.ShapeStim(
        win=win, name='actionCue_Training',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    audioGoCue_Training = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='audioGoCue_Training',    name='audioGoCue_Training'
    )
    audioGoCue_Training.setVolume(0.8)
    
    # --- Initialize components for Routine "blockStart" ---
    textBlockStart = visual.TextStim(win=win, name='textBlockStart',
        text='This is the start of a new block. \n\nPlease press SPACEBAR to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keyBlockResponse = keyboard.Keyboard(deviceName='keyBlockResponse')
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from codeActionCUE
    from PIL import Image  # Python Imaging Library (included with PsychoPy)
    
    iti = visual.Rect(
        win=win, name='iti',
        width=(2, 2)[0], height=(2, 2)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    textStart = visual.TextStim(win=win, name='textStart',
        text='START',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    movieGesture = visual.MovieStim(
        win, name='movieGesture',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=True,
        pos=(0, 0), size=sizeVideo, units='pix',
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=-3
    )
    audioStimuli = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='audioStimuli',    name='audioStimuli'
    )
    audioStimuli.setVolume(1.0)
    instructionImage = visual.ImageStim(
        win=win,
        name='instructionImage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    actionCue = visual.ShapeStim(
        win=win, name='actionCue',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    audioGoCue = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='audioGoCue',    name='audioGoCue'
    )
    audioGoCue.setVolume(0.8)
    
    # --- Initialize components for Routine "paused" ---
    textPause = visual.TextStim(win=win, name='textPause',
        text="Experiment is paused.\n\nTo continue the experiment, press 'SPACEBAR'.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keyRespPause = keyboard.Keyboard(deviceName='keyRespPause')
    
    # --- Initialize components for Routine "breakOnethird" ---
    textOneThird = visual.TextStim(win=win, name='textOneThird',
        text='You are already one third through this block!\n\nWe will continue in 15 seconds...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "breakTwothirds" ---
    # Run 'Begin Experiment' code from codeTwoThrid
    repTwoThirds = 0; 
    textTwothirds = visual.TextStim(win=win, name='textTwothirds',
        text='You are two thrids throug this block. \n\nWe will continue in 15 seconds',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "goodbyeScreen" ---
    textGoodbye = visual.TextStim(win=win, name='textGoodbye',
        text='This is the end of the task. \n\nIf you could take a few more minutes to give us feedback on this gesture - speech task, we would greatly appreciate it.\n\nThank you for your time! ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcomeScreen" ---
    # create an object to store info about Routine welcomeScreen
    welcomeScreen = data.Routine(
        name='welcomeScreen',
        components=[textWelcome, keyWelcomeResponse],
    )
    welcomeScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyWelcomeResponse
    keyWelcomeResponse.keys = []
    keyWelcomeResponse.rt = []
    _keyWelcomeResponse_allKeys = []
    # store start times for welcomeScreen
    welcomeScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcomeScreen.tStart = globalClock.getTime(format='float')
    welcomeScreen.status = STARTED
    thisExp.addData('welcomeScreen.started', welcomeScreen.tStart)
    welcomeScreen.maxDuration = None
    # keep track of which components have finished
    welcomeScreenComponents = welcomeScreen.components
    for thisComponent in welcomeScreen.components:
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
    
    # --- Run Routine "welcomeScreen" ---
    welcomeScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *keyWelcomeResponse* updates
        waitOnFlip = False
        
        # if keyWelcomeResponse is starting this frame...
        if keyWelcomeResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWelcomeResponse.frameNStart = frameN  # exact frame index
            keyWelcomeResponse.tStart = t  # local t and not account for scr refresh
            keyWelcomeResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWelcomeResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyWelcomeResponse.started')
            # update status
            keyWelcomeResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWelcomeResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWelcomeResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWelcomeResponse.status == STARTED and not waitOnFlip:
            theseKeys = keyWelcomeResponse.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyWelcomeResponse_allKeys.extend(theseKeys)
            if len(_keyWelcomeResponse_allKeys):
                keyWelcomeResponse.keys = _keyWelcomeResponse_allKeys[-1].name  # just the last key pressed
                keyWelcomeResponse.rt = _keyWelcomeResponse_allKeys[-1].rt
                keyWelcomeResponse.duration = _keyWelcomeResponse_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=welcomeScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcomeScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcomeScreen" ---
    for thisComponent in welcomeScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcomeScreen
    welcomeScreen.tStop = globalClock.getTime(format='float')
    welcomeScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcomeScreen.stopped', welcomeScreen.tStop)
    # check responses
    if keyWelcomeResponse.keys in ['', [], None]:  # No response was made
        keyWelcomeResponse.keys = None
    thisExp.addData('keyWelcomeResponse.keys',keyWelcomeResponse.keys)
    if keyWelcomeResponse.keys != None:  # we had a response
        thisExp.addData('keyWelcomeResponse.rt', keyWelcomeResponse.rt)
        thisExp.addData('keyWelcomeResponse.duration', keyWelcomeResponse.duration)
    thisExp.nextEntry()
    # the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "explanationScreen" ---
    # create an object to store info about Routine explanationScreen
    explanationScreen = data.Routine(
        name='explanationScreen',
        components=[textExplanation, keyEplanation],
    )
    explanationScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyEplanation
    keyEplanation.keys = []
    keyEplanation.rt = []
    _keyEplanation_allKeys = []
    # store start times for explanationScreen
    explanationScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    explanationScreen.tStart = globalClock.getTime(format='float')
    explanationScreen.status = STARTED
    thisExp.addData('explanationScreen.started', explanationScreen.tStart)
    explanationScreen.maxDuration = None
    # keep track of which components have finished
    explanationScreenComponents = explanationScreen.components
    for thisComponent in explanationScreen.components:
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
    
    # --- Run Routine "explanationScreen" ---
    explanationScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textExplanation* updates
        
        # if textExplanation is starting this frame...
        if textExplanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textExplanation.frameNStart = frameN  # exact frame index
            textExplanation.tStart = t  # local t and not account for scr refresh
            textExplanation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textExplanation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textExplanation.started')
            # update status
            textExplanation.status = STARTED
            textExplanation.setAutoDraw(True)
        
        # if textExplanation is active this frame...
        if textExplanation.status == STARTED:
            # update params
            pass
        
        # *keyEplanation* updates
        waitOnFlip = False
        
        # if keyEplanation is starting this frame...
        if keyEplanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyEplanation.frameNStart = frameN  # exact frame index
            keyEplanation.tStart = t  # local t and not account for scr refresh
            keyEplanation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyEplanation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyEplanation.started')
            # update status
            keyEplanation.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyEplanation.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyEplanation.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyEplanation.status == STARTED and not waitOnFlip:
            theseKeys = keyEplanation.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyEplanation_allKeys.extend(theseKeys)
            if len(_keyEplanation_allKeys):
                keyEplanation.keys = _keyEplanation_allKeys[-1].name  # just the last key pressed
                keyEplanation.rt = _keyEplanation_allKeys[-1].rt
                keyEplanation.duration = _keyEplanation_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=explanationScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            explanationScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in explanationScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "explanationScreen" ---
    for thisComponent in explanationScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for explanationScreen
    explanationScreen.tStop = globalClock.getTime(format='float')
    explanationScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('explanationScreen.stopped', explanationScreen.tStop)
    # check responses
    if keyEplanation.keys in ['', [], None]:  # No response was made
        keyEplanation.keys = None
    thisExp.addData('keyEplanation.keys',keyEplanation.keys)
    if keyEplanation.keys != None:  # we had a response
        thisExp.addData('keyEplanation.rt', keyEplanation.rt)
        thisExp.addData('keyEplanation.duration', keyEplanation.duration)
    thisExp.nextEntry()
    # the Routine "explanationScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "explInstructSpeak" ---
    # create an object to store info about Routine explInstructSpeak
    explInstructSpeak = data.Routine(
        name='explInstructSpeak',
        components=[image, textInstructSpeak, keyInstructSpeak_continue, textInstructSpeak_continue],
    )
    explInstructSpeak.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyInstructSpeak_continue
    keyInstructSpeak_continue.keys = []
    keyInstructSpeak_continue.rt = []
    _keyInstructSpeak_continue_allKeys = []
    # store start times for explInstructSpeak
    explInstructSpeak.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    explInstructSpeak.tStart = globalClock.getTime(format='float')
    explInstructSpeak.status = STARTED
    thisExp.addData('explInstructSpeak.started', explInstructSpeak.tStart)
    explInstructSpeak.maxDuration = None
    # keep track of which components have finished
    explInstructSpeakComponents = explInstructSpeak.components
    for thisComponent in explInstructSpeak.components:
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
    
    # --- Run Routine "explInstructSpeak" ---
    explInstructSpeak.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # *textInstructSpeak* updates
        
        # if textInstructSpeak is starting this frame...
        if textInstructSpeak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructSpeak.frameNStart = frameN  # exact frame index
            textInstructSpeak.tStart = t  # local t and not account for scr refresh
            textInstructSpeak.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructSpeak, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstructSpeak.started')
            # update status
            textInstructSpeak.status = STARTED
            textInstructSpeak.setAutoDraw(True)
        
        # if textInstructSpeak is active this frame...
        if textInstructSpeak.status == STARTED:
            # update params
            pass
        
        # *keyInstructSpeak_continue* updates
        waitOnFlip = False
        
        # if keyInstructSpeak_continue is starting this frame...
        if keyInstructSpeak_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyInstructSpeak_continue.frameNStart = frameN  # exact frame index
            keyInstructSpeak_continue.tStart = t  # local t and not account for scr refresh
            keyInstructSpeak_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyInstructSpeak_continue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyInstructSpeak_continue.started')
            # update status
            keyInstructSpeak_continue.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyInstructSpeak_continue.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyInstructSpeak_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyInstructSpeak_continue.status == STARTED and not waitOnFlip:
            theseKeys = keyInstructSpeak_continue.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyInstructSpeak_continue_allKeys.extend(theseKeys)
            if len(_keyInstructSpeak_continue_allKeys):
                keyInstructSpeak_continue.keys = _keyInstructSpeak_continue_allKeys[-1].name  # just the last key pressed
                keyInstructSpeak_continue.rt = _keyInstructSpeak_continue_allKeys[-1].rt
                keyInstructSpeak_continue.duration = _keyInstructSpeak_continue_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *textInstructSpeak_continue* updates
        
        # if textInstructSpeak_continue is starting this frame...
        if textInstructSpeak_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructSpeak_continue.frameNStart = frameN  # exact frame index
            textInstructSpeak_continue.tStart = t  # local t and not account for scr refresh
            textInstructSpeak_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructSpeak_continue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstructSpeak_continue.started')
            # update status
            textInstructSpeak_continue.status = STARTED
            textInstructSpeak_continue.setAutoDraw(True)
        
        # if textInstructSpeak_continue is active this frame...
        if textInstructSpeak_continue.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=explInstructSpeak,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            explInstructSpeak.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in explInstructSpeak.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "explInstructSpeak" ---
    for thisComponent in explInstructSpeak.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for explInstructSpeak
    explInstructSpeak.tStop = globalClock.getTime(format='float')
    explInstructSpeak.tStopRefresh = tThisFlipGlobal
    thisExp.addData('explInstructSpeak.stopped', explInstructSpeak.tStop)
    # check responses
    if keyInstructSpeak_continue.keys in ['', [], None]:  # No response was made
        keyInstructSpeak_continue.keys = None
    thisExp.addData('keyInstructSpeak_continue.keys',keyInstructSpeak_continue.keys)
    if keyInstructSpeak_continue.keys != None:  # we had a response
        thisExp.addData('keyInstructSpeak_continue.rt', keyInstructSpeak_continue.rt)
        thisExp.addData('keyInstructSpeak_continue.duration', keyInstructSpeak_continue.duration)
    thisExp.nextEntry()
    # the Routine "explInstructSpeak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "explInstructHand" ---
    # create an object to store info about Routine explInstructHand
    explInstructHand = data.Routine(
        name='explInstructHand',
        components=[textInstructHand, imageInstructHand, keyInstructHand, textInstructHand_continue],
    )
    explInstructHand.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyInstructHand
    keyInstructHand.keys = []
    keyInstructHand.rt = []
    _keyInstructHand_allKeys = []
    # store start times for explInstructHand
    explInstructHand.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    explInstructHand.tStart = globalClock.getTime(format='float')
    explInstructHand.status = STARTED
    thisExp.addData('explInstructHand.started', explInstructHand.tStart)
    explInstructHand.maxDuration = None
    # keep track of which components have finished
    explInstructHandComponents = explInstructHand.components
    for thisComponent in explInstructHand.components:
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
    
    # --- Run Routine "explInstructHand" ---
    explInstructHand.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstructHand* updates
        
        # if textInstructHand is starting this frame...
        if textInstructHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructHand.frameNStart = frameN  # exact frame index
            textInstructHand.tStart = t  # local t and not account for scr refresh
            textInstructHand.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructHand, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstructHand.started')
            # update status
            textInstructHand.status = STARTED
            textInstructHand.setAutoDraw(True)
        
        # if textInstructHand is active this frame...
        if textInstructHand.status == STARTED:
            # update params
            pass
        
        # *imageInstructHand* updates
        
        # if imageInstructHand is starting this frame...
        if imageInstructHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageInstructHand.frameNStart = frameN  # exact frame index
            imageInstructHand.tStart = t  # local t and not account for scr refresh
            imageInstructHand.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageInstructHand, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageInstructHand.started')
            # update status
            imageInstructHand.status = STARTED
            imageInstructHand.setAutoDraw(True)
        
        # if imageInstructHand is active this frame...
        if imageInstructHand.status == STARTED:
            # update params
            pass
        
        # *keyInstructHand* updates
        waitOnFlip = False
        
        # if keyInstructHand is starting this frame...
        if keyInstructHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyInstructHand.frameNStart = frameN  # exact frame index
            keyInstructHand.tStart = t  # local t and not account for scr refresh
            keyInstructHand.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyInstructHand, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyInstructHand.started')
            # update status
            keyInstructHand.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyInstructHand.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyInstructHand.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyInstructHand.status == STARTED and not waitOnFlip:
            theseKeys = keyInstructHand.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyInstructHand_allKeys.extend(theseKeys)
            if len(_keyInstructHand_allKeys):
                keyInstructHand.keys = _keyInstructHand_allKeys[-1].name  # just the last key pressed
                keyInstructHand.rt = _keyInstructHand_allKeys[-1].rt
                keyInstructHand.duration = _keyInstructHand_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *textInstructHand_continue* updates
        
        # if textInstructHand_continue is starting this frame...
        if textInstructHand_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructHand_continue.frameNStart = frameN  # exact frame index
            textInstructHand_continue.tStart = t  # local t and not account for scr refresh
            textInstructHand_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructHand_continue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstructHand_continue.started')
            # update status
            textInstructHand_continue.status = STARTED
            textInstructHand_continue.setAutoDraw(True)
        
        # if textInstructHand_continue is active this frame...
        if textInstructHand_continue.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=explInstructHand,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            explInstructHand.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in explInstructHand.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "explInstructHand" ---
    for thisComponent in explInstructHand.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for explInstructHand
    explInstructHand.tStop = globalClock.getTime(format='float')
    explInstructHand.tStopRefresh = tThisFlipGlobal
    thisExp.addData('explInstructHand.stopped', explInstructHand.tStop)
    # check responses
    if keyInstructHand.keys in ['', [], None]:  # No response was made
        keyInstructHand.keys = None
    thisExp.addData('keyInstructHand.keys',keyInstructHand.keys)
    if keyInstructHand.keys != None:  # we had a response
        thisExp.addData('keyInstructHand.rt', keyInstructHand.rt)
        thisExp.addData('keyInstructHand.duration', keyInstructHand.duration)
    thisExp.nextEntry()
    # the Routine "explInstructHand" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "explInstructBoth" ---
    # create an object to store info about Routine explInstructBoth
    explInstructBoth = data.Routine(
        name='explInstructBoth',
        components=[imageInstructBoth, textInstructBoth, keyResponseInstructBoth, textInstructBoth_continue],
    )
    explInstructBoth.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    # Load the image to get its size
    img = Image.open('images/speak_gesture1.png')
    width, height = img.size
    
    # Convert pixel dimensions to PsychoPy units (assuming your window uses 'pix')
    aspect = width / height
    
    # Set the image size dynamically
    # E.g., fix the height and adjust width to preserve aspect ratio:
    fixed_height = 0.4
    sizeImageDemo = [fixed_height * aspect, fixed_height]
    
    imageInstructBoth.setSize(sizeImageDemo)
    # create starting attributes for keyResponseInstructBoth
    keyResponseInstructBoth.keys = []
    keyResponseInstructBoth.rt = []
    _keyResponseInstructBoth_allKeys = []
    # store start times for explInstructBoth
    explInstructBoth.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    explInstructBoth.tStart = globalClock.getTime(format='float')
    explInstructBoth.status = STARTED
    thisExp.addData('explInstructBoth.started', explInstructBoth.tStart)
    explInstructBoth.maxDuration = None
    # keep track of which components have finished
    explInstructBothComponents = explInstructBoth.components
    for thisComponent in explInstructBoth.components:
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
    
    # --- Run Routine "explInstructBoth" ---
    explInstructBoth.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageInstructBoth* updates
        
        # if imageInstructBoth is starting this frame...
        if imageInstructBoth.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageInstructBoth.frameNStart = frameN  # exact frame index
            imageInstructBoth.tStart = t  # local t and not account for scr refresh
            imageInstructBoth.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageInstructBoth, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageInstructBoth.started')
            # update status
            imageInstructBoth.status = STARTED
            imageInstructBoth.setAutoDraw(True)
        
        # if imageInstructBoth is active this frame...
        if imageInstructBoth.status == STARTED:
            # update params
            pass
        
        # *textInstructBoth* updates
        
        # if textInstructBoth is starting this frame...
        if textInstructBoth.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructBoth.frameNStart = frameN  # exact frame index
            textInstructBoth.tStart = t  # local t and not account for scr refresh
            textInstructBoth.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructBoth, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstructBoth.started')
            # update status
            textInstructBoth.status = STARTED
            textInstructBoth.setAutoDraw(True)
        
        # if textInstructBoth is active this frame...
        if textInstructBoth.status == STARTED:
            # update params
            pass
        
        # *keyResponseInstructBoth* updates
        waitOnFlip = False
        
        # if keyResponseInstructBoth is starting this frame...
        if keyResponseInstructBoth.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyResponseInstructBoth.frameNStart = frameN  # exact frame index
            keyResponseInstructBoth.tStart = t  # local t and not account for scr refresh
            keyResponseInstructBoth.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResponseInstructBoth, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyResponseInstructBoth.started')
            # update status
            keyResponseInstructBoth.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyResponseInstructBoth.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyResponseInstructBoth.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyResponseInstructBoth.status == STARTED and not waitOnFlip:
            theseKeys = keyResponseInstructBoth.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyResponseInstructBoth_allKeys.extend(theseKeys)
            if len(_keyResponseInstructBoth_allKeys):
                keyResponseInstructBoth.keys = _keyResponseInstructBoth_allKeys[-1].name  # just the last key pressed
                keyResponseInstructBoth.rt = _keyResponseInstructBoth_allKeys[-1].rt
                keyResponseInstructBoth.duration = _keyResponseInstructBoth_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *textInstructBoth_continue* updates
        
        # if textInstructBoth_continue is starting this frame...
        if textInstructBoth_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructBoth_continue.frameNStart = frameN  # exact frame index
            textInstructBoth_continue.tStart = t  # local t and not account for scr refresh
            textInstructBoth_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructBoth_continue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstructBoth_continue.started')
            # update status
            textInstructBoth_continue.status = STARTED
            textInstructBoth_continue.setAutoDraw(True)
        
        # if textInstructBoth_continue is active this frame...
        if textInstructBoth_continue.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=explInstructBoth,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            explInstructBoth.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in explInstructBoth.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "explInstructBoth" ---
    for thisComponent in explInstructBoth.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for explInstructBoth
    explInstructBoth.tStop = globalClock.getTime(format='float')
    explInstructBoth.tStopRefresh = tThisFlipGlobal
    thisExp.addData('explInstructBoth.stopped', explInstructBoth.tStop)
    # check responses
    if keyResponseInstructBoth.keys in ['', [], None]:  # No response was made
        keyResponseInstructBoth.keys = None
    thisExp.addData('keyResponseInstructBoth.keys',keyResponseInstructBoth.keys)
    if keyResponseInstructBoth.keys != None:  # we had a response
        thisExp.addData('keyResponseInstructBoth.rt', keyResponseInstructBoth.rt)
        thisExp.addData('keyResponseInstructBoth.duration', keyResponseInstructBoth.duration)
    thisExp.nextEntry()
    # the Routine "explInstructBoth" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsTraining = data.TrialHandler2(
        name='trialsTraining',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('trainingTrials.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trialsTraining)  # add the loop to the experiment
    thisTrialsTraining = trialsTraining.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsTraining.rgb)
    if thisTrialsTraining != None:
        for paramName in thisTrialsTraining:
            globals()[paramName] = thisTrialsTraining[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialsTraining in trialsTraining:
        trialsTraining.status = STARTED
        if hasattr(thisTrialsTraining, 'status'):
            thisTrialsTraining.status = STARTED
        currentLoop = trialsTraining
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTraining.rgb)
        if thisTrialsTraining != None:
            for paramName in thisTrialsTraining:
                globals()[paramName] = thisTrialsTraining[paramName]
        
        # --- Prepare to start Routine "blockTraining" ---
        # create an object to store info about Routine blockTraining
        blockTraining = data.Routine(
            name='blockTraining',
            components=[textBlockTraining, keyBlockResponseTraining],
        )
        blockTraining.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for keyBlockResponseTraining
        keyBlockResponseTraining.keys = []
        keyBlockResponseTraining.rt = []
        _keyBlockResponseTraining_allKeys = []
        # store start times for blockTraining
        blockTraining.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blockTraining.tStart = globalClock.getTime(format='float')
        blockTraining.status = STARTED
        thisExp.addData('blockTraining.started', blockTraining.tStart)
        blockTraining.maxDuration = None
        # keep track of which components have finished
        blockTrainingComponents = blockTraining.components
        for thisComponent in blockTraining.components:
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
        
        # --- Run Routine "blockTraining" ---
        blockTraining.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrialsTraining, 'status') and thisTrialsTraining.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBlockTraining* updates
            
            # if textBlockTraining is starting this frame...
            if textBlockTraining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlockTraining.frameNStart = frameN  # exact frame index
                textBlockTraining.tStart = t  # local t and not account for scr refresh
                textBlockTraining.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlockTraining, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlockTraining.started')
                # update status
                textBlockTraining.status = STARTED
                textBlockTraining.setAutoDraw(True)
            
            # if textBlockTraining is active this frame...
            if textBlockTraining.status == STARTED:
                # update params
                pass
            
            # *keyBlockResponseTraining* updates
            waitOnFlip = False
            
            # if keyBlockResponseTraining is starting this frame...
            if keyBlockResponseTraining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyBlockResponseTraining.frameNStart = frameN  # exact frame index
                keyBlockResponseTraining.tStart = t  # local t and not account for scr refresh
                keyBlockResponseTraining.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyBlockResponseTraining, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyBlockResponseTraining.started')
                # update status
                keyBlockResponseTraining.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyBlockResponseTraining.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyBlockResponseTraining.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyBlockResponseTraining.status == STARTED and not waitOnFlip:
                theseKeys = keyBlockResponseTraining.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _keyBlockResponseTraining_allKeys.extend(theseKeys)
                if len(_keyBlockResponseTraining_allKeys):
                    keyBlockResponseTraining.keys = _keyBlockResponseTraining_allKeys[-1].name  # just the last key pressed
                    keyBlockResponseTraining.rt = _keyBlockResponseTraining_allKeys[-1].rt
                    keyBlockResponseTraining.duration = _keyBlockResponseTraining_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blockTraining,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blockTraining.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockTraining.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blockTraining" ---
        for thisComponent in blockTraining.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blockTraining
        blockTraining.tStop = globalClock.getTime(format='float')
        blockTraining.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blockTraining.stopped', blockTraining.tStop)
        # check responses
        if keyBlockResponseTraining.keys in ['', [], None]:  # No response was made
            keyBlockResponseTraining.keys = None
        trialsTraining.addData('keyBlockResponseTraining.keys',keyBlockResponseTraining.keys)
        if keyBlockResponseTraining.keys != None:  # we had a response
            trialsTraining.addData('keyBlockResponseTraining.rt', keyBlockResponseTraining.rt)
            trialsTraining.addData('keyBlockResponseTraining.duration', keyBlockResponseTraining.duration)
        # the Routine "blockTraining" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trialTraining" ---
        # create an object to store info about Routine trialTraining
        trialTraining = data.Routine(
            name='trialTraining',
            components=[iti_Training, textStart_Training, movieGesture_Training, audioStim_Training, instructionImage_Training, actionCue_Training, audioGoCue_Training],
        )
        trialTraining.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeTraining
        # select green or red circle depending on Go/Nogo trial
        if action == "go":
            circle_color = 'green'
        elif action == 'nogo':
            circle_color = 'red'
        else:
            circle_color = 'black'
            
        ## select image dimension for instruction image
        
        # Load the image to get its size
        img = Image.open(instructionSymbol)
        width, height = img.size
        
        # Convert pixel dimensions to PsychoPy units (assuming your window uses 'pix')
        aspect = width / height
        
        # Set the image size dynamically
        # E.g., fix the height and adjust width to preserve aspect ratio:
        fixed_height = 0.4
        thisExp.addData('image_aspect', aspect)
        sizeImage = [fixed_height * aspect, fixed_height]
        
        movieGesture_Training.setMovie(stimVideo)
        audioStim_Training.setSound(stimAudio, secs=6, hamming=True)
        audioStim_Training.setVolume(1.0, log=False)
        audioStim_Training.seek(0)
        instructionImage_Training.setSize(sizeImage)
        instructionImage_Training.setImage(instructionSymbol)
        actionCue_Training.setFillColor(circle_color)
        actionCue_Training.setLineColor(circle_color)
        audioGoCue_Training.setSound('audios/race-start-beeps-125125.mp3', secs=1.0, hamming=True)
        audioGoCue_Training.setVolume(0.8, log=False)
        audioGoCue_Training.seek(0)
        # store start times for trialTraining
        trialTraining.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialTraining.tStart = globalClock.getTime(format='float')
        trialTraining.status = STARTED
        thisExp.addData('trialTraining.started', trialTraining.tStart)
        trialTraining.maxDuration = None
        # keep track of which components have finished
        trialTrainingComponents = trialTraining.components
        for thisComponent in trialTraining.components:
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
        
        # --- Run Routine "trialTraining" ---
        trialTraining.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 12.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrialsTraining, 'status') and thisTrialsTraining.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iti_Training* updates
            
            # if iti_Training is starting this frame...
            if iti_Training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                iti_Training.frameNStart = frameN  # exact frame index
                iti_Training.tStart = t  # local t and not account for scr refresh
                iti_Training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(iti_Training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'iti_Training.started')
                # update status
                iti_Training.status = STARTED
                iti_Training.setAutoDraw(True)
            
            # if iti_Training is active this frame...
            if iti_Training.status == STARTED:
                # update params
                pass
            
            # if iti_Training is stopping this frame...
            if iti_Training.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    iti_Training.tStop = t  # not accounting for scr refresh
                    iti_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    iti_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'iti_Training.stopped')
                    # update status
                    iti_Training.status = FINISHED
                    iti_Training.setAutoDraw(False)
            
            # *textStart_Training* updates
            
            # if textStart_Training is starting this frame...
            if textStart_Training.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                textStart_Training.frameNStart = frameN  # exact frame index
                textStart_Training.tStart = t  # local t and not account for scr refresh
                textStart_Training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textStart_Training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textStart_Training.started')
                # update status
                textStart_Training.status = STARTED
                textStart_Training.setAutoDraw(True)
                #send_trigger()
            
            # if textStart_Training is active this frame...
            if textStart_Training.status == STARTED:
                # update params
                pass
            
            # if textStart_Training is stopping this frame...
            if textStart_Training.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 3-frameTolerance:
                    # keep track of stop time/frame for later
                    textStart_Training.tStop = t  # not accounting for scr refresh
                    textStart_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    textStart_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textStart_Training.stopped')
                    # update status
                    textStart_Training.status = FINISHED
                    textStart_Training.setAutoDraw(False)
            
            # *movieGesture_Training* updates
            
            # if movieGesture_Training is starting this frame...
            if movieGesture_Training.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                movieGesture_Training.frameNStart = frameN  # exact frame index
                movieGesture_Training.tStart = t  # local t and not account for scr refresh
                movieGesture_Training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movieGesture_Training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'movieGesture_Training.started')
                # update status
                movieGesture_Training.status = STARTED
                movieGesture_Training.setAutoDraw(True)
                movieGesture_Training.play()
            
            # if movieGesture_Training is stopping this frame...
            if movieGesture_Training.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 6-frameTolerance or movieGesture_Training.isFinished:
                    # keep track of stop time/frame for later
                    movieGesture_Training.tStop = t  # not accounting for scr refresh
                    movieGesture_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    movieGesture_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'movieGesture_Training.stopped')
                    # update status
                    movieGesture_Training.status = FINISHED
                    movieGesture_Training.setAutoDraw(False)
                    movieGesture_Training.stop()
            
            # *audioStim_Training* updates
            
            # if audioStim_Training is starting this frame...
            if audioStim_Training.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                audioStim_Training.frameNStart = frameN  # exact frame index
                audioStim_Training.tStart = t  # local t and not account for scr refresh
                audioStim_Training.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('audioStim_Training.started', tThisFlipGlobal)
                # update status
                audioStim_Training.status = STARTED
                audioStim_Training.play(when=win)  # sync with win flip
            
            # if audioStim_Training is stopping this frame...
            if audioStim_Training.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 6-frameTolerance or audioStim_Training.isFinished:
                    # keep track of stop time/frame for later
                    audioStim_Training.tStop = t  # not accounting for scr refresh
                    audioStim_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    audioStim_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'audioStim_Training.stopped')
                    # update status
                    audioStim_Training.status = FINISHED
                    audioStim_Training.stop()
            
            # *instructionImage_Training* updates
            
            # if instructionImage_Training is starting this frame...
            if instructionImage_Training.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                # keep track of start time/frame for later
                instructionImage_Training.frameNStart = frameN  # exact frame index
                instructionImage_Training.tStart = t  # local t and not account for scr refresh
                instructionImage_Training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructionImage_Training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructionImage_Training.started')
                # update status
                instructionImage_Training.status = STARTED
                instructionImage_Training.setAutoDraw(True)
            
            # if instructionImage_Training is active this frame...
            if instructionImage_Training.status == STARTED:
                # update params
                pass
            
            # if instructionImage_Training is stopping this frame...
            if instructionImage_Training.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 8.5-frameTolerance:
                    # keep track of stop time/frame for later
                    instructionImage_Training.tStop = t  # not accounting for scr refresh
                    instructionImage_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    instructionImage_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instructionImage_Training.stopped')
                    # update status
                    instructionImage_Training.status = FINISHED
                    instructionImage_Training.setAutoDraw(False)
            
            # *actionCue_Training* updates
            
            # if actionCue_Training is starting this frame...
            if actionCue_Training.status == NOT_STARTED and tThisFlip >= 8.5-frameTolerance:
                # keep track of start time/frame for later
                actionCue_Training.frameNStart = frameN  # exact frame index
                actionCue_Training.tStart = t  # local t and not account for scr refresh
                actionCue_Training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(actionCue_Training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'actionCue_Training.started')
                # update status
                actionCue_Training.status = STARTED
                actionCue_Training.setAutoDraw(True)
            
            # if actionCue_Training is active this frame...
            if actionCue_Training.status == STARTED:
                # update params
                pass
            
            # if actionCue_Training is stopping this frame...
            if actionCue_Training.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 12-frameTolerance:
                    # keep track of stop time/frame for later
                    actionCue_Training.tStop = t  # not accounting for scr refresh
                    actionCue_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    actionCue_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'actionCue_Training.stopped')
                    # update status
                    actionCue_Training.status = FINISHED
                    actionCue_Training.setAutoDraw(False)
            
            # *audioGoCue_Training* updates
            
            # if audioGoCue_Training is starting this frame...
            if audioGoCue_Training.status == NOT_STARTED and tThisFlip >= 8.5-frameTolerance:
                # keep track of start time/frame for later
                audioGoCue_Training.frameNStart = frameN  # exact frame index
                audioGoCue_Training.tStart = t  # local t and not account for scr refresh
                audioGoCue_Training.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('audioGoCue_Training.started', tThisFlipGlobal)
                # update status
                audioGoCue_Training.status = STARTED
                audioGoCue_Training.play(when=win)  # sync with win flip
            
            # if audioGoCue_Training is stopping this frame...
            if audioGoCue_Training.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > audioGoCue_Training.tStartRefresh + 1.0-frameTolerance or audioGoCue_Training.isFinished:
                    # keep track of stop time/frame for later
                    audioGoCue_Training.tStop = t  # not accounting for scr refresh
                    audioGoCue_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    audioGoCue_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'audioGoCue_Training.stopped')
                    # update status
                    audioGoCue_Training.status = FINISHED
                    audioGoCue_Training.stop()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialTraining,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trialTraining.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialTraining.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialTraining" ---
        for thisComponent in trialTraining.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialTraining
        trialTraining.tStop = globalClock.getTime(format='float')
        trialTraining.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trialTraining.stopped', trialTraining.tStop)
        audioStim_Training.pause()  # ensure sound has stopped at end of Routine
        audioGoCue_Training.pause()  # ensure sound has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if trialTraining.maxDurationReached:
            routineTimer.addTime(-trialTraining.maxDuration)
        elif trialTraining.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-12.000000)
        # mark thisTrialsTraining as finished
        if hasattr(thisTrialsTraining, 'status'):
            thisTrialsTraining.status = FINISHED
        # if awaiting a pause, pause now
        if trialsTraining.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trialsTraining.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialsTraining'
    trialsTraining.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    blockLoop = data.TrialHandler2(
        name='blockLoop',
        nReps=5.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(blockLoop)  # add the loop to the experiment
    thisBlockLoop = blockLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
    if thisBlockLoop != None:
        for paramName in thisBlockLoop:
            globals()[paramName] = thisBlockLoop[paramName]
    
    for thisBlockLoop in blockLoop:
        blockLoop.status = STARTED
        if hasattr(thisBlockLoop, 'status'):
            thisBlockLoop.status = STARTED
        currentLoop = blockLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
        if thisBlockLoop != None:
            for paramName in thisBlockLoop:
                globals()[paramName] = thisBlockLoop[paramName]
        
        # --- Prepare to start Routine "blockStart" ---
        # create an object to store info about Routine blockStart
        blockStart = data.Routine(
            name='blockStart',
            components=[textBlockStart, keyBlockResponse],
        )
        blockStart.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeStimuliLoad
        #choose new,random subset of nogo trials
        subset_nogo_trials = nogo_trials.sample(n=5).reset_index(drop=True)  # select 5 random rows
        
        # new all_trials array for the next block 
        all_trials = pd.concat([go_trials_rep, subset_nogo_trials], ignore_index = True)
        
        # re-shuffle at the beginning of each block 
        all_trials = all_trials.sample(frac=1).reset_index(drop=True)
        
        # temporary csv for this block 
        #all_trials.to_csv('block_trials.csv', index = False)
        nBlock += 1
        all_trials.to_csv(f"blocks/block_trials{nBlock}.csv", index = False)
        all_trials.to_csv("current_block_trials.csv", index = False)
        
        # set trial number to 0
        trialN = 0
        nOneThird = 26
        nTwoThirds = 52
        repOneThird = 0
        repTwoThirds = 0
        
        # create starting attributes for keyBlockResponse
        keyBlockResponse.keys = []
        keyBlockResponse.rt = []
        _keyBlockResponse_allKeys = []
        # store start times for blockStart
        blockStart.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blockStart.tStart = globalClock.getTime(format='float')
        blockStart.status = STARTED
        thisExp.addData('blockStart.started', blockStart.tStart)
        blockStart.maxDuration = None
        # keep track of which components have finished
        blockStartComponents = blockStart.components
        for thisComponent in blockStart.components:
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
        
        # --- Run Routine "blockStart" ---
        blockStart.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlockLoop, 'status') and thisBlockLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBlockStart* updates
            
            # if textBlockStart is starting this frame...
            if textBlockStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlockStart.frameNStart = frameN  # exact frame index
                textBlockStart.tStart = t  # local t and not account for scr refresh
                textBlockStart.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlockStart, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlockStart.started')
                # update status
                textBlockStart.status = STARTED
                textBlockStart.setAutoDraw(True)
            
            # if textBlockStart is active this frame...
            if textBlockStart.status == STARTED:
                # update params
                pass
            
            # *keyBlockResponse* updates
            waitOnFlip = False
            
            # if keyBlockResponse is starting this frame...
            if keyBlockResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyBlockResponse.frameNStart = frameN  # exact frame index
                keyBlockResponse.tStart = t  # local t and not account for scr refresh
                keyBlockResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyBlockResponse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyBlockResponse.started')
                # update status
                keyBlockResponse.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyBlockResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyBlockResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyBlockResponse.status == STARTED and not waitOnFlip:
                theseKeys = keyBlockResponse.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _keyBlockResponse_allKeys.extend(theseKeys)
                if len(_keyBlockResponse_allKeys):
                    keyBlockResponse.keys = _keyBlockResponse_allKeys[-1].name  # just the last key pressed
                    keyBlockResponse.rt = _keyBlockResponse_allKeys[-1].rt
                    keyBlockResponse.duration = _keyBlockResponse_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blockStart,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blockStart.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockStart.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blockStart" ---
        for thisComponent in blockStart.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blockStart
        blockStart.tStop = globalClock.getTime(format='float')
        blockStart.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blockStart.stopped', blockStart.tStop)
        # check responses
        if keyBlockResponse.keys in ['', [], None]:  # No response was made
            keyBlockResponse.keys = None
        blockLoop.addData('keyBlockResponse.keys',keyBlockResponse.keys)
        if keyBlockResponse.keys != None:  # we had a response
            blockLoop.addData('keyBlockResponse.rt', keyBlockResponse.rt)
            blockLoop.addData('keyBlockResponse.duration', keyBlockResponse.duration)
        # the Routine "blockStart" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsLoop = data.TrialHandler2(
            name='trialsLoop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('current_block_trials.csv'), 
            seed=None, 
        )
        thisExp.addLoop(trialsLoop)  # add the loop to the experiment
        thisTrialsLoop = trialsLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
        if thisTrialsLoop != None:
            for paramName in thisTrialsLoop:
                globals()[paramName] = thisTrialsLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrialsLoop in trialsLoop:
            trialsLoop.status = STARTED
            if hasattr(thisTrialsLoop, 'status'):
                thisTrialsLoop.status = STARTED
            currentLoop = trialsLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
            if thisTrialsLoop != None:
                for paramName in thisTrialsLoop:
                    globals()[paramName] = thisTrialsLoop[paramName]
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[iti, textStart, movieGesture, audioStimuli, instructionImage, actionCue, audioGoCue],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from codeActionCUE
            # select green or red circle depending on Go/Nogo trial
            if action == "go":
                circle_color = 'green'
            elif action == 'nogo':
                circle_color = 'red'
            else:
                circle_color = 'black'
                
            ## select image dimension for instruction image
            
            # Load the image to get its size
            img = Image.open(instructionSymbol)
            width, height = img.size
            
            # Convert pixel dimensions to PsychoPy units (assuming your window uses 'pix')
            aspect = width / height
            
            # Set the image size dynamically
            # E.g., fix the height and adjust width to preserve aspect ratio:
            fixed_height = 0.4
            thisExp.addData('image_aspect', aspect)
            sizeImage = [fixed_height * aspect, fixed_height]
            
            
            # check for keypress pause
            keys = event.getKeys(keyList=['p'])
            
            # if p was pressed, set a flag to run the routine
            run_routine = 'p' in keys
            print(run_routine)
            
            if run_routine:
                nPause = 1
            else:
                nPause = 0
            
            # increase trialNumber
            trialN += 1
            print(trialN)
            
            if trialN == nOneThird:
                repOneThird = 1
            elif trialN == nTwoThirds:
                repTwoThirds = 1
            movieGesture.setMovie(stimVideo)
            audioStimuli.setSound(stimAudio, secs=6, hamming=True)
            audioStimuli.setVolume(1.0, log=False)
            audioStimuli.seek(0)
            instructionImage.setSize(sizeImage)
            instructionImage.setImage(instructionSymbol)
            actionCue.setFillColor(circle_color)
            actionCue.setLineColor(circle_color)
            audioGoCue.setSound('audios/race-start-beeps-125125.mp3', secs=1.0, hamming=True)
            audioGoCue.setVolume(0.8, log=False)
            audioGoCue.seek(0)
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
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
            
            # --- Run Routine "trial" ---
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 12.0:
                # if trial has changed, end Routine now
                if hasattr(thisTrialsLoop, 'status') and thisTrialsLoop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *iti* updates
                
                # if iti is starting this frame...
                if iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    iti.frameNStart = frameN  # exact frame index
                    iti.tStart = t  # local t and not account for scr refresh
                    iti.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(iti, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'iti.started')
                    # update status
                    iti.status = STARTED
                    iti.setAutoDraw(True)
                
                # if iti is active this frame...
                if iti.status == STARTED:
                    # update params
                    pass
                
                # if iti is stopping this frame...
                if iti.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        iti.tStop = t  # not accounting for scr refresh
                        iti.tStopRefresh = tThisFlipGlobal  # on global time
                        iti.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'iti.stopped')
                        # update status
                        iti.status = FINISHED
                        iti.setAutoDraw(False)
                
                # *textStart* updates
                
                # if textStart is starting this frame...
                if textStart.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    textStart.frameNStart = frameN  # exact frame index
                    textStart.tStart = t  # local t and not account for scr refresh
                    textStart.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textStart, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textStart.started')
                    # update status
                    textStart.status = STARTED
                    textStart.setAutoDraw(True)
                   # send_trigger()
                
                # if textStart is active this frame...
                if textStart.status == STARTED:
                    # update params
                    pass
                
                # if textStart is stopping this frame...
                if textStart.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 3-frameTolerance:
                        # keep track of stop time/frame for later
                        textStart.tStop = t  # not accounting for scr refresh
                        textStart.tStopRefresh = tThisFlipGlobal  # on global time
                        textStart.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textStart.stopped')
                        # update status
                        textStart.status = FINISHED
                        textStart.setAutoDraw(False)
                
                # *movieGesture* updates
                
                # if movieGesture is starting this frame...
                if movieGesture.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                    # keep track of start time/frame for later
                    movieGesture.frameNStart = frameN  # exact frame index
                    movieGesture.tStart = t  # local t and not account for scr refresh
                    movieGesture.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movieGesture, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'movieGesture.started')
                    # update status
                    movieGesture.status = STARTED
                    movieGesture.setAutoDraw(True)
                    movieGesture.play()
                
                # if movieGesture is stopping this frame...
                if movieGesture.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 6-frameTolerance or movieGesture.isFinished:
                        # keep track of stop time/frame for later
                        movieGesture.tStop = t  # not accounting for scr refresh
                        movieGesture.tStopRefresh = tThisFlipGlobal  # on global time
                        movieGesture.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'movieGesture.stopped')
                        # update status
                        movieGesture.status = FINISHED
                        movieGesture.setAutoDraw(False)
                        movieGesture.stop()
                
                # *audioStimuli* updates
                
                # if audioStimuli is starting this frame...
                if audioStimuli.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                    # keep track of start time/frame for later
                    audioStimuli.frameNStart = frameN  # exact frame index
                    audioStimuli.tStart = t  # local t and not account for scr refresh
                    audioStimuli.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('audioStimuli.started', tThisFlipGlobal)
                    # update status
                    audioStimuli.status = STARTED
                    audioStimuli.play(when=win)  # sync with win flip
                
                # if audioStimuli is stopping this frame...
                if audioStimuli.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 6-frameTolerance or audioStimuli.isFinished:
                        # keep track of stop time/frame for later
                        audioStimuli.tStop = t  # not accounting for scr refresh
                        audioStimuli.tStopRefresh = tThisFlipGlobal  # on global time
                        audioStimuli.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'audioStimuli.stopped')
                        # update status
                        audioStimuli.status = FINISHED
                        audioStimuli.stop()
                
                # *instructionImage* updates
                
                # if instructionImage is starting this frame...
                if instructionImage.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                    # keep track of start time/frame for later
                    instructionImage.frameNStart = frameN  # exact frame index
                    instructionImage.tStart = t  # local t and not account for scr refresh
                    instructionImage.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instructionImage, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instructionImage.started')
                    # update status
                    instructionImage.status = STARTED
                    instructionImage.setAutoDraw(True)
                
                # if instructionImage is active this frame...
                if instructionImage.status == STARTED:
                    # update params
                    pass
                
                # if instructionImage is stopping this frame...
                if instructionImage.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 8.5-frameTolerance:
                        # keep track of stop time/frame for later
                        instructionImage.tStop = t  # not accounting for scr refresh
                        instructionImage.tStopRefresh = tThisFlipGlobal  # on global time
                        instructionImage.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'instructionImage.stopped')
                        # update status
                        instructionImage.status = FINISHED
                        instructionImage.setAutoDraw(False)
                
                # *actionCue* updates
                
                # if actionCue is starting this frame...
                if actionCue.status == NOT_STARTED and tThisFlip >= 8.5-frameTolerance:
                    # keep track of start time/frame for later
                    actionCue.frameNStart = frameN  # exact frame index
                    actionCue.tStart = t  # local t and not account for scr refresh
                    actionCue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(actionCue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'actionCue.started')
                    # update status
                    actionCue.status = STARTED
                    actionCue.setAutoDraw(True)
                
                # if actionCue is active this frame...
                if actionCue.status == STARTED:
                    # update params
                    pass
                
                # if actionCue is stopping this frame...
                if actionCue.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 12-frameTolerance:
                        # keep track of stop time/frame for later
                        actionCue.tStop = t  # not accounting for scr refresh
                        actionCue.tStopRefresh = tThisFlipGlobal  # on global time
                        actionCue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'actionCue.stopped')
                        # update status
                        actionCue.status = FINISHED
                        actionCue.setAutoDraw(False)
                
                # *audioGoCue* updates
                
                # if audioGoCue is starting this frame...
                if audioGoCue.status == NOT_STARTED and tThisFlip >= 8.5-frameTolerance:
                    # keep track of start time/frame for later
                    audioGoCue.frameNStart = frameN  # exact frame index
                    audioGoCue.tStart = t  # local t and not account for scr refresh
                    audioGoCue.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('audioGoCue.started', tThisFlipGlobal)
                    # update status
                    audioGoCue.status = STARTED
                    audioGoCue.play(when=win)  # sync with win flip
                
                # if audioGoCue is stopping this frame...
                if audioGoCue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > audioGoCue.tStartRefresh + 1.0-frameTolerance or audioGoCue.isFinished:
                        # keep track of stop time/frame for later
                        audioGoCue.tStop = t  # not accounting for scr refresh
                        audioGoCue.tStopRefresh = tThisFlipGlobal  # on global time
                        audioGoCue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'audioGoCue.stopped')
                        # update status
                        audioGoCue.status = FINISHED
                        audioGoCue.stop()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=trial,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            audioStimuli.pause()  # ensure sound has stopped at end of Routine
            audioGoCue.pause()  # ensure sound has stopped at end of Routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial.maxDurationReached:
                routineTimer.addTime(-trial.maxDuration)
            elif trial.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-12.000000)
            
            # set up handler to look after randomisation of conditions etc
            pause = data.TrialHandler2(
                name='pause',
                nReps=nPause, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(pause)  # add the loop to the experiment
            thisPause = pause.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisPause.rgb)
            if thisPause != None:
                for paramName in thisPause:
                    globals()[paramName] = thisPause[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisPause in pause:
                pause.status = STARTED
                if hasattr(thisPause, 'status'):
                    thisPause.status = STARTED
                currentLoop = pause
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisPause.rgb)
                if thisPause != None:
                    for paramName in thisPause:
                        globals()[paramName] = thisPause[paramName]
                
                # --- Prepare to start Routine "paused" ---
                # create an object to store info about Routine paused
                paused = data.Routine(
                    name='paused',
                    components=[textPause, keyRespPause],
                )
                paused.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from codePause
                keys = event.getKeys(keyList = ['p'])
                
                if 'p' in keys: 
                    event.clearEvents() # clear pressed key 'p'
                # create starting attributes for keyRespPause
                keyRespPause.keys = []
                keyRespPause.rt = []
                _keyRespPause_allKeys = []
                # store start times for paused
                paused.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                paused.tStart = globalClock.getTime(format='float')
                paused.status = STARTED
                thisExp.addData('paused.started', paused.tStart)
                paused.maxDuration = None
                # keep track of which components have finished
                pausedComponents = paused.components
                for thisComponent in paused.components:
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
                
                # --- Run Routine "paused" ---
                paused.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisPause, 'status') and thisPause.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *textPause* updates
                    
                    # if textPause is starting this frame...
                    if textPause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textPause.frameNStart = frameN  # exact frame index
                        textPause.tStart = t  # local t and not account for scr refresh
                        textPause.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textPause, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textPause.started')
                        # update status
                        textPause.status = STARTED
                        textPause.setAutoDraw(True)
                    
                    # if textPause is active this frame...
                    if textPause.status == STARTED:
                        # update params
                        pass
                    
                    # *keyRespPause* updates
                    waitOnFlip = False
                    
                    # if keyRespPause is starting this frame...
                    if keyRespPause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        keyRespPause.frameNStart = frameN  # exact frame index
                        keyRespPause.tStart = t  # local t and not account for scr refresh
                        keyRespPause.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(keyRespPause, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'keyRespPause.started')
                        # update status
                        keyRespPause.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(keyRespPause.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(keyRespPause.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if keyRespPause.status == STARTED and not waitOnFlip:
                        theseKeys = keyRespPause.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _keyRespPause_allKeys.extend(theseKeys)
                        if len(_keyRespPause_allKeys):
                            keyRespPause.keys = _keyRespPause_allKeys[-1].name  # just the last key pressed
                            keyRespPause.rt = _keyRespPause_allKeys[-1].rt
                            keyRespPause.duration = _keyRespPause_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=paused,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        paused.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in paused.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "paused" ---
                for thisComponent in paused.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for paused
                paused.tStop = globalClock.getTime(format='float')
                paused.tStopRefresh = tThisFlipGlobal
                thisExp.addData('paused.stopped', paused.tStop)
                # check responses
                if keyRespPause.keys in ['', [], None]:  # No response was made
                    keyRespPause.keys = None
                pause.addData('keyRespPause.keys',keyRespPause.keys)
                if keyRespPause.keys != None:  # we had a response
                    pause.addData('keyRespPause.rt', keyRespPause.rt)
                    pause.addData('keyRespPause.duration', keyRespPause.duration)
                # the Routine "paused" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                # mark thisPause as finished
                if hasattr(thisPause, 'status'):
                    thisPause.status = FINISHED
                # if awaiting a pause, pause now
                if pause.status == PAUSED:
                    thisExp.status = PAUSED
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[globalClock], 
                    )
                    # once done pausing, restore running status
                    pause.status = STARTED
                thisExp.nextEntry()
                
            # completed nPause repeats of 'pause'
            pause.status = FINISHED
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # set up handler to look after randomisation of conditions etc
            oneThirdLoop = data.TrialHandler2(
                name='oneThirdLoop',
                nReps=repOneThird, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(oneThirdLoop)  # add the loop to the experiment
            thisOneThirdLoop = oneThirdLoop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisOneThirdLoop.rgb)
            if thisOneThirdLoop != None:
                for paramName in thisOneThirdLoop:
                    globals()[paramName] = thisOneThirdLoop[paramName]
            
            for thisOneThirdLoop in oneThirdLoop:
                oneThirdLoop.status = STARTED
                if hasattr(thisOneThirdLoop, 'status'):
                    thisOneThirdLoop.status = STARTED
                currentLoop = oneThirdLoop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # abbreviate parameter names if possible (e.g. rgb = thisOneThirdLoop.rgb)
                if thisOneThirdLoop != None:
                    for paramName in thisOneThirdLoop:
                        globals()[paramName] = thisOneThirdLoop[paramName]
                
                # --- Prepare to start Routine "breakOnethird" ---
                # create an object to store info about Routine breakOnethird
                breakOnethird = data.Routine(
                    name='breakOnethird',
                    components=[textOneThird],
                )
                breakOnethird.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from codeOnethird
                # reset to default
                repOneThird = 0
                # store start times for breakOnethird
                breakOnethird.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                breakOnethird.tStart = globalClock.getTime(format='float')
                breakOnethird.status = STARTED
                thisExp.addData('breakOnethird.started', breakOnethird.tStart)
                breakOnethird.maxDuration = None
                # keep track of which components have finished
                breakOnethirdComponents = breakOnethird.components
                for thisComponent in breakOnethird.components:
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
                
                # --- Run Routine "breakOnethird" ---
                breakOnethird.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 15.0:
                    # if trial has changed, end Routine now
                    if hasattr(thisOneThirdLoop, 'status') and thisOneThirdLoop.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *textOneThird* updates
                    
                    # if textOneThird is starting this frame...
                    if textOneThird.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textOneThird.frameNStart = frameN  # exact frame index
                        textOneThird.tStart = t  # local t and not account for scr refresh
                        textOneThird.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textOneThird, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textOneThird.started')
                        # update status
                        textOneThird.status = STARTED
                        textOneThird.setAutoDraw(True)
                    
                    # if textOneThird is active this frame...
                    if textOneThird.status == STARTED:
                        # update params
                        pass
                    
                    # if textOneThird is stopping this frame...
                    if textOneThird.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > textOneThird.tStartRefresh + 15-frameTolerance:
                            # keep track of stop time/frame for later
                            textOneThird.tStop = t  # not accounting for scr refresh
                            textOneThird.tStopRefresh = tThisFlipGlobal  # on global time
                            textOneThird.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'textOneThird.stopped')
                            # update status
                            textOneThird.status = FINISHED
                            textOneThird.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=breakOnethird,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        breakOnethird.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in breakOnethird.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "breakOnethird" ---
                for thisComponent in breakOnethird.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for breakOnethird
                breakOnethird.tStop = globalClock.getTime(format='float')
                breakOnethird.tStopRefresh = tThisFlipGlobal
                thisExp.addData('breakOnethird.stopped', breakOnethird.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if breakOnethird.maxDurationReached:
                    routineTimer.addTime(-breakOnethird.maxDuration)
                elif breakOnethird.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-15.000000)
                # mark thisOneThirdLoop as finished
                if hasattr(thisOneThirdLoop, 'status'):
                    thisOneThirdLoop.status = FINISHED
                # if awaiting a pause, pause now
                if oneThirdLoop.status == PAUSED:
                    thisExp.status = PAUSED
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[globalClock], 
                    )
                    # once done pausing, restore running status
                    oneThirdLoop.status = STARTED
            # completed repOneThird repeats of 'oneThirdLoop'
            oneThirdLoop.status = FINISHED
            
            
            # set up handler to look after randomisation of conditions etc
            twoThirdsLoop = data.TrialHandler2(
                name='twoThirdsLoop',
                nReps=repTwoThirds, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(twoThirdsLoop)  # add the loop to the experiment
            thisTwoThirdsLoop = twoThirdsLoop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTwoThirdsLoop.rgb)
            if thisTwoThirdsLoop != None:
                for paramName in thisTwoThirdsLoop:
                    globals()[paramName] = thisTwoThirdsLoop[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTwoThirdsLoop in twoThirdsLoop:
                twoThirdsLoop.status = STARTED
                if hasattr(thisTwoThirdsLoop, 'status'):
                    thisTwoThirdsLoop.status = STARTED
                currentLoop = twoThirdsLoop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTwoThirdsLoop.rgb)
                if thisTwoThirdsLoop != None:
                    for paramName in thisTwoThirdsLoop:
                        globals()[paramName] = thisTwoThirdsLoop[paramName]
                
                # --- Prepare to start Routine "breakTwothirds" ---
                # create an object to store info about Routine breakTwothirds
                breakTwothirds = data.Routine(
                    name='breakTwothirds',
                    components=[textTwothirds],
                )
                breakTwothirds.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # store start times for breakTwothirds
                breakTwothirds.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                breakTwothirds.tStart = globalClock.getTime(format='float')
                breakTwothirds.status = STARTED
                thisExp.addData('breakTwothirds.started', breakTwothirds.tStart)
                breakTwothirds.maxDuration = None
                # keep track of which components have finished
                breakTwothirdsComponents = breakTwothirds.components
                for thisComponent in breakTwothirds.components:
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
                
                # --- Run Routine "breakTwothirds" ---
                breakTwothirds.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 15.0:
                    # if trial has changed, end Routine now
                    if hasattr(thisTwoThirdsLoop, 'status') and thisTwoThirdsLoop.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *textTwothirds* updates
                    
                    # if textTwothirds is starting this frame...
                    if textTwothirds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textTwothirds.frameNStart = frameN  # exact frame index
                        textTwothirds.tStart = t  # local t and not account for scr refresh
                        textTwothirds.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textTwothirds, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textTwothirds.started')
                        # update status
                        textTwothirds.status = STARTED
                        textTwothirds.setAutoDraw(True)
                    
                    # if textTwothirds is active this frame...
                    if textTwothirds.status == STARTED:
                        # update params
                        pass
                    
                    # if textTwothirds is stopping this frame...
                    if textTwothirds.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > textTwothirds.tStartRefresh + 15-frameTolerance:
                            # keep track of stop time/frame for later
                            textTwothirds.tStop = t  # not accounting for scr refresh
                            textTwothirds.tStopRefresh = tThisFlipGlobal  # on global time
                            textTwothirds.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'textTwothirds.stopped')
                            # update status
                            textTwothirds.status = FINISHED
                            textTwothirds.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=breakTwothirds,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        breakTwothirds.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in breakTwothirds.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "breakTwothirds" ---
                for thisComponent in breakTwothirds.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for breakTwothirds
                breakTwothirds.tStop = globalClock.getTime(format='float')
                breakTwothirds.tStopRefresh = tThisFlipGlobal
                thisExp.addData('breakTwothirds.stopped', breakTwothirds.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if breakTwothirds.maxDurationReached:
                    routineTimer.addTime(-breakTwothirds.maxDuration)
                elif breakTwothirds.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-15.000000)
                # mark thisTwoThirdsLoop as finished
                if hasattr(thisTwoThirdsLoop, 'status'):
                    thisTwoThirdsLoop.status = FINISHED
                # if awaiting a pause, pause now
                if twoThirdsLoop.status == PAUSED:
                    thisExp.status = PAUSED
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[globalClock], 
                    )
                    # once done pausing, restore running status
                    twoThirdsLoop.status = STARTED
                thisExp.nextEntry()
                
            # completed repTwoThirds repeats of 'twoThirdsLoop'
            twoThirdsLoop.status = FINISHED
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # mark thisTrialsLoop as finished
            if hasattr(thisTrialsLoop, 'status'):
                thisTrialsLoop.status = FINISHED
            # if awaiting a pause, pause now
            if trialsLoop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                trialsLoop.status = STARTED
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsLoop'
        trialsLoop.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # mark thisBlockLoop as finished
        if hasattr(thisBlockLoop, 'status'):
            thisBlockLoop.status = FINISHED
        # if awaiting a pause, pause now
        if blockLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            blockLoop.status = STARTED
    # completed 5.0 repeats of 'blockLoop'
    blockLoop.status = FINISHED
    
    
    # --- Prepare to start Routine "goodbyeScreen" ---
    # create an object to store info about Routine goodbyeScreen
    goodbyeScreen = data.Routine(
        name='goodbyeScreen',
        components=[textGoodbye],
    )
    goodbyeScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for goodbyeScreen
    goodbyeScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    goodbyeScreen.tStart = globalClock.getTime(format='float')
    goodbyeScreen.status = STARTED
    thisExp.addData('goodbyeScreen.started', goodbyeScreen.tStart)
    goodbyeScreen.maxDuration = None
    # keep track of which components have finished
    goodbyeScreenComponents = goodbyeScreen.components
    for thisComponent in goodbyeScreen.components:
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
    
    # --- Run Routine "goodbyeScreen" ---
    goodbyeScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textGoodbye* updates
        
        # if textGoodbye is starting this frame...
        if textGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textGoodbye.frameNStart = frameN  # exact frame index
            textGoodbye.tStart = t  # local t and not account for scr refresh
            textGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textGoodbye, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textGoodbye.started')
            # update status
            textGoodbye.status = STARTED
            textGoodbye.setAutoDraw(True)
        
        # if textGoodbye is active this frame...
        if textGoodbye.status == STARTED:
            # update params
            pass
        
        # if textGoodbye is stopping this frame...
        if textGoodbye.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textGoodbye.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                textGoodbye.tStop = t  # not accounting for scr refresh
                textGoodbye.tStopRefresh = tThisFlipGlobal  # on global time
                textGoodbye.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textGoodbye.stopped')
                # update status
                textGoodbye.status = FINISHED
                textGoodbye.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=goodbyeScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            goodbyeScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in goodbyeScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "goodbyeScreen" ---
    for thisComponent in goodbyeScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for goodbyeScreen
    goodbyeScreen.tStop = globalClock.getTime(format='float')
    goodbyeScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('goodbyeScreen.stopped', goodbyeScreen.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if goodbyeScreen.maxDurationReached:
        routineTimer.addTime(-goodbyeScreen.maxDuration)
    elif goodbyeScreen.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-20.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
