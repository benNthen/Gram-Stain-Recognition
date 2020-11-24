# Gram-Stain-Recognition
A program that uses artificial neural network and can recognize which images of microscopic slides containing gram positive and gram negative cells.

## Training Set
Consists of micro-images in magnifications of 40x, 100x, 400x. These are stored in the morph_data folder and sub-folders gram_negative and gram_positive.

## Testing Set
There are two images of microscopic slides containing several cells that have been gram stained. These are gram_slide_pink.png and gram_slide_purple.png

## How To Use
There are three main Python files contained inside the folder which must be opened in the following order as follows:

1) 01_morphology_extract.py - extracts the training set data by loading the images of microscopic slides and storing them in data files named 'i_train' and 'j_train'

2) 02_training_for_morphology.py - trains the neural network to recognize which images are gram positive and gram negative

3) 03_testing_program.py - test the program by loading one of the testing sets, by simply changing line 18 to the filename of one of the images.
