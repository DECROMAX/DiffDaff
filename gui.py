#! /bin/python3

from diff_daff import html_diff
import PySimpleGUI as sg

sg.theme("Reddit")

file_browser_pad = (10, 10)
instructions_button_pad = (10, 10)
execute_diff_button_pad = (10, 20)
clear_values_button_pad = (0, 20)

button_size = (15, 1)

layout = [
    [
        sg.Push(),
        sg.Button(
            " ? ",
            key="-display_instructions-",
            pad=instructions_button_pad,
            size=(4, 1),
        ),
    ],
    [
        sg.FileBrowse(
            file_types=[("TXT", "*.txt")],
            button_text="Right text file",
            size=button_size,
            key="file_path_1",
            target="input_file_path_1",
            pad=file_browser_pad,
        ),
        sg.Input(
            key="input_file_path_1", size=(50, 1), enable_events=True, readonly=True
        ),
    ],
    [
        sg.FileBrowse(
            file_types=[("TXT", "*.txt")],
            button_text="Left text file",
            size=button_size,
            key="file_path_2",
            target="input_file_path_2",
            pad=file_browser_pad,
        ),
        sg.Input(key="file_path_2", size=(50, 1), enable_events=True, readonly=True),
    ],
    [sg.HorizontalSeparator()],
    [
        sg.Button(
            "Execute Diff",
            key="-execute_diff-",
            pad=execute_diff_button_pad,
            size=button_size,
        ),
        sg.Push(),
        sg.Button(
            "Clear Values", key="-clear-", pad=clear_values_button_pad, size=button_size
        ),
    ],
]


def main_gui() -> None:
    window = sg.Window("DiffDaff", layout=layout, size=(1150, 300))

    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "-display_instructions-":
            sg.popup(html_diff.__doc__, title="Instructions")
        if event == "-execute_diff-":
            try:
                save_diff = html_diff(values["file_path_1"], values["file_path_2"])
                sg.popup(f"Diff saved at: {str(save_diff)}", title="Diff Saved")
            except ValueError as e:
                sg.PopupError(f"Error: {e}")


if __name__ == "__main__":
    main_gui()
