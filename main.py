from music import play_note, export_mp3


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