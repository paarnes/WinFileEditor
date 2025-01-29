"""
GUI module for WinFileEditor
"""

import os
from tkinter import filedialog, messagebox, Text, Scrollbar
import sys
import customtkinter as ctk
from PIL import Image
from VideoMod import convert_video_file, cut_movie, convert_batch_videos
from HeicConverter import convert_heic_to_jpg


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")  # Default to dark mode
        self.title("Aarnes Editor")
        self.geometry("1400x900")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons/")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, r"main_img.png")), size=(80, 50))
        self.video_conv_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "video_conv.png")),
                                                dark_image=Image.open(os.path.join(image_path, "video_conv.png")), size=(25, 25))
        self.video_cut_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "video_cut.png")),
                                                dark_image=Image.open(os.path.join(image_path, "video_cut.png")), size=(25, 25))
        self.heic_image = ctk.CTkImage(Image.open(os.path.join(image_path, "heic2jpg.png")), size=(25, 25))


        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Aarnes Editor", image=self.logo_image,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)


        # Frame 2
        self.frame_1_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Convert Video",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.video_conv_image, anchor="w", command=self.frame_1_button_event)
        self.frame_1_button.grid(row=2, column=0, sticky="ew")

        # Frame 3
        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cut Video",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.video_cut_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=3, column=0, sticky="ew")

        # Frame 4
        self.frame_3_button = ctk.CTkButton(self.navigation_frame,corner_radius=0, height=40, border_spacing=10, text="HEIC to JPG",
                                            image=self.heic_image, fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"), anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        # create first frame
        self.build_video_conv_frame()

        # create second frame
        self.build_cut_movie_frame()

        # create third frame
        self.build_heic_to_jpg_frame()

        # select default frame
        self.select_frame_by_name("frame_1")

    def select_frame_by_name(self, name):
        """ set button color for selected button """
        self.frame_1_button.configure(fg_color=("gray75", "gray25") if name == "frame_1" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

        if name == "frame_1":
            self.first_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.first_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()



    def frame_1_button_event(self):
        self.select_frame_by_name("frame_1")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    # def build_video_conv_frame(self):
    #     self.first_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

    #     # Title label
    #     title_label = ctk.CTkLabel(self.first_frame, text="Convert between video formats", font=ctk.CTkFont(family="Helvetica", weight="bold", size=34))
    #     title_label.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="w")

    #     self.label = ctk.CTkLabel(self.first_frame, text="Select input video:")
    #     self.label.grid(row=1, column=0, padx=5, pady=5)

    #     self.conv_entry = ctk.CTkEntry(self.first_frame, width=350)  # Adjusted width here
    #     self.conv_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

    #     self.browse_button = ctk.CTkButton(self.first_frame, text="Browse", command=lambda: self.browse_file(self.conv_entry))
    #     self.browse_button.grid(row=1, column=3, padx=5, pady=5)

    #     self.output_label = ctk.CTkLabel(self.first_frame, text="Output directory:")
    #     self.output_label.grid(row=2, column=0, padx=5, pady=5)

    #     self.conv_output_entry = ctk.CTkEntry(self.first_frame, width=350)
    #     self.conv_output_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

    #     self.save_as_button = ctk.CTkButton(self.first_frame, text="Save As", command=lambda: self.choose_output_dir(self.conv_output_entry))
    #     self.save_as_button.grid(row=2, column=3, padx=5, pady=5)

    #     self.fps_label = ctk.CTkLabel(self.first_frame, text="FPS:")
    #     self.fps_label.grid(row=3, column=0, padx=5, pady=5)

    #     self.fps_entry = ctk.CTkEntry(self.first_frame)
    #     self.fps_entry.grid(row=3, column=1, padx=5, pady=5)

    #     self.bitrate_label = ctk.CTkLabel(self.first_frame, text="Bitrate:")
    #     self.bitrate_label.grid(row=4, column=0, padx=5, pady=5)

    #     self.bitrate_entry = ctk.CTkEntry(self.first_frame)
    #     self.bitrate_entry.grid(row=4, column=1, padx=5, pady=5)

    #     self.rotate_label = ctk.CTkLabel(self.first_frame, text="Rotation (degrees):")
    #     self.rotate_label.grid(row=5, column=0, padx=5, pady=5)

    #     self.rotate_entry = ctk.CTkEntry(self.first_frame)
    #     self.rotate_entry.grid(row=5, column=1, padx=5, pady=5)

    #     self.convert_button = ctk.CTkButton(self.first_frame, text="Convert", command=self.convert_video)
    #     self.convert_button.grid(row=6, column=1, padx=5, pady=5)

    # def build_video_conv_frame(self):
    #     """Build video conversion frame with improved layout and spacing."""
    #     self.first_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

    #     # Title Label
    #     title_label = ctk.CTkLabel(self.first_frame, text="Convert Between Video Formats",
    #                             font=ctk.CTkFont(size=34, weight="bold"))
    #     title_label.grid(row=0, column=0, columnspan=5, padx=5, pady=(10, 20), sticky="w")

    #     # Select Input Video
    #     self.label = ctk.CTkLabel(self.first_frame, text="Select input video:")
    #     self.label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.conv_entry = ctk.CTkEntry(self.first_frame, width=350)
    #     self.conv_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

    #     self.browse_button = ctk.CTkButton(self.first_frame, text="Browse",
    #                                     command=lambda: self.browse_file(self.conv_entry))
    #     self.browse_button.grid(row=1, column=3, padx=(5, 10), pady=5, sticky="ew")

    #     # Select Output Directory
    #     self.output_label = ctk.CTkLabel(self.first_frame, text="Output directory:")
    #     self.output_label.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.conv_output_entry = ctk.CTkEntry(self.first_frame, width=350)
    #     self.conv_output_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

    #     self.save_as_button = ctk.CTkButton(self.first_frame, text="Save As",
    #                                         command=lambda: self.choose_output_dir(self.conv_output_entry))
    #     self.save_as_button.grid(row=2, column=3, padx=(5, 10), pady=5, sticky="ew")

    #     # **Video Settings (FPS, Bitrate, Rotation)**
    #     settings_title = ctk.CTkLabel(self.first_frame, text="Video Settings (Optional)",
    #                                 font=ctk.CTkFont(size=20, weight="bold"))
    #     settings_title.grid(row=3, column=0, columnspan=5, padx=5, pady=(15, 10), sticky="w")

    #     # FPS
    #     self.fps_label = ctk.CTkLabel(self.first_frame, text="FPS:")
    #     self.fps_label.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.fps_entry = ctk.CTkEntry(self.first_frame, width=120)
    #     self.fps_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    #     # Bitrate
    #     self.bitrate_label = ctk.CTkLabel(self.first_frame, text="Bitrate:")
    #     self.bitrate_label.grid(row=5, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.bitrate_entry = ctk.CTkEntry(self.first_frame, width=120)
    #     self.bitrate_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    #     # Rotation
    #     self.rotate_label = ctk.CTkLabel(self.first_frame, text="Rotation (degrees):")
    #     self.rotate_label.grid(row=6, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.rotate_entry = ctk.CTkEntry(self.first_frame, width=120)
    #     self.rotate_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    #     # Convert Button (Aligned, Green Color, Prominent)
    #     self.convert_button = ctk.CTkButton(self.first_frame, text="Convert",
    #                                         height=50, width=100, fg_color="green",  # Green for visibility
    #                                         command=self.convert_video)
    #     self.convert_button.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky="ew")


    # def build_video_conv_frame(self):
    #     """Build video conversion frame with improved layout and separate sections for single & batch processing."""
    #     self.first_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

    #     # Title Label
    #     title_label = ctk.CTkLabel(self.first_frame, text="Convert Video Formats",
    #                             font=ctk.CTkFont(size=34, weight="bold"))
    #     title_label.grid(row=0, column=0, columnspan=5, padx=5, pady=(10, 20), sticky="w")

    #     # -----------------------------------
    #     # 🔹 SINGLE FILE CONVERSION SECTION
    #     # -----------------------------------
    #     single_file_title = ctk.CTkLabel(self.first_frame, text="Single File Conversion",
    #                                     font=ctk.CTkFont(size=20, weight="bold"))
    #     single_file_title.grid(row=1, column=0, columnspan=5, padx=5, pady=15, sticky="w")

    #     # Select Input Video
    #     self.label = ctk.CTkLabel(self.first_frame, text="Select input video:")
    #     self.label.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.conv_entry = ctk.CTkEntry(self.first_frame, width=350)
    #     self.conv_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

    #     self.browse_button = ctk.CTkButton(self.first_frame, text="Browse",
    #                                     command=lambda: self.browse_file(self.conv_entry))
    #     self.browse_button.grid(row=2, column=3, padx=(5, 10), pady=5, sticky="ew")

    #     # Select Output File
    #     self.output_label = ctk.CTkLabel(self.first_frame, text="Save as:")
    #     self.output_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.conv_output_entry = ctk.CTkEntry(self.first_frame, width=350)
    #     self.conv_output_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

    #     self.save_as_button = ctk.CTkButton(self.first_frame, text="Save As",
    #                                         command=lambda: self.choose_output_dir(self.conv_output_entry))
    #     self.save_as_button.grid(row=3, column=3, padx=(5, 10), pady=5, sticky="ew")

    #     # **Video Settings (FPS, Bitrate, Rotation)**
    #     settings_title = ctk.CTkLabel(self.first_frame, text="Video Settings (Optional)",
    #                                 font=ctk.CTkFont(size=18, weight="bold"))
    #     settings_title.grid(row=4, column=0, columnspan=5, padx=5, pady=(15, 10), sticky="w")

    #     # FPS
    #     self.fps_label = ctk.CTkLabel(self.first_frame, text="FPS:")
    #     self.fps_label.grid(row=5, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.fps_entry = ctk.CTkEntry(self.first_frame, width=120)
    #     self.fps_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    #     # Bitrate
    #     self.bitrate_label = ctk.CTkLabel(self.first_frame, text="Bitrate:")
    #     self.bitrate_label.grid(row=6, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.bitrate_entry = ctk.CTkEntry(self.first_frame, width=120)
    #     self.bitrate_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    #     # Rotation
    #     self.rotate_label = ctk.CTkLabel(self.first_frame, text="Rotation (degrees):")
    #     self.rotate_label.grid(row=7, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.rotate_entry = ctk.CTkEntry(self.first_frame, width=120)
    #     self.rotate_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    #     # Extra Space Before Convert Button
    #     self.spacing_label = ctk.CTkLabel(self.first_frame, text="")
    #     self.spacing_label.grid(row=8, column=0, columnspan=3, pady=10)

    #     # Convert Button
    #     self.convert_single_button = ctk.CTkButton(self.first_frame, text="Convert File",
    #                                             height=75, width=150,
    #                                             fg_color="green",
    #                                             command=self.convert_video)
    #     self.convert_single_button.grid(row=5, column=2, rowspan=3, padx=5, pady=5, sticky="ns")

    #     # Extra Space Before Batch Processing Section
    #     self.spacing_label = ctk.CTkLabel(self.first_frame, text="")
    #     self.spacing_label.grid(row=9, column=0, columnspan=5, pady=20)

    #     # -----------------------------------
    #     # 🔹 BATCH PROCESSING SECTION
    #     # -----------------------------------
    #     batch_title = ctk.CTkLabel(self.first_frame, text="Batch Processing",
    #                             font=ctk.CTkFont(size=20, weight="bold"))
    #     batch_title.grid(row=10, column=0, columnspan=5, padx=5, pady=15, sticky="w")

    #     # Select Input Folder
    #     self.batch_folder_label = ctk.CTkLabel(self.first_frame, text="Select folder:")
    #     self.batch_folder_label.grid(row=11, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.batch_folder_entry = ctk.CTkEntry(self.first_frame, width=350)
    #     self.batch_folder_entry.grid(row=11, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

    #     self.batch_folder_button = ctk.CTkButton(self.first_frame, text="Browse",
    #                                             command=lambda: self.browse_folder(self.batch_folder_entry))
    #     self.batch_folder_button.grid(row=11, column=3, padx=(5, 10), pady=5, sticky="ew")

    #     # Select Output Folder
    #     self.batch_output_label = ctk.CTkLabel(self.first_frame, text="Output folder:")
    #     self.batch_output_label.grid(row=12, column=0, padx=(10, 5), pady=5, sticky="w")

    #     self.batch_output_entry = ctk.CTkEntry(self.first_frame, width=350)
    #     self.batch_output_entry.grid(row=12, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

    #     self.batch_output_button = ctk.CTkButton(self.first_frame, text="Select",
    #                                             command=lambda: self.choose_output_folder(self.batch_output_entry))
    #     self.batch_output_button.grid(row=12, column=3, padx=(5, 10), pady=5, sticky="ew")

    #     # Convert Button for Batch Processing
    #     self.convert_batch_button = ctk.CTkButton(self.first_frame, text="Convert Folder",
    #                                             height=75, width=150,
    #                                             fg_color="green",
    #                                             command=self.convert_batch_videos_gui)
    #     self.convert_batch_button.grid(row=11, column=4, rowspan=2, padx=10, pady=5, sticky="ns")



    def build_video_conv_frame(self):
        """Build video conversion frame with improved layout and separate sections for single & batch processing."""
        self.first_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Title Label
        title_label = ctk.CTkLabel(self.first_frame, text="Convert Video Formats",
                                font=ctk.CTkFont(size=34, weight="bold"))
        title_label.grid(row=0, column=0, columnspan=5, padx=5, pady=(10, 20), sticky="w")

        # -----------------------------------
        # 🔹 SINGLE FILE CONVERSION SECTION
        # -----------------------------------
        single_file_title = ctk.CTkLabel(self.first_frame, text="Single File Conversion",
                                        font=ctk.CTkFont(size=24, weight="bold"))
        single_file_title.grid(row=1, column=0, columnspan=5, padx=5, pady=15, sticky="w")

        # Select Input Video
        self.label = ctk.CTkLabel(self.first_frame, text="Select input video:")
        self.label.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")

        self.conv_entry = ctk.CTkEntry(self.first_frame, width=350)
        self.conv_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

        self.browse_button = ctk.CTkButton(self.first_frame, text="Browse",
                                        command=lambda: self.browse_file(self.conv_entry))
        self.browse_button.grid(row=2, column=3, padx=(5, 10), pady=5, sticky="ew")

        # Select Output File
        self.output_label = ctk.CTkLabel(self.first_frame, text="Save as:")
        self.output_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")

        self.conv_output_entry = ctk.CTkEntry(self.first_frame, width=350)
        self.conv_output_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

        self.save_as_button = ctk.CTkButton(self.first_frame, text="Save As",
                                            command=lambda: self.choose_output_dir(self.conv_output_entry))
        self.save_as_button.grid(row=3, column=3, padx=(5, 10), pady=5, sticky="ew")

        # Convert Button - Now Closer to Inputs
        self.convert_single_button = ctk.CTkButton(self.first_frame, text="Convert File",
                                                height=50, width=150,
                                                fg_color="green",
                                                command=self.convert_video)
        self.convert_single_button.grid(row=2, column=4, rowspan=2, padx=10, pady=5, sticky="ns")

        # **Video Settings (FPS, Bitrate, Rotation)**
        settings_title = ctk.CTkLabel(self.first_frame, text="Video Settings (Optional)",
                                    font=ctk.CTkFont(size=18, weight="bold"))
        settings_title.grid(row=4, column=0, columnspan=5, padx=5, pady=(15, 10), sticky="w")

        # FPS
        self.fps_label = ctk.CTkLabel(self.first_frame, text="FPS:")
        self.fps_label.grid(row=5, column=0, padx=(10, 5), pady=5, sticky="w")

        self.fps_entry = ctk.CTkEntry(self.first_frame, width=120)
        self.fps_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Bitrate
        self.bitrate_label = ctk.CTkLabel(self.first_frame, text="Bitrate:")
        self.bitrate_label.grid(row=6, column=0, padx=(10, 5), pady=5, sticky="w")

        self.bitrate_entry = ctk.CTkEntry(self.first_frame, width=120)
        self.bitrate_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        # Rotation
        self.rotate_label = ctk.CTkLabel(self.first_frame, text="Rotation (degrees):")
        self.rotate_label.grid(row=7, column=0, padx=(10, 5), pady=5, sticky="w")

        self.rotate_entry = ctk.CTkEntry(self.first_frame, width=120)
        self.rotate_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        # Extra Space Before Batch Processing Section
        self.spacing_label = ctk.CTkLabel(self.first_frame, text="")
        self.spacing_label.grid(row=8, column=0, columnspan=5, pady=20)

        # -----------------------------------
        # 🔹 BATCH PROCESSING SECTION
        # -----------------------------------
        batch_title = ctk.CTkLabel(self.first_frame, text="Batch Processing",
                                font=ctk.CTkFont(size=24, weight="bold"))
        batch_title.grid(row=9, column=0, columnspan=5, padx=5, pady=15, sticky="w")

        # Select Input Folder
        self.batch_folder_label = ctk.CTkLabel(self.first_frame, text="Select folder:")
        self.batch_folder_label.grid(row=10, column=0, padx=(10, 5), pady=5, sticky="w")

        self.batch_folder_entry = ctk.CTkEntry(self.first_frame, width=350)
        self.batch_folder_entry.grid(row=10, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

        self.batch_folder_button = ctk.CTkButton(self.first_frame, text="Browse",
                                                command=lambda: self.browse_folder(self.batch_folder_entry))
        self.batch_folder_button.grid(row=10, column=3, padx=(5, 10), pady=5, sticky="ew")

        # Select Output Folder
        self.batch_output_label = ctk.CTkLabel(self.first_frame, text="Output folder:")
        self.batch_output_label.grid(row=11, column=0, padx=(10, 5), pady=5, sticky="w")

        self.batch_output_entry = ctk.CTkEntry(self.first_frame, width=350)
        self.batch_output_entry.grid(row=11, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

        self.batch_output_button = ctk.CTkButton(self.first_frame, text="Select",
                                                command=lambda: self.choose_output_folder(self.batch_output_entry))
        self.batch_output_button.grid(row=11, column=3, padx=(5, 10), pady=5, sticky="ew")

        # **Batch Processing Video Settings**
        batch_settings_title = ctk.CTkLabel(self.first_frame, text="Video Settings (Optional)",
                                            font=ctk.CTkFont(size=18, weight="bold"))
        batch_settings_title.grid(row=12, column=0, columnspan=5, padx=5, pady=(15, 10), sticky="w")

        # FPS (Batch)
        self.batch_fps_label = ctk.CTkLabel(self.first_frame, text="FPS:")
        self.batch_fps_label.grid(row=13, column=0, padx=(10, 5), pady=5, sticky="w")

        self.batch_fps_entry = ctk.CTkEntry(self.first_frame, width=120)
        self.batch_fps_entry.grid(row=13, column=1, padx=5, pady=5, sticky="w")

        # Bitrate (Batch)
        self.batch_bitrate_label = ctk.CTkLabel(self.first_frame, text="Bitrate:")
        self.batch_bitrate_label.grid(row=14, column=0, padx=(10, 5), pady=5, sticky="w")

        self.batch_bitrate_entry = ctk.CTkEntry(self.first_frame, width=120)
        self.batch_bitrate_entry.grid(row=14, column=1, padx=5, pady=5, sticky="w")

        # Rotation (Batch)
        self.batch_rotate_label = ctk.CTkLabel(self.first_frame, text="Rotation (degrees):")
        self.batch_rotate_label.grid(row=15, column=0, padx=(10, 5), pady=5, sticky="w")

        self.batch_rotate_entry = ctk.CTkEntry(self.first_frame, width=120)
        self.batch_rotate_entry.grid(row=15, column=1, padx=5, pady=5, sticky="w")

        # Convert Button for Batch Processing
        self.convert_batch_button = ctk.CTkButton(self.first_frame, text="Convert Folder",
                                                height=50, width=150,
                                                fg_color="green",
                                                command=self.convert_batch_videos_gui)
        self.convert_batch_button.grid(row=10, column=4, rowspan=2, padx=10, pady=5, sticky="ns")


    def build_cut_movie_frame(self):
        """Build up movie cut frame with consistent alignment and spacing."""
        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Title Label
        title_label = ctk.CTkLabel(self.second_frame, text="Cut Video Clip",
                                font=ctk.CTkFont(size=34, weight="bold"))
        title_label.grid(row=0, column=0, columnspan=4, padx=5, pady=(10, 20), sticky="w")  # Added bottom padding for spacing

        # Select Input Video
        self.label = ctk.CTkLabel(self.second_frame, text="Select input video:")
        self.label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="w")  # Left-aligned

        self.cut_entry = ctk.CTkEntry(self.second_frame, width=350)
        self.cut_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

        self.browse_button = ctk.CTkButton(self.second_frame, text="Browse",
                                        command=lambda: self.browse_file(self.cut_entry))
        self.browse_button.grid(row=1, column=3, padx=(5, 10), pady=5, sticky="ew")

        # Select Output Directory
        self.output_label = ctk.CTkLabel(self.second_frame, text="Output directory:")
        self.output_label.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")

        self.cut_output_entry = ctk.CTkEntry(self.second_frame, width=350)
        self.cut_output_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

        self.save_as_button = ctk.CTkButton(self.second_frame, text="Save As",
                                            command=lambda: self.choose_output_dir(self.cut_output_entry))
        self.save_as_button.grid(row=2, column=3, padx=(5, 10), pady=5, sticky="ew")

        # Select Start Time
        self.start_time_label = ctk.CTkLabel(self.second_frame, text="Start time (seconds):")
        self.start_time_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")

        self.start_time_entry = ctk.CTkEntry(self.second_frame, width=120)
        self.start_time_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Select End Time
        self.end_time_label = ctk.CTkLabel(self.second_frame, text="End time (seconds):")
        self.end_time_label.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="w")  # Placed on same row for better layout

        self.end_time_entry = ctk.CTkEntry(self.second_frame, width=120)
        self.end_time_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Convert Button (Properly Aligned)
        self.convert_button = ctk.CTkButton(self.second_frame, text="Cut Movie",
                                            height=65, width=150, fg_color="green",  # Green for emphasis
                                            command=self.cut_movie_between_start_and_stop)
        self.convert_button.grid(row=3, column=2, columnspan=1, rowspan=3, padx=0, pady=10, sticky="ew")


    def build_heic_to_jpg_frame(self):
        """ Build HEIC to JPG frame """
        self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Main Title
        title_label = ctk.CTkLabel(self.third_frame, text="HEIC to JPG Converter",
                                font=ctk.CTkFont(size=34, weight="bold"))
        title_label.grid(row=0, column=0, columnspan=4, padx=5, pady=15, sticky="w")

        # -----------------------------------
        # 🔹 SINGLE FILE CONVERSION SECTION
        # -----------------------------------
        single_file_title = ctk.CTkLabel(self.third_frame, text="Single File Conversion",
                                        font=ctk.CTkFont(size=20, weight="bold"))
        single_file_title.grid(row=1, column=0, columnspan=4, padx=5, pady=20, sticky="w")

        # Select HEIC File
        self.heic_file_label = ctk.CTkLabel(self.third_frame, text="Select HEIC file:")
        self.heic_file_label.grid(row=2, column=0, padx=5, pady=5)

        self.heic_file_entry = ctk.CTkEntry(self.third_frame, width=350)
        self.heic_file_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

        self.heic_file_button = ctk.CTkButton(self.third_frame, text="Browse",
                                            command=lambda: self.browse_file(self.heic_file_entry))
        self.heic_file_button.grid(row=2, column=3, padx=5, pady=5)

        # Select Output File
        self.output_file_label = ctk.CTkLabel(self.third_frame, text="Save as:")
        self.output_file_label.grid(row=3, column=0, padx=5, pady=5)

        self.output_file_entry = ctk.CTkEntry(self.third_frame, width=350)
        self.output_file_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

        self.output_file_button = ctk.CTkButton(self.third_frame, text="Save As",
                                                command=lambda: self.choose_output_file(self.output_file_entry))
        self.output_file_button.grid(row=3, column=3, padx=5, pady=5)

        # Convert Button (Aligned Right and Same Height as Input/Output Buttons)
        self.convert_single_button = ctk.CTkButton(self.third_frame, text="Convert File",
                                                height=75, width=150,
                                                fg_color = "green",
                                                command=self.convert_single_heic)
        self.convert_single_button.grid(row=2, column=4, rowspan=2, padx=10, pady=5, sticky="ns")

        # Extra Space Between Single and Batch Sections
        self.spacing_label = ctk.CTkLabel(self.third_frame, text="")  # Empty label for spacing
        self.spacing_label.grid(row=4, column=0, columnspan=5, pady=20)  # Extra padding

        # -----------------------------------
        # 🔹 BATCH PROCESSING SECTION
        # -----------------------------------
        batch_title = ctk.CTkLabel(self.third_frame, text="Batch Processing",
                                font=ctk.CTkFont(size=20, weight="bold"))
        batch_title.grid(row=5, column=0, columnspan=4, padx=5, pady=10, sticky="w")

        # Select Folder
        self.heic_folder_label = ctk.CTkLabel(self.third_frame, text="Select Folder:")
        self.heic_folder_label.grid(row=6, column=0, padx=5, pady=5)

        self.heic_folder_entry = ctk.CTkEntry(self.third_frame, width=350)
        self.heic_folder_entry.grid(row=6, column=1, padx=5, pady=5, columnspan=2)

        self.heic_folder_button = ctk.CTkButton(self.third_frame, text="Browse",
                                                command=lambda: self.browse_folder(self.heic_folder_entry))
        self.heic_folder_button.grid(row=6, column=3, padx=5, pady=5)

        # Select Output Folder
        self.output_folder_label = ctk.CTkLabel(self.third_frame, text="Output Folder:")
        self.output_folder_label.grid(row=7, column=0, padx=5, pady=5)

        self.output_folder_entry = ctk.CTkEntry(self.third_frame, width=350)
        self.output_folder_entry.grid(row=7, column=1, padx=5, pady=5, columnspan=2)

        self.output_folder_button = ctk.CTkButton(self.third_frame, text="Select",
                                                command=lambda: self.choose_output_folder(self.output_folder_entry))
        self.output_folder_button.grid(row=7, column=3, padx=5, pady=5)

        # Convert Button (Aligned Right and Same Height as Input/Output Buttons)
        self.convert_batch_button = ctk.CTkButton(self.third_frame, text="Convert Folder",
                                                height=75, width=150,
                                                fg_color = "green",
                                                command=self.convert_batch_heic)
        self.convert_batch_button.grid(row=6, column=4, rowspan=2, padx=10, pady=5, sticky="ns")



    def choose_output_file(self, output_entry):
        """Opens a file dialog to select the output file location."""
        output_file = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG files", "*.jpg")])
        if output_file:
            output_entry.delete(0, "end")
            output_entry.insert(0, output_file)

    def choose_output_folder(self, output_entry):
        """Opens a directory dialog to select the output folder."""
        output_folder = filedialog.askdirectory()
        if output_folder:
            output_entry.delete(0, "end")
            output_entry.insert(0, output_folder)


    def convert_single_heic(self):
        input_file = self.heic_file_entry.get()
        output_file = self.output_file_entry.get()  # Get user-defined output file
        if not input_file or not output_file:
            messagebox.showerror("Error", "Please select both input and output files.")
            return
        success = convert_heic_to_jpg(input_file, output_file)
        if success:
            messagebox.showinfo("Success", "File converted successfully!")

    def convert_batch_heic(self):
        folder_path = self.heic_folder_entry.get()
        output_folder = self.output_folder_entry.get()  # Get user-defined output folder
        if not folder_path or not output_folder:
            messagebox.showerror("Error", "Please select both input and output folders.")
            return
        success = convert_heic_to_jpg(folder_path, output_folder)
        if success:
            messagebox.showinfo("Success", "Batch conversion completed!")


    def browse_file(self, entry_widget):
        filename = filedialog.askopenfilename()
        entry_widget.delete(0, "end")
        entry_widget.insert(0, filename)

    def browse_folder(self, entry_widget):
        """Opens a folder dialog and inserts the selected path into the entry widget."""
        folder_path = filedialog.askdirectory()
        if folder_path:
            entry_widget.delete(0, "end")
            entry_widget.insert(0, folder_path)


    def choose_output_dir(self, output_entry):
        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[
            ("MP4 files", "*.mp4"),
            ("MOV files", "*.mov"),
            ("AVI files", "*.avi"),
            ("MKV files", "*.mkv")
        ])
        if output_file:
            output_entry.delete(0, "end")
            output_entry.insert(0, output_file)


    def convert_video(self):
        """
        Main method for triggering the
        file conversion.
        """
        input_file = self.conv_entry.get()
        output_dir = self.conv_output_entry.get()
        bitrate = str(self.bitrate_entry.get()) if self.bitrate_entry.get() else None
        fps = int(self.fps_entry.get()) if self.fps_entry.get() else None
        rotate_degrees = int(self.rotate_entry.get()) if self.rotate_entry.get() else None
        success = convert_video_file(input_file, output_dir, bitrate=bitrate, fps=fps, rotate_degrees=rotate_degrees)

        if not input_file or not output_dir:
            messagebox.showerror("Error", "Please select both input and output folders.")
            return
        if success:
            messagebox.showinfo("Conversion Complete", "Video conversion completed successfully.")
        else:
            messagebox.showerror("Conversion Failed", "An error occurred during video conversion.")


    def convert_batch_videos_gui(self):
        """
        GUI-triggered batch video conversion.
        """
        input_folder = self.batch_folder_entry.get()
        output_folder = self.batch_output_entry.get()
        bitrate = str(self.batch_bitrate_entry.get()) if self.batch_bitrate_entry.get() else None
        fps = int(self.batch_fps_entry.get()) if self.batch_fps_entry.get() else None
        rotate_degrees = int(self.batch_rotate_entry.get()) if self.batch_rotate_entry.get() else None

        if not input_folder or not output_folder:
            messagebox.showerror("Error", "Please select both input and output folders.")
            return

        # Perform batch video conversion
        success = convert_batch_videos(input_folder, output_folder, bitrate=bitrate, fps=fps, rotate_degrees=rotate_degrees)

        if success:
            messagebox.showinfo("Conversion Complete", "Batch video conversion completed successfully!")
        else:
            messagebox.showerror("Conversion Failed", "An error occurred during batch conversion.")



    def cut_movie_between_start_and_stop(self):
        input_file = self.cut_entry.get()
        output_file = self.cut_output_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()
        success = cut_movie(input_file=input_file, output_file=output_file, start_time=start_time, end_time=end_time)
        if success:
            messagebox.showinfo("Cutting complete", "Cutting the video completed successfully!")
        else:
            messagebox.ERROR("Aarnes Tool failed big time! Time to breathe..")



    # def convert_video(self):
    #     """
    #     Main method for triggering the
    #     file conversion.
    #     """
    #     input_file = r"{}".format(self.conv_entry.get())
    #     output_dir = r"{}".format(self.conv_output_entry.get())
    #     bitrate = int(self.bitrate_entry.get()) if self.bitrate_entry.get() else None
    #     fps = int(self.fps_entry.get()) if self.fps_entry.get() else None
    #     rotate_degrees = int(self.rotate_entry.get()) if self.rotate_entry.get() else None

    #     # Redirect stdout to a new Text widget
    #     output_window = ctk.CTk()
    #     output_window.title("Conversion Output")
    #     output_text = Text(output_window, wrap='word', font=('Helvetica', 10))
    #     output_text.pack(expand=True, fill='both')
    #     scrollbar = ctk.CTkScrollbar(output_window, command=output_text.yview)
    #     scrollbar.pack(side='right', fill='y')
    #     output_text['yscrollcommand'] = scrollbar.set

    #     sys.stdout = output_text

    #     Convert_MOV_2_MP4(input_file, output_dir, bitrate=bitrate, fps=fps, rotate_degrees=rotate_degrees)

    #     # Restore stdout and show message box after conversion is finished
    #     sys.stdout = sys.__stdout__
    #     messagebox.showinfo("Conversion Complete", "Video conversion completed successfully.")




if __name__ == "__main__":
    app = App()
    app.mainloop()

