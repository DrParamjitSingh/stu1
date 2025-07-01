# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 21:21:06 2025

@author: Dell
"""

import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Model training data
X = np.array([
    [2, 50, 60, 5],
    [3, 60, 65, 6],
    [4, 55, 70, 6],
    [5, 70, 80, 7],
    [6, 80, 90, 8],
    [7, 85, 95, 8]
])
y = np.array([55, 65, 60, 75, 85, 90])
model = LinearRegression().fit(X, y)

# Web UI

#st.subheader("📚 STUDENT GRADE PREDICTION SYSTEM")
st.write("##### 📚 STUDENT GRADE PREDICTION SYSTEM")

# Using padding-left or margin-left to push the text over.
# 'em' units are relative to the font size, so it can be more robust than 'px'
# for text alignment, but still requires tuning.
st.markdown(
    """
    <p style="padding-left: 5ch; font-weight: 300; font-size: small;color: #666;margin-bottom: 0px;">
        © Copyright Dr Paramjit Singh, 2025. All Rights Reserved.
    </p>
    """,
    unsafe_allow_html=True
)

#st.divider() # This adds a horizontal line
st.markdown("---") # This adds a horizontal line using Markdown


hours = st.slider("Hours Studied", 0, 10, 5)
past = st.slider("Past Score (%)", 0, 100, 60)
attn = st.slider("Attendance (%)", 0, 100, 80)
sleep = st.slider("Sleep Hours", 0, 12, 7)

if st.button("Predict Grade"):
    pred = model.predict([[hours, past, attn, sleep]])
    st.success(f"Predicted Final Grade: {pred[0]:.2f}%")
