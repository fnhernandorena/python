#Requires Pytube, pandas and stramlit.

import pandas as pd
from pytube import YouTube

#var excel
file_path = 'urls.csv'
column_name = 'urls'

def main():
    df = pd.read_csv(file_path)
    column_data = df[column_name]
    urls = column_data.values
    id = 1
    for url in urls:
            
            print(f'Starting download video {id}\n')
            yt = YouTube(url)
            video = yt.streams.get_lowest_resolution()
            video.download('./YT')
            print(f'Finish download video {id}\n')
            id += 1
    

if __name__ == '__main__':
    main()