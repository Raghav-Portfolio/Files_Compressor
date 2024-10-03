import FreeSimpleGUI as sg
import zip_function

label1=sg.Text('Add Files to Compress')
inp=sg.InputText()
choose_button=sg.FilesBrowse('Choose', key='files')

label2=sg.Text('Select Destination Folder')
inp2=sg.InputText()
choose_button_2=sg.FolderBrowse('Choose', key='folder')

compress_button=sg.Button('Compress')
output_label=sg.Text(key='output', text_color='blue')

window=sg.Window('Compressor', layout=[[label1],
                                       [inp, choose_button],
                                       [label2],
                                       [inp2, choose_button_2],
                                       [compress_button, output_label]
                                       ])

while True:
    event, values= window.read()
    print(event, values)
    filepaths=values['files'].split(';')
    folder=values['folder']
    zip_function.make_archive(filepaths, folder)
    window['output'].update(value='Compress Successful!')
    
window.close()
