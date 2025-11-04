import pandas as pd
import numpy as np

#Load the raw file and return a pandas dataframe
def load_raw_eye(eye_tracking_file_path):
    eye_data = pd.read_csv(eye_tracking_file_path)

    #We are only keeping relevant eye tracking information for constructing the graph

    data = {
        'timestamp': eye_data['S0100_RecTime'].values,
        'gazedir_x': eye_data['V0300_Combine_GazeDir'].values,
        'gazedir_y': eye_data['V0301_Combine_GazeDir'].values,
        'gazedir_z': eye_data['V0302_Combine_GazeDir'].values,
        'gazepoint_x': eye_data['V0300_Combine_GazePoint'].values,
        'gazepoint_y': eye_data['V0301_Combine_GazePoint'].values,
        'gazepoint_z': eye_data['V0302_Combine_GazePoint'].values,
        'pupil_left': eye_data['S0100_Left_Diameter'].values,
        'pupil_right': eye_data['S0100_Right_Diameter'].values,
    }
    return pd.DataFrame(data)

