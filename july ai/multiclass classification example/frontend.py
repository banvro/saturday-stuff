import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import joblib
# ImageOps
from PIL import ImageOps

model = joblib.load("image_classification.joblib")

def uploadimage():
    filepath = filedialog.askopenfilename()
    open_image = Image.open(filepath)
    #only to show image
    open_image_resize  = open_image.resize((400, 400))
    img = ImageTk.PhotoImage(open_image_resize)
    lblim.config(image = img)
    lblim.image = img

    imaggary = ImageOps.grayscale(open_image)
    imgs28 = imaggary.resize((28, 28))
    image_array = np.array(imgs28)
    
    flat_image = image_array.flatten()
    # print(flat_image, "xxxxxxxxxx")
    flat_image = flat_image.reshape(1, -1)
    result = model.predict(flat_image)

    print(result, "eeeeeeeeeee")
    lblshow.config(text = f"the uplaod image label is : {result[0]}")
    # imsge_reshap = image_array.



app = tk.Tk()
app.geometry("700x600")
app.title("Image Classification")
app.config(background = "#c4c3be")

lbl = tk.Label(app, text = "Image Classification", font = ("robort", 30, "bold"), bg = "black", fg = "white")
lbl.pack(fill = "x", ipady = 7)

lblim = tk.Label(app, background = "#c4c3be")
lblim.pack(pady = 16)


btn = tk.Button(app, text = "Upload Image", font = ("robort", 20, "bold"), background = "black", fg = "white", command = uploadimage)
btn.pack()

lblshow = tk.Label(app, text = "dbadka", font = ("robort", 16), background = "#c4c3be")
lblshow.pack(pady = 10)

app.mainloop()