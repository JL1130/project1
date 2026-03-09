import streamlit as st
import time

st.set_page_config(page_title="Fitness Tracker", layout="wide")

# SIDEBAR NAVIGATION
page = st.sidebar.radio("Navigation", ["Home", "Workout Form", "Results", "About"])

# HOME PAGE
if page == "Home":
    st.title("🏋 Fitness Tracker App")

    st.header("Welcome")
    st.text("This app demonstrates Streamlit UI components.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Features")
        st.markdown("""
        - Track workouts
        - Input fitness data
        - Demo UI components
        """)

    with col2:
        st.image("https://images.unsplash.com/photo-1599058917212-d750089bc07e")

    with st.expander("Click to learn more"):
        st.write("This is a demo Streamlit UI project.")

# WORKOUT FORM
elif page == "Workout Form":

    st.title("Workout Information")

    name = st.text_input("Enter your name")
    age = st.number_input("Age", 10, 80)

    gender = st.radio("Gender", ["Male", "Female"])

    workout = st.selectbox(
        "Workout Type",
        ["Cardio", "Strength Training", "Yoga", "Flexibility"]
    )

    exercises = st.multiselect(
        "Select Exercises",
        ["Pushups", "Squats", "Running", "Jump Rope", "Plank"]
    )

    duration = st.slider("Workout Duration (minutes)", 10, 120)

    date = st.date_input("Workout Date")

    time_input = st.time_input("Workout Time")

    water = st.checkbox("Did you drink enough water?")

    photo = st.file_uploader("Upload workout photo")

    if st.button("Submit Workout"):

        with st.spinner("Processing..."):
            time.sleep(2)

        st.success("Workout Recorded!")

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

# RESULTS PAGE
elif page == "Results":

    st.title("Workout Summary")

    tab1, tab2 = st.tabs(["Today's Stats", "Tips"])

    with tab1:
        st.write("Calories burned estimate")
        st.metric("Calories", "350 kcal")

    with tab2:
        st.write("Fitness Tips")
        st.info("Stay hydrated and maintain proper form.")

# ABOUT PAGE
elif page == "About":

    st.title("About This App")

    st.markdown("""
    *Fitness Tracker UI Demo*

    This application demonstrates a meaningful UI flow using multiple Streamlit components.

    *Developer:* Your Name  
    *Course:* Your Subject  
    *Purpose:* Streamlit UI Demonstration Project
    """)
