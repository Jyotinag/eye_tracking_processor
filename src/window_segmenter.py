import pandas as pd
import numpy as np
from typing import List, Tuple, Optional
from .base import GraphWindow


#We want to segment the whole graph into 60s window. 
#The data can have more than 14 minutes per participant, we will process this in the main file

class WindowSegmenter:
    def __init__(self, window_duration: float = 60.0):
        self.window_duration = window_duration

    def segment_by_fixed_duration(self,
                       data_df: pd.DataFrame,
                       fms_df: Optional[pd.DataFrame] = None) -> List[Tuple[pd.DataFrame, GraphWindow]]:
        windows = []

        start_time = data_df['timestamps'].iloc[0]
        end_time = start_time + 8400000000 #taking only the first 14 minutes

        total_duration = (end_time-start_time)/ 1e7

        window_duration_us = self.window_duration * 1e7

        window_id = 0

        current_start = start_time

        while current_start < end_time:
            current_end = current_start + window_duration_us
            window_mask = (data_df['timestamps'] >= current_start) & (data_df['timestamps'] <= current_end)
            window_data = data_df[window_mask].copy()

            window_info = GraphWindow(
                window_id = window_id,
                start_time = current_start,
                end_time = current_end,
                num_fixations = 0,
                num_saccades = 0
            )

            windows.append(window_data, window_info)

            window_id += 1
            current_start = current_end
        return windows


