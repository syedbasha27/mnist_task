#task3 mnist digit classification

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatte

#load dataset
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)
print(x_test.shape)

#diplaying the data

plt.imshow(x_train[0], cmap='gray')
plt.title(y_train[0])
plt.show()

#preprocessing of data using normalization formula


x_train = x_train / 255.0
x_test = x_test / 255.0

#creating a neural network

model = Sequential([
    Flatten(input_shape=(28, 28)),
    
    Dense(128, activation='relu'),
    
    Dense(10, activation='softmax')
])


#compilation of model

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

#training the model

model.fit(x_train, y_train, epochs=5)

#testing the model

test_loss, test_accuracy = model.evaluate(x_test, y_test)

print("Test Accuracy:", test_accuracy)

#prdicting the result

predictions = model.predict(x_test)

print(np.argmax(predictions[0]))
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
#predicting the own data

import requests
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

# Image URL
url = ""   # direct image URL

# Download image
response = requests.get(url)

# Open image
img = Image.open(BytesIO(response.content))

# Convert to grayscale
img = img.convert('L')

# Resize image
img = img.resize((28, 28))

# Display image
plt.imshow(img, cmap='gray')
plt.show()

# Convert to array
img_array = np.array(img)

# Normalize
img_array = img_array / 255.0

# Invert colors
img_array = 1 - img_array

# Reshape for model
img_array = img_array.reshape(1, 28, 28)

# Predict
predictions = model.predict(img_array)

# Final output
print("Predicted Digit:", np.argmax(predictions[0]))
