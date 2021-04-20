import random
import PySimpleGUI as sg
import os

class Generator:
    def __init__(self):
        #Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Email/User', size=(10, 1)),
             sg.Input(key='email/user', size=(20, 1))],
            [sg.Text('Number of Characters'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Create Password')]    
        ]
        #Declare Window
        self.window = sg.Window('Password Generator', layout)

        #Starts the program
    def Start(self):
        while True:
            event, amount = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Create Password':
                new_password = self.create_password(amount)
                print(new_password)
                self.save_password(new_password, amount)

        #Create to password
    def create_password(self, amount):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*' 
        chars = random.choices(char_list, k=int(amount['total_chars']))
        new_password = ''.join(chars)
        return new_password           

        #Save to password
    def save_password(self, new_password, amount):
        with open('passwords.txt', 'a', newline='') as file:
            file.write(
                f"\nEmail/User: {amount['email/user']} \nPassword: {new_password}")

        print('File Save')        
        

gen = Generator()
gen.Start()