# subwer

A python package for calculating Word Error Rate (WER) and Character Error Rate (CER) between subtitle files.<br>
This uses [`jiwer`](https://github.com/jitsi/jiwer) to compare WER / CER.

## Installation

```bash
pip install subwer
```

## Usage
```python
from subwer import wer, cer

# Calculate WER between two subtitle files
reference_subtitle_path = "answer_subtitle.srt"
hypothesis_subtitle_path = "predicted_subtitle.srt"

# Calculate with default normalization (True by default)
wer_score = wer(reference_subtitle_path, hypothesis_subtitle_path)
cer_score = cer(reference_subtitle_path, hypothesis_subtitle_path)

print(f"WER: {wer_score}")
print(f"CER: {cer_score}")

# Calculate without normalization
wer_score_no_norm = wer(reference_subtitle_path, hypothesis_subtitle_path, normalize=False)
cer_score_no_norm = cer(reference_subtitle_path, hypothesis_subtitle_path, normalize=False)
```

## Normalization

By default, the text is normalized before WER/CER calculation. This includes:
- Converting to lowercase
- Removing punctuation
- Removing extra whitespace (Replace double spaces to single space)

Normalization can be disabled by setting `normalize=False` when calling the functions.
