import PySimpleGUI as sg
# import os.path
# from home import home_collection


a1 = sg.Text("hello world")
window = sg.Window("Test", layout=[[a1]])


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
