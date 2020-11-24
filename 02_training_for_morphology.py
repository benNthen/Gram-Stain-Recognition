from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from pathlib import Path
import joblib

# Load the training data set
i_train = joblib.load("i_train.dat")
j_train = joblib.load("j_train.dat")

# Create a model and add layers
model = Sequential()

model.add(Flatten(input_shape=i_train.shape[1:]))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

# Train the model
model.fit(i_train, j_train, epochs=10, shuffle=True)

# Save neural network structure under a json file titled 'cell_structure.json'
model_structure = model.to_json()
f = Path("cell_structure.json")
f.write_text(model_structure)

# Save neural network's trained weights under h5 file titled 'cell_weights.h5'
model.save_weights("cell_weights.h5")