from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple, List, Optional
import numpy as np
import pandas as pd


@dataclass
class FixationDetectionConfig:
    sampling_rate: float = 60.0


    #I-VT configuration
    ivt_velocity_threshold: float = 30.0
    ivt_upper_saccade_threshold: float = 1000.0
    ivt_fixation_threshold: float = 30.0
    ivt_use_filter: bool = True

    #I-DT configuration
    idt_dispersion_threshold: float = 1.0
    idt_min_duration: int = 100


    #window based processing
    window_duration: float = 60.0


@dataclass
class FixationData:
    fixation_id: int
    start_idx: int
    end_idx: int
    indices: List[int]
    centroid: Tuple[float, float, float]
    duration: float
    num_samples: int



@dataclass
class SaccadeData:
    source_fixation_id: int
    target_fixation_id: int
    amplitude: float
    duration: float
    peak_velocity: float



@dataclass
class GraphWindow:
    window_id: int
    start_time: float
    end_time: float
    fms_score: Optional[float]
    num_fixations: int
    num_saccades: int



class FixationDetectionStrategy(ABC):
    def __init__(self, config: FixationDetectionConfig):
        self.config = config
    
    @abstractmethod
    def detect_fixation(self, gaze_data: np.ndarray, timestamps: np.ndarray) -> List[FixationData]:
        pass

    @abstractmethod
    def get_algorithm_name(self) -> str:
        pass

    