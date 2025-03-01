import streamlit as st
import matplotlib.pyplot as plt

# App Title
st.title("🚀 Growth Mindset Challenge")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Progress Tracker", "📝 Daily Challenge", "💡 Tips for Growth",
    "📖 Success Stories", "🎯 Goal Setting", "🤔 Self-Reflection", "🧠 Brain Exercises"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Growth Mindset Challenge! 🎯")
    st.markdown("""
    ### Why Adopt a Growth Mindset?
    ✅ **Embrace Challenges**: View obstacles as opportunities to learn rather than setbacks.  
    ✅ **Learn from Mistakes**: Mistakes help you improve.  
    ✅ **Persist Through Difficulties**: Stay determined!  
    ✅ **Celebrate Effort**: Focus on growth, not just results.  
    ✅ **Stay Curious**: Always be open to learning.  
    """)
    st.image("https://media.istockphoto.com/id/1973623637/photo/mindset-loading-bar-concept.webp?a=1&b=1&s=612x612&w=0&k=20&c=_IrFcWJW6qoDNKpKgSNT4rY78RxoQYJo9kkPPXh7cFc=", use_container_width=True)

# Progress Tracker
elif page == "📊 Progress Tracker":
    st.header("📊 Your Growth Progress")
    
    days = st.slider("How many days have you been practicing a Growth Mindset?", 1, 30, 5)
    effort = st.slider("How much effort do you put in (1-10)?", 1, 10, 7)

    st.session_state["days"] = days  

    fig, ax = plt.subplots()
    ax.bar(["Days Practiced", "Effort Level"], [days, effort], color=["blue", "green"])
    ax.set_ylabel("Level")
    st.pyplot(fig)

# Daily Challenge
elif page == "📝 Daily Challenge":
    st.header("📝 Today's Growth Mindset Challenge")
    
    days = st.session_state.get("days", 1)

    challenges = [
        "🔹 Identify one mistake you made today and what you learned from it.",
        "🔹 Try something new that challenges you.",
        "🔹 Replace a negative thought with a positive one.",
        "🔹 Teach a new skill to a friend.",
        "🔹 Read about someone who overcame obstacles and got successful.",
        "🔹 Write down three things you're grateful for today."
    ]

    st.write("💡 **Challenge for Today:**", challenges[days % len(challenges)])

# Tips for Growth
elif page == "💡 Tips for Growth":
    st.header("💡 Daily Growth Tips")
    
    tips = [
        "🔥 **Learn from Feedback** – Constructive criticism helps you improve.",
        "🔥 **Be Persistent** – Hard work leads to success.",
        "🔥 **Surround Yourself with Positive People** – Learn from those with a growth mindset.",
        "🔥 **Stay Curious** – Ask questions and keep learning.",
        "🔥 **Break Big Goals into Small Steps** – Focus on progress, not perfection.",
        "🔥 **Celebrate Small Wins** – Every step forward counts!",
        "🔥 **Develop a Learning Habit** – Read books, watch tutorials, and improve every day."
    ]

    days = st.session_state.get("days", 1)
    st.markdown(f"💡 **Tip for Today:** {tips[days % len(tips)]}")

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Real-Life Growth Mindset Stories")
    
    stories = [
        ("💪 **Thomas Edison**", "Failed over 1,000 times before inventing the light bulb."),
        ("🌍 **Oprah Winfrey**", "Was fired from her first TV job but never gave up."),
        ("🎶 **Eminem**", "Rejected multiple times before becoming a rap legend."),
        ("🏀 **Michael Jordan**", "Cut from his high school basketball team, but became a legend."),
        ("📚 **J.K. Rowling**", "Harry Potter was rejected by 12 publishers before success.")
    ]
    
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")

    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")

    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 Daily Self-Reflection")

    journal = st.text_area("📖 Write about your day, your challenges, and what you learned:")
    
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep learning and growing.")

# Brain Exercises
elif page == "🧠 Brain Exercises":
    st.header("🧠 Daily Brain Challenge")

    riddles = [
        ("🤔 **I speak without a mouth and hear without ears. Who am I?**", "An echo"),
        ("🔍 **The more you take, the more you leave behind. What am I?**", "Footsteps"),
        ("🎭 **I have keys but open no locks. What am I?**", "A piano"),
        ("💡 **What has to be broken before you can use it?**", "An egg")
    ]
    
    days = st.session_state.get("days", 1)
    question, answer = riddles[days % len(riddles)]

    st.write(question)
    if st.button("Show Answer"):
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("🌱 *Developed with ❤️ using Streamlit. Keep Growing!*")