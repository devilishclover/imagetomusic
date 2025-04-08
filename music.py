import numpy as np
import simpleaudio as sa
from scipy import signal
from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth

note_frequencies = {
            'C0': 16.35, 'C#0': 17.32, 'D0': 18.35, 'D#0': 19.45, 'E0': 20.60, 'F0': 21.83, 'F#0': 23.12, 'G0': 24.50, 'G#0': 25.96, 'A0': 27.50, 'A#0': 29.14, 'B0': 30.87,
            'C1': 32.70, 'C#1': 34.65, 'D1': 36.71, 'D#1': 38.89, 'E1': 41.20, 'F1': 43.65, 'F#1': 46.25, 'G1': 49.00, 'G#1': 51.91, 'A1': 55.00, 'A#1': 58.27, 'B1': 61.74,
            'C2': 65.41, 'C#2': 69.30, 'D2': 73.42, 'D#2': 77.78, 'E2': 82.41, 'F2': 87.31, 'F#2': 92.50, 'G2': 98.00, 'G#2': 103.83, 'A2': 110.00, 'A#2': 116.54, 'B2': 123.47,
            'C3': 130.81, 'C#3': 138.59, 'D3': 146.83, 'D#3': 155.56, 'E3': 164.81, 'F3': 174.61, 'F#3': 185.00, 'G3': 196.00, 'G#3': 207.65, 'A3': 220.00, 'A#3': 233.08, 'B3': 246.94,
            'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'E4': 329.63, 'F4': 349.23, 'F#4': 369.99, 'G4': 392.00, 'G#4': 415.30, 'A4': 440.00, 'A#4': 466.16, 'B4': 493.88,
            'C5': 523.25, 'C#5': 554.37, 'D5': 587.33, 'D#5': 622.25, 'E5': 659.25, 'F5': 698.46, 'F#5': 739.99, 'G5': 783.99, 'G#5': 830.61, 'A5': 880.00, 'A#5': 932.33, 'B5': 987.77,
            'C6': 1046.50, 'C#6': 1108.73, 'D6': 1174.66, 'D#6': 1244.51, 'E6': 1318.51, 'F6': 1396.91, 'F#6': 1479.98, 'G6': 1567.98, 'G#6': 1661.22, 'A6': 1760.00, 'A#6': 1864.66, 'B6': 1975.53,
            'C7': 2093.00, 'C#7': 2217.46, 'D7': 2349.32, 'D#7': 2489.02, 'E7': 2637.02, 'F7': 2793.83, 'F#7': 2959.96, 'G7': 3135.96, 'G#7': 3322.44, 'A7': 3520.00, 'A#7': 3729.31, 'B7': 3951.07,
            'C8': 4186.01
        }

def play_note(length, wave_type, note, duration):
    frequency = note_frequencies.get(note, 440.00) if isinstance(note, str) else note if isinstance(note, (int, float)) else None
    if frequency is None:
        print("Invalid note type. Please use a string (e.g., 'C4') or a number (frequency in Hz).")
        return

    wave_generators = {
        'sine': generate_sine_wave,
        'saw': generate_saw_wave,
        'square': generate_square_wave
    }

    if wave_type not in wave_generators:
        print("Unsupported wave type. Please use 'sine', 'saw', or 'square'.")
        return

    wave = wave_generators[wave_type](frequency=frequency, duration=duration, volume=length)
    play_audio(wave)

def generate_wave(frequency, duration, volume, wave_func):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = wave_func(2 * np.pi * frequency * t)
    return (note * (2**15 - 1) * volume).astype(np.int16)

def generate_sine_wave(frequency, duration, volume):
    return generate_wave(frequency, duration, volume, np.sin)

def generate_saw_wave(frequency, duration, volume):
    return generate_wave(frequency, duration, volume, signal.sawtooth)

def generate_square_wave(frequency, duration, volume):
    return generate_wave(frequency, duration, volume, signal.square)

def play_audio(audio):
    sample_rate = 44100
    sa.play_buffer(audio, 1, 2, sample_rate).wait_done()

def export_mp3(song, filename="output.mp3"):
    from tqdm import tqdm  # Import tqdm for the progress bar

    sample_rate = 44100
    combined = AudioSegment.silent(duration=0)

    print("Exporting song to MP3...")
    for note, duration, wave_type in tqdm(song, desc="Processing notes", unit="note"):
        frequency = note_frequencies.get(note, 440.00)
        duration_ms = int(duration * 1000)
        wave_generators = {
            "sine": Sine,
            "saw": Sawtooth,
            "square": Square
        }

        if wave_type not in wave_generators:
            print(f"Unsupported wave type: {wave_type}")
            continue

        wave = wave_generators[wave_type](frequency).to_audio_segment(duration=duration_ms)
        combined += wave

    combined.export(filename, format="mp3")
    print(f"Export completed: {filename}")

if __name__ == "__main__":
    # example 
    song = [
        ('C4', 0.05, "saw"),
        ('E4', 0.05, "square"),
        ('G4', 0.05, "saw"),
        ('C5', 0.05, "sine"),
        ('G4', 0.05, "saw"),
        ('E4', 0.05, "square"),
        ('C4', 0.05, "saw"),
    ]
    
    export_mp3(song, "output.mp3")

    for note, duration, wave in song:
        play_note(length=0.5, wave_type=wave, note=note, duration=duration)
