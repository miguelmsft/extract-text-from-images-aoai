# Extracting Information from Images using Azure OpenAI GPT-4o  
   
This repository contains code and examples demonstrating how to extract information from images using the Azure OpenAI GPT-4o model. You can specify the information or questions you want to extract, and the model can return the results in a structured format such as JSON.  
   
## Table of Contents  
   
- [Overview](#overview)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Setup](#setup)  
- [Usage](#usage)  
  - [Extract Text from Images](#extract-text-from-images)  
  - [Answer Questions from Image Content](#answer-questions-from-image-content)  
  - [Extract Structured Data](#extract-structured-data)  
- [Files](#files)  
- [License](#license)  
   
## Overview  
   
This repository leverages Azure's OpenAI GPT-4o model to:  
   
- Describe images in detail.  
- Extract text content directly from images.  
- Answer specific questions based on the content of images.  
- Extract answers in structured formats like JSON for easy integration into applications.  
   
## Features  
   
- **Flexible Information Extraction**: Specify exactly what information you want to extract from an image.  
- **Structured Output**: Receive outputs in structured formats such as JSON for seamless data handling.  
- **Interactive Notebook and Script**: Use the Jupyter notebook for step-by-step execution or the script for quick runs.  
- **Azure OpenAI Integration**: Leverage the powerful GPT-4o model hosted on Azure for robust image understanding.  
   
## Prerequisites  
   
- Python 3.7 or higher  
- Azure OpenAI Service access with GPT-4o model deployed  
- Required Python packages:  
  - `openai`  
  - `pydantic`  
  - `python-dotenv`  
- An Azure account with proper permissions to use the OpenAI service  
- Image file(s) you wish to analyze  
   
## Setup  
   
1. **Clone the Repository**  
  
   ```bash  
   git clone https://github.com/yourusername/your-repo-name.git  
   cd your-repo-name  
   ```  
   
2. **Install Dependencies**  
  
   It's recommended to use a virtual environment.  
  
   ```bash  
   pip install -r requirements.txt  
   ```  
   
3. **Configure Environment Variables**  
  
   Create a `.env` file in the root directory and add your Azure OpenAI credentials:  
  
   ```env  
   AOAI_ENDPOINT=your_azure_openai_endpoint  
   AOAI_API_KEY=your_azure_openai_api_key  
   AOAI_DEPLOYMENT=your_azure_openai_deployment_name  
   ```  
   
## Usage  
   
### Extract Text from Images  
   
Use the `extract_text.py` script to extract and print a description of an image.  
   
```bash  
python extract_text.py  
```  
   
**Note**: Ensure you've set the `image_path` variable in the script to point to your target image.  
   
### Answer Questions from Image Content  
   
In the `extract_text.ipynb` notebook, you can specify prompts to extract specific information.  
   
#### Example: Describe the Image  
   
```python  
prompt = "Describe this image:"  
call_azure_openai(prompt, image_data_url)  
```  
   
#### Example: Extract Text Content  
   
```python  
prompt = "Extract the text from this image:"  
call_azure_openai(prompt, image_data_url)  
```  
   
### Extract Structured Data  
   
You can define a structured output format using `pydantic` models.  
   
#### Example: Extract Specific Answers  
   
```python  
prompt = """Based on this image, answer the questions:  
            1) What percentage of knowledge workers around the world use generative AI at work?  
            2) What percentage of leaders believe their company needs to adopt AI to stay competitive?"""  
   
# Define output format  
class ExtractedAnswers(BaseModel):  
    PctWorkersAI: int  
    PctLeadersAI: int  
   
call_azure_openai(prompt, image_data_url, response_format=ExtractedAnswers)  
```  
   
The model will return a JSON object with the specified fields:  
   
```json  
{  
  "PctWorkersAI": 75,  
  "PctLeadersAI": 79  
}  
```  
   
## Files  
   
- `extract_text.ipynb`: Jupyter notebook with step-by-step examples and explanations.  
- `extract_text.py`: Standalone script to extract text from an image and print the description.  
- `requirements.txt`: List of Python dependencies.  
   
## License  
   
This project is licensed under the [MIT License](LICENSE).  
   
---  
   
Feel free to contribute by opening issues or submitting pull requests.