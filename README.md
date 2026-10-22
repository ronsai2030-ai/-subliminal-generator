# -subliminal-generator
An open-source AI audio tool to reverse-engineer subliminal videos, analyze frequencies/masking, and safely generate custom audio tailored for sensitive hearing.
# 🎧 Safe Subliminal Audio Analyzer & Generator

An open-source Python tool designed to reverse-engineer subliminal audio tracks (from YouTube URLs), identify their underlying audio techniques, and re-apply those parameters to generate new, personalized tracks—while enforcing strict hearing safety controls for users with Auditory Nerve Impairment or sensitive hearing.

---

## 🌟 Key Features & Workflow

### 1. Analysis & Reverse Engineering (Reference Track)
* **Audio Extraction:** Fetch high-quality audio from a YouTube URL.
* **Spectral Analysis:** 
  * Identify background masking sound types (Pink Noise, Brown Noise, Rain, Ambient, etc.).
  * Detect embedded brainwave entrainment frequencies (Binaural Beats, Isochronic Tones, Alpha/Theta/Delta waves).
  * Estimate affirmation parameters (volume attenuation relative to background, pitch shifts, speed manipulation).

### 2. Safe Custom Generation
* **Affirmation Processing:** Accept user text affirmations, convert them via TTS (Text-to-Speech), and match the extracted parameters.
* **Hearing Safety & Auditory Protection (Critical):**
  * **Notch Filtering & Frequency Capping:** Low-pass and notch filters to remove high-pitched, irritating frequencies safe for sensitive auditory nerves.
  * **Decibel Limiting & Peak Compression:** Enforce strict dB safety thresholds to prevent sudden volume spikes and ear fatigue.
* **Multi-Layer Mixing:** Merge processed affirmations with chosen background sound and safe entrainment frequencies.

---

## 🛠️ Suggested Tech Stack
* **Language:** Python
* **Audio Processing:** `yt-dlp`, `librosa`, `pydub`, `scipy`, `soundfile`
* **Text-to-Speech (TTS):** `Edge-TTS` / `gTTS`

---

## 🤝 Looking for Contributors!
This project is **open for contributions**. If you are experienced in Audio Processing, DSP Filters, Neuro-psychoacoustics, or Python scripting, feel free to submit a Pull Request or open a Discussion!
