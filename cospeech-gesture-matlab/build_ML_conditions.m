function condFile = build_ML_conditions(goFile, noFile, outFile, nGoReps, nNoGoSample, blockNumber)
% BUILD_ML_CONDITIONS  Convert PsychoPy go/nogo stimulus tables into a
% MonkeyLogic condition (.txt) file for a single block.
%
% This mirrors the block-construction logic from the original
% CoSpeechGestures.py:
%   go_trials_rep   = go trials repeated nGoReps times      (py: pd.concat([go_trials]*3))
%   subset_nogo     = nNoGoSample random rows from noFile   (py: nogo_trials.sample(n=7))
%   all_trials      = concat + full shuffle                 (py: .sample(frac=1))
%
% Because this per-block sampling/shuffling is bespoke (not a simple
% "N repeats of each condition" design), it's easiest to pre-build the
% exact trial order in MATLAB and hand ML an already-shuffled,
% one-row-per-trial condition file, run with Sequential control (no
% further randomization needed on ML's side). Re-run this function
% before each block to get a fresh random order (like the Python script
% does at the start of every block).
%
% USAGE:
%   build_ML_conditions('stimuli_go.xlsx', 'stimuli_no.xlsx', 'block01_conditions.txt')
%   build_ML_conditions('stimuli_go.xlsx', 'stimuli_no.xlsx', 'block01_conditions.txt', 3, 7)
%   build_ML_conditions('stimuli_go.xlsx', 'stimuli_no.xlsx', 'block02_conditions.txt', 3, 7, 2)  % block number 2
%
% REQUIRED COLUMNS in both xlsx files (same as your PsychoPy conditions file):
%   instructionType, instructionSymbol, action, stimText, stimAudio, stimVideo, movement
%
% OUTPUT
%   A tab-delimited .txt file with the standard MonkeyLogic condition-file
%   header (Condition / Frequency / Block / Timing File / Info /
%   TaskObject#1 ... TaskObject#6), ready to be loaded from the
%   MonkeyLogic main menu.
%     - "Frequency" (relative sampling frequency, only matters if you use
%       ML's own randomizer) is set to 1 for every row here, since we
%       already control the exact trial order ourselves.
%     - "Block" (which block number(s) a condition may appear in) must be
%       an actual number, e.g. 1 - NOT the word 'all'. This loader does
%       eval() on the Block column too (after turning spaces into commas),
%       so the literal text 'all' gets mistaken for a call to MATLAB's
%       built-in all() function and errors ("Not enough input arguments").
%       Since this script already generates one condition file per block,
%       every row here is simply given Block = blockNumber (default 1).
%     - "Info" is NOT a free-text label on this ML version - the loader
%       runs eval(['struct(' Info ');']) on it (mlconditions/load_file.m),
%       so it must be a valid comma-separated 'fieldname',value list, e.g.
%       'instructionType','speech','action','go','stimText','OK','movement','digits'
%       This script builds it that way, so in the timing script you can
%       read TrialRecord.CurrentConditionInfo.stimText, .action, etc.
%     - Action cue circle: rather than the crc() shape TaskObject (whose
%       exact argument format turned out to vary between MonkeyLogic
%       builds and kept failing to parse), this uses two pre-rendered PNG
%       images, green_circle.png and red_circle.png (provided alongside
%       this script), referenced via the well-documented pic() syntax.
%       Copy both PNGs next to your images/ folder (or add their folder
%       to [Set path]).
%     - "START" cue: a plain white-text-on-black PNG (start.png, provided),
%       shown for the full trial-start window (see CoSpeechGestures_timing.m).
%     - IMAGE COLORS: this ML build does not alpha-blend transparent PNGs -
%       transparent pixels render as black, so black-line-on-transparent
%       icons (the original speak.png/hand.png/speak_gesture.png style)
%       are invisible against the black task background. All images this
%       script references (speak.png, hand.png, speak_gesture.png,
%       start.png, green_circle.png, red_circle.png) must be fully opaque
%       with light-colored content on a black background - regenerate any
%       new stimulus image the same way if you add more.
%     - "Timing File" is a required column - it names the .m timing
%       script (no extension) that should run for that condition; here
%       every row uses the same script, CoSpeechGestures_timing.m, which
%       must sit in the task directory (next to this condition file) or
%       be discoverable via Main Menu > [Set path].
%
% TaskObject layout used here (must match CoSpeechGestures_timing.m):
%   TaskObject#1 = mov(...)  gesture video
%   TaskObject#2 = snd(...)  spoken word audio
%   TaskObject#3 = pic(...)  instruction symbol image
%   TaskObject#4 = pic(...)  action cue circle image, green(go)/red(nogo)
%   TaskObject#5 = snd(...)  "go" cue beep (same sound file every trial)
%   TaskObject#6 = pic(...)  "START" text cue (same image every trial)
%
% TaskObject syntax used (confirmed against the NIMH MonkeyLogic "TaskObjects"
% doc, https://monkeylogic.nimh.nih.gov/docs_TaskObjects.html):
%   pic(filename, Xdeg, Ydeg)
%   mov(filename, Xdeg, Ydeg)
%   snd(filename)
% filename KEEPS its extension (unlike some other ML variants that strip it).
% Xdeg/Ydeg here are left at (0,0), i.e. screen center, since I don't have
% your original PsychoPy pixel/position values for these components -
% adjust if your stimuli weren't centered.
%
% NOTE ON FILE REFERENCES: NIMH ML looks for each filename in this order:
%   1. the given path, if it's already a full path
%   2. the folder containing the conditions file/timing script (the "task directory")
%   3. the ML installation folder
%   4. the folders listed in Main Menu > [Set path]
% Easiest setup: add your "images/", "videos/" and "audios/" folders to
% [Set path] (Main Menu, next to "Load a conditions file"), then this
% script's filenames (name+extension only, no subfolder) will resolve.

if nargin < 4 || isempty(nGoReps),     nGoReps = 3;  end
if nargin < 5 || isempty(nNoGoSample), nNoGoSample = 7; end
if nargin < 6 || isempty(blockNumber), blockNumber = 1; end

goT = readtable(goFile, 'TextType', 'string');
noT = readtable(noFile, 'TextType', 'string');

expectedCols = {'instructionType','instructionSymbol','action','stimText','stimAudio','stimVideo','movement'};
for c = 1:numel(expectedCols)
    if ~ismember(expectedCols{c}, goT.Properties.VariableNames)
        error('Column "%s" not found in %s', expectedCols{c}, goFile);
    end
    if ~ismember(expectedCols{c}, noT.Properties.VariableNames)
        error('Column "%s" not found in %s', expectedCols{c}, noFile);
    end
end

% --- repeat go trials ---
goRep = repmat(goT, nGoReps, 1);

% --- random subset of nogo trials ---
if nNoGoSample > height(noT)
    error('nNoGoSample (%d) is larger than the number of rows in %s (%d)', ...
        nNoGoSample, noFile, height(noT));
end
sampleIdx = randperm(height(noT), nNoGoSample);
noSample  = noT(sampleIdx, :);

% --- combine + shuffle ---
allT = [goRep; noSample];
allT = allT(randperm(height(allT)), :);

nTrials = height(allT);

% --- fixed go-cue beep, used identically on every trial (matches
%     audioGoCue.setSound('audios/race-start-beeps-125125.mp3', ...) ) ---
goBeepName = 'race-start-beeps-125125.mp3';

fid = fopen(outFile, 'w');
if fid == -1
    error('Could not open %s for writing', outFile);
end
cleanupObj = onCleanup(@() fclose(fid));

fprintf(fid, 'Condition\tFrequency\tBlock\tTiming File\tInfo\tTaskObject#1\tTaskObject#2\tTaskObject#3\tTaskObject#4\tTaskObject#5\tTaskObject#6\n');

timingFileName = 'CoSpeechGestures_timing';  % .m name of the timing script (no extension), must sit in the task directory or Set path
startImgName   = 'start.png';                % same "START" cue image every trial

for i = 1:nTrials
    row = allT(i,:);

    % keep filename + extension (NIMH ML wants the extension), drop any
    % leading subfolder from the xlsx path (see [Set path] note above)
    [~, vName, vExt] = fileparts(row.stimVideo);
    [~, aName, aExt] = fileparts(row.stimAudio);
    [~, iName, iExt] = fileparts(row.instructionSymbol);
    videoName = [char(vName) char(vExt)];
    audioName = [char(aName) char(aExt)];
    imgName   = [char(iName) char(iExt)];

    action = lower(strtrim(row.action));
    if action == "go"
        cueObj = 'pic(green_circle.png,0,0)';
    else
        cueObj = 'pic(red_circle.png,0,0)';
    end

    stimTextClean = erase(row.stimText, '"');
    % Escape any single quotes so they don't break the struct() literal below
    escq = @(s) strrep(char(s), '''', '''''');

    % IMPORTANT: this ML loader does eval(['struct(' Info ');']) on the
    % Info column (see mlconditions/load_file.m line 73), so Info must be
    % a valid comma-separated list of 'fieldname', value pairs - NOT a
    % free-text label. This also means you can read this metadata back in
    % the timing script as TrialRecord.CurrentConditionInfo.<fieldname>.
    info = sprintf('''instructionType'',''%s'',''action'',''%s'',''stimText'',''%s'',''movement'',''%s''', ...
        escq(row.instructionType), escq(action), escq(stimTextClean), escq(row.movement));

    fprintf(fid, '%d\t1\t%d\t%s\t%s\tmov(%s,0,0)\tsnd(%s)\tpic(%s,0,0)\t%s\tsnd(%s)\tpic(%s,0,0)\n', ...
        i, blockNumber, timingFileName, info, videoName, audioName, imgName, cueObj, goBeepName, startImgName);
end

fprintf('Wrote %d trials to %s\n', nTrials, outFile);
condFile = outFile;
end
