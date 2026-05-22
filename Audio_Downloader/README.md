# 🎵 YouTube Audio Downloader using Python

A simple and efficient Python project that allows users to download audio directly from YouTube videos and convert it into MP3 format.
This project uses **PyTube** for fetching YouTube streams and **MoviePy** for audio conversion.

---

## 🚀 Features

* 🎧 Download audio from any YouTube video
* 🔄 Automatically converts audio to MP3 format
* ⚡ Fast and lightweight script
* 🐍 Beginner-friendly Python project
* 💾 Save audio files to any custom location

---

## 🛠️ Technologies Used

* 🐍 Python
* 📥 PyTube
* 🎬 MoviePy

---

## 📦 Required Libraries

Install the required modules before running the project:

```bash
pip install pytube
pip install moviepy
```

---

## ▶️ How to Run

1️⃣ Open the Python script

2️⃣ Replace the default YouTube URL with your own video link:

```python
youtube_url = "YOUR_YOUTUBE_VIDEO_URL"
```

3️⃣ Add your own file path and output file name:

```python
mp3_file = os.path.join("Your Path", "SongName.mp3")
```

4️⃣ Run the script:

```bash
python main.py
```

---

## 📌 Project Workflow

* Connects to YouTube using PyTube
* Fetches the audio stream from the video
* Downloads the audio temporarily
* Converts the audio into MP3 format using MoviePy
* Saves the final MP3 file to the selected location
* Deletes temporary files automatically

---

## 🌟 Use Cases

* 🎶 Download music or podcasts
* 📚 Save educational audio lectures
* 🎤 Extract audio from interviews or tutorials

---

## ⚠️ Disclaimer

This project is created for educational purposes only.
Please respect YouTube's Terms of Service and copyright policies while using this script.

---


