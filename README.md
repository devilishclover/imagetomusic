# IMAGE TO "MUSIC"

ImageToMusic is a Python-based tool that converts images into "music" by mapping pixel data to sound frequencies, durations, and waveforms. The resulting audio is exported as an MP3 file.

## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/devilishclover/imagetomusic
     cd imagetomusic
     ```

2. Install the required dependencies:
     ```bash
     pip install pillow numpy simpleaudio scipy pydub
     ```

## Usage

Run the script with the following command:

```bash
python ImageToMusic.py <image_file>
```

### Optional Modifier

You can adjust the duration of the notes using the `-d` flag:

```bash
python ImageToMusic.py -d <mod> <image_file>
```

- `<mod>`: A float value to change the note durations.

### Example

```bash
python ImageToMusic.py -d .5 path/to/example_image.png
```

This will generate an MP3 file named `output.mp3` based on the pixel data of `example_image.png`. The mod is .5 so the notes will be half the normal length

### Notes
* Larger images take longer to generate.
* Images with more colors will take longer to generate. 
* I recomend using a very low mod value for large images as the processing time will be high.
* these are not good songs, dont get your hopes up or anything lol




