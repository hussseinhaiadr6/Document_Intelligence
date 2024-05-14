# Document_Intelligence
Pipeline to transform PDF and extract all table detected in the PDF to Excel Format : Object Detection , OCR , table recognition , Document scripting
# Document Intelligence

This project provides tools for intelligent document processing.

Prerequisites
Git: To clone the repository, you'll need Git installed on your system. You can download it from https://git-scm.com/downloads.
Python 3.9: Ensure you have Python 3.9 installed. If not, download it from https://www.python.org/downloads/.
Virtual Environment (Optional but Recommended): We recommend using a virtual environment to isolate project dependencies. Consider using venv or tools like virtualenv.
Setting Up the Environment
Clone the Repository:

Bash
git clone https://github.com/hussseinhaiadr6/Document_Intelligence.git
Use code with caution.
Create a Virtual Environment (Optional but Recommended):

Bash
python -m venv <path/to/your/virtual/environment>
Use code with caution.
Replace <path/to/your/virtual/environment> with your desired virtual environment path.

Activate the Virtual Environment:

Bash
source <path/to/your/virtual/environment>/bin/activate
Use code with caution.
(For Windows, replace source with venv\Scripts\activate)

Install Dependencies (if using a virtual environment):

Bash
pip install -r requirements.txt
Use code with caution.
Installing Python 3.9 in a Specific Location (if needed):

Refer to the official Python documentation for detailed instructions: https://www.python.org/downloads/

Project-Specific Setup
These steps require project-specific details and might differ from your setup.

PaddleOCR Integration:

The instructions mention replacing the paddleOCR directory and copying the Poppler file.
Follow the specific steps required for integrating PaddleOCR and Poppler with your project.
Input File Path: In Pipeline.py, update the variable holding the input file path with the correct location of your document.

Running the Script
Open a terminal or command prompt and navigate to the project directory.

If using a virtual environment, activate it first.

Run the script:

Bash
python Pipeline.py




Git clone  the repository 


extract the popppler zip file 


delete the paddle ocr foler and git clone the paddle OCR 


cretae a virtual env : virtualenv -p C:/Users/HHR6/AppData/Local/Programs/Python/Python39/python.exe C:/Users/HHR6/Desktop/Document-Intelligence/Document_Intelligence/Hussein



activate the environment   ./Scripts/activate 

chnage to python 3.9: virtualenv -p C:/Users/HHR6/AppData/Local/Programs/Python/Python39/python.exe C:/Users/HHR6/Desktop/TESTING CODE/husvenv


install the requirments 
pip install setuptools 


run the pipeline  from the terminal


note that if you have run th epiplie and some of the step were failed , and you havr to run the pipline again just comment the already executed and succeded code 
