import PySimpleGUI as sg
# import Backend
# from Backend import boardgame
from Backend import API

layout = [
    [sg.Text("boardgame id: "), sg.Input(key='INPUT')],
    [sg.Ok()],
    [sg.Text("Name: "), sg.Text("", key='NAME')],
    [sg.Text("Minimum players: "), sg.Text("", key='MIN')],
    [sg.Text("Maximum players: "), sg.Text("", key='MAX')],
    [sg.Text("Weight: "), sg.Text("", key='WEIGHT')]
]

window = sg.Window("test window", layout)

while True:
    event, values = window.read()
    searched_game = None

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Ok':
        id = values['INPUT']
        searched_game = API.find_game_specific(id)
        window['NAME'].update(value=searched_game.get_name())
        window['MIN'].update(value=searched_game.get_min())
        window['MAX'].update(values=searched_game.get_max())
        window['WEIGHT'].update(values=searched_game.get_weight())