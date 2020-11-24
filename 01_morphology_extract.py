import numpy as np
import joblib
from pathlib import Path
from keras.preprocessing import image
from keras.applications import vgg16
from io import BytesIO

# Path to folders with training data
pos_path = Path("morph_data") / "gram_positive"
neg_path = Path("morph_data") / "gram_negative"

slides = []
labels = []

# Load all the gram_positive slides
for img in pos_path.glob("*.png"):
    # Load the image from disk
    img = image.load_img(img)

    # Convert the image to a numpy array
    image_array = image.img_to_array(img)

    # Add the image to the list of slides
    slides.append(image_array)

    # For each gram negative slide, label with value of 1
    labels.append(1)

# Load all the gram_negative slides
for img in neg_path.glob("*.png"):
    # Load the image from disk
    img = image.load_img(img)

    # Convert the image to a numpy array
    image_array = image.img_to_array(img)

    # Add the image to the list of images
    slides.append(image_array)

    # For each gram negative slide, label with value of 0
    labels.append(0)

# Create a single numpy array with all the images we loaded
i_train = np.array(slides)

# Also convert the labels to a numpy array
j_train = np.array(labels)

# Normalize image data to 0-to-1 range
i_train = vgg16.preprocess_input(i_train)

# Load a pre-trained neural network to use as a feature extractor
pretrained_nn = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(200, 200, 3))

# Extract features for each slide 
features_i = pretrained_nn.predict(i_train)

# Save the array of extracted features to file titled 'i_train'
joblib.dump(features_i, "i_train.dat")

# Save the matching array of expected values to a file titled 'j_train'
joblib.dump(j_train, "j_train.dat")
