#Requires pillow

import os
from PIL import Image

selected_folder = input('\x1b[1;33m'+'Please, paste the path: \n')

if __name__ == '__main__':
    for filename in os.listdir(selected_folder):
        try:
            name, extension = os.path.splitext(filename)

            if extension.lower() in ['.jpg', '.jpeg', '.png']:
                picture_path = os.path.join(selected_folder, filename)
                compressed_path = os.path.join(selected_folder, '.compressed_' + filename)

                picture = Image.open(picture_path)
                picture.save(compressed_path, optimize=True, quality=60)
                print(f'It has been compressed correctly: {filename}')
        except FileNotFoundError:
            print(f'Error: Could not find file: {filename}, this may be because the route is in OneDrive or similar.')
            

print('\033[4;35m'+'Finished')
