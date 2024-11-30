# 🚀 AssistAI: A Generative AI Solution for Accessibility 🧑‍🦯

AssistAI is an advanced Generative AI-powered solution designed to empower visually impaired individuals by enhancing their understanding and interaction with their surroundings. It leverages cutting-edge technologies to provide real-time scene understanding, text-to-speech conversion, object detection, and personalized task assistance.
![AssistAI App](https://github.com/Parmod2310/AssistAI-A-Generative-AI-Solution-for-Accessibility/blob/main/Screenshot%20%26%20Recording/143632.png)

---
## 📑 Table of Contents

1. [🚀 Features](#-features)
2. [🛠️ Tech Stack](#-tech-stack)
3. [📂 Dependencies](#-dependencies)
4. [🛠️ Configuration](#-configuration)
5. [💡 How It Works](#-how-it-works)
6. [📸 Screenshots & Recordings](#-screenshots--recordings)
7. [🔧 Setup and Installation](#-setup-and-installation)
8. [🗂️ Project Structure](#-project-structure)
9. [🌟 Future Improvements](#-future-improvements)
10. [🙏 Acknowledgements](#-acknowledgements)
11. [📄 License](#-license)
12. [📬 Contact](#-contact)

---



## 🚀 Features

- **🖼️ Real-Time Scene Understanding**:  
  Generate descriptive and context-rich text based on uploaded or captured images.

- **🗣️ Text-to-Speech Conversion**:  
  Convert scene descriptions into clear and natural-sounding speech for auditory feedback.

- **🔍 Object & Obstacle Detection**:  
  Identify and highlight objects or obstacles in images to improve navigation and situational awareness.

- **🛠️ Personalized Task Assistance**:  
  Provide tailored guidance based on detected objects for everyday tasks like recognizing items or reading labels.

---


## 🛠️ Tech Stack

- **Streamlit**: For creating a sleek, interactive user interface.
- **Google Generative AI**: To power natural language understanding and generation.
- **LangChain**: For managing language model workflows.
- **Tesseract OCR**: For optical character recognition.
- **Pillow (PIL)**: For image processing and manipulation.

---

## 📂 Dependencies

Key libraries and frameworks used in the project:

- `streamlit`
- `google-cloud-speech`
- `google-cloud-vision`
- `pillow`
- `pytesseract`
- `opencv-python`

---

## 🛠️ Configuration
- Update the **Google Cloud API Key** in the respective modules for accessing Google Cloud services.
- Verify the **Tesseract OCR** Path in your local environment.

---
## 💡 How It Works

1. **Upload or capture an image**:  
   The user provides an image as input, either by uploading a file or using a live camera.

2. **Perform tasks**:  
   - **Describe the Scene**: Generates a detailed text description of the image.  
   - **Convert to Speech**: Converts the generated text into speech for accessibility.  
   - **Object Detection**: Identifies and highlights objects or obstacles in the image.  
   - **Task Assistance**: Offers guidance based on the detected objects.

3. **Output**:  
   The results are displayed on the interface, including text, speech, or annotated images.

---

 ## 📸 Screenshots & Recordings

You can find additional screenshots and recordings for the AssistAI project in the following directory on [GitHub](https://github.com/Parmod2310/AssistAI-A-Generative-AI-Solution-for-Accessibility/tree/043c6777f31e2d0a43678be681d0cf41c8357e87/Screenshot%20%26%20Recording).

| Feature                     | Screenshot |
|-----------------------------|------------|
| **Real-Time Scene Understanding** | ![Scene Understanding](https://github.com/Parmod2310/AssistAI-A-Generative-AI-Solution-for-Accessibility/blob/main/Screenshot%20%26%20Recording/180758.png) |
| **Text-to-Speech Conversion**    | ![Text-to-Speech](https://github.com/Parmod2310/AssistAI-A-Generative-AI-Solution-for-Accessibility/blob/main/Screenshot%20%26%20Recording/180806.png) |
| **Object Detection**        | ![Object Detection](https://github.com/Parmod2310/AssistAI-A-Generative-AI-Solution-for-Accessibility/blob/main/Screenshot%20%26%20Recording/180821.png) |
| **Personalized Assistance**         | ![Personalized Assistance](https://github.com/Parmod2310/AssistAI-A-Generative-AI-Solution-for-Accessibility/blob/main/Screenshot%20%26%20Recording/180838.png) |

---
## 🔧 Setup and Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/AssistAI.git
    cd AssistAI
    ```

2. **Install dependencies**:
    Make sure you have Python installed. Then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Tesseract**:
    - Download and install Tesseract from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
    - Update the Tesseract path in your script (if necessary).

4. **Run the application**:
    ```bash
    streamlit run app.py
    ```

5. **Upload or capture an image**, and explore the features!

---
## 🗂️ Project Structure  
```plaintext
AssistAI/  
│  
├── app.py                      # Main application script  
├── scene_understanding.py      # Script for scene description functionality  
├── text_to_speech.py           # Script for text-to-speech conversion  
├── object_detection.py         # Script for object detection  
└── personalized_assistance.py  # Script for task-specific guidance
```
---

## 🌟 Future Improvements

- 🗣️ Voice Command Integration: Hands-free navigation.
- 📱 Mobile App Deployment: Accessible on smartphones.
- 🌐 Multi-language Support: Break language barriers.
- 🤖 Enhanced AI Models: Improve detection and descriptive accuracy.

---

## 🙏 Acknowledgements

This project was developed as the **Final Internship Project** at [Innomatics Research Labs](https://www.innomatics.in).  
Special thanks to **Kanav Bansal** for mentorship and guidance.

---

## 📄 License

This project is licensed under the MIT License.  
Feel free to use, modify, and distribute as per the terms of the license.

---

## 📬 Contact

If you have any questions, feel free to reach out:

- **Email**: p921035@gmail.com  
- **LinkedIn**: [Parmod's LinkedIn Profile](https://www.linkedin.com/in/parmod2310/)  
- **GitHub**: [Parmod's GitHub Profile](https://github.com/Parmod2310/)  

--- 

### Let’s make accessibility a reality for everyone! 🌟


