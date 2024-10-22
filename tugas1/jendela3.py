import PySimpleGUI as sg
sg.theme("DarkGreen4")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM     : 2210010748")],
                           [sg.Text("Nama    : Addin Husnan Nadhari")],
                           [sg.Text("Kelas   : 5B NonReg Banjarmasin")],
                           [sg.Text("Matkul  : Pemrograman Visual 3")],
                           ],
                        size=(400,200),
                        font=("Times", 18))
window()
window.close()