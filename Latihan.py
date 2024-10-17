import PySimpleGUI as sg
window = sg.Window(title="Profile", 
                layout=[[sg.Text("NPM    : 2210010483")],
                   [sg.Text("Nama   : NUR AL BAR BASKORO")],
                   [sg.Text("Kelas  : 5O Reguler Banjarmasin")],
                   [sg.Text("Matkul : Pemrograman Visual 3")]],
                   size=(400,200))

window.read()
window.close()