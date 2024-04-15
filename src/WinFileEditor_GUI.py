import customtkinter as ctk
import os
from tkinter import filedialog, messagebox
from PIL import Image
from VideoMod import Convert_MOV_2_MP4, cut_movie

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

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

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Aarnes Editor", image=self.logo_image,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)


        # Frame 2
        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Convert Video",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.video_conv_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        # Frame 3
        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cut Video",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.video_cut_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        # create second frame
        self.build_video_conv_frame()

        # create third frame
        self.build_cut_movie_frame()

        # select default frame
        self.select_frame_by_name("frame_2")

    def select_frame_by_name(self, name):
        """ set button color for selected button """
        # self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        # if name == "home":
        #     self.home_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)



    def build_video_conv_frame(self):
        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.label = ctk.CTkLabel(self.second_frame, text="Select input video:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.conv_entry = ctk.CTkEntry(self.second_frame, width=350)  # Adjusted width here
        self.conv_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

        # self.browse_button = ctk.CTkButton(self.second_frame, text="Browse", command=self.browse_file)
        self.browse_button = ctk.CTkButton(self.second_frame, text="Browse", command=lambda: self.browse_file(self.conv_entry))

        self.browse_button.grid(row=0, column=3, padx=5, pady=5)

        self.output_label = ctk.CTkLabel(self.second_frame, text="Output directory:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5)

        self.conv_output_entry = ctk.CTkEntry(self.second_frame, width=350)
        self.conv_output_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

        # self.save_as_button = ctk.CTkButton(self.second_frame, text="Save As", command=self.choose_output_dir)
        self.save_as_button = ctk.CTkButton(self.second_frame, text="Save As", command=lambda: self.choose_output_dir(self.conv_output_entry))

        self.save_as_button.grid(row=1, column=3, padx=5, pady=5)

        self.fps_label = ctk.CTkLabel(self.second_frame, text="FPS:")
        self.fps_label.grid(row=2, column=0, padx=5, pady=5)

        self.fps_entry = ctk.CTkEntry(self.second_frame)
        self.fps_entry.grid(row=2, column=1, padx=5, pady=5)

        self.bitrate_label = ctk.CTkLabel(self.second_frame, text="Bitrate:")
        self.bitrate_label.grid(row=3, column=0, padx=5, pady=5)

        self.bitrate_entry = ctk.CTkEntry(self.second_frame)
        self.bitrate_entry.grid(row=3, column=1, padx=5, pady=5)

        self.rotate_label = ctk.CTkLabel(self.second_frame, text="Rotation (degrees):")
        self.rotate_label.grid(row=4, column=0, padx=5, pady=5)

        self.rotate_entry = ctk.CTkEntry(self.second_frame)
        self.rotate_entry.grid(row=4, column=1, padx=5, pady=5)

        self.convert_button = ctk.CTkButton(self.second_frame, text="Convert", command=self.convert_video)
        self.convert_button.grid(row=5, column=1, padx=5, pady=5)


    def build_cut_movie_frame(self):
        """Build up movie cut frame"""
        self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.label = ctk.CTkLabel(self.third_frame, text="Select input video:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.cut_entry = ctk.CTkEntry(self.third_frame, width=350)  # Adjusted width here
        self.cut_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

        # self.browse_button = ctk.CTkButton(self.third_frame, text="Browse", command=self.browse_file)
        self.browse_button = ctk.CTkButton(self.third_frame, text="Browse", command=lambda: self.browse_file(self.cut_entry))
        self.browse_button.grid(row=0, column=3, padx=5, pady=5)

        self.output_label = ctk.CTkLabel(self.third_frame, text="Output directory:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5)

        self.cut_output_entry = ctk.CTkEntry(self.third_frame, width=350)
        self.cut_output_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

        # self.save_as_button = ctk.CTkButton(self.third_frame, text="Save As", command=self.choose_output_dir)
        self.save_as_button = ctk.CTkButton(self.third_frame, text="Save As", command=lambda: self.choose_output_dir(self.cut_output_entry))
        self.save_as_button.grid(row=1, column=3, padx=5, pady=5)

        self.start_time_label = ctk.CTkLabel(self.third_frame, text="Start time:")
        self.start_time_label.grid(row=2, column=0, padx=5, pady=5)

        self.start_time_entry = ctk.CTkEntry(self.third_frame)
        self.start_time_entry.grid(row=2, column=1, padx=5, pady=5)

        self.end_time_label = ctk.CTkLabel(self.third_frame, text="End time:")
        self.end_time_label.grid(row=3, column=0, padx=5, pady=5)

        self.end_time_entry = ctk.CTkEntry(self.third_frame)
        self.end_time_entry.grid(row=3, column=1, padx=5, pady=5)

        self.convert_button = ctk.CTkButton(self.third_frame, text="Cut Movie", command=cut_movie)
        self.convert_button.grid(row=4, column=1, padx=5, pady=5)



    # def browse_file(self):
    #     filename = filedialog.askopenfilename()
    #     self.entry.delete(0, "end")
    #     self.entry.insert(0, filename)
    def browse_file(self, entry_widget):
        filename = filedialog.askopenfilename()
        entry_widget.delete(0, "end")
        entry_widget.insert(0, filename)

    # def choose_output_dir(self):
    #     output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    #     if output_file:
    #         self.output_entry.delete(0, "end")
    #         self.output_entry.insert(0, output_file)
    def choose_output_dir(self, output_entry):
        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if output_file:
            output_entry.delete(0, "end")
            output_entry.insert(0, output_file)


    def convert_video(self):
        input_file = self.conv_entry.get()
        output_dir = self.conv_output_entry.get()
        bitrate = int(self.bitrate_entry.get()) if self.bitrate_entry.get() else None
        fps = int(self.fps_entry.get()) if self.fps_entry.get() else None
        rotate_degrees = int(self.rotate_entry.get()) if self.rotate_entry.get() else None
        Convert_MOV_2_MP4(input_file, output_dir, bitrate=bitrate, fps=fps, rotate_degrees=rotate_degrees)
        # Show message box after conversion is finished
        messagebox.showinfo("Conversion Complete", "Video conversion completed successfully.")




if __name__ == "__main__":
    app = App()
    app.mainloop()

