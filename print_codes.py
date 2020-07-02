from pathlib import Path
from fpdf import FPDF
import sys
import os
pdf = FPDF()

#################### IF NEEDED, MODIFY HERE ###################################################################

pdf.set_font("Arial", size=10)
alignment="L"
width_cells=200
height_cells=10
string_separator="##########################################################################"

###############################################################################################################



def get_all_codes_from_direc(path_aux):
    global path
    print("DIR: ",path)
    text=""
    for input_file in os.scandir(path_aux):
        text_aux=""
        #print(input_file)
        if(not(input_file.name.endswith("png")) and not(input_file.name.endswith("jpeg")) and not(input_file.name.endswith("jpg"))   ):
            if (input_file.is_dir()):
                text+=get_all_codes_from_direc(input_file)
            else:
                print("FILE: ",input_file.name)
                text_aux+="\n\n\n"
                text_aux+=string_separator
                text_aux+="\n"
                text_aux+=str("INÍCIO DO ARQUIVO: "+str(input_file.name)+str("\n"))
                text_aux+=str("caminho: "+(str(input_file.path)[(str(input_file.path).find(path)+len(path)):])+str("\n"))
                text_aux+=string_separator
                text_aux+="\n"
                f=open(input_file,  'r')
                text_aux+=f.read()
                f.close()
                text_aux+="\n\n\n"
                text_aux+=string_separator
                text_aux+="\n"
                text_aux+=str(" FIM DO ARQUIVO: "+str(input_file.name)+str("\n"))
                text_aux+=string_separator
                text_aux+="\n"
                text+=text_aux
    return text

name_file=sys.argv[1]
path=sys.argv[2]
text=""
text=get_all_codes_from_direc(path)
f=open(name_file+str(".txt"),"w")
f.write(text)
f.close()
pdf.add_page()
pdf.multi_cell(width_cells, height_cells, txt=str(text), align=alignment)
pdf.output(name_file+str(".pdf"))

print("FINISHED, VERIFY ",Path.cwd())



