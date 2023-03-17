# deep_learning_training.py

# %%
import tensorflow as tf
from tensorflow import keras
tf.__version__

# %%
fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()


# %%
# creating a validation set, because it is not given:
X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000] / 255.0, y_train_full[5000:] / 255.0
X_test = X_test / 255.0 

# %%
class_names = ["tshirt", "trouser", "pullover", "dress", "coat", "sandal",
                "shirt", "sneaker", "bag", "ankle boot"]
# ### Building the neural network!

# %%
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28,28]))
model.add(keras.layers.Dense(300, activation='relu'))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax')) #10 classes of output!

model.summary()


model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train,y_train, epochs=3, validation_data=(X_valid,y_valid))

# ### Saving a trained model to disk:

# %%
model_save_location = "deep_learning/Sequential_DNN_1.h5"
model.save(model_save_location)




