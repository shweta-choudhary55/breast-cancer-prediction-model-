# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:17:42 2024

@author: shwet
"""

import numpy as np
import pickle
import streamlit  as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/shwet/OneDrive/Desktop/PDTM/trained_model.sav', 'rb'))


##creating a function for prediction

def cancer_prediction(input_data):
    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for one datapoint
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The Breast cancer is Malignant'

    else:
      return 'The Breast Cancer is Benign'
  
    
def main():
    
    
    
    
    ##giving a title
    st.title('cancer prediction web App')
    
    ##getting the input data  from the user 
    #"id","diagnosis,"radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"
    
    radius_mean= st.text_input('mean radius')
    texture_mean=st.text_input('mean texture')
    perimeter_mean=st.text_input('mean perimeter')
    area_mean= st.text_input('mean area')
    smoothness_mean = st.text_input('mean smoothness')
    compactness_mean= st.text_input('mean compactness')
    concavity_mean= st.text_input('mean concavity')
    concave_points_mean= st.text_input('mean concave points')
    symmetry_mean=st.text_input('mean symmetry ')
    fractal_dimension_mean=st.text_input('mean fractal dimension')
    radius_se=st.text_input('radius error')
    texture_se=st.text_input('texture error')
    perimeter_se=st.text_input('perimeter error')
    area_se= st.text_input(' area error ')
    smoothness_se = st.text_input(' smoothness error')
    compactness_se= st.text_input('compactness error')
    concavity_se= st.text_input(' concavity error')
    concave_points_se= st.text_input(' concave points error')
    symmetry_se=st.text_input(' symmetry error ')
    fractal_dimension_se=st.text_input(' fractal dimension error')
    radius_worst=st.text_input(' worst radius')
    texture_worst=st.text_input(' worst texture ')
    perimeter_worst=st.text_input(' worst perimeter ')
    area_worst= st.text_input('  worst area  ')
    smoothness_worst = st.text_input(' worst smoothness')
    compactness_worst= st.text_input('worst compactness')
    concavity_worst= st.text_input('  worst concavity ')
    concave_points_worst= st.text_input('worst concave points ')
    symmetry_worst=st.text_input('  worst symmetry  ')
    fractal_dimension_worst=st.text_input('worst fractal dimension ')
    
    
    ### code for prediction
    diagnosis =''
    
    ###creating a button for prediction
    if st.button('Breast Cancer test results'):
        diagnosis= cancer_prediction([radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst])
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    