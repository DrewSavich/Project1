from tkinter import *

from match_classes import *


class GUI:
    start = Game()

    def __init__(self, window) -> None:
        """
        Initializes the display for the game
        :param window: the frames for creating the display
        """
        self.__match = 0
        # Sets up the GUI box
        self.window = window

        # Setup for the game
        self.frame_name = Frame(self.window)
        self.label_display = Label(self.frame_name, text='')
        self.label_match = Label(self.frame_name, text='Welcome!')
        self.window.resizable(False, False)

        self.frame_name.pack(anchor='n')
        self.label_display.pack(side='top', padx=10)
        self.label_match.pack(side='top')

        self.frame_choice = Frame(self.window)
        self.label_text = Label(self.frame_choice, text='Choose your option!')
        self.radio_1 = IntVar()
        self.radio_rock = Radiobutton(self.frame_choice, text='Rock', variable=self.radio_1, value=1, command=self.ready)
        self.radio_paper = Radiobutton(self.frame_choice, text='Paper', variable=self.radio_1, value=2, command=self.ready)
        self.radio_scissor = Radiobutton(self.frame_choice, text='Scissor', variable=self.radio_1, value=3, command=self.ready)
        self.label_text.pack(padx=5, side='top')
        self.radio_rock.pack(side='left')
        self.radio_paper.pack(side='left')
        self.radio_scissor.pack(side='left')
        self.frame_choice.pack(anchor='n')

        self.frame_save = Frame(self.window)
        self.button_submit = Button(self.frame_save, text='SUBMIT', state=DISABLED, command=self.clicked)
        self.label_result = Label(self.frame_save, text='')
        self.button_submit.pack(side='top')
        self.label_result.pack(side='top')
        self.frame_save.pack(anchor='n')

        self.frame_reset = Frame(self.window)
        self.label_reset = Label(self.frame_reset, text='')
        self.button_reset = Button(self.frame_reset, text='RESET', state=DISABLED, command=self.reset)
        self.button_reset.pack(side='top', pady=10)
        self.label_reset.pack(side='top')
        self.frame_reset.pack(anchor='s')

    def ready(self) -> None:
        self.button_submit['state'] = ACTIVE

    def clicked(self) -> None:
        """
        Allows the player to submit their choice,
        running matches until the winner is decided
        :return: Status of each game
        """
        self.button_submit['state'] = DISABLED
        self.__match += 1
        self.label_display['text'] = self.start.choice_user(self.radio_1.get())
        self.radio_1.set(0)
        self.label_match['text'] = self.start.shoot()

        if self.__match == 2:
            result = self.start.two_result()
            try:
                if result[0:4] == 'GAME':
                    self.label_result['text'] = result
                    self.__match = 0
                    self.radio_rock['state'] = DISABLED
                    self.radio_paper['state'] = DISABLED
                    self.radio_scissor['state'] = DISABLED
                    self.button_submit['state'] = DISABLED
                    self.button_reset['state'] = ACTIVE
                    self.label_reset['text'] = "Hit RESET if you want to play again! ^_^"
            except TypeError:
                self.label_reset['text'] = ''

        if self.__match == 3:
            result = self.start.three_result()
            if result[0:4] == 'GAME':
                self.label_result['text'] = result
            self.__match = 0
            self.radio_rock['state'] = DISABLED
            self.radio_paper['state'] = DISABLED
            self.radio_scissor['state'] = DISABLED
            self.button_submit['state'] = DISABLED
            self.button_reset['state'] = ACTIVE
            self.label_reset['text'] = "Hit RESET if you want to play again! ^_^"

    def reset(self):
        self.start.__score = 0
        self.label_display['text'] = ''
        self.label_match['text'] = 'Welcome Back!'
        self.label_text['text'] = 'Choose your option!'
        self.label_reset['text'] = ''
        self.label_result['text'] = ''
        self.radio_rock['state'] = ACTIVE
        self.radio_paper['state'] = ACTIVE
        self.radio_scissor['state'] = ACTIVE
        self.button_submit['state'] = ACTIVE
        self.button_reset['state'] = DISABLED
