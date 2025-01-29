"""
Module for the ConvertVideo_GUI
"""

# from moviepy.video.fx.all import resize
# from moviepy.video.fx import resize
from moviepy.video.fx.resize import resize
from moviepy.editor import VideoFileClip
import sys

def Convert_MOV_2_MP4(input_file, output_file, bitrate=None, fps=None, rotate_degrees=None):
    """
    Convert from MOV to MP4
    """
    if fps is None:
        fps = 60

    my_clip = VideoFileClip(input_file)

    # ##
    # hold_stdout = sys.stdout
    # sys.stdout = open("test_log", 'w')
    # ##
    if rotate_degrees:
        my_clip = my_clip.rotate(rotate_degrees)

        if rotate_degrees % 180 != 0:
            my_clip = resize(my_clip, (my_clip.size[1], my_clip.size[0]))  # Swap width and height

    if bitrate is not None:
        my_clip.write_videofile(output_file, fps=fps, bitrate=bitrate)
    else:
        my_clip.write_videofile(output_file, fps=fps)

    # sys.stdout = hold_stdout # test
    return


def cut_movie():
    return


if __name__ == "__main__":
    inputf = r"C:\Users\perhe\OneDrive\Bilder og filmer\2023\Munkstigen\Filmer\Snapchat-1372024074 – Kopi.mp4"
    outputf = r"C:\Users\perhe\OneDrive\Bilder og filmer\2023\Munkstigen\Filmer\Snapchat-1372024074 – WWWWWWWWW.mp4"
    Convert_MOV_2_MP4(inputf, outputf, rotate_degrees=90)
