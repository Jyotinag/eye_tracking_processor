#Test file for running and debugging
import os
from scripts.fms_processor import parse_fms_file
from src.eye_tracking_processor import load_raw_eye


#####Checking if the FMS value extractor works

# fms_file_path = os.path.join("eye_tracking_processor","Data", "Participant001", "Participant001_fms.txt")

# fms_values = parse_fms_file(fms_file_path=fms_file_path)
## Only take first 14 values
# print(fms_values[:14])


#####Checking and debugging eye tracking files

raw_eye_path = os.path.join("Data", "Participant001", "Participant001_eye.csv")

data = load_raw_eye(raw_eye_path)
print(data)

