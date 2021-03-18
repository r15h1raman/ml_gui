import tkinter as tk
from tkinter import filedialog
from tkinter.constants import HORIZONTAL

from keras.models import load_model
from keras.preprocessing.image import save_img
from predict import predict

class MainApp(tk.Tk): 
    def __init__(self):
        
        #region initialize tk app
        super().__init__()
        #endregion
        
        #region model frame
        self.model_frame = tk.LabelFrame(self, text = "Model Selection", padx=10, pady=10)
        self.model_frame.grid(row=0, column=0, padx=10, pady=10)
        
        self.model_selected = tk.StringVar()
        self.model_selected.set("model")
        self.model_dropdown = tk.OptionMenu(self.model_frame, self.model_selected, "model_2")
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
    
    def get_img_paths(self):
        self.img_paths = list(filedialog.askopenfilenames(initialdir="C:/", title="Images"))
        self.img_paths_field.delete(0, len(self.img_paths_field.get()))
        self.img_paths_field.insert(0, str(self.img_paths))

    def get_save_path(self):
        save_path = filedialog.askdirectory(initialdir="C:/", title="Save Directory")
        self.destination_path_field.delete(0, len(self.destination_path_field.get()))
        self.destination_path_field.insert(0, save_path)
        
    def run(self): 
        model = load_model(self.model_selected.get())
        for i, img_path in enumerate(self.img_paths):
            pred = predict(model, self.model_threshold_slider.get(), img_path)
            save_img(self.destination_path_field.get() + "/" + str(i) + ".png", pred)