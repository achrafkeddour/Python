import os
from TTS.api import TTS
from TTS.utils.manage import ModelManager

# Step 1: Download a pre-trained model if not already downloaded
model_path = ModelManager().download_model("tts_models/en/ljspeech/tacotron2-DDC")

# Step 2: Initialize the TTS with the pre-trained model
tts = TTS(model_path=model_path)

# Step 3: Fine-tune the model on your custom voice dataset
# Replace '~/my_voice_data' with the path to your voice dataset folder
# This assumes your dataset is organized as described
tts.fine_tune(dataset_path="~/my_voice_data", output_path="~/my_custom_tts_model")

# Step 4: Reload the fine-tuned model
tts = TTS(model_path="~/my_custom_tts_model")

# Step 5: Function to convert text to your voice
def text_to_voice(text):
    file_path = "output.wav"
    tts.tts_to_file(text=text, file_path=file_path)
    os.system(f"aplay {file_path}")  # Plays the audio file on Debian
    return file_path

# Example usage: generate and play the audio
text = "Hello AI, I'm very happy."
text_to_voice(text)