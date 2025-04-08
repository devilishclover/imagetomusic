from music import play_note, export_mp3
#To design a program that generates music from a 512x512 image file based on pixel colors and allows the user to pick a musical key, here’s a suggested approach:
#
#1. **Input Handling**:
#    - Allow the user to upload a 512x512 image file.
#    - Provide an option for the user to select a musical key (e.g., C Major, A Minor).
#
#2. **Image Processing**:
#    - Read the image and extract pixel color data (RGB values).
#    - Map pixel positions to time and pitch in the music.
#
#3. **Color-to-Music Mapping**:
#    - Use the RGB values to determine the pitch, duration, and intensity of notes:
#      - Red (R): Maps to pitch (frequency).
#      - Green (G): Maps to note duration.
#      - Blue (B): Maps to velocity (volume).
#
#4. **Key Constraint**:
#    - Ensure the generated notes fit within the selected musical key by snapping pitches to the scale.
#
#5. **Music Generation**:
#    - Use a library like `MIDIUtil` or `music21` to create a MIDI file from the mapped notes.
#
#6. **Output**:
#    - Save the generated music as a MIDI file.
#    - Optionally, play the MIDI file directly in the program.
#
#7. **User Interface**:
#    - Create a simple GUI or command-line interface for file upload and key selection.
#
#Would you like me to start implementing any specific part of this design?

song = [
        ('C4', 0.05, "saw"),
        ('E4', 0.05, "square"),
        ('G4', 0.05, "saw"),
        ('C5', 0.05, "sine"),
        ('G4', 0.05, "saw"),
        ('E4', 0.05, "square"),
        ('C4', 0.05, "saw"),
    ]

export_mp3(song, filename="output.mp3")