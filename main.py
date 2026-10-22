import os
from audio_downloader import download_youtube_audio
from audio_analyzer import analyze_reference_audio
from subliminal_generator import build_safe_subliminal

def main():
    print("🎧 === Safe Subliminal Generator & Reverse Engineering Tool ===")
    
    # Step 1: Get YouTube URL for reference audio
    youtube_url = input("Enter YouTube reference URL (or press Enter to skip): ").strip()
    
    reference_audio_path = None
    if youtube_url:
        print("\n--- Step 1: Downloading Reference Audio ---")
        reference_audio_path = download_youtube_audio(youtube_url)
        
        if reference_audio_path:
            print("\n--- Step 2: Analyzing Reference Audio ---")
            analysis_results = analyze_reference_audio(reference_audio_path)
            print("Analysis Summary:", analysis_results)
    
    # Step 2: Get user affirmation text
    print("\n--- Step 3: Affirmations Setup ---")
    affirmation_text = input("Enter your custom affirmations text: ").strip()
    
    if not affirmation_text:
        print("❌ Error: Affirmation text cannot be empty!")
        return
        
    output_filename = input("Enter output file name (default: safe_subliminal_output.wav): ").strip()
    if not output_filename:
        output_filename = "safe_subliminal_output.wav"
    elif not output_filename.endswith(".wav"):
        output_filename += ".wav"
    
    # Step 3: Generate the final safe subliminal track
    print("\n--- Step 4: Generating Safe Subliminal Track ---")
    build_safe_subliminal(
        affirmation_text=affirmation_text,
        reference_audio_path=reference_audio_path,
        final_output_path=output_filename
    )
    
    print("\n✨ All processes completed successfully! Your safe subliminal file is ready.")

if __name__ == "__main__":
    main()
