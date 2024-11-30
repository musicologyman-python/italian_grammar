#!/usr/bin/env python3

import enum
import tkinter as tk

APP_TITLE: str = "Past Imperfect"


class MainContentFrame(tk.Frame):

    # region constants 

    _SHOW_ANSWERS_CAPTION = 'Show answers'
    _HIDE_ANSWERS_CAPTION = 'Hide answers'

    _FONT_NAME = 'Arial'
    _FONT_SIZE = 14
    _DEFAULT_FONT = (_FONT_NAME, _FONT_SIZE, 'normal')
    _BOLD_FONT = (_FONT_NAME, _FONT_SIZE, 'bold')
    
    # endregion

    # region answers

    _ANSWERS = ['arrivavo', 'arrivavi', 'arrivava',
                'arrivavamo', 'arrivavate', 'arrivavano']

    # endregion

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        PRONOUNS = ['io', 'tu', 'lui/lei', 'noi', 'voi', 'loro']

        top_label = tk.Label(self, text='arrivare')
        top_label.grid(row=0, column=0, columnspan=2)

        answer_frame = tk.Frame(self)
        answer_frame.grid(row=1, column=0, sticky='nw')

        self.answer_variables = [tk.StringVar(self) for _ in range(6)]
        self.answer_entries = [tk.Entry(answer_frame, 
                                 textvariable=self.answer_variables[i])
                        for i in range(len(self.answer_variables))]

        for i, pronoun in enumerate(PRONOUNS):
            lbl = tk.Label(answer_frame, text=pronoun, anchor='nw')
            lbl.grid(row=i, column=0, sticky='w')
            self.answer_entries[i].grid(row=i, column=1)

        button_frame = tk.Frame(self)
        button_frame.grid(row=2, column=0)

        self.clear_button = tk.Button(button_frame, text='Clear', 
                                      command=self._clear)
        self.clear_button.grid(row=0, column=0, sticky='nesw')

        self.check_button = tk.Button(button_frame, text='Check',
                                      command=self._check)
        self.check_button.grid(row=0, column=1, sticky='nesw')

        self.show_button = tk.Button(button_frame, text='Show\nAnswers',
                                     command=self._show_answers)
        self.show_button.grid(row=0, column=2, sticky='nesw')
       
    def _clear(self):
        for i in range(6):
            self.answer_variables[i].set('')
            self.answer_entries[i].configure(fg='black')

    def _check(self):
        for i in range(6):
            if ((answer:=self.answer_variables[i].get()) is not None and
                answer.strip() == self.__class__._ANSWERS[i]):
                self.answer_entries[i].configure(fg='blue')
            else:
                self.answer_entries[i].configure(fg='red')

    def _show_answers(self):
        for i in range(6):
            self.answer_variables[i].set(self.__class__._ANSWERS[i])
            self.answer_entries[i].configure(fg='blue')

class MainAppWindow(tk.Tk):

    def __init__(self, content_frame_factory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(APP_TITLE)
        self.bind('<Visibility>', self.center)
        
        self.content_frame = content_frame_factory(self)
        self.content_frame.grid(row=0, column=0, padx=5, pady=5)

    def center(self, event) -> None:
        
        window_height = self.winfo_height()
        window_width = self.winfo_width()
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        top = (screen_height - window_height) // 2
        left = (screen_width - window_width) // 2
        
        self.geometry(f'{window_width}x{window_height}+{left}+{top}')
        self.resizable(True, False)

def create_main_content_frame(parent: tk.Tk) -> MainContentFrame:
    return MainContentFrame(parent)

def main():

    MainAppWindow(create_main_content_frame).mainloop()

if __name__ == '__main__':
    main()
