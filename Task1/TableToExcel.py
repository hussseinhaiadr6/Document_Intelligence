import os
import wget
import subprocess
from variables import get_path
# Navigate to the desired directory (assuming you're in the working directory where you want the script to run)
"""
# Create the "inference" directory
os.makedirs("C:/Users/HHR6/PycharmProjects/Task1/inference", exist_ok=True)  # Create directory only if it doesn't exist

# Download the PP-OCRv3 text detection model
model_url = "https://paddleocr.bj.bcebos.com/dygraph_v2.0/table/en_ppocr_mobile_v2.0_table_det_infer.tar"
download_path = os.path.join("inference", "en_ppocr_mobile_v2.0_table_det_infer.tar")
wget.download(model_url, download_path)

# Unzip the downloaded model
os.system("tar -xf " + download_path)  # Use system call for tar extraction

# Download the PP-OCRv3 text recognition model
model_url = "https://paddleocr.bj.bcebos.com/PP-OCRv3/chinese/ch_PP-OCRv3_rec_infer.tar"
download_path = os.path.join("inference", "ch_PP-OCRv3_rec_infer.tar")
wget.download(model_url, download_path)

# Unzip the downloaded model
os.system("tar -xf " + download_path)

# Download the PP-StructureV2 form recognition model
model_url = "https://paddleocr.bj.bcebos.com/dygraph_v2.0/table/en_ppocr_mobile_v2.0_table_structure_infer.tar"
download_path = os.path.join("inference", "en_ppocr_mobile_v2.0_table_structure_infer.tar")
wget.download(model_url, download_path)

# Unzip the downloaded model
os.system("tar -xf " + download_path)
"""
# You can replace the placeholder "# run" with your actual code for using the downloaded models
#print("Downloaded and unzipped the models. Now you can proceed with using them in your code.")
root=get_path()
def process_directory(directory):
    """Processes a single directory containing images using PaddleOCR for table detection and recognition.

    Args:
        directory (str): The path to the directory containing images.
    """

    det_model_dir = f"{root}/Task1/en_ppocr_mobile_v2.0_table_det_infer"
    rec_model_dir = f"{root}Task1/ch_PP-OCRv3_rec_infer"
    table_model_dir = f"{root}Task1/en_ppocr_mobile_v2.0_table_structure_infer"
    rec_char_dict_path = f"{root}Task1/PaddleOCR/ppocr/utils/ppocr_keys_v1.txt"
    table_char_dict_path = f"{root}Task1/PaddleOCR/ppocr/utils/dict/table_structure_dict.txt"
    image_dir = directory
    #output_name=directory.split("\\")[0].split("/")[-1]
    output_name = directory.split("\\")[1]
    print(output_name)
    output_dir = f"{root}/Task1/Output/{output_name}"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)  # Handle pre-existing directories gracefully

    # Construct the command with string formatting for flexibility
    command = f""" python C:/Users/HHR6/PycharmProjects/Task1/PaddleOCR/ppstructure/table/predict_table.py --det_model_dir={det_model_dir} --rec_model_dir={rec_model_dir} --table_model_dir={table_model_dir} --rec_char_dict_path={rec_char_dict_path}  --table_char_dict_path={table_char_dict_path}  --image_dir={image_dir}  --merge_no_span_structure=False --output={output_dir} """
    #print(command)
    subprocess.run(command,shell=True)
    print("done")
