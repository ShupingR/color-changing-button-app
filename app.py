import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Color Changing Button",
    page_icon="🎨",
    layout="centered"
)

# Initialize session state for button color
if 'button_color' not in st.session_state:
    st.session_state.button_color = "#FF6B6B"  # Default red color

# Title and description
st.title("🎨 Color Changing Button")
st.markdown("Click the button below to see it change colors!")

# Function to change button color
def change_color():
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD", "#98D8C8", "#F7DC6F"]
    st.session_state.button_color = random.choice(colors)

# Create the button with dynamic styling
button_style = f"""
<style>
.stButton > button {{
    background-color: {st.session_state.button_color};
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 18px;
    border-radius: 10px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}}

.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.3);
}}
</style>
"""

st.markdown(button_style, unsafe_allow_html=True)

# Center the button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Click Me!", key="color_button", on_click=change_color):
        pass

# Display current color info
st.markdown("---")
st.markdown(f"**Current Color:** {st.session_state.button_color}")
st.markdown("**Click count:** " + str(st.session_state.get('click_count', 0)))

# Update click count
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

# Footer
st.markdown("---")
st.markdown("*Deployed with Streamlit Cloud*") 