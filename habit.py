import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("🌱 Growth Habit Tracker")

# Habit List
habits = ["Learn something new", "Write self-reflection", "Accept challenges", "Read a book", "Exercise"]
selected_habits = st.multiselect("Select your habits:", habits, default=habits[:2])

# Data Storage (Session State)
if "habit_data" not in st.session_state:
    st.session_state.habit_data = {habit: [] for habit in habits}

# Mark Completion
st.subheader("✅ Mark Today's Completed Habits")
for habit in selected_habits:
    done = st.checkbox(f"{habit} Completed")
    if done:
        st.success(f"🎉 Great! You completed '{habit}' today! 👍")
        st.session_state.habit_data[habit].append(1)  # ✅ Habit ko store karo
    else:
        st.session_state.habit_data[habit].append(0)  #

# **Fix: Ensure Equal Lengths**
max_length = max(len(v) for v in st.session_state.habit_data.values())  # Find longest list
for habit in st.session_state.habit_data:
    while len(st.session_state.habit_data[habit]) < max_length:
        st.session_state.habit_data[habit].append(0)  # Fill missing entries with 0

# Show Progress
st.subheader("📊 Habit Completion Progress")
df = pd.DataFrame(st.session_state.habit_data)  # Now all arrays have the same length!
st.line_chart(df)

# Reset Data
if st.button("Reset Progress"):
    st.session_state.habit_data = {habit: [] for habit in habits}
    st.success("Progress Reset Successfully!")
