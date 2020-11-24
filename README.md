# Gram-Stain-Recognition
A program that uses artificial neural network and can recognize if an image of a microscopic slide has gram positive cells. The results are displayed in percentage

## Training Set
Consists of multiplile micro-images in magnification sizes of 40x, 80x, 100x. These are stored in the morph_data folder and sub-folders gram_negative and gram_positive. These images contains cells of different shapes(cocci, bacilli and spiral).

## Testing Set
There are two images of microscopic slides containing several cells that have been gram stained. These are named gram_slide_pink.png and gram_slide_purple.png. These were randomly obtained from Google images.

## How To Use
There are three main Python files contained inside the folder which must be opened in the following order as follows:

1) 01_morphology_extract.py - extracts the training set data by loading the images of microscopic slides and storing them in data files named 'i_train' and 'j_train'.

2) 02_training_for_morphology.py - trains the neural network to recognize which images are gram positive and gram negative.

3) 03_testing_program.py - test the program by loading one of the testing sets, by simply changing line 18 to the filename of one of the images.
