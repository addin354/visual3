import PySimpleGUI as sg
window = sg.Window(title="Profile",layout=[[sg.Text("NPM    : 2210010037")],
                                           [sg.Text("Nama   : ADDIN HUSNAN NADHARI")],
                                           [sg.Text("Kelas   : 5B Nonreg Banjarmasin ")],
                                           [sg.Text("MAtkul : Pemrograman Visual 3")]],
                                           size=(400,200))
window()
window.close()