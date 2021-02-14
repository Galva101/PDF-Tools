import subprocess
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

pdfs = list_files(dir_path, "pdf")

for pdf in pdfs:
    print("editing "+str(pdf))
    subprocess.call('pdf-crop-margins -u -s \"'+pdf+"\"", shell=True)
