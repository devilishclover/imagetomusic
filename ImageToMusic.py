from music import play_note, export_mp3
import sys
from PIL import Image
from random import randint

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_file path>")
        sys.exit(1)

    image_file = sys.argv[1]
    song = []

    with Image.open(image_file) as img:
        pixels = list(img.getdata())
        
        pixel_list = []
        last_pixel = None
        for pixel in pixels:
            if pixel != last_pixel:
                pixel_list.append(pixel)
                last_pixel = pixel

        for pixel in pixel_list:
            frequency = 440.0 + pixel[0] % 1000
            duration = 0.025 + (pixel[1] % 100) / 1000.0
            waveform = ["saw", "square", "sine"][pixel[2] % 3]
            song.append((frequency, duration, waveform))
            
    export_mp3(song, "output.mp3")

if __name__ == "__main__":
    main()

    
