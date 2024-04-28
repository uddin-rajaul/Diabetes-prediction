from urllib import request
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

# Create your views here.
def home(request):
    return render(request, 'index.html')

def diabetic_prediction(input_data):
    # Load the trained model
    model = pickle.load(open("C:/Users/uddin/Documents/Diabetes_prediction/predictModel/trained_model.sav", "rb"))
    # Load the scaler
    scaled = pickle.load(open("predictModel/scaler.sav", "rb"))
    #input_data = (5,116,74,0,0,25.6,0.201,30)

    #changing this list type of data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Scale the input features
    #scaled_features = scaled.transform(input_data_as_numpy_array)

     #now reshape the data to make it work for 1 single data bcoz our system was trained only for 768 data
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    #now value cannot be given directly it must be standarised
    #std_data=scaler.transform(input_data_reshaped)
    #print(std_data)
    prediction = model.predict(input_data_reshaped)
    return prediction
    # print(prediction)
    # if prediction[0]==0:
    #   print("not dibetic")
    # else:
    #   print("dibetic")

def result(request):
    #input_data = (5,116,74,0,0,25.6,0.201,30)

    Pregnancies=request.GET['Pregnancies']
    #st.text_input function takes the data from user as input
    Glucose = request.GET['Glucose']
    BloodPressure = request.GET['BloodPressure']
    SkinThickness = request.GET['SkinThickness']
    Insulin=request.GET['Insulin']
    BMI=float(request.GET['BMI'])
    DiabetesPedigreeFunction=request.GET['DiabetesPedigreeFunction']
    Age=request.GET['Age']

    result = diabetic_prediction(([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]))
    return render(request, 'result.html', {'result':result})