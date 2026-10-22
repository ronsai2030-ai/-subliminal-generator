import os
import yt_dlp

def download_youtube_audio(youtube_url: str, output_folder: str = "downloads") -> str:
    """
    Downloads audio from a given YouTube URL and converts it to WAV format for safe processing.
    
    :param youtube_url: The full YouTube video URL.
    :param output_folder: Directory where the extracted audio file will be stored.
    :return: File path of the downloaded audio.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    out_template = os.path.join(output_folder, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': out_template,
        'quiet': False
    }

    try:
        print(f"📥 Starting audio extraction from: {youtube_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            filename = ydl.prepare_filename(info_dict)
            wav_filename = os.path.splitext(filename)[0] + '.wav'
            print(f"✅ Download complete: {wav_filename}")
            return wav_filename
    except Exception as e:
        print(f"❌ Error downloading audio: {e}")
        return None

if __name__ == "__main__":
    # Test example
    test_url = input("Enter YouTube URL to test: ")
    if test_url:
        download_youtube_audio(test_url)
