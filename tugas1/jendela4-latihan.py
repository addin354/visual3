import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.theme_text_color("#0000FF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM     : 2210010748")],
                           [sg.Text("Nama    : Addin Husnan Nadhari")],
                           [sg.Text("Kelas   : 5B NonReg Banjarmasin")],
                           [sg.Text("Matkul  : Pemrograman Visual 3")],
                           ],
                        size=(400,200),
                        font=("Arial", 18))
window()
window.close()