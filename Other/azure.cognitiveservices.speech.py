from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

speech_config = SpeechConfig(subscription="191417a8ebea44619b7500a2580fdbc7", region="westeurope")

#audio_config = AudioOutputConfig(filename="c:/repos/python/file.wav")
audio_config = AudioOutputConfig(use_default_speaker=True)
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

say = input('What would you like to say ?')
synthesizer.speak_text_async(say)


