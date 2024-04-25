from urllib import request
from django.shortcuts import render
from .diabeties_prediction import diabetic_prediction
import numpy as np
import pickle

# Create your views here.
def home(request):
    return render(request, 'index.html')

def result(request):
    #input_data = (5,116,74,0,0,25.6,0.201,30)

    Pregnancies=int(request.GET['Number of pregnancies'])
    #st.text_input function takes the data from user as input
    Glucose=int(request.GET['Glucose Level'])
    BloodPressure=int(request.GET['Blood pressure value'])
    SkinThickness=int(request.GET['Skin Thickness Value'])
    Insulin=int(request.GET['Insulin value'])
    BMI=int(request.GET['BMI value'])
    DiabetesPedigreeFunction=int(request.GET['Diabetes Pedigree function value'])
    Age=int(request.GET['Age of a person'])

    result = diabetic_prediction(([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]))
    return render(request, 'result.html', {'result':result})