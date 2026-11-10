import numpy as np
import scipy.io.wavfile as wavfile
import subprocess
import imageio_ffmpeg

sample_rate = 44100
duration = 66.0 # seconds
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Let's generate a very gentle, modern lofi / ambient chord progression
# Chords: Cmaj7 - Am7 - Fmaj7 - G
# Frequencies:
# Cmaj7: C4 (261.63), E4 (329.63), G4 (392.00), B4 (493.88)
# Am7:   A3 (220.00), C4 (261.63), E4 (329.63), G4 (392.00)
# Fmaj7: F3 (174.61), A3 (220.00), C4 (261.63), E4 (329.63)
# G:     G3 (196.00), B3 (246.94), D4 (293.66), G4 (392.00)

chord_cycle = [
    [261.63, 329.63, 392.00, 493.88], # Cmaj7
    [220.00, 261.63, 329.63, 392.00], # Am7
    [174.61, 220.00, 261.63, 329.63], # Fmaj7
    [196.00, 246.94, 293.66, 392.00]  # G
]

chord_duration = 4.0 # 4 seconds per chord
total_chords = int(duration / chord_duration) + 1

audio_signal = np.zeros_like(t)

for i in range(total_chords):
    start_t = i * chord_duration
    end_t = min((i + 1) * chord_duration, duration)
    mask = (t >= start_t) & (t < end_t)
    sub_t = t[mask] - start_t
    
    chord = chord_cycle[i % len(chord_cycle)]
    chord_sig = np.zeros_like(sub_t)
    
    for f in chord:
        # Soft sine with subtle overtone
        sine = 0.7 * np.sin(2 * np.pi * f * sub_t) + 0.3 * np.sin(2 * np.pi * f * 2 * sub_t)
        chord_sig += sine
        
    # Apply smooth envelope (attack & decay)
    attack = np.minimum(sub_t / 0.5, 1.0)
    decay = np.maximum(1.0 - (sub_t / chord_duration)**2 * 0.3, 0.2)
    env = attack * decay
    chord_sig *= env
    
    audio_signal[mask] += chord_sig

# Add a very gentle low bass pad
bass_cycle = [130.81, 110.00, 87.31, 98.00]
for i in range(total_chords):
    start_t = i * chord_duration
    end_t = min((i + 1) * chord_duration, duration)
    mask = (t >= start_t) & (t < end_t)
    sub_t = t[mask] - start_t
    f_bass = bass_cycle[i % len(bass_cycle)]
    bass_sig = 0.8 * np.sin(2 * np.pi * f_bass * sub_t)
    audio_signal[mask] += bass_sig

# Normalize and reduce volume for background (subtle background volume: ~12%)
audio_signal = audio_signal / np.max(np.abs(audio_signal)) * 0.10

# Fade in and fade out
fade_in_len = int(sample_rate * 2.0)
audio_signal[:fade_in_len] *= np.linspace(0, 1, fade_in_len)

fade_out_len = int(sample_rate * 3.0)
audio_signal[-fade_out_len:] *= np.linspace(1, 0, fade_out_len)

int_signal = (audio_signal * 32767).astype(np.int16)
wavfile.write("bg_music.wav", sample_rate, int_signal)

print("Background music generated: bg_music.wav")
