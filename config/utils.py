# utils.py
from typing import List, Tuple, Dict

def validate_file_path(file_path: str) -> bool:
    """Validate if a file path exists and is accessible."""
    import os
    return os.path.isfile(file_path)

def read_file(file_path: str) -> List[str]:
    """Read the contents of a file into a list of lines."""
    if not validate_file_path(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except Exception as e:
        raise Exception(f"Failed to read file: {e}")

def split_string_into_lines(input_string: str) -> List[str]:
    """Split a string into a list of lines."""
    return input_string.split('\n')

def merge_lists(list1: List[str], list2: List[str]) -> List[str]:
    """Merge two lists into one."""
    return list1 + list2

def get_unique_elements(collection: List[str]) -> List[str]:
    """Remove duplicates from a list."""
    return list(set(collection))

def remove_empty_lines(lines: List[str]) -> List[str]:
    """Remove empty lines from a list."""
    return [line for line in lines if line.strip()]

def split_on_comma(collection: List[str]) -> List[Tuple[str, str]]:
    """Split a list of strings into pairs based on comma."""
    return [line.split(',') for line in collection]

def format_json(json_string: str) -> Dict[str, str]:
    """Parse a JSON string into a dictionary."""
    import json
    return json.loads(json_string)