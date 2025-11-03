#Test file for running and debugging
import os
from scripts.fms_processor import parse_fms_file


fms_file_path = os.path.join("eye_tracking_processor","Data", "Participant001", "Participant001_fms.txt")

fms_values = parse_fms_file(fms_file_path=fms_file_path)

print(fms_values[:14])

