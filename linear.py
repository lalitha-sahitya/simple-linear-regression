import streamlit as st
import pickle
import numpy as np
st.title("SIMPLE LINEAR REGRESSION")
x=st.text_input("Enter x value:")
model="/model.pkl"
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
bt=st.button('predict y value')
if bt:
    x=np.array([[float(x)]])
    p=model.predict(x)
    st.write(f"predicted: {p}")
