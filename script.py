
import streamlit as st
#import pandas as pd

# Inject custom CSS for animated gradient background
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, red, blue, yellow, green, magenta, purple, white);
        background-size: 1600% 1600%;
        animation: gradientShift 30s ease infinite;
    }

    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Optional: style input boxes and buttons for better contrast */
    .stTextInput > div > div > input {
        background-color: #ffffffcc;
        color: #000;
    }

    .stButton > button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.header("Buy Our Course for your Education by Entering your details below:")

# Form inputs
Name = st.text_input("Enter your Full Name")
Age = st.text_input("Enter your Age")
Parents_Name = st.text_input("Enter your Parents Name, Any")
Email = st.text_input("Enter your Email for Contact Purpose")
Course_You_Need = st.text_input("Enter the Course you are Looking for")
Course_stream = st.selectbox("Enter the Stream of your Education:",
                             ("B.Tech", "BCom.", "MCom.", "12th", "BCA", "BBA", "MBA"))

# Submit button
button = st.button("Submit")

# Display entered details
if button:
    st.markdown(f"""
    **Name:** {Name}  
    **Age:** {Age}  
    **Parent Details:** {Parents_Name}  
    **Email:** {Email}  
    **Course Interested:** {Course_You_Need}  
    **Stream:** {Course_stream}
    """)

##

import streamlit as st

# Horizontal navigation bar
st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        background-color: #333;
        padding: 10px 0;
        border-radius: 8px;
        margin-bottom: 30px;
        flex-wrap: wrap;
    }

    .navbar a {
        color: white;
        padding: 12px 20px;
        text-decoration: none;
        font-size: 16px;
        transition: background-color 0.3s;
    }

    .navbar a:hover {
        background-color: #ddd;
        color: black;
        border-radius: 5px;
    }

    .navbar a.active {
        background-color: #04AA6D;
        color: white;
        border-radius: 5px;
    }
    </style>

    <div class="navbar">
        <a href="#home" class="active">🏠 Home</a>
        <a href="#life">🌟 Life at Edu.sonalisingh</a>
        <a href="#privacy">🔐 Privacy Policy</a>
        <a href="#terms">📜 Terms & Use</a>
        <a href="#location">📍 Location</a>
        <a href="#team">👥 Team Members</a>
    </div>
""", unsafe_allow_html=True)

##

import streamlit as st

# Fixed top header with left-aligned welcome text and right-aligned profile image
st.markdown("""
    <style>
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 9999;
        background-color: #f0f0f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 30px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .welcome-text {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }

    .profile-box {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .profile-box img {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #04AA6D;
    }

    .profile-role {
        font-size: 14px;
        color: #555;
    }

    /* Push content below fixed header */
    .stApp {
        margin-top: 80px;
    }
    </style>

    <div class="fixed-header">
        <div class="welcome-text">Welcome to Sonali Singh Educational Website 🙂</div>
        <div class="profile-box">
            <img src="https://image2url.com/images/1761230227272-93e7a7f3-bd5d-4b69-9431-84e0f528535a.jpg" alt="Profile Image">
            <div class="profile-role">Educator & Mentor</div>
        </div>
    </div>
""", unsafe_allow_html=True)
