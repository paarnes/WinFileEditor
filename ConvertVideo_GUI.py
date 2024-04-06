
from tkinter import filedialog
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
from VideoMod import Convert_MOV_2_MP4

class VideoConverterApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Video Converter")
        self.create_widgets()

    def create_widgets(self):
        self.label = CTkLabel(self, text="Select input video:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry = CTkEntry(self, width=350)  # Adjusted width here
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.browse_button = CTkButton(self, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        self.fps_label = CTkLabel(self, text="FPS:")
        self.fps_label.grid(row=1, column=0, padx=5, pady=5)

        self.fps_entry = CTkEntry(self)
        self.fps_entry.grid(row=1, column=1, padx=5, pady=5)

        self.bitrate_label = CTkLabel(self, text="Bitrate:")
        self.bitrate_label.grid(row=2, column=0, padx=5, pady=5)

        self.bitrate_entry = CTkEntry(self)
        self.bitrate_entry.grid(row=2, column=1, padx=5, pady=5)

        self.rotate_label = CTkLabel(self, text="Rotation (degrees):")
        self.rotate_label.grid(row=3, column=0, padx=5, pady=5)

        self.rotate_entry = CTkEntry(self)
        self.rotate_entry.grid(row=3, column=1, padx=5, pady=5)

        self.convert_button = CTkButton(self, text="Convert", command=self.convert_video)
        self.convert_button.grid(row=4, column=1, padx=5, pady=5)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.entry.delete(0, "end")
        self.entry.insert(0, filename)

    def convert_video(self):
        input_file = self.entry.get()
        bitrate = int(self.bitrate_entry.get()) if self.bitrate_entry.get() else None
        fps = int(self.fps_entry.get()) if self.fps_entry.get() else None
        rotate_degrees = int(self.rotate_entry.get()) if self.rotate_entry.get() else None
        Convert_MOV_2_MP4(input_file, bitrate=bitrate, fps=fps, rotate_degrees=rotate_degrees)

if __name__ == "__main__":
    app = VideoConverterApp()
    app.mainloop()
