import numpy as np
import librosa

def analyze_reference_audio(file_path: str) -> dict:
    """
    Analyzes a reference audio track to extract parameters like 
    sample rate, duration, spectral centroid, and estimated noise profile.
    
    :param file_path: Path to the audio WAV file.
    :return: Dictionary containing extracted audio features.
    """
    print(f"🔍 Analyzing audio file: {file_path}")
    
    try:
        # Load audio file using librosa
        y, sr = librosa.load(file_path, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)
        
        # Spectral features extraction
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        mean_centroid = float(np.mean(spectral_centroids))
        
        # RMS energy to estimate loudness/masking levels
        rms = librosa.feature.rms(y=y)[0]
        mean_rms = float(np.mean(rms))
        
        analysis_results = {
            "sample_rate": int(sr),
            "duration_seconds": float(duration),
            "mean_spectral_centroid": mean_centroid,
            "average_energy_rms": mean_rms,
            "status": "Success"
        }
        
        print("✅ Audio analysis completed successfully.")
        return analysis_results

    except Exception as e:
        print(f"❌ Error during audio analysis: {e}")
        return {"status": "Failed", "error": str(e)}

if __name__ == "__main__":
    test_file = input("Enter path to WAV audio file for testing: ")
    if test_file:
        results = analyze_reference_audio(test_file)
        print("Analysis Results:", results)
