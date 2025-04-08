from music import play_note, export_mp3
import sys
from PIL import Image
from random import randint

def main():
    mod = 1
    args = sys.argv[1:]

    if len(args) < 1:
        print("Usage: python ImageToMusic.py <image_file>")
        sys.exit(1)

    if args[0] == "-d" :
        mod = float(args[1])
        args = args[2:]

    if len(args) < 1:
        print("Usage: python -d mod ImageToMusic.py <image_file>")
        sys.exit(1)
        

    image_file = args[0]
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
            duration = (0.025 + (pixel[1] % 100) / 1000.0) * mod
            waveform = ["saw", "square", "sine"][pixel[2] % 3]
            song.append((frequency, duration, waveform))
            
    export_mp3(song, "output.mp3")

if __name__ == "__main__":
    main()

    
