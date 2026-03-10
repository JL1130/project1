import streamlit as st
import time

# Store workouts in session state
if "workouts" not in st.session_state:
    st.session_state.workouts = []

# MET values for different exercises
MET_VALUES = {
    "Pushups": 8.0,
    "Squats": 5.0,
    "Running": 9.8,
    "Yoga": 3.0,
    "Plank": 4.0,
    "Jogging": 7.0
}

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

#SIDEBAR MENU
    st.sidebar.header("GYMBRO")
if "menu" not in st.session_state:
    st.session_state.menu = "🏠 HOME"

#MENU OPTIONS
menu = [
    "🏠 HOME",
    "📝 LOGIN/REGISTER",
    "💪 WORKOUT PLANNER",
    "✍️ PROGRESS TRACKER",
    "🤔 ABOUT"
]
#SIDEBAR 
menu = st.sidebar.selectbox("MENU",
    menu, index=menu.index(st.session_state.menu))
st.session_state.menu = menu

#HOME PAGE
if menu == "🏠 HOME":
    st.title("🏋 Welcome! GYMBRO")
    st.text("ENJOY YOUR FITNESS JOURNEY BUDDY")

    if st.button("Explore More"):
        with st.spinner("Loading..."):
             time.sleep(2)
        st.session_state.menu = "📝 LOGIN/REGISTER"
        st.rerun()

    if st.subheader("Web App Features"):
        st.markdown("""
        - LOG DAILY WORKOUT PLAN
        - REGISTER TO BE PART OF OUR FITNESS GYM
        - PRECISELY PLAN YOUR GOAL
        - TRACK YOUR PROGRESS 
        """)

    with st.expander("Click to see more"):
        st.write("You have 0 logs today")
        st.write("Register and start your fitness journey")


#REGI FORM PAGE
elif menu == "📝 LOGIN/REGISTER":
    st.title("GYMBROOO 💪😤 almost there! ")
    tab1,tab2 = st.tabs(["LOGIN", "REGISTER"])

#TEMPORARYLY STORE USERNAME AND PASSWORD
    if "registered_username" not in st.session_state:
       st.session_state.registered_username = ""
       st.session_state.registered_password = ""

#LOGIN TAB   
    with tab1:
        username = st.text_input("USERNAME:")
        password = st.text_input("PASSWORD:", type= "password")
        #LOGIN BUTTOON
        login = st.button("LOGIN")
        if login:
            if username and password:
             st.success("✅ Log Successful!!!")
             with st.spinner("Logging in... Please wait"):
              time.sleep(2)

              st.session_state.logged_in = True
              st.session_state.menu = "💪 WORKOUT PLANNER"
              st.rerun()
            else:
              st.error("❌ Please fill in all fields.")

#REGISTER TAB
    with tab2:
        st.subheader("Fill the following information")
        name = st.text_input("NAME:")
        username1 = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email Address")

#TERMS AND CONDITIONS      
        with st.expander("📄 Terms and Conditions"):
            st.write("""
        By using this Workout Planner app, you agree to the following:

        1. This app is for educational and personal fitness planning only.
        2. The developers are not responsible for any injuries from workouts.
        3. Do not share your account credentials with others.
        4. Use the app responsibly and follow proper exercise safety guidelines.
        """)
#REGISTER BHTTON
        agree = st.checkbox("I agree to the Terms and Conditions")
        register = st.button("REGISTER")
        if register:
         if name and username1 and password and email:
           st.success("✅ Registration Complete!")
           with st.spinner("Registering... Please wait"):
              time.sleep(2)

              st.session_state.logged_in = True
              st.session_state.menu = "💪 WORKOUT PLANNER"
              st.rerun()
         else:
           st.error("❌ Please fill in all fields.")
            

#DAILY PLANNER
elif menu == "💪 WORKOUT PLANNER":

    if not st.session_state.logged_in:
        st.warning("⚠ Please login first!")
        st.session_state.menu = "📝 LOGIN/REGISTER"
        st.rerun()
#WORKOHT INFO
    st.title("LET'S GET STARTED")
    st.subheader("Set your workout plan")

