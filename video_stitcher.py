from moviepy.editor import *

from glob import glob

def stitch_all_gifs(videos_path):
    file_dir = glob(f'{videos_path}/*.gif')

    print(sorted(file_dir))


# final_clip = concatenate_videoclips([clip1,clip2,clip3])


if __name__ == "__main__":
    stitch_all_gifs('output_videos/')