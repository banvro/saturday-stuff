import tkinter as tk
import joblib
import numpy as np

model = joblib.load("student_package_predictor.joblib")

def predictpkg():
    cgpa = float(ent.get())
    cgpa_array = np.array(cgpa)
    new_cgpa = cgpa_array.reshape(-1, 1)
    predicted_pkg = model.predict(new_cgpa)[0]
    
    lblx.config(text = f"Predicted Package is : {str(predicted_pkg)[:4]} lakh.")

    ent.delete(0, tk.END)

app = tk.Tk()

app.geometry("600x300")
app.title("Package Predictor")
app.config(background = "lightgreen")

lbl = tk.Label(app, text = "Package Predictor", font = ("robort", 30, "bold"),
               fg = "white", bg = "green")
lbl.pack(ipady = 15, fill = "x")

ent = tk.Entry(app, font = ("robort", 26))
ent.pack(pady = 15)

btn = tk.Button(app, text = "Predict", font = ("robort", 21, "bold"),  fg = "white", bg = "green", command = predictpkg)
btn.pack(ipadx = 40)

lblx = tk.Label(app, text = "", font = ("robort", 19),  fg = "green", bg = "lightgreen")
lblx.pack(pady = 15)


app.mainloop()