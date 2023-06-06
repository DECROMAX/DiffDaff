from diff_daff import html_diff
import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('File 1'), sg.FileBrowse(file_types=[('CSV', '*.csv')])]

]

def main_gui():
    window = sg.Window('DiffDaff', layout=layout)

    while True:
        event, values = window.Read()

main_gui()
