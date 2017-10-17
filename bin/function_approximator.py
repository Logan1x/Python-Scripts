import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.models import load_model
from keras.optimizers import RMSprop

from keras import regularizers
from keras.constraints import *
from keras.callbacks import *

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

x = np.random.rand(10000)*100
y = np.random.rand(10000)*100
train = np.array([[i, j] for i, j in zip(x, y)])
z = x**2 + y**2

def create_model():
	model = Sequential()
	model.add(Dense(200, activation='sigmoid', input_dim=2, kernel_regularizer=regularizers.l2(0.001), bias_regularizer=regularizers.l1(0.001), bias_constraint=max_norm(2, 0)))
	model.add(Dense(100, activation='sigmoid', kernel_regularizer=regularizers.l2(0.001), bias_regularizer=regularizers.l1(0.001)))
	model.add(Dense(100, activation='relu', kernel_regularizer=regularizers.l2(0.001), bias_regularizer=regularizers.l1(0.001)))
	model.add(Dense(25, activation='relu', kernel_regularizer=regularizers.l2(0.001), bias_regularizer=regularizers.l1(0.001)))
	model.add(Dense(1, activation='relu'))

	rms = RMSprop(lr=0.005, rho=0.9, epsilon=1e-08, decay=0.0001)
	model.compile(loss='mean_absolute_error', optimizer=rms)
	return model

model = create_model()
model.fit(train, z, epochs=150, batch_size=5)
model.save('my_model.h5')
# model = load_model('my_model.h5')
s = np.array([[5, 5], [25, 25], [50, 50], [2, 2], [20, 20], [100, 100]])
print(model.predict(s))