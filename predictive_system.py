# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# loading the saved model 

loaded_model = pickle.load(open('C:/Users/sagnik panda/Desktop/Heart Disease Prediction/heart_disease_model.sav', 'rb'))

input_data = (57,0,0,120,354,0,1,163,1,0.6,2,0,2)
#input_data = (63,0,0,108,269,0,1,169,1,1.8,1,2,2)

# change the input into np array
input_np_array = np.asarray(input_data)
# reshape the np array as we are predicting for only one data point
reshaped_data = input_np_array.reshape(1,-1)

prediction = loaded_model.predict(reshaped_data)
print(prediction)

if(prediction[0] == 0):
    print('The person does not have heart disease')
else:
    print('The person has heart disease')