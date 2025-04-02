# subwer

A `jiwer` wrapper python package for calculating Word Error Rate (WER) and Character Error Rate (CER) between subtitle files.

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

# Calculate without normalization
wer_score_no_norm = wer(reference_subtitle_path, hypothesis_subtitle_path, normalize=False)
cer_score_no_norm = cer(reference_subtitle_path, hypothesis_subtitle_path, normalize=False)

print(f"WER: {wer_score}")
print(f"CER: {cer_score}")
```

## Normalization

By default, the text is normalized before WER/CER calculation. This includes:
- Converting to lowercase
- Removing punctuation
- Removing extra whitespace (Replace double spaces to single space)

Normalization can be disabled by setting `normalize=False` when calling the functions.

## Publishing to PyPI

This package uses GitHub Actions for automatic publishing to PyPI. To publish a new version:

1. Update the version number in `setup.cfg`
2. Commit and push your changes
3. Create a new release on GitHub:
   - Go to the Releases page in your GitHub repository
   - Click "Draft a new release"
   - Set a tag version (e.g., `v0.1.0`) that matches your `setup.cfg` version
   - Set a release title
   - Click "Publish release"

The GitHub Actions workflow will automatically:
1. Build the package
2. Upload it to PyPI

### Setting up PyPI API Token

Before you can publish, you need to add your PyPI API token as a GitHub secret:

1. Generate an API token on PyPI:
   - Go to https://pypi.org/manage/account/
   - Create an API token with scope "Upload to PyPI"
2. Add the token to your GitHub repository:
   - Go to your repository Settings > Secrets > Actions
   - Create a new secret named `PYPI_API_TOKEN`
   - Paste your PyPI token as the value 