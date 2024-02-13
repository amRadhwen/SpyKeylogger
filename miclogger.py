import pyaudio
import wave
from dateTime import Datetime
class MicLogger:

    def __init__(self, mic_log_filename):
        self.FORMAT = pyaudio.paInt16  # Format of audio samples (16-bit signed integers)
        self.CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
        self.RATE = 44100  # Sample rate (samples per second)
        self.CHUNK = 1024  # Number of frames per buffer
        self.RECORD_SECONDS = 5  # Duration of recording in seconds
        self.frames = []
        self.mic_output_filename = Datetime().get_date_time()
        self.mic_log_filename = mic_log_filename

        # initialize pyaudio
        self.pa = pyaudio.PyAudio()


    def record_mic(self):
        print("Recording !")
        self.write_mic_log(self.mic_log_filename, Datetime.get_date_time() + "Recording started !\n")
        stream = self.init_stream()
        for _ in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            self.frames.append(data)
        print("Recording Stopped !")
        self.write_mic_log(self.mic_log_filename, Datetime.get_date_time() + "Recording stopped !\n")
        # close the stream
        stream.stop_stream()
        stream.close()
        self.pa.terminate()

    # open audio stream
    def init_stream(self):
        stream = self.pa.open(
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK,
        )
        return stream

    def generate_audio_file(self, mic_output_filename):
        wf = wave.open(self.mic_output_filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.pa.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def write_mic_log(self, mic_log_filename, input):
        with open(mic_log_filename, "a+") as mic_log:
            mic_log.write(input + "\n")
        return True

# Test
mic_logger = MicLogger("mic_log.txt")

'''
# using tkSnack
import tkSnack
from tkinter import *

class MicLogger:
    def __init__(self, mic_log_filename):
        self.mic_log_filename = mic_log_filename

    def start_recording(self):
        root = Tk()
        tkSnack.initializeSnack(root)
        c = tkSnack.Sound(file="test.wav")
        c.record()
        root.after(5000, c.stop)
        root.mainloop()


    def stop_recording(self):
        pass

# Test
mclogger = MicLogger("mic_log.txt")
mclogger.start_recording()
'''