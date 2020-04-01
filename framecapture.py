 
import cv2
import os  
from moviepy.editor import *
import shutil 
  

def turn_to_gif(video_path):
    video_file = VideoFileClip(video_path)
    print(video_file.duration)
    done = False
    start = 0
    end = start + 0.5
    counter = 1
    while end <  video_file.duration:
        clip = video_file.subclip(start,end)
        clip.write_gif(f'output_videos/test{counter}.gif')

        counter +=1
        start += 0.5
        end = start + 0.5




  
if __name__ == '__main__': 
  
    # Calling the function 
    input_directory = os.getcwd()
    turn_to_gif('./001.mp4')
    print(os.getcwd())