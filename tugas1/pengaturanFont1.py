import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM     : 2210010748")],
                           [sg.Text("Nama    : Addin Husnan Nadhari")],
                           [sg.Text("Kelas   : 5B NonReg Banjarmasin")],
                           ],
                        size=(400,200),
                        font=("Times", 18))
window()
window.close()