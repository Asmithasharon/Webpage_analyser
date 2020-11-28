import PySimpleGUI as sg
from webanalyser.webpage_demo import get_html_content, parse_html_using_tag
from webanalyser.utils import get_statistics
sg.theme("DarkAmber") # To make the output colourful

layout = [
    [sg.Text("Web Page Analyzer", font=("Arial", 18))],
    [sg.Text("Enter URL", font=("Arial", 14)), sg.InputText("", font=("Arial", 14), key='url'),
     sg.Button("Get Data", font=("Arial", 14), key='get')],
    [sg.Multiline("", font=("Arial", 14), size=(60, 15), key='output')],
    [sg.Cancel()]
]


def get_details(url):
    html_content = get_html_content(url)
    data = parse_html_using_tag(html_content, 'p')
    statistics = get_statistics(data)
    display_output(statistics)


def display_output(statistics):
    # To get the output
    window['output'].print('These are the details :')
    for key, value in  statistics.items():
        window['output'].print("{}: {}".format(key, value))


if __name__ == '__main__':
    window = sg.Window("WebPageAnalyser", layout)
    while True:
        event, values = window.Read()
        if event == 'Cancel':
            break
        elif event == 'get':
            get_details(values['url'])


    window.Close()
