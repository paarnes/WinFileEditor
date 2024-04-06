"""
Module for the ConvertVideo_GUI
"""

import os
from moviepy.video.fx.all import resize
from moviepy.editor import VideoFileClip

def Convert_MOV_2_MP4(input_file, bitrate=None, fps=None, rotate_degrees=None):
    """
    Convert from MOV to MP4
    """
    if fps is None:
        fps = 60
    
    output_file = os.path.basename(input_file)
    output_file = os.path.join(os.path.dirname(input_file), os.path.splitext(output_file)[0] + "_conv.mp4")
    clip = VideoFileClip(input_file)
    
    if rotate_degrees:
        clip = clip.rotate(rotate_degrees)
        
        if rotate_degrees % 180 != 0:
            clip = resize(clip, (clip.size[1], clip.size[0]))  # Swap width and height
        
    if bitrate is not None:
        clip.write_videofile(output_file, fps=fps, bitrate=bitrate)
    else:
        clip.write_videofile(output_file, fps=fps)
