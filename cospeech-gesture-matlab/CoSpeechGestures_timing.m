% CoSpeechGestures_timing.m
% -----------------------------------------------------------------------
% MonkeyLogic timing script
%
%   0.0 - 2.0 s   ITI
%   2.0 - 3.0 s   trialStart window, "START" text cue shown (no TTL)
%   3.0 - 6.0 s   gesture video                (movieGesture)
%   3.5 - 5.5 s   spoken word audio            (soundStimulus, 2 s)
%   6.0 - 8.5 s   instruction symbol image     (instructionImage)
%   8.5 -11.0 s   action cue circle, green(go)/red(nogo)  (actionCue)
%   8.5 - 9.5 s   "go" beep audio              (audioGoCue, 1 s)
%
% Total trial length = 11 s, matching:
%   while continueRoutine and routineTimer.getTime() < 11.0
%
% TaskObjects expected (see in condition file produced by
% build_ML_conditions.m):
%   1 = mov(...)   gesture video
%   2 = snd(...)   spoken gesture audio
%   3 = pic(...)   instruction symbol image
%   4 = pic(...)   action cue circle image (green/red per condition)
%   5 = snd(...)   go-cue beep (same file every trial)
%   6 = pic(...)   "START" text cue (same file every trial)
%
% Per-trial metadata (instructionType, action, stimText, movement) is
% available as a struct via the condition file's Info column, e.g.:
%   info = TrialRecord.CurrentConditionInfo;
%   disp(info.stimText);   % e.g. 'cutting'
%   disp(info.action);     % 'go' or 'nogo'
%
% Event marker codes (also exported to the .bhv2 file for offline
% alignment):
%   1 = ITI start
%   2 = trialStart -> external trigger onset
%   3 = video onset      4 = video offset
%   5 = word audio onset 6 = word audio offset
%   7 = instruction image onset   8 = instruction image offset
%   9 = action cue onset          10 = action cue offset
%   11 = go-beep onset            12 = go-beep offset
%   99 = trial end
%
% -----------------------------------------------------------------------

% --- timeline constants (ms) ---
ITI_DUR        = 2000;
TRIALSTART_DUR = 1000;   % 2.0 - 3.0 s
VIDEO_DUR      = 3000;   % 3.0 - 6.0 s
AUDIO_DELAY    = 500;    % word audio starts 0.5 s after video onset (3.5 s)
AUDIO_DUR      = 2000;   % 3.5 - 5.5 s
IMG_DUR        = 2500;   % 6.0 - 8.5 s
CUE_DUR        = 2500;   % 8.5 - 11.0 s
BEEP_DUR       = 1000;   % 8.5 - 9.5 s

% TaskObject indices (must match the column order in the condition file)
OBJ_VIDEO = 1;
OBJ_AUDIO = 2;
OBJ_IMAGE = 3;
OBJ_CUE   = 4;
OBJ_BEEP  = 5;
OBJ_START = 6;   % new: "START" text cue, shown during the trial-start window

% --- ITI ---
eventmarker(1);
idle(ITI_DUR);

% --- trial start / external trigger ---
% timestap in .bhv2 file? 
eventmarker(2);
toggleobject(OBJ_START, 'eventmarker', 2, 'status', 'on');   % "START" cue onset
idle(TRIALSTART_DUR);
toggleobject(OBJ_START, 'status', 'off');                   % "START" cue offset

% --- gesture video starts; word audio starts 0.5 s later, nested inside it ---
toggleobject(OBJ_VIDEO, 'eventmarker', 3, 'status', 'on');   % video onset
idle(AUDIO_DELAY);

toggleobject(OBJ_AUDIO, 'eventmarker', 5, 'status', 'on');   % word audio onset
idle(AUDIO_DUR);
toggleobject(OBJ_AUDIO, 'eventmarker', 6, 'status', 'off');  % word audio offset

idle(VIDEO_DUR - AUDIO_DELAY - AUDIO_DUR);
toggleobject(OBJ_VIDEO, 'eventmarker', 4, 'status', 'off');  % video offset

% --- instruction symbol image ---
toggleobject(OBJ_IMAGE, 'eventmarker', 7, 'status', 'on');
idle(IMG_DUR);
toggleobject(OBJ_IMAGE, 'eventmarker', 8, 'status', 'off');

% --- action cue circle + go-cue beep, both start together ---
toggleobject(OBJ_CUE,  'eventmarker', 9,  'status', 'on');
toggleobject(OBJ_BEEP, 'eventmarker', 11, 'status', 'on');
idle(BEEP_DUR);
toggleobject(OBJ_BEEP, 'eventmarker', 12, 'status', 'off');

idle(CUE_DUR - BEEP_DUR);
toggleobject(OBJ_CUE, 'eventmarker', 10, 'status', 'off');

eventmarker(99); % trial end
