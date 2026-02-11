# Co-speech Gestures

This repository contains the materials and scripts for two experimental tasks investigating co-speech gesture processing. Each experiment has its own dedicated folder, including Python scripts, PsychoPy Scripts and all required stimuli.

## Repository Structure

```bash
CoSpeechGestures/
│   ├── CoSpeechGestures.psyexp
│   ├── CoSpeechGestures.py
│   ├── folderswithstimuli/
│   └── data/
│
CoSpeech_Congruency/
│   ├── CoSpeech_congruency.psyexp
│   ├── CoSpeech_congruency.py
│   ├── folderswithstimuli/
│   └── data/
│
README.md
```


### Experiment I: Co-speech Gesture
This folder contains the full script and stimuli for the Co-speech Gesture task.

### Experiment II: Speech–Gesture Congruency
This folder contains all materials for the Speech–Gesture Congruency task.


## Running the Experiments
You can run each experiment in one of two ways:

1. Using PsychoPy Standalone
Open PsychoPy.
Load the corresponding .psyexp file located in each experiment folder.
Run the task through the PsychoPy Runner.

3. Running directly via Terminal (conda recommended) or VS Code etc. 
Each experiment folder contains a corresponding .py script that can be executed directly. Navigate to folder and run: 

python name.py


## Important Note
Download or clone the entire repository before running any experiment.
Each task relies on multiple subfolders (e.g. videos/, audios/) that contain necessary materials. Running only the script without the associated stimuli will result in errors.
