import deepspeech 
import wave
import numpy as np

MODEL_PATH = 'deepspeech-0.9.3-models.pbmm'
SCORER_PATH = 'deepspeech-0.9.3-models.scorer'
model = deepspeech.Model(MODEL_PATH)
model.enableExternalScorer(SCORER_PATH)

def read_wav_file(filename):
    with wave.open(filename, 'rb') as wf:
        rate = wf.getframerate()
        frames = wf.getnframes()
        buffer = wf.readframes(frames)
        return buffer, rate

audio_path = 'caminho_para_seu_audio.wav'
audio, sample_rate = read_wav_file(audio_path)
audio = np.frombuffer(audio, dtype=np.int16)
text = model.stt(audio)

# Exibe o texto reconhecido
print('Texto reconhecido:', text)
