import numpy as np
import pandas as pd
from typing import Callable, Generator, Tuple
import logging

#### My From Scratch Interpolation Using Numpy #####
# logging.basicConfig(level=logging.ERROR)

def look_ahead_behind_gen(iterable: np.ndarray) -> Generator[Tuple[int, int, int], None, None]:
    """Generator that iterates over an array while keeping track of the previous, current, and next elements."""
    iterator = iter(iterable)
    prev_val = None
    curr_val = next(iterator)
    for next_val in iterator:
        yield prev_val, curr_val, next_val
        prev_val, curr_val = curr_val, next_val
    yield prev_val, curr_val, None

def linear(X: np.ndarray, start_point: np.ndarray, end_point: np.ndarray) -> np.ndarray:
    """Linear interpolation function."""
    X[:, 1] = (X[:, 1] - start_point[0]) * ((end_point[1] - start_point[1]) / (end_point[0] - start_point[0])) + start_point[1]
    return X

def interpolate(vals: np.ndarray, f: Callable) -> np.ndarray:
    """Interpolates missing values in the array using a specified function."""
    segments = np.empty((0, 2))
    start_point, end_point = np.array([np.nan, np.nan]), np.array([np.nan, np.nan])
    segment = np.empty((0, 2))

    for prev_idx, cur_idx, next_idx in look_ahead_behind_gen(range(len(vals))):
        if np.isnan(vals[cur_idx]):
            new_row = np.array([[cur_idx, cur_idx]])
            segment = np.vstack((segment, new_row))
            
            if np.isnan(start_point).any() and np.isnan(end_point).any():
                start_point = np.array([prev_idx, vals[prev_idx]])   

            if not np.isnan(vals[next_idx]):
                end_point = np.array([next_idx, vals[next_idx]])

            if not np.isnan(end_point).any():
                segments = np.vstack((segments, f(segment, start_point, end_point)))
                start_point, end_point = np.array([np.nan, np.nan]), np.array([np.nan, np.nan])
                segment = np.empty((0, 2))
    return segments

def imputer(to_be_imputed: np.ndarray, imputation_strategy: Callable, interpolation_func: Callable) -> np.ndarray:
    """Imputes missing values in an array using a specified interpolation strategy."""
    if np.isnan(to_be_imputed[0]) or np.isnan(to_be_imputed[-1]):
        logging.error('The first and last elements of the array to be imputed cannot be np.nan')
        raise ValueError('The first and last elements of the array to be imputed cannot be np.nan')
    
    interpolated_segments = imputation_strategy(to_be_imputed, interpolation_func)

    for segment in interpolated_segments:
        idx, interpolated_val = int(segment[0]), segment[1]
        to_be_imputed[idx] = interpolated_val
    return to_be_imputed

# Test
vals = np.array([0, 1, 2, np.nan, np.nan, 7, 8, np.nan, np.nan, 11, np.nan, 13])
imputed_vals = imputer(vals, interpolate, interpolation_func = linear)
print(imputed_vals)

# Test 2
print("Test two!")
vals_2 = np.array([7, np.nan, 11, np.nan, np.nan, 13])
imputed_vals_2 = imputer(vals_2, interpolate, interpolation_func=linear)
print(imputed_vals_2)
