import sys
from pydub import AudioSegment
from pydub.utils import which, mediainfo

# Set ffmpeg path explicitly
AudioSegment.converter = which("ffmpeg")

def get_audio_bitrate(audio_file):
    try:
        # Load the audio file
        audio = AudioSegment.from_file(audio_file)
        
        # Get bitrate from audio file metadata
        audio_info = mediainfo(audio_file)
        bitrate = audio_info.get("bit_rate", None)  # Fetch the "bit_rate" field
        
        if bitrate:
            return int(bitrate) // 1000  # Convert to kbps
        else:
            return "Unable to determine the bitrate."
    except Exception as e:
        print("An error occurred:", e)
        # Print detailed audio information for debugging
        try:
            audio_info = mediainfo(audio_file)
            print("Audio info:", audio_info)
        except Exception as info_error:
            print("Could not retrieve audio info:", info_error)
        return "Error processing the file."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 analyze_audio.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    bitrate = get_audio_bitrate(audio_file)
    print(f"Bitrate: {bitrate} kbps" if isinstance(bitrate, int) else bitrate)


