import streamlit as st
from PIL import Image
from scene_understanding import describe_scene
from text_to_speech import convert_text_to_speech
from object_detection import detect_objects
from personalized_assistance import provide_task_assistance


st.set_page_config(
    page_title="AssistAI - Internship Project",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header Section
st.title("🚀 AssistAI: A Generative AI Solution for Accessibility🧑‍🦯")
st.subheader("**Final Project for My Internship at Innomatics Research Labs💼**")
st.caption("Supervised by: **Kanav Bansal** 👨‍🏫")
st.write("👁️‍🗨️ Designed to empower visually impaired individuals with real-time scene understanding, text-to-speech capabilities, object detection, and personalized assistance.")

st.sidebar.title("🌟 Welcome to AssistAI")

logo_path = "C:/Users/parmo/Downloads/logo.jpg"
img = Image.open(logo_path)
width, height = img.size  
st.sidebar.image(logo_path, width=200,use_column_width=False) 

# Adding Custom CSS for Centering the Logo
st.sidebar.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;  /* Align content to the top */
            align-items: center;  /* Center align the content horizontally */
        }
        .sidebar img {
            align-self: center;  /* Center align the logo */
            width: 200px;  /* Set the logo width */
            height: auto;  /* Maintain aspect ratio */
        }
    </style>
    """, unsafe_allow_html=True
)

# Project Overview Sidebar
st.sidebar.markdown("""
### Empowering Accessibility through Innovation
AssistAI is designed to enhance the daily lives of visually impaired individuals, leveraging state-of-the-art Generative AI technologies for intuitive scene understanding, speech feedback, and personalized assistance.
""")

st.sidebar.subheader("✨ Key Features")
st.sidebar.markdown("""
- 🖼️ **Real-Time Scene Understanding**: Generate descriptive, context-rich text based on the uploaded image to help users understand their environment.
- 🗣️ **Text-to-Speech Conversion**: Seamlessly convert descriptive text into clear, natural-sounding speech for auditory feedback.
- 🔍 **Object & Obstacle Detection**: Identify objects and potential obstacles within images to assist with navigation and situational awareness.
- 🛠️ **Personalized Assistance**: Provide tailored guidance to users for everyday tasks such as item recognition and contextual instructions.
""")


st.sidebar.subheader("🔧 Powered by")
st.sidebar.markdown("""
- 🚀 **Streamlit**: A powerful framework for creating fast, interactive applications.
- 🤖 **Google Generative AI**: State-of-the-art generative AI models for natural language understanding and generation.
- 🖹 **Tesseract OCR**: A reliable open-source tool for accurate text extraction from images.
- 🔗 **LangChain**: A versatile library for managing language model chains and data flows.
""")

st.sidebar.subheader("🛠️ How to Use")
st.sidebar.markdown("""
1. 📂 **Upload an Image**: Use the main interface to upload an image for analysis.
2. ▶️ **Run the Task**: Click on the respective button to execute the selected task.
3. 👀 **View Results**: Outputs will be displayed sequentially in the main interface.
""")
st.sidebar.subheader("🔍 About AssistAI")
st.sidebar.markdown("""
Developed during my internship at **Innomatics Research Labs**, **AssistAI** leverages cutting-edge AI technologies to empower visually impaired individuals, making their daily interactions with the world more accessible and seamless.
""")

# Innomatics Research Labs Link
st.sidebar.markdown("[🔗 Visit Innomatics Research Labs](https://www.innomatics.in)")

st.sidebar.markdown("---")
st.sidebar.markdown("💡 *Driven by the mission to make accessibility a reality for everyone.*")

# Initialize session state to store uploaded image and outputs
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None
if "scene_description" not in st.session_state:
    st.session_state.scene_description = None
if "audio_path" not in st.session_state:
    st.session_state.audio_path = None
if "detected_image_path" not in st.session_state:
    st.session_state.detected_image_path = None
if "task_assistance" not in st.session_state:
    st.session_state.task_assistance = None


# Image Upload Section
st.header("🖼️ Upload an Image")
image_file = st.file_uploader("📤 Upload an image:", type=["jpg", "jpeg", "png"])

# Handle image input
if image_file:
    st.session_state.uploaded_image = image_file

# Proceed with the tasks only if an image is available
if st.session_state.uploaded_image:
    st.image(st.session_state.uploaded_image, caption="Uploaded Image 📸", use_container_width=True)  
else:
    st.warning("⚠️ Please upload an image to proceed.")


# Custom CSS for unique design and hover effects
st.markdown("""
    <style>
        /* Apply a background color to the task blocks */
        .task-block {
            background-color: #f0f0f5;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        /* Hover effect for task blocks */
        .task-block:hover {
            background-color: #e1e1f1;
            box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.15);
        }

        /* Style the task titles */
        .task-title {
            font-size: 1.5rem;
            font-weight: bold;
            color: #3A3A3A;
            margin-bottom: 10px;
        }

        /* Style for task descriptions */
        .task-description {
            font-size: 1rem;
            color: #555555;
            margin-bottom: 15px;
        }

        /* Add a custom border and shadow to images */
        .task-image img {
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Style for the buttons */
        .task-button {
            background-color: #5C6BC0;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }

        /* Hover effect for buttons */
        .task-button:hover {
            background-color: #3F51B5;
        }
    </style>
""", unsafe_allow_html=True)

# Task Execution Section
st.header("🛠️ Task Execution Section")
st.markdown("""
### Perform tasks to analyze the uploaded image:
""")

# Create a 2x2 grid using columns
col1, col2 = st.columns(2)  
col3, col4 = st.columns(2) 

# Task 1: Describe the Scene
with col1:
    st.markdown('<div class="task-block">', unsafe_allow_html=True)
    st.markdown('<div class="task-title">🧐 Describe the Scene</div>', unsafe_allow_html=True)
    st.markdown('<div class="task-description">Generate a textual understanding of the uploaded image.</div>', unsafe_allow_html=True)
    if st.button("Describe Scene", key="describe_scene", use_container_width=True):
        if st.session_state.uploaded_image:
            st.session_state.scene_description = describe_scene(st.session_state.uploaded_image)
            st.success("✅ Scene described successfully!")
            st.markdown(f"**Output:** {st.session_state.scene_description}")
        else:
            st.warning("⚠️ Please upload or capture an image first.")
    st.markdown('</div>', unsafe_allow_html=True)

# Task 2: Convert Text to Speech
with col2:
    st.markdown('<div class="task-block">', unsafe_allow_html=True)
    st.markdown('<div class="task-title">🗣️ Convert Text to Speech</div>', unsafe_allow_html=True)
    st.markdown('<div class="task-description">Convert the scene description into an audio format.</div>', unsafe_allow_html=True)
    if st.button("Convert to Speech", key="convert_speech", use_container_width=True):
        if st.session_state.scene_description:
            st.session_state.audio_path = convert_text_to_speech(st.session_state.scene_description)
            st.success("✅ Text converted to speech!")
            st.audio(st.session_state.audio_path, format="audio/mp3")
        else:
            st.warning("⚠️ Please describe the scene first.")
    st.markdown('</div>', unsafe_allow_html=True)

# Task 3: Detect Objects and Obstacles
with col3:
    st.markdown('<div class="task-block">', unsafe_allow_html=True)
    st.markdown('<div class="task-title">🔍 Detect Objects and Obstacles</div>', unsafe_allow_html=True)
    st.markdown('<div class="task-description">Identify objects and potential obstacles in the image.</div>', unsafe_allow_html=True)
    if st.button("Detect Objects", key="detect_objects", use_container_width=True):
        if st.session_state.uploaded_image:
            st.session_state.detected_image_path = detect_objects(st.session_state.uploaded_image)
            st.success("✅ Objects detected successfully!")
            st.image(st.session_state.detected_image_path, caption="Objects Detected 🛑", use_container_width=True)
        else:
            st.warning("⚠️ Please upload or capture an image first.")
    st.markdown('</div>', unsafe_allow_html=True)

# Task 4: Personalized Task Assistance
with col4:
    st.markdown('<div class="task-block">', unsafe_allow_html=True)
    st.markdown('<div class="task-title">🛠️ Personalized Assistance</div>', unsafe_allow_html=True)
    st.markdown('<div class="task-description">Get task-specific guidance based on detected objects.</div>', unsafe_allow_html=True)
    if st.button("Get Assistance", key="get_assistance", use_container_width=True):
        if st.session_state.detected_image_path:
            st.session_state.task_assistance = provide_task_assistance(st.session_state.detected_image_path)
            st.success("✅ Personalized assistance generated successfully!")
            st.markdown(f"**Guidance:** {st.session_state.task_assistance}")
        else:
            st.warning("⚠️ Please detect objects first.")
    st.markdown('</div>', unsafe_allow_html=True)


# Display all outputs sequentially
st.header("📋 Output Section")
if st.session_state.scene_description:
    st.markdown(f"**Scene Description:** {st.session_state.scene_description} 🖼️")
    
if st.session_state.audio_path:
    st.audio(st.session_state.audio_path, format="audio/mp3")
    st.success("✅ Text has been successfully converted to speech!")
    
if st.session_state.detected_image_path:
    st.image(st.session_state.detected_image_path, caption="Objects Detected 🛑", use_container_width=True)
    
if st.session_state.task_assistance:
    st.markdown(f"**Task Guidance:** {st.session_state.task_assistance} ✅")


