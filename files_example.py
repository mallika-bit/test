import shutil

shutil.copy2('Documents/python_file_ex.html', 'Documents/python_file2_ex.html')

sent = "{% extends \" encyclopedia/layout.html \" %} \n {% block title %}"

myfile_ex = open('Documents/python_file2_ex.html', 'w')

myfile_ex.write(sent)
#myfile_ex.write("\n")
#myfile_ex.write( "{% block title %}" )
myfile_ex.write()
myfile_ex.close()



