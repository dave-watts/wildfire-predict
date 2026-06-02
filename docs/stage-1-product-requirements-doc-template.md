# Stage 1: Product Requirements Document (PRD)

## Interface for wildfire identification in satellite images


## Input
- kaggle dataset online 
- download val and test dataset 
- 2 model versions locally + inference architecture (via a training notebook on kaggle)
- training time series with metrics in csv format


## User stories

### User 1: Developer Dashboard

As a developer I want to:

know problems with the app
log information from the app
get new ideas how to improve app
get truth data from event to use in future training of models
...


### User 2: Emergcy Responder Interface

As an emergency responder I want to use the system to:

get alerted to fire
get estimate on fire size and firefighting requirements
know where the fire is
know how to get to the fire
report my firefighting actions back to command
produce report of incident, eg. including video.
report errors to developers
...


## Tools
User 1 story: Streamlit
User 2 story: Gradio
User 1 and 2 communication: Google Sheets via Google Cloud API

## PRD-to-issues



## UI Success Metrics








## Resources
https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset/data
`models.zip`- model checkpoiints, training history and evaluation csvs for the workshop. Download and unzip into a local folder.
