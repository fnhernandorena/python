import pytube 
import whisper
import os
from pytube.exceptions import RegexMatchError

#example_link: https://www.youtube.com/watch?v=cgVA2OYH-nk&pp=ygUaY2hhcmxhIGNvcnRhIG11eSBtdXkgY29ydGE%3D

youtube_video_id = input('\x1b[1;33m'+'Please, paste the path: \n \n')

field_to_delete = "tmp.mp4"

model = whisper.load_model('small')


try:
    
    print("\033[4;35m"+"\n Starting search \n")
    youtube_video = pytube.YouTube(youtube_video_id)

    audio = youtube_video.streams.get_audio_only()
    
    audio.download(filename='tmp.mp4')

    print("\033[4;35m"+"Starting write audio \n")
    result = model.transcribe('tmp.mp4')

    print(f"\n\n\x1b[1;33m{result['text']}")

    if os.path.exists(field_to_delete):
        os.remove(field_to_delete)
        print("\033[4;35m"+"\n The audio field was deleted correctly!")
    else:
        print("\033[4;35m"+"\n Can`t delete the audio file")

except RegexMatchError:
    print("\033[4;35m"+"\n \n Error: The provided YouTube video URL is invalid or cannot be processed.")
