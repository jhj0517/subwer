import re

def read_srt(file_path):
    """
    Read an SRT subtitle file and extract the text.
    
    Args:
        file_path (str): Path to the SRT file
        
    Returns:
        str: Combined text from all subtitle entries
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove index and timestamp
    pattern = r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n'
    cleaned_content = re.sub(pattern, '', content)
    
    # Remove line breaks
    cleaned_content = re.sub(r'\n+', ' ', cleaned_content)
    
    # Replace multiple spaces with a single space
    cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip()
    
    return cleaned_content 