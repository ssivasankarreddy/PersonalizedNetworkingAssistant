import streamlit as st
import requests

# -----------------------------
# Load CSS
# -----------------------------
def load_css():
    try:
        with open("frontend/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

load_css()

BASE_URL = "https://personalizednetworkingassistant-2.onrender.com"

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image(
    "https://img.icons8.com/color/96/conference-call.png",
    width=80
)

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "",
    [
        "🏠 Home",
        "💬 Generate Conversation",
        "🧠 Theme Extraction",
        "📖 Fact Checker",
        "📜 History",
        "ℹ️ About"
    ]
)

# =====================================================
# HOME
# =====================================================

if menu == "🏠 Home":

    st.title("🤝 Personalized Networking Assistant")

    st.write(
        """
Generate intelligent conversation starters for networking events using AI.
This application helps professionals prepare for conferences,
career fairs, meetups, and networking sessions.
"""
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("💬 AI Conversation Generator")
        st.info("🧠 Theme Extraction")
        st.info("📖 Wikipedia Fact Checker")

    with col2:
        st.success("📜 Conversation History")
        st.success("👍 Feedback System")
        st.success("⚡ FastAPI + Streamlit")

# =====================================================
# GENERATE CONVERSATION
# =====================================================

elif menu == "💬 Generate Conversation":

    st.header("💬 Generate Conversation")

    event = st.text_input("Event")

    interest = st.text_input("Interest")

    if st.button("🚀 Generate Conversation"):

        if event == "" or interest == "":
            st.warning("Please enter both Event and Interest.")

        else:

            with st.spinner("Generating conversation..."):

                try:

                    response = requests.post(
                        f"{BASE_URL}/generate",
                        json={
                            "event": event,
                            "interest": interest
                        }
                    )

                    if response.status_code == 200:

                        conversations = response.json()["conversation"]

                        st.success("Conversation Generated Successfully")

                        for item in conversations:

                            st.markdown(
                                f"""
<div class="feature-card">
✅ {item}
</div>
""",
                                unsafe_allow_html=True,
                            )

                    else:

                        st.error("Backend Error")

                        st.code(response.text)

                except Exception as e:

                    st.error(str(e))

# =====================================================
# THEME EXTRACTION
# =====================================================

elif menu == "🧠 Theme Extraction":

    st.header("🧠 Theme Extraction")

    event = st.text_area("Event Description")

    if st.button("Extract Themes"):

        if event == "":
            st.warning("Please enter an event description.")

        else:

            response = requests.post(
                f"{BASE_URL}/extract-theme",
                json={
                    "event": event
                }
            )

            if response.status_code == 200:

                st.success("Themes Found")

                themes = response.json()["themes"]

                if len(themes) == 0:

                    st.info("No themes found.")

                else:

                    for theme in themes:

                        st.markdown(
                            f"""
<div class="feature-card">
✅ {theme}
</div>
""",
                            unsafe_allow_html=True,
                        )

            else:

                st.error(response.text)

# =====================================================
# FACT CHECKER
# =====================================================

elif menu == "📖 Fact Checker":

    st.header("📖 Wikipedia Fact Checker")

    topic = st.text_input("Topic")

    if st.button("Search"):

        if topic == "":
            st.warning("Please enter a topic.")

        else:

            response = requests.get(
                f"{BASE_URL}/fact",
                params={
                    "topic": topic
                }
            )

            if response.status_code == 200:

                st.success("Summary")

                st.write(response.json()["summary"])

            else:

                st.error(response.text)

# =====================================================
# HISTORY
# =====================================================

elif menu == "📜 History":

    st.header("📜 Conversation History")

    response = requests.get(f"{BASE_URL}/history")

    if response.status_code == 200:

        history = response.json()

        if len(history) == 0:

            st.info("No history found.")

        else:

            for item in history:

                with st.expander(f"📅 {item['event']}"):

                    st.write("### Interest")
                    st.write(item["interest"])

                    st.write("### Conversation")
                    st.text(item["response"])

                    st.write("### Created At")
                    st.write(item["created_at"])

    else:

        st.error(response.text)

# =====================================================
# ABOUT
# =====================================================

elif menu == "ℹ️ About":

    st.header("ℹ️ About Project")

    st.markdown("""
### Personalized Networking Assistant

An AI-powered web application that helps users generate professional networking conversation starters.

### Technologies Used

- Python
- FastAPI
- Streamlit
- SQLite
- SQLAlchemy
- Google Gemini AI
- Transformers
- REST APIs

### Developed By

**SIVA SANKAR REDDY**

B.Tech (CSE(IoT and Automation)

2027 Batch
""")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    """
<div class="footer">
Developed by <b>Siva Sankar Reddy</b><br>
Personalized Networking Assistant • FastAPI • Streamlit • Gemini AI
</div>
""",
    unsafe_allow_html=True,
)
