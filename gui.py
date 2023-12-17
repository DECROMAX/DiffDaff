from diff_daff import html_diff
import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.FileBrowse(file_types=[('TXT', '*.txt')]), sg.Text('File 1')],
    [sg.FileBrowse(file_types=[('TXT', '*.txt')]), sg.Text('File 2')],
    [sg.Button('Execute Diff', key='execute_diff')]

]


def main_gui() -> None:
    window = sg.Window('DiffDaff', layout=layout)

    while True:
        event, values = window.Read()
        if event == 'execute_diff':
            print('test')

if __name__ == '__main__':
    main_gui()
