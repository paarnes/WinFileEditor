"""
Module for the ConvertVideo_GUI
"""
import os
from moviepy.video.fx.resize import resize
from moviepy.editor import VideoFileClip



def convert_video_file(input_file, output_file, bitrate=None, fps=None, rotate_degrees=None):
    """
    Converts a single video file to MP4 format with optional settings.

    :param input_file: Path to the input video file.
    :param output_file: Path to save the converted video.
    :param bitrate: Optional bitrate setting for output video.
    :param fps: Optional frames per second setting.
    :param rotate_degrees: Optional rotation in degrees (90, 180, 270).
    :return: True if successful, False otherwise.
    """
    if not os.path.exists(input_file):
        print(f"❌ Error: Input file does not exist -> {input_file}")
        return False

    try:
        print(f"🔄 Converting: {input_file} -> {output_file}")

        # Load the video
        my_clip = VideoFileClip(input_file)

        # Apply rotation if needed
        if rotate_degrees:
            my_clip = my_clip.rotate(rotate_degrees)
            # If 90 or 270 degrees, swap width & height to maintain aspect ratio
            # if rotate_degrees in [90, 270]:
            #     width, height = my_clip.size
            #     my_clip = resize(my_clip, (height, width))  # Swap width & height

        # Convert and save the video
        if bitrate:
            my_clip.write_videofile(output_file, fps=fps if fps else my_clip.fps, bitrate=bitrate)
        else:
            my_clip.write_videofile(output_file, fps=fps if fps else my_clip.fps)

        print(f"✅ Successfully converted: {output_file}")
        return True  # Indicate success

    except Exception as e:
        print(f"❌ Failed to convert video: {e}")
        return False  # Indicate failure



def convert_batch_videos(input_folder, output_folder, bitrate=None, fps=None, rotate_degrees=None):
    """
    Converts all video files in a folder to MP4 using the same settings.

    :param input_folder: Path to the folder containing input video files.
    :param output_folder: Path to save the converted videos.
    :param bitrate: Optional bitrate setting for output videos.
    :param fps: Optional frames per second setting.
    :param rotate_degrees: Optional rotation in degrees (90, 180, 270).
    """
    if not os.path.exists(input_folder):
        print("Error: Input folder does not exist.")
        return False

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create output folder if it doesn't exist

    # Supported video formats
    video_extensions = (".mp4", ".mov", ".avi", ".mkv")

    # Process each video file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(video_extensions):  # Only process video files
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp4")

            try:
                print(f"Converting: {filename} -> {output_file}")
                my_clip = VideoFileClip(input_file)

                if rotate_degrees:
                    my_clip = my_clip.rotate(rotate_degrees)
                    # if rotate_degrees % 180 != 0:
                    #     my_clip = resize(my_clip, (my_clip.size[1], my_clip.size[0]))  # Swap width & height if rotated

                if bitrate:
                    my_clip.write_videofile(output_file, fps=fps if fps else my_clip.fps, bitrate=bitrate)
                else:
                    my_clip.write_videofile(output_file, fps=fps if fps else my_clip.fps)

                print(f"✅ Successfully converted: {output_file}")

            except Exception as e:
                print(f"❌ Failed to convert {filename}: {e}")

    print("\n🎉 Batch conversion completed!")
    return True  # Indicate success


def cut_movie(input_file: str, output_file: str, start_time: str, end_time: str):
    """
    Cuts a video file from start_time to end_time and saves the output.

    Parameters:
    -----------
    input_file: Path to the input video file.
    output_file: Path to save the trimmed video.
    start_time: Start time in seconds (float or int).
    end_time: End time in seconds (float or int).
    """
    try:
        # Convert start and end times to float
        start_time = float(start_time)
        end_time = float(end_time)

        if start_time < 0 or end_time <= start_time:
            raise ValueError("Start time must be non-negative and less than end time.")

        # Load the video
        video = VideoFileClip(input_file)

        if end_time > video.duration:
            raise ValueError("End time exceeds video duration.")

        # Extract the desired clip
        trimmed_video = video.subclip(start_time, end_time)

        # Write output file
        trimmed_video.write_videofile(output_file, codec="libx264", audio_codec="aac")

        return True  # Indicate success

    except Exception as e:
        print(f"Error cutting video: {e}")
        return False  # Indicate failure




if __name__ == "__main__":
    # inputf = r"C:\Users\perhe\OneDrive\Bilder og filmer\2023\Munkstigen\Filmer\Snapchat-1372024074 – Kopi.mp4"
    # outputf = r"C:\Users\perhe\OneDrive\Bilder og filmer\2023\Munkstigen\Filmer\Snapchat-1372024074 – WWWWWWWWW.mp4"
    # Convert_MOV_2_MP4(inputf, outputf, rotate_degrees=90)
    inputf = r"C:\Users\perhe\OneDrive\Documents\GitHub\WinFileEditor\testdata\mov\2.MOV"
    outputf = r"C:\Users\perhe\OneDrive\Documents\GitHub\WinFileEditor\testdata\resultat_test\TESTTEST.mov"
    cut_movie(inputf, outputf, 10, 30)

