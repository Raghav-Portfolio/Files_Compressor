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

'''
the split(';') is used to separate multiple file paths returned by the sg.FilesBrowse
element (the "Choose" button) when a user selects multiple files.
Why .split(';') is Necessary:
When using the FilesBrowse element in PySimpleGUI, if the user selects multiple files, 
they are returned as a single string where each file path is separated by a semicolon (;).
To work with each file individually, you need to split this string into a list of file paths. 
The semicolon acts as the separator between the paths, and .split(';') breaks the string into individual file paths, 
allowing you to iterate over them or process them separately.
'''

window.close()
