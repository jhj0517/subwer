import re
import string

class Normalizer:
    """
    Class for normalizing text before WER/CER calculation.
    """
    
    @staticmethod
    def normalize(text):
        """
        Normalize text by:
        - Converting to lowercase
        - Removing punctuation
        - Removing extra whitespace
        
        Args:
            text (str): Input text to normalize
            
        Returns:
            str: Normalized text
        """
        # Lowercase
        text = text.lower()
        
        # Remove special characters (w/ `string.punctuation`) from text
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text 