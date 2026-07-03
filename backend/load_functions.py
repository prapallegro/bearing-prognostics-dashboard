import os
import re
from datetime import datetime, timedelta
from scipy.io import loadmat

# ----------------------------------------------------------------------
# Loader for WT-HSS (MAT)
# ----------------------------------------------------------------------
def load_wt_hss_data(file_path, filecount, metadata_only=True):
    filename = os.path.basename(file_path)
    match = re.search(r'data-(\d{8}T\d{6})Z\.mat', filename)
    if not match:
        return None
    dt = datetime.strptime(match.group(1), "%Y%m%dT%H%M%S")
    sampling_frequency = 97656
    time_in_days = filecount   # one file per day

    result = {
        'datetime': dt,
        'sampling_frequency': sampling_frequency,
        'file_index': filecount,
        'time_in_days': time_in_days,
    }

    # For now, only metadata (full signal loading postponed)
    # TODO: Enable full vibration loading in v0.2.0 when vibration plot tab is ready.
    return result

# ----------------------------------------------------------------------
# Loader for XJTU-SY (CSV)
# ----------------------------------------------------------------------
def load_xjtu_sy_data(file_path, filecount, metadata_only=True):
    sampling_frequency = 25600
    start_time = datetime(2019, 1, 31, 9, 50, 0)
    dt = start_time + timedelta(minutes=filecount)
    time_in_days = filecount / 1440.0

    result = {
        'datetime': dt,
        'sampling_frequency': sampling_frequency,
        'file_index': filecount,
        'time_in_days': time_in_days,
    }

    # For now, only metadata (full signal loading postponed)
    # TODO: Enable full vibration loading in v0.2.0 when vibration plot tab is ready.

    return result

# ----------------------------------------------------------------------
# Generic entry point (initial: WT-HSS and XJTU-SY)
# ----------------------------------------------------------------------
def load_data(datafile, dataset_type, filecount, metadata_only=True, **kwargs):
    """
    Main entry point: routes to the appropriate loader based on dataset_type.
    """
    if dataset_type == 'WT-HSS':
        return load_wt_hss_data(datafile, filecount, metadata_only=metadata_only)
    elif dataset_type == 'XJTU-SY':
        return load_xjtu_sy_data(datafile, filecount, metadata_only=metadata_only)
    else:
        raise ValueError(f"Dataset type {dataset_type} not yet supported")