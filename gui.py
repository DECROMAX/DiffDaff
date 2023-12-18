from diff_daff import html_diff
import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.FileBrowse(file_types=[('TXT', '*.txt')], key='file_path_1'), sg.Text('File 1')],
    [sg.FileBrowse(file_types=[('TXT', '*.txt')], key='file_path_2'), sg.Text('File 2')],
    [sg.Button('Execute Diff', key='execute_diff')]

]


def main_gui() -> None:
    window = sg.Window('DiffDaff', layout=layout)

    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'execute_diff':
            try:
                save_diff = html_diff(values['file_path_1'], values['file_path_1'])
                sg.popup(f'Diff saved at: {str(save_diff)}', title='Diff Saved')
            except (FileNotFoundError | KeyError) as e:
                sg.PopupError(f'Error: {e}')


if __name__ == '__main__':
    main_gui()
