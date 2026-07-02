import os
import re
from datetime import datetime
from scipy.io import loadmat

def load_wt_hss_data(file_path, filecount, metadata_only=True):
    filename = os.path.basename(file_path)
    match = re.search(r'data-(\d{8}T\d{6})Z\.mat', filename)
    if not match:
        return None
    dt = datetime.strptime(match.group(1), "%Y%m%dT%H%M%S")
    return {
        'datetime': dt,
        'sampling_frequency': 97656,
        'file_index': filecount,
        'time_in_days': filecount,
    }

def load_data(datafile, dataset_type, filecount, **kwargs):
    if dataset_type == 'WT-HSS':
        return load_wt_hss_data(datafile, filecount)
    raise ValueError(f"Dataset {dataset_type} not supported")