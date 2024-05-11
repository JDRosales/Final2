from gui import *


def main():
    window = Tk()
    window.title('Grade Book')
    window.geometry("400x400")
    window.resizable(False, False)
    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
