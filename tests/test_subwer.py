"""
Tests for the subwer package.
"""
import pytest
from subwer import wer, cer
from subwer.normalizer import Normalizer
import os

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
REF_PATH = os.path.join(TEST_DIR, "reference.srt")
HYP_PATH = os.path.join(TEST_DIR, "hypothesis.srt")

def test_normalizer():
    """Test the normalizer functionality."""
    text1 = "Hello, World!"
    text2 = "hello world"
    
    assert Normalizer.normalize(text1) == Normalizer.normalize(text2)

def test_wer_with_normalization():
    """Test WER calculation with normalization."""
    result = wer(REF_PATH, HYP_PATH, normalize=True)
    
    assert 0 < result < 0.2 

def test_wer_without_normalization():
    """Test WER calculation without normalization."""
    # w/o normalization
    result = wer(REF_PATH, HYP_PATH, normalize=False)
    assert result > 0

    # w/ normalization
    norm_result = wer(REF_PATH, HYP_PATH, normalize=True)
    assert result >= norm_result

def test_cer_with_normalization():
    """Test CER calculation with normalization."""
    result = cer(REF_PATH, HYP_PATH, normalize=True)
    
    assert 0 < result < 0.1
