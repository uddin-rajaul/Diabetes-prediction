import numpy as np
import pickle

def diabetic_prediction(input_data):
    # Load the trained model
    model = pickle.load(open("trained_model.sav", "rb"))
    # Load the scaler
    scaled = pickle.load(open("scaler.sav", "rb"))
    #input_data = (5,116,74,0,0,25.6,0.201,30)

    #changing this list type of data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Scale the input features
    scaled_features = scaled.transform(input_data_as_numpy_array)

     #now reshape the data to make it work for 1 single data bcoz our system was trained only for 768 data
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    #now value cannot be given directly it must be standarised
    #std_data=scaler.transform(input_data_reshaped)
    #print(std_data)
    prediction = model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0]==0:
      print("not dibetic")
    else:
      print("dibetic")