from moviepy.editor import *

from glob import glob

def stitch_all_gifs(videos_path):
    files_in_dir = sorted(glob(f'{videos_path}/*.gif'))
    stitched_video = []
    for video in files_in_dir:
        stitched_video.append(VideoFileClip(video))

    full_composite_video = concatenate_videoclips(stitched_video, method='compose')

    full_composite_video.write_videofile("stitched_video.mp4")



# final_clip = concatenate_videoclips([clip1,clip2,clip3])


if __name__ == "__main__":
    stitch_all_gifs('output_videos/')