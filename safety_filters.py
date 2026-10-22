import numpy as np
from scipy.signal import butter, lfilter

def butter_lowpass(cutoff: float, fs: int, order: int = 5):
    """Calculates Butterworth low-pass filter coefficients."""
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data: np.ndarray, cutoff: float, fs: int, order: int = 5) -> np.ndarray:
    """Applies low-pass filter to the audio signal to remove harsh high frequencies."""
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def apply_hearing_safety_limits(audio_data: np.ndarray, fs: int, max_db: float = -3.0, cutoff_freq: float = 8000.0) -> np.ndarray:
    """
    Applies strict auditory safety controls:
    1. Removes high-pitched frequencies above cutoff_freq (default 8kHz) for sensitive hearing.
    2. Applies a peak limiter to prevent sudden volume spikes and ear fatigue.
    
    :param audio_data: Numpy array of the audio signal.
    :param fs: Sampling rate of the audio.
    :param max_db: Maximum peak decibel limit.
    :param cutoff_freq: Maximum allowed frequency in Hz.
    :return: Processed safe audio array.
    """
    print("🛡️ Applying hearing safety filters (Low-pass & Peak Limiter)...")
    
    # Step 1: Low-pass filter for sensitive auditory nerve protection
    filtered_audio = lowpass_filter(audio_data, cutoff_freq, fs, order=5)
    
    # Step 2: Peak Limiter / Normalization to cap volume safely
    peak = np.max(np.abs(filtered_audio))
    if peak > 0:
        target_peak = 10 ** (max_db / 20.0)
        if peak > target_peak:
            filtered_audio = filtered_audio * (target_peak / peak)
            
    print("✅ Hearing safety processing complete.")
    return filtered_audio
