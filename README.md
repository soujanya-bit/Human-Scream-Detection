

# Human Scream Detection

## Overview

**Human Scream Detection** is a machine learning project designed to detect human screams in audio recordings. It can be used in applications such as surveillance systems, safety alerts, or emergency monitoring. The system processes audio input, extracts features, and classifies whether a scream is present.

---

## Features

* Detects human screams in real-time or from audio files.
* Uses **feature extraction** techniques such as MFCC (Mel-Frequency Cepstral Coefficients).
* Implements a **machine learning model** for accurate classification.
* Can be integrated into security or alert systems.

---

## Dataset

* Dataset contains labeled audio files of **human screams** and **non-screams**.
* Preprocessing includes normalization and noise reduction to improve model performance.

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/soujanya-bit/Human-Scream-Detection.git
cd Human-Scream-Detection
```

2. **Create a virtual environment** (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

## Usage

1. **Train the model** (if training from scratch):

```bash
python train_model.py
```

2. **Detect screams in audio files**:

```bash
python detect_scream.py --input path_to_audio_file.wav
```

3. **Real-time detection** (if implemented):

```bash
python real_time_detection.py
```

---

## Model

* Model architecture: **\[Specify: CNN, LSTM, or any other used]**
* Input: Preprocessed audio features (MFCC, Chroma, etc.)
* Output: Binary classification – **Scream / No Scream**

---

## Folder Structure

```
Human-Scream-Detection/
│
├── data/               # Audio datasets
├── src/                # Source code
│   ├── train_model.py
│   ├── detect_scream.py
│   └── real_time_detection.py
├── requirements.txt    # Python dependencies
├── README.md
└── config.py           # Config file (DO NOT include secrets)
```

---

## Important Notes

* **Do NOT commit sensitive information** such as API keys. Use environment variables or a `.env` file.
* Ensure the input audio is in **WAV format** for best results.

---

## License

This project is licensed under the MIT License.

---

I can also create a **more GitHub-friendly version** with badges, setup instructions for `.env` secrets, and optional sample audio links so it looks professional on your repo.

Do you want me to do that?
