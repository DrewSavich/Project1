from match_classes import *
from gui import *

def main() -> None:
    """
    Runs the game between the user and computer
    """
    window = Tk()
    window.title('Rock, Paper, Scissor')
    window.geometry('300x200')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
