import base64
import os
from dotenv import load_dotenv
from mimetypes import guess_type
from openai import AzureOpenAI

load_dotenv()

# Azure OpenAI environment variables
aoai_endpoint = os.getenv("AOAI_ENDPOINT")
aoai_api_key = os.getenv("AOAI_API_KEY")
aoai_deployment_name = os.getenv("AOAI_DEPLOYMENT")

# Set the path to the image file
image_path = "2024_Work_Trend_Index_Annual_Report.png"

# Initialize the AzureOpenAI client  
client = AzureOpenAI(  
    azure_endpoint=aoai_endpoint,  
    api_key=aoai_api_key, 
    api_version="2024-08-01-preview"  
)  

def local_image_to_data_url(image_path):
    """
    Convert a local image file to a data URL.

    Parameters:
    -----------
    image_path : str
        The path to the local image file to be converted.

    Returns:
    --------
    str
        A data URL representing the image, suitable for embedding in HTML or other web contexts.
    """
    # Get mime type
    mime_type, _ = guess_type(image_path)

    if mime_type is None:
        mime_type = 'application/octet-stream'

    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(
            image_file.read()).decode('utf-8')

    return f"data:{mime_type};base64,{base64_encoded_data}"


# data url
data_url = local_image_to_data_url(image_path)

response = client.chat.completions.create(
    model=aoai_deployment_name,
    messages=[{
        "role": "system",
        "content": "You are an AI helpful assistant."
    }, {
        "role":
        "user",
        "content": [{
            "type": "text",
            "text": "Extract the text from this image:"
        }, {
            "type": "image_url",
            "image_url": {
                "url": data_url
            }
        }]
    }],
    max_tokens=4000,
    temperature=0.7)

# result
img_description = response.choices[0].message.content

print("Image Description: ", img_description)
