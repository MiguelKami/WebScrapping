# WebScrapping Automation

This repository contains simple web scrapers and a new script `auto_youtuber.py` that demonstrates how to generate short video clips automatically. The videos focus on **"Enigmas Ancestrais"** and can be shared on platforms like YouTube or TikTok.

## auto_youtuber.py

The script creates a slideshow video using `moviepy` and `gTTS` without requiring external images. It generates Portuguese speech, overlays text and saves the final video as `enigma_short.mp4`.

### Usage

```bash
pip install moviepy==1.0.3 gTTS
sudo apt-get update && sudo apt-get install -y imagemagick
python auto_youtuber.py
```

After running, you will find `enigma_short.mp4` in the project folder. You can upload this video to your preferred social media channel. The code can be extended with APIs such as the YouTube Data API or Instagram Graph API to upload automatically (tokens not included).

