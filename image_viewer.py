import tkinter as tk

class ImageViewer(tk.Toplevel):
    def __init__(self, main_app):
        
        #region initialize window
        super().__init__(main_app)
        #endregion
        
        #region menu bar
        self.menu_bar = tk.Menu(self)

        #region file_menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=lambda: self.destroy())
        self.menu_bar.add_cascade(label="File", menu = self.file_menu)
        #endregion
        #endregion

        #region list dropdowns and load buttons
        self.left_list = tk.StringVar()
        self.left_list_dropdown = tk.OptionMenu(self, self.left_list, "list_1")
        self.left_list_dropdown.grid(row=0, column=1)

        self.left_list_load_button = tk.Button(self, text="Load").grid(row=0, column=2)
        
        self.right_list = tk.StringVar()
        self.right_list_dropdown = tk.OptionMenu(self, self.right_list, "list_2")
        self.right_list_dropdown.grid(row=0, column=4)
        
        self.right_list_load_button = tk.Button(self, text="Load").grid(row=0, column=5)
        #endregion

        #region image labels
        self.left_image = tk.Label(self, text="left img")
        self.left_image.grid(row=1, column=0, columnspan=3)
        
        self.right_image = tk.Label(self, text="right img")
        self.right_image.grid(row=1, column=3, columnspan=3)
        #endregion

        #region list navigation
        self.left_image_back_button = tk.Button(self, text="<").grid(row=2, column=0)
        
        self.left_list_images = tk.StringVar()
        self.left_list_images_dropdown = tk.OptionMenu(self, self.left_list_images, "left images")
        self.left_list_images_dropdown.grid(row=2 , column=1)

        self.left_image_forward_button = tk.Button(self, text=">").grid(row=2, column=2)

        self.right_image_back_button = tk.Button(self, text="<").grid(row=2, column=3)
        
        self.right_list_images = tk.StringVar()
        self.right_list_images_dropdown = tk.OptionMenu(self, self.right_list_images, "right images")
        self.right_list_images_dropdown.grid(row=2 , column=4)

        self.right_image_forward_button = tk.Button(self, text=">").grid(row=2, column=5)
        #endregion
        
        #region final configuration
        self.title("Image Viewer")
        self.config(menu=self.menu_bar)
        #endregion