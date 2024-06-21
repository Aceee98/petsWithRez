import customtkinter
import tkinterDnD
import math
import tkinter


pi = math.pi

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Area of shapes")




def anErrorOccuredNumsOnly():
    tkinter.messagebox.showerror("Error", "Error: Invalid input.")(master=app, text="Error: Invalid input.")


class area:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.shapeBase = 0
        self.shapeHeight = 0

        math.sin()


def destroy_items():
    for item in frame_1.winfo_children():
        item.destroy()

def button_callback():
    print("Button clicked")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)





def switchMode_callback():
    print(customtkinter.get_appearance_mode())
    if customtkinter.get_appearance_mode() == "Dark":
        customtkinter.set_appearance_mode("light")
        switchMode.configure(text="Light Mode")
    else:
        customtkinter.set_appearance_mode("dark")
        switchMode.configure(text="Dark Mode")
    app.update()

switchMode = customtkinter.CTkSwitch(master=frame_1, command=switchMode_callback)
switchMode.pack(pady=1, padx=1, anchor="ne", side = "top")
switchMode.configure(text="Light Mode")
switchMode.configure(font=("Arial", 15))


title = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
title.pack(pady=10, padx=10)
title.configure(text="Shapes")
title.configure(font=("Arial", 50))


class ShapeCalculator:
    def __init__(self, master):
        self.master = master
        self.frame_1 = customtkinter.CTkFrame(master=self.master)
        

        self.title = customtkinter.CTkLabel(master=self.frame_1)
        self.title.configure(text="")
        self.title.pack(pady=10, padx=10)

        self.shapeBase = None
        self.shapeHeight = None
        self.calculate_button = None
        self.areaResult = customtkinter.CTkLabel(master=self.frame_1)
        self.areaResult.configure(text="")
        self.circumferenceLengthResult = customtkinter.CTkLabel(master=self.frame_1)
        self.circumferenceLengthResult.configure(text="")
        

    def optionMenu_1_callback(self, value):
        # Destroy previous widgets if they existb00
        for widget in [self.shapeBase, self.shapeHeight, self.calculate_button]:
            if widget is not None:
                widget.destroy()
        self.areaResult.pack_forget()
        self.circumferenceLengthResult.pack_forget()

        # Clear results
        self.areaResult.configure(text="")
        self.circumferenceLengthResult.configure(text="")

        self.frame_1.pack(pady=10, padx=10)

        
        # Create new widgets based on the selected shape
        if value == "Triangle":
            self.title.configure(text="Triangle")
            self.shapeHeight = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the height of the triangle", width=200)
            self.shapeHeight.pack(pady=10, padx=10)
            self.shapeBase = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the base of the triangle", width=200)
            self.shapeBase.pack(pady=10, padx=10)
            self.calculate_button = customtkinter.CTkButton(master=self.frame_1, command=self.calculate_triangle_area)
            self.calculate_button.pack(pady=10, padx=10)
            self.calculate_button.configure(text="Calculate dimensions")

        if value == "Square":
            self.title.configure(text="Square")
            self.shapeBase = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the base of the square", width=200)
            self.shapeBase.pack(pady=10, padx=10)
            self.calculate_button = customtkinter.CTkButton(master=self.frame_1, command=self.calculate_square_area)
            self.calculate_button.pack(pady=10, padx=10)
            self.calculate_button.configure(text="Calculate dimensions")

        if value == "Hexagon":
            self.title.configure(text="Hexagon")
            self.shapeBase = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the base of the hexagon", width=200)
            self.shapeBase.pack(pady=10, padx=10)
            self.calculate_button = customtkinter.CTkButton(master=self.frame_1, command=self.calculate_hexagon_area)
            self.calculate_button.pack(pady=10, padx=10)
            self.calculate_button.configure(text="Calculate dimensions")

        if value == "Circle":
            self.title.configure(text="Circle")
            self.shapeBase = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the radius of the circle", width=200)
            self.shapeBase.pack(pady=10, padx=10)
            self.calculate_button = customtkinter.CTkButton(master=self.frame_1, command=self.calculate_circle_area)
            self.calculate_button.pack(pady=10, padx=10)
            self.calculate_button.configure(text="Calculate dimensions")

        if value == "Pentagon":
            self.title.configure(text="Pentagon")
            self.shapeBase = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the base of the pentagon", width=200)
            self.shapeBase.pack(pady=10, padx=10)
            self.calculate_button = customtkinter.CTkButton(master=self.frame_1, command=self.calculate_pentagon_area)
            self.calculate_button.pack(pady=10, padx=10)
            self.calculate_button.configure(text="Calculate dimensions")

        if value == "Octagon":
            self.title.configure(text="Octagon")
            self.shapeBase = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the base of the octagon", width=200)
            self.shapeBase.pack(pady=10, padx=10)
            self.calculate_button = customtkinter.CTkButton(master=self.frame_1, command=self.calculate_octagon_area)
            self.calculate_button.pack(pady=10, padx=10)
            self.calculate_button.configure(text="Calculate dimensions")

        if value == "Nonagon":
            self.title.configure(text="Nonagon")
            self.shapeBase = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the base of the nonagon", width=200)
            self.shapeBase.pack(pady=10, padx=10)
            self.calculate_button = customtkinter.CTkButton(master=self.frame_1, command=self.calculate_nonagon_area)
            self.calculate_button.pack(pady=10, padx=10)
            self.calculate_button.configure(text="Calculate dimensions")

        if value == "Right angled triangle":
            self.title.configure(text="Right angled triangle")
            self.shapeHeight = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the height of the right angled triangle", width=200)
            self.shapeHeight.pack(pady=10, padx=10)
            self.shapeBase = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Enter the base of the right angled triangle", width=200)
            self.shapeBase.pack(pady=10, padx=10)
            self.calculate_button = customtkinter.CTkButton(master=self.frame_1, command=self.calculate_right_angled_triangle_area)
            self.calculate_button.pack(pady=10, padx=10)
            self.calculate_button.configure(text="Calculate dimensions")



    def calculate_triangle_area(self):
        try:
            base = float(self.shapeBase.get())
            height = float(self.shapeHeight.get())
            area = 0.5 * base * height
            self.areaResult.configure(text=f"Area of the Triangle: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    def calculate_square_area(self):
        try:
            base = float(self.shapeBase.get())
            area = base * base
            self.areaResult.configure(text=f"Area of the Square: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    def calculate_hexagon_area(self):
        try:
            base = float(self.shapeBase.get())
            area = 3 * math.sqrt(3) * base * base / 2
            self.areaResult.configure(text=f"Area of the Hexagon: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    def calculate_circle_area(self):
        try:
            base = float(self.shapeBase.get())
            area = pi * base * base
            self.areaResult.configure(text=f"Area of the Circle: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
            self.circumferenceLengthResult.configure(text=f"Circumference of the Circle: {2 * pi * base:.2f}")
            self.circumferenceLengthResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    def calculate_parallelogram_area(self):
        try:
            base = float(self.shapeBase.get())
            height = float(self.shapeHeight.get())
            area = base * height
            self.areaResult.configure(text=f"Area of the Parallelogram: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    def calculate_octagon_area(self):
        try:
            base = float(self.shapeBase.get())
            area = 2 * (1 + math.sqrt(2)) * base * base
            self.areaResult.configure(text=f"Area of the Octagon: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    def calculate_nonagon_area(self):
        try:
            base = float(self.shapeBase.get())
            area = 1.801707 * base * base
            self.areaResult.configure(text=f"Area of the Nonagon: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    def calculate_right_angled_triangle_area(self):
        try:
            base = float(self.shapeBase.get())
            height = float(self.shapeHeight.get())
            area = 0.5 * base * height
            self.areaResult.configure(text=f"Area of the Right angled triangle: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    def calculate_pentagon_area(self):
        try:
            base = float(self.shapeBase.get())
            area = 1.720477 * base * base
            self.areaResult.configure(text=f"Area of the Pentagon: {area:.2f}")
            self.areaResult.pack(pady=10, padx=10)
        except:
            self.anErrorOccuredNumsOnly()

    



    @staticmethod
    def anErrorOccuredNumsOnly():
        tkinter.messagebox.showerror("Error", "Error: Invalid input.")(master=app, text="Error: Invalid input.")

        


shape_calculator = ShapeCalculator(app)

# Create the optionmenu_1 widget
optionmenu_1 = customtkinter.CTkOptionMenu(
    frame_1,
    values=[
        "Circle",
        "Triangle", 
        "Square", 
        "Hexagon",
        "Pentagon",
        "Octagon",
        "Nonagon",
        "Decagon",
        "Right angled triangle",
    ],
    command=shape_calculator.optionMenu_1_callback,  # Use the optionMenu_1_callback method of the shape_calculator instance
    width=200
)
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Select a shape")




# checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
# checkbox_1.pack(pady=10, padx=10)





app.mainloop()