import google.generativeai as genai
from PIL import Image

# Initialize the Google Generative AI model
api_key = "Enter your API key"  # Replace with your actual API key
genai.configure(api_key=api_key)

def generate_scene_description(input_prompt, image_data):
    """Generates a scene description using Google Generative AI."""
    try:
        # Initialize the Generative Model
        model = genai.GenerativeModel("gemini-1.5-pro")  

        # Generate the scene description based on the input prompt and image data
        response = model.generate_content([input_prompt, image_data[0]])

        # Return the generated text description
        return response.text.strip()  

    except Exception as e:
        return f"Error: {str(e)}"

def describe_scene(image_file):
    try:
        # Open the image file (for processing)
        image = Image.open(image_file)

        # Use OCR to extract text from the image or pass the image data to the model
        image_data = [image]  
        input_prompt = "Describe this image scene for a visually impaired person."

        # Generate the scene description using the new method
        description = generate_scene_description(input_prompt, image_data)

        return description

    except Exception as e:
        return f"Error: {str(e)}"
