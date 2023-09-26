import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image


st.set_page_config(page_title="Haritha's Portfoli",page_icon=":🧑‍💻:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

pdf_content = "CV/Haritha's_CV.pdf"
lottie_coding = load_lottieurl("https://lottie.host/4c2d960e-fb05-439e-b387-76b12d2b4cf7/gkNL8yRt9q.json")
lottie_contact = load_lottieurl("https://lottie.host/3c3eb496-0c87-4042-b552-5f9793186de5/0zrCIqegrs.json")
img_contact_form = Image.open("images/Alogedara.png")
img_lottie_animation = Image.open("images/mobileAppBook.png")
erlsonImg = Image.open("images/elson.png")



with st.container():
     left_column, right_column = st.columns([2,1])
     with left_column:
        st.header("Hi my Name is Haritha Migara 🧑‍💻")
        st.title("A software Engeneering Student From Sri Lanka")
        st.write("Passionate software engineering student 🚀 | Code enthusiast 💻 | Problem solver by day, coder by night 🌙 | Building a future powered by technology 🌐 | Learning and growing one line of code at a time 📈 #CodeLife")
        st.write("[**Check me out At Linkedin**](https://www.linkedin.com/in/haritha-migara-070685215/)")
        if st.button("Download CV"):
        # When the button is clicked, create and offer the PDF download
            st.markdown(
            f'<a href="data:application/pdf;base64,{pdf_content.encode("utf-8").hex()}" download="sample.pdf">Download CV</a>',
            unsafe_allow_html=True
        )
     with right_column:
        image_url = "images/migara.jpeg"
        st.image(image_url, caption="Haritha Migara", width=300)

    
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do As a software engineering student: ")
        st.write("##")
        st.write(
            """
           

**Code Creatively:** I write, debug, and optimize code to create innovative software solutions.

**Solve Complex Problems:** I tackle challenging programming problems, finding elegant and efficient solutions.

**Collaborate:** I work in teams, sharing ideas and knowledge to build robust software projects.

**Learn Continuously:** I stay up-to-date with the latest technologies, languages, and development trends.

**Test and Debug:** I ensure software reliability by testing and debugging to fix issues.

**Design User Interfaces:** I create user-friendly interfaces for seamless user experiences.

**Contribute to Open Source:** I give back to the community by contributing to open-source projects.

**Attend Hackathons:** I participate in hackathons to showcase my skills and creativity.

**Stay Organized:** I manage projects, timelines, and resources to deliver software on schedule.

**Innovate:** I strive to find novel solutions to real-world problems through software.

My journey as a software engineering student is a blend of creativity, problem-solving,
and continuous learning to shape a tech-savvy future.
💡💻🌟 #SoftwareEngineeringStudent
            """
        )
        st.write("[**GitHub Account**](https://github.com/HMigara)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
     #   ---- PROJECTS ----
     #projct 01
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
        
    with text_column:
        st.subheader("Hotel resevetion System For AliGedara Villa's")
        st.write(
            """
            A hotel booking system is a software application or platform that allows users to 
            browse, search for, and reserve accommodations 
            in hotels, motels, resorts, or other lodging establishments. This system streamlines the process
            of booking a room by providing users with detailed information about available rooms, their amenities, prices, and booking conditions.
            """
        )
        st.markdown("[GitHub Repository](https://github.com/HMigara/AliGedara-Booking-System-Hotel-Reservation-System-)")
        
#porject 02
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(erlsonImg)
        
    with text_column:
        st.subheader("Elson vehical validation System")
        st.write(
            """
             🚗 Our Vehicle Validation System brings advanced security and efficiency to your access control needs. 
             Using cutting-edge technology like license plate recognition and RFID, we ensure only authorized vehicles gain entry, whether it's for parking facilities, gated communities, or transportation services. With real-time monitoring, automated access control, and seamless integration, our system offers top-tier security and convenience.
             Explore our repository to learn more about how we're revolutionizing vehicle access management
            """
        )
        st.markdown("[GitHub Repository](https://github.com/HMigara/web---CW)")

        
        

# ---- CONTACT ----
with st.container():

    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/harimigara@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
  
    with right_column:
        st_lottie(lottie_contact, height=300, key="tetxt")
            
    