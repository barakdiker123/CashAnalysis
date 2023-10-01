import tkinter as tk
import numpy as np
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.widgets import Slider

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def main():
    root = tk.Tk()
    root.title("Matplotlib in Tkinter with Slider")
    fig = Figure(figsize=(5, 4), dpi=100)
    a = fig.add_subplot(111)
    t = np.arange(0.0, 1.0, 0.01)
    s = np.sin(2 * np.pi * t)
    a.plot(t, s)
    slider = Slider(a, "Freq", 0.1, 30.0, valinit=3)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update(val):
        a.clear()
        s = np.sin(2 * np.pi * t * val)
        a.plot(t, s)
        canvas.draw()

    slider.on_changed(update)
    tk.mainloop()


def example1():
    root = tk.Tk()
    root.title("Matplotlib in Tkinter with Slider")
    label = tk.Label(text="Hello, Tkinter")
    label.pack()
    entry = tk.Entry()
    entry.pack()
    tk.mainloop()


def example2():
    window = tk.Tk()
    frame_a = tk.Frame()
    frame_b = tk.Frame()
    label_a = tk.Label(master=frame_a, text="I'm in Frame A")
    label_b = tk.Label(master=frame_b, text="I'm in Frame B")
    label_a.pack()
    label_b.pack()
    frame_a.pack()
    frame_b.pack()
    window.mainloop()


class App(tk.Tk):
    """Manage the gui."""

    def __init__(self):
        """Init the app."""
        super().__init__()
        self.title("Tkinter Matplotlib Demo")
        self.frame_a = tk.Frame(master=self)
        self.label_a = tk.Label(master=self.frame_a, text="Hello Everyone !!!")
        self.label_b = tk.Label(master=self.frame_a, text="Some another text")
        # prepare data
        data = {"Python": 11.27, "C": 11.16, "Java": 10.46, "C++": 7.5, "C#": 5.26}
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        #########
        ax1 = figure.add_subplot(2, 3, 1)  # equivalent but more general

        ax2 = figure.add_subplot(232, frameon=False)  # subplot with no frame
        figure.add_subplot(233, projection="polar")  # polar subplot
        figure.add_subplot(234, sharex=ax1)  # subplot sharing x-axis with ax1
        figure.add_subplot(235, facecolor="red")  # red subplot

        ax1.plot(np.arange(0, 1000, 50))
        ax1.set_ylabel("YLabel 0")

        ax2.plot(np.arange(0, 1000, 50))
        ax2.set_ylabel("YLabel 0")

    def packing(self):
        """Display the Widgets."""
        self.frame_a.pack()
        self.label_a.pack()
        self.label_b.pack()


if __name__ == "__main__":
    app = App()
    app.packing()
    app.mainloop()
