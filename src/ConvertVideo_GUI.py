import os
from tkinter import filedialog, Menu, messagebox, simpledialog
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkOptionMenu
from VideoMod import convert_video_file, cut_movie

import customtkinter
customtkinter.set_appearance_mode("dark")

class VideoConverterApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Video Converter")
        self.center_window()
        self.create_menu()
        self.create_widgets()

    def center_window(self):
        # Calculate the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the window width and height
        window_width = 800
        window_height = 600

        # Calculate the x and y coordinates for the window to be centered
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window dimensions and position
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_menu(self):
        # menubar = Menu(self)
        # self.config(menu=menubar)

        # # File menu
        # file_menu = Menu(menubar, tearoff=0)
        # file_menu.add_command(label="Exit", command=self.exit_app)
        # menubar.add_cascade(label="File", menu=file_menu)

        # # Tools menu
        # tools_menu = Menu(menubar, tearoff=0)
        # tools_menu.add_command(label="Convert MOV to MP4", command=self.convert_video)
        # tools_menu.add_command(label="Cut movie file", command=self.cut_movie)
        # menubar.add_cascade(label="Tools", menu=tools_menu)

        # # Test CUSTOM PH
        optionmenu = customtkinter.CTkOptionMenu(self, values=["option 1", "option 2"],
                                         command=self.exit_app)
        optionmenu.set("option 2")

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.destroy()

    def create_widgets(self):
        self.label = CTkLabel(self, text="Select input video:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry = CTkEntry(self, width=350)  # Adjusted width here
        self.entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

        self.browse_button = CTkButton(self, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=3, padx=5, pady=5)

        self.output_label = CTkLabel(self, text="Output directory:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5)

        self.output_entry = CTkEntry(self, width=350)
        self.output_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

        self.save_as_button = CTkButton(self, text="Save As", command=self.choose_output_dir)
        self.save_as_button.grid(row=1, column=3, padx=5, pady=5)

        self.fps_label = CTkLabel(self, text="FPS:")
        self.fps_label.grid(row=2, column=0, padx=5, pady=5)

        self.fps_entry = CTkEntry(self)
        self.fps_entry.grid(row=2, column=1, padx=5, pady=5)

        self.bitrate_label = CTkLabel(self, text="Bitrate:")
        self.bitrate_label.grid(row=3, column=0, padx=5, pady=5)

        self.bitrate_entry = CTkEntry(self)
        self.bitrate_entry.grid(row=3, column=1, padx=5, pady=5)

        self.rotate_label = CTkLabel(self, text="Rotation (degrees):")
        self.rotate_label.grid(row=4, column=0, padx=5, pady=5)

        self.rotate_entry = CTkEntry(self)
        self.rotate_entry.grid(row=4, column=1, padx=5, pady=5)

        self.convert_button = CTkButton(self, text="Convert", command=self.convert_video)
        self.convert_button.grid(row=5, column=1, padx=5, pady=5)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.entry.delete(0, "end")
        self.entry.insert(0, filename)

    def choose_output_dir(self):
        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if output_file:
            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, output_file)

    def convert_video(self):
        input_file = self.entry.get()
        output_dir = self.output_entry.get()
        bitrate = int(self.bitrate_entry.get()) if self.bitrate_entry.get() else None
        fps = int(self.fps_entry.get()) if self.fps_entry.get() else None
        rotate_degrees = int(self.rotate_entry.get()) if self.rotate_entry.get() else None
        convert_video_file(input_file, output_dir, bitrate=bitrate, fps=fps, rotate_degrees=rotate_degrees)
        # Show message box after conversion is finished
        messagebox.showinfo("Conversion Complete", "Video conversion completed successfully.")

    def cut_movie(self):
        # Retrieve input parameters
        input_file = self.entry.get()
        start_time = self.ask_time("Start Time")
        end_time = self.ask_time("End Time")

        # Perform the cut operation
        # (Add your implementation here)
        cut_movie()

        messagebox.showinfo("Cut Movie", "Movie has been cut successfully.")

    def ask_time(self, prompt):
        while True:
            time = simpledialog.askstring(prompt, "Enter time in format HH:MM:SS")
            if time:
                return time.strip()

if __name__ == "__main__":
    app = VideoConverterApp()
    app.mainloop()
