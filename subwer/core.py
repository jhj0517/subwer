from jiwer import wer as jiwer_wer, cer as jiwer_cer

from .subtitle_reader import read_srt
from .normalizer import Normalizer


def wer(reference_path, hypothesis_path, normalize=True):
    """
    Calculate the Word Error Rate (WER) between two subtitle files.
    
    Args:
        reference_path (str): Path to the reference subtitle file
        hypothesis_path (str): Path to the hypothesis subtitle file
        normalize (bool, optional): Whether to normalize text before comparison. Defaults to True.
        
    Returns:
        float: The Word Error Rate (WER) between the two subtitle files
    """
    reference_text = read_srt(reference_path)
    hypothesis_text = read_srt(hypothesis_path)
    
    if normalize:
        reference_text = Normalizer.normalize(reference_text)
        hypothesis_text = Normalizer.normalize(hypothesis_text)
    
    return jiwer_wer(reference_text, hypothesis_text)

def cer(reference_path, hypothesis_path, normalize=True):
    """
    Calculate the Character Error Rate (CER) between two subtitle files.
    
    Args:
        reference_path (str): Path to the reference subtitle file
        hypothesis_path (str): Path to the hypothesis subtitle file
        normalize (bool, optional): Whether to normalize text before comparison. Defaults to True.
        
    Returns:
        float: The Character Error Rate (CER) between the two subtitle files
    """
    reference_text = read_srt(reference_path)
    hypothesis_text = read_srt(hypothesis_path)
    
    if normalize:
        reference_text = Normalizer.normalize(reference_text)
        hypothesis_text = Normalizer.normalize(hypothesis_text)
    
    return jiwer_cer(reference_text, hypothesis_text) 