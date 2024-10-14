import subprocess

def synthesize_text(text, speaker_idx):
    # Define the paths for configuration and model files
    config_path = "/Users/aditya.narayan/Desktop/speechToSpeech/indic-tts/models/v1/kn/fastpitch/config.json"
    model_path = "/Users/aditya.narayan/Desktop/speechToSpeech/indic-tts/models/v1/kn/fastpitch/best_model.pth"
    out_path = "/Users/aditya.narayan/Desktop/speechToSpeech/indic-tts/output.wav"
    vocoder_path = "/Users/aditya.narayan/Desktop/speechToSpeech/indic-tts/models/v1/kn/hifigan/best_model.pth"
    vocoder_config_path = "/Users/aditya.narayan/Desktop/speechToSpeech/indic-tts/models/v1/kn/hifigan/config.json"

    # Create the command
    command = [
        "tts",
        "--text", text,
        "--config_path", config_path,
        "--model_path", model_path,
        "--out_path", out_path,
        "--vocoder_path", vocoder_path,
        "--vocoder_config_path", vocoder_config_path,
        "--speaker_idx", str(speaker_idx)  # Convert speaker_idx to string if necessary
    ]

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output and errors (if any)
    # print("Output:", result.stdout)
    # print("Error:", result.stderr)
    # print('---->',result)
    
    print("🟢 Speech Generated")

if __name__ == "__main__":
    text_to_synthesize = """ನಮಸ್ಕಾರ! ನಿಮ್ಮ ನಮಯಾತ್ರಿ ಆಪ್ ಕಾರ್ಯ ನಿರ್ವಹಣೆ ಮಾಡುವುದಿಲ್ಲ ಎಂದು ತಿಳಿದು ಸಂತೋಷವಾಯಿತು. ದಯವಿಟ್ಟು ಕೆಳಗಿನ ಸಲಹೆಗಳನ್ನು ಪ್ರಯತ್ನಿಸಿ:
ಆಪ್‌ ಅನ್ನು ಮರುಾರಂಭಿಸಿ, ಆಪ್‌ ಅನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಮುಚ್ಚಿ, ನಂತರ ಮತ್ತೆ ತೆರೆದುಕೊಳ್ಳಿ.
ಈ ಪ್ರಯತ್ನಗಳಲ್ಲಿ ಯಾವುದೇ ಸಹಾಯ ಬೇಕಾದರೆ ಅಥವಾ ಇನ್ನಷ್ಟು ವಿವರ ಬೇಕಾದರೆ ತಿಳಿಸಿ!"""
    speaker_index = "female"
    synthesize_text(text_to_synthesize, speaker_index)
