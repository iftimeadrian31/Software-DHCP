import tkinter as tk
import GUI

if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Client DHCP")
    gui.resizable(False, False)
    GUI = GUI.GUI(gui)
    gui.mainloop()
