"""
Unit tests for the dataset loader registry.

These tests validate the routing logic and metadata extraction
without requiring real data files on disk.
"""

import pytest
from datetime import datetime
from backend.load_functions import DATASET_LOADERS, load_data


def test_registry_contains_expected_keys():
    """
    Ensure the registry contains the currently supported dataset types.
    
    Note: When adding a new dataset loader, update this list and add 
    corresponding tests. This is standard practice and ensures the 
    registry remains consistent with the implemented loaders.
    """
    expected = {'WT-HSS', 'XJTU-SY', 'PHM-2012'}
    assert set(DATASET_LOADERS.keys()) == expected


def test_registry_values_are_functions():
    """
    Every value in DATASET_LOADERS must be a callable function.
    """
    for dataset_type, loader in DATASET_LOADERS.items():
        assert callable(loader), f"Loader for {dataset_type} is not callable"


def test_load_data_routes_correct_loader():
    """
    Verify that load_data correctly routes to the appropriate loader
    based on dataset_type, returning metadata without reading files.
    
    Since metadata_only=True, the loaders parse filenames (WT-HSS)
    or calculate dates from filecount (XJTU-SY, PHM-2012) without 
    touching the disk. We can test the routing logic with dummy paths.
    """
    # 1. WT-HSS: Needs a dummy filename with the correct pattern
    dummy_path = "data-20230101T000000Z.mat"
    result_wt = load_data(dummy_path, "WT-HSS", 0, metadata_only=True)
    assert result_wt is not None
    assert result_wt['sampling_frequency'] == 97656
    assert result_wt['file_index'] == 0
    assert result_wt['datetime'] == datetime(2023, 1, 1, 0, 0, 0)
    
    # 2. XJTU-SY: Ignores file_path, uses filecount for time calculation
    result_xjtu = load_data("dummy_path", "XJTU-SY", 5, metadata_only=True)
    assert result_xjtu is not None
    assert result_xjtu['sampling_frequency'] == 25600
    assert result_xjtu['file_index'] == 5
    # 5 minutes after 2019-01-31 09:50:00
    expected_dt = datetime(2019, 1, 31, 9, 55, 0)
    assert result_xjtu['datetime'] == expected_dt
    
    # 3. PHM-2012: Ignores file_path, uses filecount for time calculation
    result_phm = load_data("dummy_path", "PHM-2012", 10, metadata_only=True)
    assert result_phm is not None
    assert result_phm['sampling_frequency'] == 25600
    assert result_phm['file_index'] == 10
    # 60 seconds (10 * 6) after 2012-01-27 00:00:00
    expected_dt = datetime(2012, 1, 27, 0, 1, 0)
    assert result_phm['datetime'] == expected_dt


def test_load_data_raises_error_on_unknown_dataset():
    """
    load_data() must raise a KeyError when dataset_type is not registered.
    """
    with pytest.raises(KeyError, match="Dataset type 'UNKNOWN' not registered"):
        load_data("dummy_path", "UNKNOWN", 0, metadata_only=True)