#INPHT FIELDS
    date = st.date_input("Workout Date")
    name = st.text_input("Enter your name")
    age = st.number_input("Age", 10 )
    gender = st.radio("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (kg)", 30)
    height = st.number_input("Height (cm)", 100)
    workout = st.selectbox("Workout Type",
      ["Aerobic Exercises", "Strength Training", "Yoga", "Flexibility", 
       "High Intensity Interval Training (HIIT)"])
    exercises = st.multiselect(
        "Select Exercises",
        ["Pushups", "Squats", "Running", "Yoga", "Plank", "Jogging"])
    duration = st.slider("Workout Duration (minutes)", 10, 120)
    time_input = st.time_input("Workout Time")

    if st.button("LOG Workout"):
        with st.spinner("Processing..."):
            time.sleep(1)

#store data in a container      
        data = {
            "date": date,
            "name": name,
            "age": age,
            "weight": weight,
            "height": height,
            "workout": workout,
            "exercises": exercises,
            "duration": duration,
            "time": time_input
        }
        st.session_state.workouts.append(data)
        st.success("Workout Recorded!")
        st.success(f"Great job, {name}! Visit the PROGRESS TRACKER to see your fitness journey.")

#DAILY LOG
elif menu == "✍️ PROGRESS TRACKER":

    if not st.session_state.logged_in:
        st.warning("⚠ Please login first!")
        st.session_state.menu = "📝 LOGIN/REGISTER"
        st.rerun()

    st.title("PROGRESS TRACKER")
    st.subheader("Track your fitness progress")

#Workout History
    if len(st.session_state.workouts) == 0:
        st.info("No workouts logged yet. Start logging your workouts in the WORKOUT PLANNER!")
    else:
        for workout in st.session_state.workouts:
            st.write(f"**Date:** {workout['date']}")
            st.write(f"**Name:** {workout['name']}")
            st.write(f"**Age:** {workout['age']}")
            st.write(f"**Weight:** {workout['weight']} kg")
            st.write(f"**Height:** {workout['height']} cm")
            st.write(f"**Workout Type:** {workout['workout']}")
            st.write(f"**Exercises:** {', '.join(workout['exercises'])}")
            st.write(f"**Duration:** {workout['duration']} minutes")
            st.write(f"**Time:** {workout['time']}")
 
        MET = MET_VALUES.get(workout['exercises'][0], 1)
        calories_burned = (MET * workout['weight'] * workout['duration']) / 60
        st.write(f"**Estimated Calories Burned:** {calories_burned:.2f} kcal")
        
#ABOUT PAGE
elif menu == "🤔 ABOUT":
      st.header("ABOUT")
      st.markdown("""
       - The "GYMBRO" web app, is interactive UI web app 
    with allows the user to set their daily workout plan 
    and immediately process and see the result after
    they input the following informations on the workout 
    planner. This web app is designed for local gym to 
    analyze the memberships of user joined or logged in
    on the web app, once the user registered they also 
    provide a preveladge as a member to access the physical 
    gym, its like a local gym web app, which has a features 
    of daily workout planning and real-time access on their 
    progress a day. Moreover, on its features it has a
    tracker which analyze the calories burned using
    "Metabolic Equivalent of Task" to compute the energy 
    used on each workout activity based on user's weight, 
    activity, and intensity. 
                
    - The classified target user of "GYMBRO" web app is 
    those gym buddies that are currently a member of the
    physical gym and allows them to have an daily plan and 
    real-time progress history. Additionally,
    the individuals who's planning to commit on fitness 
    industry and prioritize the health using clear goal and 
    planning
                
    - After the webapp dashboard it has login and register
    page which collects the username, name, password, and 
    email. Upon the workout planner page, it collects the data 
    of the user such as (weight, height, age, and name) for the 
    workout information it collects the (workout type,
    workout selection, duration, etc.). 
    After completing the planner is has a feature which
    collecting those data into one container or array 
    and push into progress, from this the data displayed 
    and provide additional details such as calories burned.
    """)
      st.write("This web app is created by: ")
      st.write("- JOHN LLOYD L. CONDE")
