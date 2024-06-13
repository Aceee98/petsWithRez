import customtkinter
import tkinterDnD
import math

pi = math.pi

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("I am a triangle!")



class area:
    def __init__(self, base, height):
        self.base = base
        self.height = height

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
        switchMode.configure(text="Dark Mode")
    else:
        customtkinter.set_appearance_mode("dark")
        switchMode.configure(text="Light Mode")
    app.update()

switchMode = customtkinter.CTkSwitch(master=frame_1, command=switchMode_callback)
switchMode.pack(pady=1, padx=1, anchor="ne", side = "top")
switchMode.configure(text="Dark Mode")
switchMode.configure(font=("Arial", 15))


title = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
title.pack(pady=10, padx=10)
title.configure(text="Shapes")
title.configure(font=("Arial", 50))






def optionMenu_1_callback(value):
    def calculate_area():
        try:
            base = float(shapeBase.get())
            height = float(shapeHeight.get())
            area = 0.5 * base * height
            print(f"Area of the Triangle: {area:.2f}")  # Format area with 2 decimal places
        except ValueError:
            print("Invalid input. Please enter numbers only.")


    if value == "Triangle":
        title.configure(text="Triangle")
        height = True
        base = True
        half = True
    
    elif value == "Square":
        title.configure(text="Square")
        height = True
        base = True
        half = False

    elif value == "Hexagon":
        title.configure(text="Hexagon")
        height = True
        base = True
        half = False
    elif value == "Circle":
        title.configure(text="Circle")
        height = False
        base = True
        half = False

    

    
    if height:
        shapeHeight = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter the height of the triangle")
        shapeHeight.pack(pady=10, padx=10)
    
    if base:
        shapeBase = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter the base of the triangle")
        shapeBase.pack(pady=10, padx=10)
    
    if half:
        half = 0.5

    
    calculate_button = customtkinter.CTkButton(master=frame_1, command=calculate_area)
    calculate_button.pack(pady=10, padx=10)
    calculate_button.configure(text="Calculate Area")



        


optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=[
    "Triangle", 
    "Square", 
    "Hexagon",
    "Circle",
    "Pentagon",
    "Octagon",
    "Nonagon",
    "Decagon",
    ], command=optionMenu_1_callback)
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Select a shape")



# checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
# checkbox_1.pack(pady=10, padx=10)





app.mainloop()