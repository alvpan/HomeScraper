import os
import shutil

#this should be adjustable on setup
directory = r"C:\Users\user\Downloads"
files = os.listdir(directory)

#rename Screenshot to image
for filename in files:
    if filename.startswith('Screenshot') and filename.endswith('.png'):
        old_filepath = os.path.join(directory, filename)
        new_filename = 'image.png'
        new_filepath = os.path.join(directory, new_filename)
        os.rename(old_filepath, new_filepath)
        print(f"Renamed '{filename}' to '{new_filename}'")
print("Renaming complete.")

#move image from Downloads to Desktop (this should be adjustable too on setup)
downloads = os.path.expanduser('~/Downloads')
desktop = os.path.expanduser('~/Desktop')
file_to_move = 'image.png'
try:
    shutil.move(os.path.join(downloads, file_to_move), os.path.join(desktop, file_to_move))
    print(f"File '{file_to_move}' moved to Desktop.")
except FileNotFoundError:
    print(f"File '{file_to_move}' not found in Downloads!")
except Exception as e:
    print(f"ERROR while trying to move file!: {e}")
