<<<<<<< Updated upstream
#region imports
=======
>>>>>>> Stashed changes
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.constants import HORIZONTAL

from keras.models import load_model
from keras.preprocessing.image import save_img
from keras_preprocessing.image.utils import img_to_array, load_img

from predict import predict
from image_viewer import ImageViewer
#endregion

class MainApp(tk.Tk): 
    def __init__(self):
        
        #region initialize tk app
        super().__init__()
        #endregion
        
        #region menu bar
        self.menu_bar = tk.Menu(self)

        #region file_menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New Workspace", command=self.placeholder)
        self.file_menu.add_command(label="New Window", command=self.placeholder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Open Image(s)", command=self.placeholder)
        self.file_menu.add_command(label="Open Directory", command=self.placeholder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.placeholder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Preferences", command=self.placeholder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=lambda: self.destroy())
        self.menu_bar.add_cascade(label="File", menu = self.file_menu)
        #endregion
        
        #region options_menu
        #endregion
        #endregion

        #region model frame
        self.model_frame = tk.LabelFrame(self, text = "Model Selection", padx=10, pady=10)
        self.model_frame.grid(row=0, column=0, padx=10, pady=10)
        
        self.model_list = [model.name for model in os.scandir("./models")]
        self.model_selected = tk.StringVar()
        self.model_selected.set(self.model_list[0])
        self.model_dropdown = tk.OptionMenu(self.model_frame, self.model_selected, *self.model_list)
        self.model_dropdown.bind("<Button-1>", self.model_dropdown_clicked)
        self.model_dropdown.pack(pady=5)

        self.model_threshold_slider = tk.Scale(self.model_frame, from_=0, to=1, resolution=0.01, orient=HORIZONTAL)
        self.model_threshold_slider.pack(pady=5)
        self.model_threshold_slider.set(0.5)
        #endregion
        
        #region directory frame
        self.directory_frame = tk.LabelFrame(self, text = "Directory", padx=10, pady=10)
        self.directory_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.img_paths_field = tk.Entry(self.directory_frame, width=50)
        self.img_paths_field.grid(row=0, column=0)

        self.img_paths = None
        self.img_paths_button = tk.Button(self.directory_frame, text="Open", command=lambda: self.get_img_paths()).grid(row=0, column=1)

        self.destination_path_field = tk.Entry(self.directory_frame, width=50)
        self.destination_path_field.grid(row=1, column=0)

        self.destination_path_button = tk.Button(self.directory_frame, text="Open", command=lambda: self.get_save_path()).grid(row=1, column=1)
        #endregion

        #region run frame
        self.run_frame = tk.LabelFrame(self, text = "Run", padx=10, pady=10)
        self.run_frame.grid(row=0, column=1, padx=10, pady=10)

        self.run_button = tk.Button(self.run_frame, text="Run", command=self.run).grid(row=0, column=0)
        #endregion
        
        #region final configuration
        self.title("Command Palette")
        self.config(menu=self.menu_bar)
        self.mainloop()
        #endregion

    def placeholder(self):
        img_viewer = ImageViewer(self)
        img_viewer.mainloop()
    
    def model_dropdown_clicked(self, event):
        menu = self.model_dropdown["menu"]
        menu.delete(0, "end")
        for model in os.scandir("./models"):
            menu.add_command(label=model.name, command=lambda value = model.name: self.model_selected.set(value))

    def get_img_paths(self):
        self.img_paths = list(filedialog.askopenfilenames(initialdir="C:/", title="Images"))
        self.img_paths_field.delete(0, len(self.img_paths_field.get()))
        self.img_paths_field.insert(0, str(self.img_paths))

    def get_save_path(self):
        save_path = filedialog.askdirectory(initialdir="C:/", title="Save Directory")
        self.destination_path_field.delete(0, len(self.destination_path_field.get()))
        self.destination_path_field.insert(0, save_path)
        
    def run(self): 
        model = load_model("./models/" + self.model_selected.get())
        for i, img_path in enumerate(self.img_paths):
<<<<<<< Updated upstream
            img_array = img_to_array(load_img(img_path, color_mode="grayscale"))/255
            pred = predict(img_array, model, self.model_threshold_slider.get())
            save_img(self.destination_path_field.get() + "/" + str(i) + ".png", pred)
=======
            pred = predict(model, self.model_threshold_slider.get(), img_path)
            save_img(self.destination_path_field.get() + "/" + os.path.splitext(img_path.split("/")[-1])[0] + ".png", pred)
>>>>>>> Stashed changes
