---
author: Matt Humphrey
date_started: 27/08/2025
date_completed:
type: harmonisation
status: in-progress
---

# Harmonising Dysmorphology Variables

## Project Structure

### data

Contains four sub-directories with the datasets...
- Original: as they were at the beginning of the project
- Raw: as they were prior to harmonising (some datasets may have been changed by other data officers while the project was underway)
- Interim: processed initially to rename and delete specified variables
- Processed: with all transformations completed to harmonise the variables across datasets

### docs

Contains all relevant information related to the project

### notebooks

A collection of Marimo notebooks both for experimentation, and in some cases, used for running the functions to create the interim and processed datasets.

### src/dysmorph

This is the where all code related to the project is stored.
The key files to be aware of are:
- `config/metadata.py`: where the metadata for each unique variable is defined
- `config/variables.py`: the variables specified for alteration/exploration, renaming, and deleting
- `harmonise.py`: contains all the logic/functions to change the raw data and harmonise the variables
- `validate.py`: specifies the expected values/ranges for each variable for testing
