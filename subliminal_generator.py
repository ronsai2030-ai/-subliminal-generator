import os
import asyncio
import edge_tts
import numpy as np
import librosa
import soundfile as sf
from safety_filters import apply_hearing_safety_limits

async def generate_affirmation_speech(text: str, output_path: str = "affirmation.wav"):
    """
    Converts affirmation text to speech using Edge-TTS.
    """
    print(f"🎙️ Generating speech for affirmations...")
    communicate = edge_tts.Communicate(text, voice="ar-SA-ZariyahNeural") # يمكنك تغيير الصوت حسب الرغبة
    await communicate.save(output_path)
    print(f"✅ Affirmation audio saved to {output_path}")

def build_safe_subliminal(affirmation_text: str, reference_audio_path: str, final_output_path: str = "safe_subliminal_output.wav"):
    """
    Main pipeline:
    1. Generates speech from custom text affirmations.
    2. Applies strict hearing safety limits (Low-pass & Peak Limiter).
    3. Mixes with reference background audio if available.
    """
    print("🚀 Starting safe subliminal generation pipeline...")
    
    # Step 1: Generate speech file asynchronously
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate_affirmation_speech(affirmation_text, "temp_affirmation.wav"))
    
    # Step 2: Load generated affirmation audio
    aff_y, sr = librosa.load("temp_affirmation.wav", sr=None)
    
    # Step 3: Apply strict hearing safety filters (protecting sensitive ears)
    safe_aff_y = apply_hearing_safety_limits(aff_y, sr, max_db=-6.0, cutoff_freq=7500.0)
    
    # Step 4: If reference background audio exists, mix them together quietly
    if reference_audio_path and os.path.exists(reference_audio_path):
        print(f"🎶 Mixing with background audio: {reference_audio_path}")
        ref_y, _ = librosa.load(reference_audio_path, sr=sr)
        
        # Match lengths (loop or truncate background to match affirmation)
        if len(ref_y) > len(safe_aff_y):
            ref_y = ref_y[:len(safe_aff_y)]
        else:
            ref_y = np.pad(ref_y, (0, len(safe_aff_y) - len(ref_y)), 'wrap')
            
        # Make affirmations very low/subliminal compared to background (-15dB adjustment)
        safe_aff_y = safe_aff_y * 0.15
        final_mix = ref_y + safe_aff_y
    else:
        final_mix = safe_aff_y
        
    # Save final safe output
    sf.write(final_output_path, final_mix, sr)
    print(f"🎉 Success! Safe subliminal track generated at: {final_output_path}")
    
    # Cleanup temporary file
    if os.path.exists("temp_affirmation.wav"):
        os.remove("temp_affirmation.wav")

if __name__ == "__main__":
    text_input = input("Enter your custom affirmations text: ")
    ref_input = input("Enter reference audio path (or press Enter to skip): ").strip()
    
    if text_input:
        build_safe_subliminal(text_input, ref_input if ref_input else None)
