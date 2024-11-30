import google.generativeai as genai
from PIL import Image

# Initialize the Google Generative AI model
api_key = "Enter Your API Key"  # Replace with your actual API key
genai.configure(api_key=api_key)

def generate_task_assistance(input_prompt, image_data):
    """Generates task assistance using Google Generative AI."""
    try:
        # Initialize the Generative Model (using the correct model)
        model = genai.GenerativeModel("gemini-1.5-pro")  

        # Generate the task assistance based on the prompt and image data
        response = model.generate_content([input_prompt, image_data[0]])

        # Return the generated  assistance text
        return response.text.strip() 

    except Exception as e:
        return f"Error: {str(e)}"

def provide_task_assistance(image_file):
    try:
        # Open the image file for processing
        image = Image.open(image_file)

        # Convert image to appropriate data format for the API (base64 or raw bytes depending on requirements)
        image_data = [image]  
        # Prepare the prompt for generating task assistance
        prompt = "Assist with the task depicted in this image for a visually impaired person."

        # Generate task assistance using the new method
        task_assistance = generate_task_assistance(prompt, image_data)

        return task_assistance

    except Exception as e:
        return f"Error: {str(e)}"
