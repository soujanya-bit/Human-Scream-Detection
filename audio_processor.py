import numpy as np
import pyaudio
import wave
from scipy.io import wavfile
from scipy import signal

class AudioProcessor:
    def __init__(self):
        self.format = pyaudio.paFloat32
        self.channels = 1
        self.rate = 44100
        self.chunk = 1024
        self.audio = pyaudio.PyAudio()

    def record_audio(self, duration=5):
        stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )

        frames = []
        for _ in range(0, int(self.rate / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(np.frombuffer(data, dtype=np.float32))

        stream.stop_stream()
        stream.close()
        return np.concatenate(frames)