#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Mon Dec  8 19:34:48 2025
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
import serial
#import nidaqmx

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'CoSpeechGestures'  # from the Builder filename that created this script
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
#    trigger_task.write(True)
 #   core.wait(0.002)  # 2 milliseconds
#    trigger_task.write(False)
    
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
_winSize = [1800, 1169]
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
        originPath='/Users/sara-sofiagorriz/Library/CloudStorage/OneDrive-Chalmers/Experiments/CoSpeechGestures/CoSpeechGestures.py',
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
            winType='pyglet', allowGUI=False, allowStencil=False,
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
    if deviceManager.getDevice('keyWelcome') is None:
        # initialise keyWelcome
        keyWelcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyWelcome',
        )
    if deviceManager.getDevice('keyExplanationResponse') is None:
        # initialise keyExplanationResponse
        keyExplanationResponse = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyExplanationResponse',
        )
    if deviceManager.getDevice('keyInstructSpeak_continue') is None:
        # initialise keyInstructSpeak_continue
        keyInstructSpeak_continue = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyInstructSpeak_continue',
        )
    if deviceManager.getDevice('keyInstructHand_continue') is None:
        # initialise keyInstructHand_continue
        keyInstructHand_continue = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyInstructHand_continue',
        )
    if deviceManager.getDevice('keyresponseInstructBoth') is None:
        # initialise keyresponseInstructBoth
        keyresponseInstructBoth = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyresponseInstructBoth',
        )
    if deviceManager.getDevice('keyBlockResponseTraining') is None:
        # initialise keyBlockResponseTraining
        keyBlockResponseTraining = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyBlockResponseTraining',
        )
    # create speaker 'soundStimulus_Training'
    deviceManager.addDevice(
        deviceName='soundStimulus_Training',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index = '-1',
       # index=None,
       # name="SAMSUNG (NVIDIA High Definition Audio)",
        resample='True',
        latencyClass=1,
    )
    # create speaker 'soundGoCue_Training'
    deviceManager.addDevice(
        deviceName='soundGoCue_Training',
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
    # create speaker 'soundStimulus'
    deviceManager.addDevice(
        deviceName='soundStimulus',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index = '-1',
        #index=None,
        #name="SAMSUNG (NVIDIA High Definition Audio)",
        resample='True',
        latencyClass=1,
    )
    # create speaker 'audioGoCue'
    deviceManager.addDevice(
        deviceName='audioGoCue',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index = '-1',
        #index=None,
        #name="SAMSUNG (NVIDIA High Definition Audio)",
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
    # Run 'Begin Experiment' code from codeStart
    from psychopy import visual, core
    import pandas as pd 
    import numpy as np
    import random
    from PIL import Image  # Python Imaging Library (included with PsychoPy)
   
    ## specifiy current Block number
    nBlock = 0
    
    ## load stimuli
    # load go trials
    go_trials = pd.read_excel('stimuli_go.xlsx')
    
    # repeat go trials 3 times
    go_trials_rep = pd.concat([go_trials]*3, ignore_index = True)
    
    # load nogo trials
    nogo_trials = pd.read_excel('stimuli_no.xlsx')
    subset_nogo_trials = nogo_trials.sample(n=7).reset_index(drop=True)  # select 5 random rows
    
    # Combine Go and NoGo trials
    all_trials = pd.concat([go_trials_rep, subset_nogo_trials], ignore_index = True)
    
    # shuffle 
    all_trials = all_trials.sample(frac=1).reset_index(drop=True)
    
    # temporary csv
    all_trials.to_csv("current_block_trials.csv", index = False)
    
    # choose subset from go-trials for training block
    # we want to show each gesture once during training, choose instruciton type randomly 
    
    # choose subset in go_trials
    samples = []
    for i in range(0, len(go_trials), 3):
        block = go_trials.iloc[i:i+3]  # block of 3 rows of excel
        if len(block) > 0:
            chosen = block.sample(n=1)  # random instruction
            samples.append(chosen)
    
    # 12 Samples
    samples = pd.concat(samples).head(12)
    nogo_sample = nogo_trials.sample(n=1).reset_index(drop=True)
    trainingTrials = pd.concat([samples, nogo_sample], ignore_index = True)
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
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keyWelcome = keyboard.Keyboard(deviceName='keyWelcome')
    
    # --- Initialize components for Routine "explanationScreen" ---
    textExplanation = visual.TextStim(win=win, name='textExplanation',
        text='In the following task, each trial will begin with a word played over the speakers, accompanied by a video showing a gesture on the\nscreen in front of you. \n\nAfter this, you’ll be asked to do one of the following - repeat the word, perform the gesture, or do both at the same time — depending on the trial.\n\nYou’ll know when to respond by a GO cue, which will appear as a green circle. If instead a red circle appears, it’s a No-Go trial - in that case, simply relax and do nothing. \n\nPlease attempt to perform the gesture with only your right hand to the best of your abilities. Even if you cannot physically produce the gesture, please give it your best try.\n\nPress SPACEBAR to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyExplanationResponse = keyboard.Keyboard(deviceName='keyExplanationResponse')
    
    # --- Initialize components for Routine "expInstructSpeak" ---
    textInstructSpeak = visual.TextStim(win=win, name='textInstructSpeak',
        text='The shown symbol is the image you will see when you are asked to repeat the word.',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageSpeak = visual.ImageStim(
        win=win,
        name='imageSpeak', 
        image='images/speak.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    textInstructSpeak_continue = visual.TextStim(win=win, name='textInstructSpeak_continue',
        text='Press SPACEBAR to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    keyInstructSpeak_continue = keyboard.Keyboard(deviceName='keyInstructSpeak_continue')
    
    # --- Initialize components for Routine "expInstructHand" ---
    textInstructHand = visual.TextStim(win=win, name='textInstructHand',
        text='The shown symbol is the image you will see when you are asked to repeat the gesture.',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyInstructHand_continue = keyboard.Keyboard(deviceName='keyInstructHand_continue')
    textInstructHand_continue = visual.TextStim(win=win, name='textInstructHand_continue',
        text='Press SPACEBAR to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    imageInstructHand = visual.ImageStim(
        win=win,
        name='imageInstructHand', 
        image='images/hand.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "expInstructBoth" ---
    textInstructBoth = visual.TextStim(win=win, name='textInstructBoth',
        text='The shown symbol is the image you will see when you are asked to repeat the word and the gesture simultaneously. ',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    imageInstructBoth = visual.ImageStim(
        win=win,
        name='imageInstructBoth', 
        image='images/speak_gesture.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    keyresponseInstructBoth = keyboard.Keyboard(deviceName='keyresponseInstructBoth')
    textInstructBoth_continue = visual.TextStim(win=win, name='textInstructBoth_continue',
        text='Press SPACEBAR to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trainingBlock" ---
    textBlockTraining = visual.TextStim(win=win, name='textBlockTraining',
        text='This is the beginning of the training. If you want to start, please press SPACEBAR.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyBlockResponseTraining = keyboard.Keyboard(deviceName='keyBlockResponseTraining')
    
    # --- Initialize components for Routine "trainingTrials" ---
    itiTraining = visual.Rect(
        win=win, name='itiTraining',
        width=(2, 2)[0], height=(2, 2)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    trialStart_Training = visual.TextStim(win=win, name='trialStart_Training',
        text='START',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    movieGesture_Training = visual.MovieStim(
        win, name='movieGesture_Training',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=sizeVideo, units='pix',
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=-3
    )
    soundStimulus_Training = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='soundStimulus_Training',    name='soundStimulus_Training'
    )
    soundStimulus_Training.setVolume(1.0)
    instructionImageTraining = visual.ImageStim(
        win=win,
        name='instructionImageTraining', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    actionCueTraining = visual.ShapeStim(
        win=win, name='actionCueTraining',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    soundGoCue_Training = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='soundGoCue_Training',    name='soundGoCue_Training'
    )
    soundGoCue_Training.setVolume(0.8)
    
    # --- Initialize components for Routine "blockTrials" ---
    textBlockOne = visual.TextStim(win=win, name='textBlockOne',
        text='This is the beginning of a new block. If you want to start, please press SPACEBAR.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keyBlockResponse = keyboard.Keyboard(deviceName='keyBlockResponse')
    
    # --- Initialize components for Routine "trials" ---
    # Run 'Begin Experiment' code from code
    from psychopy import event
    
    
    iti = visual.Rect(
        win=win, name='iti',
        width=(2, 2)[0], height=(2, 2)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    trialStart = visual.TextStim(win=win, name='trialStart',
        text='START',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    movieGesture = visual.MovieStim(
        win, name='movieGesture',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=sizeVideo, units='pix',
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=-3
    )
    soundStimulus = sound.Sound(
        'A', 
        secs=2.0, 
        stereo=True, 
        hamming=True, 
        speaker='soundStimulus',    name='soundStimulus'
    )
    soundStimulus.setVolume(1.0)
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
        secs=-1, 
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
    
    # --- Initialize components for Routine "halfTime" ---
    textHalfTime = visual.TextStim(win=win, name='textHalfTime',
        text='You are halfway through this block!\n\nThe experiment continues in 30 seconds.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "goodbyeScreen" ---
    textGoodbye = visual.TextStim(win=win, name='textGoodbye',
        text='This is the end of the experiment. \n\nThank you for your time!',
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
        components=[textWelcome, keyWelcome],
    )
    welcomeScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyWelcome
    keyWelcome.keys = []
    keyWelcome.rt = []
    _keyWelcome_allKeys = []
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
        
        # *keyWelcome* updates
        waitOnFlip = False
        
        # if keyWelcome is starting this frame...
        if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWelcome.frameNStart = frameN  # exact frame index
            keyWelcome.tStart = t  # local t and not account for scr refresh
            keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyWelcome.started')
            # update status
            keyWelcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWelcome.status == STARTED and not waitOnFlip:
            theseKeys = keyWelcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyWelcome_allKeys.extend(theseKeys)
            if len(_keyWelcome_allKeys):
                keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
                keyWelcome.rt = _keyWelcome_allKeys[-1].rt
                keyWelcome.duration = _keyWelcome_allKeys[-1].duration
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
    if keyWelcome.keys in ['', [], None]:  # No response was made
        keyWelcome.keys = None
    thisExp.addData('keyWelcome.keys',keyWelcome.keys)
    if keyWelcome.keys != None:  # we had a response
        thisExp.addData('keyWelcome.rt', keyWelcome.rt)
        thisExp.addData('keyWelcome.duration', keyWelcome.duration)
    thisExp.nextEntry()
    # the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "explanationScreen" ---
    # create an object to store info about Routine explanationScreen
    explanationScreen = data.Routine(
        name='explanationScreen',
        components=[textExplanation, keyExplanationResponse],
    )
    explanationScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyExplanationResponse
    keyExplanationResponse.keys = []
    keyExplanationResponse.rt = []
    _keyExplanationResponse_allKeys = []
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
        
        # *keyExplanationResponse* updates
        waitOnFlip = False
        
        # if keyExplanationResponse is starting this frame...
        if keyExplanationResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyExplanationResponse.frameNStart = frameN  # exact frame index
            keyExplanationResponse.tStart = t  # local t and not account for scr refresh
            keyExplanationResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyExplanationResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyExplanationResponse.started')
            # update status
            keyExplanationResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyExplanationResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyExplanationResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyExplanationResponse.status == STARTED and not waitOnFlip:
            theseKeys = keyExplanationResponse.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyExplanationResponse_allKeys.extend(theseKeys)
            if len(_keyExplanationResponse_allKeys):
                keyExplanationResponse.keys = _keyExplanationResponse_allKeys[-1].name  # just the last key pressed
                keyExplanationResponse.rt = _keyExplanationResponse_allKeys[-1].rt
                keyExplanationResponse.duration = _keyExplanationResponse_allKeys[-1].duration
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
    if keyExplanationResponse.keys in ['', [], None]:  # No response was made
        keyExplanationResponse.keys = None
    thisExp.addData('keyExplanationResponse.keys',keyExplanationResponse.keys)
    if keyExplanationResponse.keys != None:  # we had a response
        thisExp.addData('keyExplanationResponse.rt', keyExplanationResponse.rt)
        thisExp.addData('keyExplanationResponse.duration', keyExplanationResponse.duration)
    thisExp.nextEntry()
    # the Routine "explanationScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "expInstructSpeak" ---
    # create an object to store info about Routine expInstructSpeak
    expInstructSpeak = data.Routine(
        name='expInstructSpeak',
        components=[textInstructSpeak, imageSpeak, textInstructSpeak_continue, keyInstructSpeak_continue],
    )
    expInstructSpeak.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyInstructSpeak_continue
    keyInstructSpeak_continue.keys = []
    keyInstructSpeak_continue.rt = []
    _keyInstructSpeak_continue_allKeys = []
    # store start times for expInstructSpeak
    expInstructSpeak.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    expInstructSpeak.tStart = globalClock.getTime(format='float')
    expInstructSpeak.status = STARTED
    thisExp.addData('expInstructSpeak.started', expInstructSpeak.tStart)
    expInstructSpeak.maxDuration = None
    # keep track of which components have finished
    expInstructSpeakComponents = expInstructSpeak.components
    for thisComponent in expInstructSpeak.components:
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
    
    # --- Run Routine "expInstructSpeak" ---
    expInstructSpeak.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        
        # *imageSpeak* updates
        
        # if imageSpeak is starting this frame...
        if imageSpeak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageSpeak.frameNStart = frameN  # exact frame index
            imageSpeak.tStart = t  # local t and not account for scr refresh
            imageSpeak.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageSpeak, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageSpeak.started')
            # update status
            imageSpeak.status = STARTED
            imageSpeak.setAutoDraw(True)
        
        # if imageSpeak is active this frame...
        if imageSpeak.status == STARTED:
            # update params
            pass
        
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
                currentRoutine=expInstructSpeak,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            expInstructSpeak.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expInstructSpeak.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "expInstructSpeak" ---
    for thisComponent in expInstructSpeak.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for expInstructSpeak
    expInstructSpeak.tStop = globalClock.getTime(format='float')
    expInstructSpeak.tStopRefresh = tThisFlipGlobal
    thisExp.addData('expInstructSpeak.stopped', expInstructSpeak.tStop)
    # check responses
    if keyInstructSpeak_continue.keys in ['', [], None]:  # No response was made
        keyInstructSpeak_continue.keys = None
    thisExp.addData('keyInstructSpeak_continue.keys',keyInstructSpeak_continue.keys)
    if keyInstructSpeak_continue.keys != None:  # we had a response
        thisExp.addData('keyInstructSpeak_continue.rt', keyInstructSpeak_continue.rt)
        thisExp.addData('keyInstructSpeak_continue.duration', keyInstructSpeak_continue.duration)
    thisExp.nextEntry()
    # the Routine "expInstructSpeak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "expInstructHand" ---
    # create an object to store info about Routine expInstructHand
    expInstructHand = data.Routine(
        name='expInstructHand',
        components=[textInstructHand, keyInstructHand_continue, textInstructHand_continue, imageInstructHand],
    )
    expInstructHand.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyInstructHand_continue
    keyInstructHand_continue.keys = []
    keyInstructHand_continue.rt = []
    _keyInstructHand_continue_allKeys = []
    # store start times for expInstructHand
    expInstructHand.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    expInstructHand.tStart = globalClock.getTime(format='float')
    expInstructHand.status = STARTED
    thisExp.addData('expInstructHand.started', expInstructHand.tStart)
    expInstructHand.maxDuration = None
    # keep track of which components have finished
    expInstructHandComponents = expInstructHand.components
    for thisComponent in expInstructHand.components:
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
    
    # --- Run Routine "expInstructHand" ---
    expInstructHand.forceEnded = routineForceEnded = not continueRoutine
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
        
        # *keyInstructHand_continue* updates
        waitOnFlip = False
        
        # if keyInstructHand_continue is starting this frame...
        if keyInstructHand_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyInstructHand_continue.frameNStart = frameN  # exact frame index
            keyInstructHand_continue.tStart = t  # local t and not account for scr refresh
            keyInstructHand_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyInstructHand_continue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyInstructHand_continue.started')
            # update status
            keyInstructHand_continue.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyInstructHand_continue.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyInstructHand_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyInstructHand_continue.status == STARTED and not waitOnFlip:
            theseKeys = keyInstructHand_continue.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyInstructHand_continue_allKeys.extend(theseKeys)
            if len(_keyInstructHand_continue_allKeys):
                keyInstructHand_continue.keys = _keyInstructHand_continue_allKeys[-1].name  # just the last key pressed
                keyInstructHand_continue.rt = _keyInstructHand_continue_allKeys[-1].rt
                keyInstructHand_continue.duration = _keyInstructHand_continue_allKeys[-1].duration
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
                currentRoutine=expInstructHand,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            expInstructHand.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expInstructHand.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "expInstructHand" ---
    for thisComponent in expInstructHand.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for expInstructHand
    expInstructHand.tStop = globalClock.getTime(format='float')
    expInstructHand.tStopRefresh = tThisFlipGlobal
    thisExp.addData('expInstructHand.stopped', expInstructHand.tStop)
    # check responses
    if keyInstructHand_continue.keys in ['', [], None]:  # No response was made
        keyInstructHand_continue.keys = None
    thisExp.addData('keyInstructHand_continue.keys',keyInstructHand_continue.keys)
    if keyInstructHand_continue.keys != None:  # we had a response
        thisExp.addData('keyInstructHand_continue.rt', keyInstructHand_continue.rt)
        thisExp.addData('keyInstructHand_continue.duration', keyInstructHand_continue.duration)
    thisExp.nextEntry()
    # the Routine "expInstructHand" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "expInstructBoth" ---
    # create an object to store info about Routine expInstructBoth
    expInstructBoth = data.Routine(
        name='expInstructBoth',
        components=[textInstructBoth, imageInstructBoth, keyresponseInstructBoth, textInstructBoth_continue],
    )
    expInstructBoth.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeImageBoth
    # Load the image to get its size
    img = Image.open('images/speak_gesture.png')
    width, height = img.size
    
    # Convert pixel dimensions to PsychoPy units (assuming your window uses 'pix')
    aspect = width / height
    
    # Set the image size dynamically
    # E.g., fix the height and adjust width to preserve aspect ratio:
    fixed_height = 0.4
    sizeImageDemo = [fixed_height * aspect, fixed_height]
    
    imageInstructBoth.setSize(sizeImageDemo)
    # create starting attributes for keyresponseInstructBoth
    keyresponseInstructBoth.keys = []
    keyresponseInstructBoth.rt = []
    _keyresponseInstructBoth_allKeys = []
    # store start times for expInstructBoth
    expInstructBoth.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    expInstructBoth.tStart = globalClock.getTime(format='float')
    expInstructBoth.status = STARTED
    thisExp.addData('expInstructBoth.started', expInstructBoth.tStart)
    expInstructBoth.maxDuration = None
    # keep track of which components have finished
    expInstructBothComponents = expInstructBoth.components
    for thisComponent in expInstructBoth.components:
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
    
    # --- Run Routine "expInstructBoth" ---
    expInstructBoth.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        
        # *keyresponseInstructBoth* updates
        waitOnFlip = False
        
        # if keyresponseInstructBoth is starting this frame...
        if keyresponseInstructBoth.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyresponseInstructBoth.frameNStart = frameN  # exact frame index
            keyresponseInstructBoth.tStart = t  # local t and not account for scr refresh
            keyresponseInstructBoth.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyresponseInstructBoth, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyresponseInstructBoth.started')
            # update status
            keyresponseInstructBoth.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyresponseInstructBoth.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyresponseInstructBoth.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyresponseInstructBoth.status == STARTED and not waitOnFlip:
            theseKeys = keyresponseInstructBoth.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyresponseInstructBoth_allKeys.extend(theseKeys)
            if len(_keyresponseInstructBoth_allKeys):
                keyresponseInstructBoth.keys = _keyresponseInstructBoth_allKeys[-1].name  # just the last key pressed
                keyresponseInstructBoth.rt = _keyresponseInstructBoth_allKeys[-1].rt
                keyresponseInstructBoth.duration = _keyresponseInstructBoth_allKeys[-1].duration
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
                currentRoutine=expInstructBoth,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            expInstructBoth.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expInstructBoth.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "expInstructBoth" ---
    for thisComponent in expInstructBoth.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for expInstructBoth
    expInstructBoth.tStop = globalClock.getTime(format='float')
    expInstructBoth.tStopRefresh = tThisFlipGlobal
    thisExp.addData('expInstructBoth.stopped', expInstructBoth.tStop)
    # check responses
    if keyresponseInstructBoth.keys in ['', [], None]:  # No response was made
        keyresponseInstructBoth.keys = None
    thisExp.addData('keyresponseInstructBoth.keys',keyresponseInstructBoth.keys)
    if keyresponseInstructBoth.keys != None:  # we had a response
        thisExp.addData('keyresponseInstructBoth.rt', keyresponseInstructBoth.rt)
        thisExp.addData('keyresponseInstructBoth.duration', keyresponseInstructBoth.duration)
    thisExp.nextEntry()
    # the Routine "expInstructBoth" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trainingTrials_block = data.TrialHandler2(
        name='trainingTrials_block',
        nReps=0.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('trainingTrials.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trainingTrials_block)  # add the loop to the experiment
    thisTrainingTrials_block = trainingTrials_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrainingTrials_block.rgb)
    if thisTrainingTrials_block != None:
        for paramName in thisTrainingTrials_block:
            globals()[paramName] = thisTrainingTrials_block[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrainingTrials_block in trainingTrials_block:
        trainingTrials_block.status = STARTED
        if hasattr(thisTrainingTrials_block, 'status'):
            thisTrainingTrials_block.status = STARTED
        currentLoop = trainingTrials_block
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrainingTrials_block.rgb)
        if thisTrainingTrials_block != None:
            for paramName in thisTrainingTrials_block:
                globals()[paramName] = thisTrainingTrials_block[paramName]
        
        # --- Prepare to start Routine "trainingBlock" ---
        # create an object to store info about Routine trainingBlock
        trainingBlock = data.Routine(
            name='trainingBlock',
            components=[textBlockTraining, keyBlockResponseTraining],
        )
        trainingBlock.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for keyBlockResponseTraining
        keyBlockResponseTraining.keys = []
        keyBlockResponseTraining.rt = []
        _keyBlockResponseTraining_allKeys = []
        # store start times for trainingBlock
        trainingBlock.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trainingBlock.tStart = globalClock.getTime(format='float')
        trainingBlock.status = STARTED
        thisExp.addData('trainingBlock.started', trainingBlock.tStart)
        trainingBlock.maxDuration = None
        # keep track of which components have finished
        trainingBlockComponents = trainingBlock.components
        for thisComponent in trainingBlock.components:
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
        
        # --- Run Routine "trainingBlock" ---
        trainingBlock.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrainingTrials_block, 'status') and thisTrainingTrials_block.status == STOPPING:
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
                    currentRoutine=trainingBlock,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trainingBlock.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trainingBlock.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trainingBlock" ---
        for thisComponent in trainingBlock.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trainingBlock
        trainingBlock.tStop = globalClock.getTime(format='float')
        trainingBlock.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trainingBlock.stopped', trainingBlock.tStop)
        # check responses
        if keyBlockResponseTraining.keys in ['', [], None]:  # No response was made
            keyBlockResponseTraining.keys = None
        trainingTrials_block.addData('keyBlockResponseTraining.keys',keyBlockResponseTraining.keys)
        if keyBlockResponseTraining.keys != None:  # we had a response
            trainingTrials_block.addData('keyBlockResponseTraining.rt', keyBlockResponseTraining.rt)
            trainingTrials_block.addData('keyBlockResponseTraining.duration', keyBlockResponseTraining.duration)
        # the Routine "trainingBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trainingTrials" ---
        # create an object to store info about Routine trainingTrials
        trainingTrials = data.Routine(
            name='trainingTrials',
            components=[itiTraining, trialStart_Training, movieGesture_Training, soundStimulus_Training, instructionImageTraining, actionCueTraining, soundGoCue_Training],
        )
        trainingTrials.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeTraining
        # different action display for GO/No-GO conditions
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
        
        # DO the same with the 
        movieGesture_Training.setMovie(stimVideo)
        soundStimulus_Training.setSound(stimAudio, secs=6, hamming=True)
        soundStimulus_Training.setVolume(1.0, log=False)
        soundStimulus_Training.seek(0)
        instructionImageTraining.setSize(sizeImage)
        instructionImageTraining.setImage(instructionSymbol)
        actionCueTraining.setFillColor(circle_color)
        actionCueTraining.setLineColor(circle_color)
        soundGoCue_Training.setSound('audios/race-start-beeps-125125.wav', secs=1.0, hamming=True)
        soundGoCue_Training.setVolume(0.8, log=False)
        soundGoCue_Training.seek(0)
        # store start times for trainingTrials
        trainingTrials.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trainingTrials.tStart = globalClock.getTime(format='float')
        trainingTrials.status = STARTED
        thisExp.addData('trainingTrials.started', trainingTrials.tStart)
        trainingTrials.maxDuration = None
        # keep track of which components have finished
        trainingTrialsComponents = trainingTrials.components
        for thisComponent in trainingTrials.components:
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
        
        # --- Run Routine "trainingTrials" ---
        trainingTrials.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 11.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrainingTrials_block, 'status') and thisTrainingTrials_block.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *itiTraining* updates
            
            # if itiTraining is starting this frame...
            if itiTraining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                itiTraining.frameNStart = frameN  # exact frame index
                itiTraining.tStart = t  # local t and not account for scr refresh
                itiTraining.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(itiTraining, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiTraining.started')
                # update status
                itiTraining.status = STARTED
                itiTraining.setAutoDraw(True)
            
            # if itiTraining is active this frame...
            if itiTraining.status == STARTED:
                # update params
                pass
            
            # if itiTraining is stopping this frame...
            if itiTraining.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2-frameTolerance:
                    # keep track of stop time/frame for later
                    itiTraining.tStop = t  # not accounting for scr refresh
                    itiTraining.tStopRefresh = tThisFlipGlobal  # on global time
                    itiTraining.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'itiTraining.stopped')
                    # update status
                    itiTraining.status = FINISHED
                    itiTraining.setAutoDraw(False)
                    
            
            # *trialStart_Training* updates
            
            # if trialStart_Training is starting this frame...
            if trialStart_Training.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                trialStart_Training.frameNStart = frameN  # exact frame index
                trialStart_Training.tStart = t  # local t and not account for scr refresh
                trialStart_Training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialStart_Training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialStart_Training.started')
                # update status
                trialStart_Training.status = STARTED
                trialStart_Training.setAutoDraw(True)
               # send_trigger()
            
            # if trialStart_Training is active this frame...
            if trialStart_Training.status == STARTED:
                # update params
                pass
            
            # if trialStart_Training is stopping this frame...
            if trialStart_Training.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 3-frameTolerance:
                    # keep track of stop time/frame for later
                    trialStart_Training.tStop = t  # not accounting for scr refresh
                    trialStart_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    trialStart_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trialStart_Training.stopped')
                    # update status
                    trialStart_Training.status = FINISHED
                    trialStart_Training.setAutoDraw(False)
            
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
                if tThisFlip > 6.0-frameTolerance or movieGesture_Training.isFinished:
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
            
            # *soundStimulus_Training* updates
            
            # if soundStimulus_Training is starting this frame...
            if soundStimulus_Training.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                soundStimulus_Training.frameNStart = frameN  # exact frame index
                soundStimulus_Training.tStart = t  # local t and not account for scr refresh
                soundStimulus_Training.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('soundStimulus_Training.started', tThisFlipGlobal)
                # update status
                soundStimulus_Training.status = STARTED
                soundStimulus_Training.play(when=win)  # sync with win flip
            
            # if soundStimulus_Training is stopping this frame...
            if soundStimulus_Training.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 6-frameTolerance or soundStimulus_Training.isFinished:
                    # keep track of stop time/frame for later
                    soundStimulus_Training.tStop = t  # not accounting for scr refresh
                    soundStimulus_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    soundStimulus_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'soundStimulus_Training.stopped')
                    # update status
                    soundStimulus_Training.status = FINISHED
                    soundStimulus_Training.stop()
            
            # *instructionImageTraining* updates
            
            # if instructionImageTraining is starting this frame...
            if instructionImageTraining.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                instructionImageTraining.frameNStart = frameN  # exact frame index
                instructionImageTraining.tStart = t  # local t and not account for scr refresh
                instructionImageTraining.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructionImageTraining, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructionImageTraining.started')
                # update status
                instructionImageTraining.status = STARTED
                instructionImageTraining.setAutoDraw(True)
            
            # if instructionImageTraining is active this frame...
            if instructionImageTraining.status == STARTED:
                # update params
                pass
            
            # if instructionImageTraining is stopping this frame...
            if instructionImageTraining.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 8.5-frameTolerance:
                    # keep track of stop time/frame for later
                    instructionImageTraining.tStop = t  # not accounting for scr refresh
                    instructionImageTraining.tStopRefresh = tThisFlipGlobal  # on global time
                    instructionImageTraining.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instructionImageTraining.stopped')
                    # update status
                    instructionImageTraining.status = FINISHED
                    instructionImageTraining.setAutoDraw(False)
            
            # *actionCueTraining* updates
            
            # if actionCueTraining is starting this frame...
            if actionCueTraining.status == NOT_STARTED and tThisFlip >= 8.5-frameTolerance:
                # keep track of start time/frame for later
                actionCueTraining.frameNStart = frameN  # exact frame index
                actionCueTraining.tStart = t  # local t and not account for scr refresh
                actionCueTraining.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(actionCueTraining, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'actionCueTraining.started')
                # update status
                actionCueTraining.status = STARTED
                actionCueTraining.setAutoDraw(True)
            
            # if actionCueTraining is active this frame...
            if actionCueTraining.status == STARTED:
                # update params
                pass
            
            # if actionCueTraining is stopping this frame...
            if actionCueTraining.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 11-frameTolerance:
                    # keep track of stop time/frame for later
                    actionCueTraining.tStop = t  # not accounting for scr refresh
                    actionCueTraining.tStopRefresh = tThisFlipGlobal  # on global time
                    actionCueTraining.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'actionCueTraining.stopped')
                    # update status
                    actionCueTraining.status = FINISHED
                    actionCueTraining.setAutoDraw(False)
            
            # *soundGoCue_Training* updates
            
            # if soundGoCue_Training is starting this frame...
            if soundGoCue_Training.status == NOT_STARTED and tThisFlip >= 8.5-frameTolerance:
                # keep track of start time/frame for later
                soundGoCue_Training.frameNStart = frameN  # exact frame index
                soundGoCue_Training.tStart = t  # local t and not account for scr refresh
                soundGoCue_Training.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('soundGoCue_Training.started', tThisFlipGlobal)
                # update status
                soundGoCue_Training.status = STARTED
                soundGoCue_Training.play(when=win)  # sync with win flip
            
            # if soundGoCue_Training is stopping this frame...
            if soundGoCue_Training.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > soundGoCue_Training.tStartRefresh + 1.0-frameTolerance or soundGoCue_Training.isFinished:
                    # keep track of stop time/frame for later
                    soundGoCue_Training.tStop = t  # not accounting for scr refresh
                    soundGoCue_Training.tStopRefresh = tThisFlipGlobal  # on global time
                    soundGoCue_Training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'soundGoCue_Training.stopped')
                    # update status
                    soundGoCue_Training.status = FINISHED
                    soundGoCue_Training.stop()
            
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
                    currentRoutine=trainingTrials,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trainingTrials.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trainingTrials.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trainingTrials" ---
        for thisComponent in trainingTrials.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trainingTrials
        trainingTrials.tStop = globalClock.getTime(format='float')
        trainingTrials.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trainingTrials.stopped', trainingTrials.tStop)
        movieGesture_Training.stop()  # ensure movie has stopped at end of Routine
        soundStimulus_Training.pause()  # ensure sound has stopped at end of Routine
        soundGoCue_Training.pause()  # ensure sound has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if trainingTrials.maxDurationReached:
            routineTimer.addTime(-trainingTrials.maxDuration)
        elif trainingTrials.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-11.000000)
        # mark thisTrainingTrials_block as finished
        if hasattr(thisTrainingTrials_block, 'status'):
            thisTrainingTrials_block.status = FINISHED
        # if awaiting a pause, pause now
        if trainingTrials_block.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trainingTrials_block.status = STARTED
        thisExp.nextEntry()
        
    # completed 0.0 repeats of 'trainingTrials_block'
    trainingTrials_block.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    blockLoop = data.TrialHandler2(
        name='blockLoop',
        nReps=5.0, 
        method='random', 
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
        
        # --- Prepare to start Routine "blockTrials" ---
        # create an object to store info about Routine blockTrials
        blockTrials = data.Routine(
            name='blockTrials',
            components=[textBlockOne, keyBlockResponse],
        )
        blockTrials.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeBlockPartOne
        #choose new,random subset of nogo trials
        subset_nogo_trials = nogo_trials.sample(n=7).reset_index(drop=True)  # select 7 random rows
        
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
        nHalfTime = 59
        repHalftime = 0
        
        # create starting attributes for keyBlockResponse
        keyBlockResponse.keys = []
        keyBlockResponse.rt = []
        _keyBlockResponse_allKeys = []
        # store start times for blockTrials
        blockTrials.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blockTrials.tStart = globalClock.getTime(format='float')
        blockTrials.status = STARTED
        thisExp.addData('blockTrials.started', blockTrials.tStart)
        blockTrials.maxDuration = None
        # keep track of which components have finished
        blockTrialsComponents = blockTrials.components
        for thisComponent in blockTrials.components:
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
        
        # --- Run Routine "blockTrials" ---
        blockTrials.forceEnded = routineForceEnded = not continueRoutine
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
            
            # *textBlockOne* updates
            
            # if textBlockOne is starting this frame...
            if textBlockOne.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlockOne.frameNStart = frameN  # exact frame index
                textBlockOne.tStart = t  # local t and not account for scr refresh
                textBlockOne.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlockOne, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlockOne.started')
                # update status
                textBlockOne.status = STARTED
                textBlockOne.setAutoDraw(True)
            
            # if textBlockOne is active this frame...
            if textBlockOne.status == STARTED:
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
                    currentRoutine=blockTrials,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blockTrials.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockTrials.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blockTrials" ---
        for thisComponent in blockTrials.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blockTrials
        blockTrials.tStop = globalClock.getTime(format='float')
        blockTrials.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blockTrials.stopped', blockTrials.tStop)
        # check responses
        if keyBlockResponse.keys in ['', [], None]:  # No response was made
            keyBlockResponse.keys = None
        blockLoop.addData('keyBlockResponse.keys',keyBlockResponse.keys)
        if keyBlockResponse.keys != None:  # we had a response
            blockLoop.addData('keyBlockResponse.rt', keyBlockResponse.rt)
            blockLoop.addData('keyBlockResponse.duration', keyBlockResponse.duration)
        # the Routine "blockTrials" was not non-slip safe, so reset the non-slip timer
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
            
            # --- Prepare to start Routine "trials" ---
            # create an object to store info about Routine trials
            trials = data.Routine(
                name='trials',
                components=[iti, trialStart, movieGesture, soundStimulus, instructionImage, actionCue, audioGoCue],
            )
            trials.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            # different action display for GO/No-GO conditions
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
            print("Pausing in next trial: ", run_routine)
            
            if run_routine:
                nPause = 1
            else:
                nPause = 0
            
            # increase trialNumber
            trialN += 1
            print(trialN)
            
            if trialN == nHalfTime:
                repHalftime = 1
            
            
            movieGesture.setMovie(stimVideo)
            soundStimulus.setSound(stimAudio, secs=2.0, hamming=True)
            soundStimulus.setVolume(1.0, log=False)
            soundStimulus.seek(0)
            instructionImage.setSize(sizeImage)
            instructionImage.setImage(instructionSymbol)
            actionCue.setFillColor(circle_color)
            actionCue.setLineColor(circle_color)
            audioGoCue.setSound('audios/race-start-beeps-125125.mp3', secs=9.5, hamming=True)
            audioGoCue.setVolume(0.8, log=False)
            audioGoCue.seek(0)
            # store start times for trials
            trials.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trials.tStart = globalClock.getTime(format='float')
            trials.status = STARTED
            thisExp.addData('trials.started', trials.tStart)
            trials.maxDuration = None
            # keep track of which components have finished
            trialsComponents = trials.components
            for thisComponent in trials.components:
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
            
            # --- Run Routine "trials" ---
            trials.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 11.0:
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
                    if tThisFlip > 2-frameTolerance:
                        # keep track of stop time/frame for later
                        iti.tStop = t  # not accounting for scr refresh
                        iti.tStopRefresh = tThisFlipGlobal  # on global time
                        iti.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'iti.stopped')
                        # update status
                        iti.status = FINISHED
                        iti.setAutoDraw(False)
                
                # *trialStart* updates
                
                # if trialStart is starting this frame...
                if trialStart.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    trialStart.frameNStart = frameN  # exact frame index
                    trialStart.tStart = t  # local t and not account for scr refresh
                    trialStart.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(trialStart, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trialStart.started')
                    # update status
                    trialStart.status = STARTED
                    trialStart.setAutoDraw(True)
                    #send_trigger()
                
                # if trialStart is active this frame...
                if trialStart.status == STARTED:
                    # update params
                    pass
                
                # if trialStart is stopping this frame...
                if trialStart.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 3-frameTolerance:
                        # keep track of stop time/frame for later
                        trialStart.tStop = t  # not accounting for scr refresh
                        trialStart.tStopRefresh = tThisFlipGlobal  # on global time
                        trialStart.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trialStart.stopped')
                        # update status
                        trialStart.status = FINISHED
                        trialStart.setAutoDraw(False)
                
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
                    if tThisFlip > 6.0-frameTolerance or movieGesture.isFinished:
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
                
                # *soundStimulus* updates
                
                # if soundStimulus is starting this frame...
                if soundStimulus.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                    # keep track of start time/frame for later
                    soundStimulus.frameNStart = frameN  # exact frame index
                    soundStimulus.tStart = t  # local t and not account for scr refresh
                    soundStimulus.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('soundStimulus.started', tThisFlipGlobal)
                    # update status
                    soundStimulus.status = STARTED
                    soundStimulus.play(when=win)  # sync with win flip
                
                # if soundStimulus is stopping this frame...
                if soundStimulus.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > soundStimulus.tStartRefresh + 2.0-frameTolerance or soundStimulus.isFinished:
                        # keep track of stop time/frame for later
                        soundStimulus.tStop = t  # not accounting for scr refresh
                        soundStimulus.tStopRefresh = tThisFlipGlobal  # on global time
                        soundStimulus.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'soundStimulus.stopped')
                        # update status
                        soundStimulus.status = FINISHED
                        soundStimulus.stop()
                
                # *instructionImage* updates
                
                # if instructionImage is starting this frame...
                if instructionImage.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
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
                    if tThisFlip > 11-frameTolerance:
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
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 9.5-frameTolerance or audioGoCue.isFinished:
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
                        currentRoutine=trials,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trials.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trials.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trials" ---
            for thisComponent in trials.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trials
            trials.tStop = globalClock.getTime(format='float')
            trials.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trials.stopped', trials.tStop)
            movieGesture.stop()  # ensure movie has stopped at end of Routine
            soundStimulus.pause()  # ensure sound has stopped at end of Routine
            audioGoCue.pause()  # ensure sound has stopped at end of Routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trials.maxDurationReached:
                routineTimer.addTime(-trials.maxDuration)
            elif trials.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-11.000000)
            
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
            
            for thisPause in pause:
                pause.status = STARTED
                if hasattr(thisPause, 'status'):
                    thisPause.status = STARTED
                currentLoop = pause
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
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
                    event.clearEvents()
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
            # completed nPause repeats of 'pause'
            pause.status = FINISHED
            
            
            # set up handler to look after randomisation of conditions etc
            halfTimeLoop = data.TrialHandler2(
                name='halfTimeLoop',
                nReps=repHalftime, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(halfTimeLoop)  # add the loop to the experiment
            thisHalfTimeLoop = halfTimeLoop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisHalfTimeLoop.rgb)
            if thisHalfTimeLoop != None:
                for paramName in thisHalfTimeLoop:
                    globals()[paramName] = thisHalfTimeLoop[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisHalfTimeLoop in halfTimeLoop:
                halfTimeLoop.status = STARTED
                if hasattr(thisHalfTimeLoop, 'status'):
                    thisHalfTimeLoop.status = STARTED
                currentLoop = halfTimeLoop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisHalfTimeLoop.rgb)
                if thisHalfTimeLoop != None:
                    for paramName in thisHalfTimeLoop:
                        globals()[paramName] = thisHalfTimeLoop[paramName]
                
                # --- Prepare to start Routine "halfTime" ---
                # create an object to store info about Routine halfTime
                halfTime = data.Routine(
                    name='halfTime',
                    components=[textHalfTime],
                )
                halfTime.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from codeHalftime
                # reset to default
                repHalftime = 0
                # store start times for halfTime
                halfTime.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                halfTime.tStart = globalClock.getTime(format='float')
                halfTime.status = STARTED
                thisExp.addData('halfTime.started', halfTime.tStart)
                halfTime.maxDuration = None
                # keep track of which components have finished
                halfTimeComponents = halfTime.components
                for thisComponent in halfTime.components:
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
                
                # --- Run Routine "halfTime" ---
                halfTime.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 30.0:
                    # if trial has changed, end Routine now
                    if hasattr(thisHalfTimeLoop, 'status') and thisHalfTimeLoop.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *textHalfTime* updates
                    
                    # if textHalfTime is starting this frame...
                    if textHalfTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textHalfTime.frameNStart = frameN  # exact frame index
                        textHalfTime.tStart = t  # local t and not account for scr refresh
                        textHalfTime.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textHalfTime, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textHalfTime.started')
                        # update status
                        textHalfTime.status = STARTED
                        textHalfTime.setAutoDraw(True)
                    
                    # if textHalfTime is active this frame...
                    if textHalfTime.status == STARTED:
                        # update params
                        pass
                    
                    # if textHalfTime is stopping this frame...
                    if textHalfTime.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > textHalfTime.tStartRefresh + 30-frameTolerance:
                            # keep track of stop time/frame for later
                            textHalfTime.tStop = t  # not accounting for scr refresh
                            textHalfTime.tStopRefresh = tThisFlipGlobal  # on global time
                            textHalfTime.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'textHalfTime.stopped')
                            # update status
                            textHalfTime.status = FINISHED
                            textHalfTime.setAutoDraw(False)
                    
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
                            currentRoutine=halfTime,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        halfTime.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in halfTime.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "halfTime" ---
                for thisComponent in halfTime.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for halfTime
                halfTime.tStop = globalClock.getTime(format='float')
                halfTime.tStopRefresh = tThisFlipGlobal
                thisExp.addData('halfTime.stopped', halfTime.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if halfTime.maxDurationReached:
                    routineTimer.addTime(-halfTime.maxDuration)
                elif halfTime.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-30.000000)
                # mark thisHalfTimeLoop as finished
                if hasattr(thisHalfTimeLoop, 'status'):
                    thisHalfTimeLoop.status = FINISHED
                # if awaiting a pause, pause now
                if halfTimeLoop.status == PAUSED:
                    thisExp.status = PAUSED
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[globalClock], 
                    )
                    # once done pausing, restore running status
                    halfTimeLoop.status = STARTED
                thisExp.nextEntry()
                
            # completed repHalftime repeats of 'halfTimeLoop'
            halfTimeLoop.status = FINISHED
            
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
    while continueRoutine and routineTimer.getTime() < 5.0:
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
            if tThisFlipGlobal > textGoodbye.tStartRefresh + 5-frameTolerance:
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
        routineTimer.addTime(-5.000000)
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
