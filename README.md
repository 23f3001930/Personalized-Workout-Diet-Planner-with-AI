🏋️ Personalized Workout & Diet Planner with AI

A Streamlit-based application that generates personalized workout and diet plans for students using AI logic based on body metrics, fitness goals, and diet preferences.

Features

Personalized workout plan

Indian diet suggestions

BMI calculation

AI calorie estimation

Weekly progress tracking

Wearable data simulation

Mobile-friendly UI

Project Structure
Personalized-Fitness-Planner/
│
├── app.py
├── requirements.txt
├── utils/
│   ├── bmi.py
│   ├── workout.py
│   ├── diet.py
│   ├── calorie.py
│   ├── progress.py
│   └── wearable.py
└── README.md

Installation
python -m pip install -r requirements.txt
python -m pip install streamlit

Run Application
python -m streamlit run app.py


Open browser and visit:

http://localhost:8501                         
https://personalized-workout-diet-planner-with-ai11.streamlit.app/              
How It Works

User enters age, height, weight, goal, and diet preference

BMI is calculated and health status is shown

AI estimates daily calorie needs

Workout and diet plans are generated

Progress is tracked weekly

Technologies Used

Python

Streamlit

AI-based logic

Conclusion

This project demonstrates how AI and Streamlit can be used to build a smart, personalized fitness planning system for students.
