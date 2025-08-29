# TODO

- [ ] Write function to convert letters to numbers for field values from G205, and compare with metadata from G201-G203
    - Note the differences for each variable
    - Strip out the field values like "A and Z"

- [/] Convert letters (A-Z) to corresponding numbers (1-26) for G205 dysmorphology variables
- [/] Create second variable for G205 for cases with multiple dysmorphologies

- [ ] Add expected type schema to apply for test_validate
- [ ] Turn `validate.py` into a legitimate test with pytest - can run tests to ensure changes are correct
    - [ ] Write tests from the beginning for validations and testing harmonisation functions
    - [ ] Use as part of the data exploration phase


## On Hold

Rename the following to avoid cross-over from previous harmonisation!

G217_BP64
G214_BP64
G217_BP65
G214_BP65
G217_BP66
G214_BP66


## Done

- [x] Identify remaining blood pressure variables to harmonise
- [x] Find the relevant dysmorphology variables across the physical assessment sheets AND the datasets
