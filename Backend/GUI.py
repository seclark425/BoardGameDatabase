import PySimpleGUI as sg
import API



top1 = sg.Text("boardgame id: ")
top2 = sg.Input(key='INPUT')
l11 = sg.Button("Search", key='SEARCH')
l21 = sg.Text("Name: ")
l22 = sg.Text("", key='NAME')
l31 = sg.Text("Minimum players: ")
l32 = sg.Text("", key='MIN')
l41 = sg.Text("Maximum players: ")
l42 = sg.Text("", key='MAX')
l51 = sg.Text("Weight: ")
l52 = sg.Text("", key='WEIGHT')
col1 = [[l11], [l21, l22], [l31, l32], [l41, l42], [l51, l52]]
r1 = sg.Image('', key = 'IMAGE')
col2=[[r1]]
layout = [[top1, top2],
          [sg.Column(col1), sg.Column(col2)], 
          [sg.Text("", key='ERROR', colors="red")]
        ]

window = sg.Window("test window", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'SEARCH':
        search = values['INPUT']
        results = API.find_game_all(search)
        for each in results:
            window.extend_layout(f)





# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     if event == 'SEARCH':
#         id = values['INPUT']
#         searched_game = API.find_game_specific(id)
#         if searched_game is None:
#             window['ERROR'].update(value="Search unsuccessful, please enter a valid id")
#         else:
#             window['NAME'].update(value=searched_game.get_name())
#             window['MIN'].update(value=searched_game.get_min())
#             window['MAX'].update(value=searched_game.get_max())
#             window['WEIGHT'].update(value=searched_game.get_weight())
#             # window['IMAGE'].update(value=searched_game.get_pic())
#             window['ERROR'].update(value="")
            