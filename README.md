[![dep1](https://img.shields.io/badge/Tensorflow-2.0+-brightgreen.svg)](https://www.tensorflow.org/) 
[![dep2](https://img.shields.io/badge/Keras-2.0+-brightgreen.svg)](https://keras.io/) 
# Gram-Stain-Recognition
A program that demonstrates the use of artificial neural network to recognize if an image of a microscopic slide has gram positive cells. The results are displayed in percentage.

## Training Set
Consists of 18 micro-images in magnification sizes of 40x, 80x and 100x. The images cells of different shapes(cocci, bacilli and spiral). These are all stored in the morph_data folder and sub-folders gram_negative and gram_positive. 

## Testing Set
There are two images of microscopic slides containing several cells that have been gram stained. These are named gram_slide_pink.png and gram_slide_purple.png. These were randomly obtained from Google images.

## How To Use
There are three main Python files contained inside the folder which must be opened in the following order as follows:

1) 01_morphology_extract.py - extracts the training set data by loading the images of microscopic slides and storing them in data files named 'i_train' and 'j_train'.

2) 02_training_for_morphology.py - trains the neural network to recognize which images are gram positive and gram negative.

3) 03_testing_program.py - test the program by loading one of the testing sets, by simply changing line 18 to the filename of one of the images.

## Demonstration

https://github.com/benNthen/Gram-Stain-Recognition/blob/master/gram_slide_purple.png

Opened `03_testing_program.py` then editted line 18's `image.load_img()` with the filename `gram_side_purple.png`. Run the program.

```python
# Load the image file to test, resizing
# it to 200x200 (as required by this model)
>>> img = image.load_img("gram_slide_purple.png", target_size=(200, 200))
```
Output: 
>>The possibility that this slide contains gram positive cells are: 100%

https://github.com/benNthen/Gram-Stain-Recognition/blob/master/gram_slide_pink.png

Opened `03_testing_program.py` then edit line 18's `image.load_img()` with the filename `gram_side_pink.png`. Run the program.

```python
# Load the image file to test, resizing
# it to 200x200 (as required by this model)
>>> img = image.load_img("gram_slide_pink.png", target_size=(200, 200))
```

Output: 
>>The possibility that this slide contains gram positive cells are: 19%

#### Requirements

- [Python](https://www.python.org)
- [NumPy](http://www.numpy.org) 
- [Pandas](http://pandas.pydata.org) 
- [Tensorflow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
