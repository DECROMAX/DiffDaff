#! /bin/python3

from diff_daff import html_diff
import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Button('Display Instructions', key='-display_instructions-')],
    [sg.Push()],
    [sg.FileBrowse(file_types=[('TXT', '*.txt')], key='file_path_1'), sg.Text('File 1')],
    [sg.FileBrowse(file_types=[('TXT', '*.txt')], key='file_path_2'), sg.Text('File 2')],
    [sg.Push()],
    [sg.Button('Execute Diff', key='-execute_diff-'), sg.Push(), sg.Button('Clear Values', key='-clear-')]

]


def main_gui() -> None:
    window = sg.Window('DiffDaff', layout=layout, size=(1150, 250))

    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-display_instructions-':
            sg.popup(html_diff.__doc__, title='Instructions')
        if event == '-execute_diff-':
            try:
                save_diff = html_diff(values['file_path_1'], values['file_path_2'])
                sg.popup(f'Diff saved at: {str(save_diff)}', title='Diff Saved')
            except ValueError as e:
                sg.PopupError(f'Error: {e}')


if __name__ == '__main__':
    main_gui()
