import streamlit as st
import time

#SIDEBAR MENU
st.sidebar.header("GYMBRO")

if "menu" not in st.session_state:
    st.session_state.menu = "🏠 HOME"

menu = [
    "🏠 HOME",
    "📝 REGISTRATION FORM",
    "💪 DAILY PLANNER",
    "✍️ WORKOUT GOAL",
    "🤔 ABOUT"
]

menu = st.sidebar.selectbox("MENU",
    menu,
    index=menu.index(st.session_state.menu)
)

st.session_state.menu = menu

#HOME PAGE
if menu == "🏠 HOME":
    st.title("🏋 Welcome! GYMBRO")
    st.text("ENJOY YOUR FITNESS JOURNEY BUDDY")

    if st.button("Explore More"):
        with st.spinner("Loading..."):
             time.sleep(2)
        st.session_state.menu = "📝 REGISTRATION FORM"
        st.rerun()

    if st.subheader("Web App Features"):
        st.markdown("""
        - LOG DAILY WORKOUT PLAN
        - REGISTER TO BE PART OF OUR FITNESS GYM
        - PRECISELY PLAN YOUR GOAL
        """)

    with st.expander("Click to see more"):
        st.write("You have 0 logs today")
        st.write("Register and start your fitness journey")


#REGI FORM PAGE
elif menu == "📝 REGISTRATION FORM":
    st.title("GYMBROOO 💪😤 almost there! ")

    tab1,tab2 = st.tabs(["LOGIN", "REGISTER"])

    with tab1:
        username = st.text_input("USERNAME:")
        password = st.text_input("PASSWORD:")

    with tab2:
        st.text("register")


#DAILY PLANNER
elif menu == "💪 DAILY PLANNER":
    st.write("daily planner page")

#DAILY LOG
elif menu == "✍️ Workout Goal":
    st.write("YOUR LOG ")

#ABOUT PAGE
elif menu == "🤔 ABOUT":
    st.write("ABOUT")

