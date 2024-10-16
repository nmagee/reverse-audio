#!/Users/nem2p/.local/share/virtualenvs/reverse-audio-XK6q0tXx/bin/python3

from pydub import AudioSegment

def reverse_audio(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    reversed_audio = audio.reverse()
    reversed_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    input_file = "talking-heads.mp3"
    output_file = "reversed_audio.mp3"
    reverse_audio(input_file, output_file)
