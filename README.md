# SConverter

A CLI-based YouTube video and audio downloader built with Python, yt-dlp, and FFmpeg.

## Features

- Download videos in high quality (MKV by default).
- Download audio in high quality.
- Support for custom format conversion (mp4, avi, wav, m4a, flac, etc.).
- Integrated cleanup option to delete source files after conversion.
- Safety warnings for video-to-audio conversions.

## Requirements

- Python 3.x
- FFmpeg and FFprobe (must be in system PATH or root directory)
- Python dependencies:
  - yt-dlp
  - colorama

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install yt-dlp colorama
