import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('deep_learning/Sequential_DNN_1.h5')

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

X_new = X_test[:3]
y_pred = model.predict(X_new) #of gewoon predict, met probabiliteiten
print(y_pred)