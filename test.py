import os
import pdfkit
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
if os.path.exists('d:\helloworld.pdf'):
    os.remove('d:\helloworld.pdf')

Report = ''
Report = Report + '='.center(70,'=')+ "\n"
Report = Report + '                                                  List of Free Volumes id '                                                   + "\n"
Report = Report + '='.center(70,'=')+ "\n"
Report = Report + ' VolumeId                Size             Type           Av-Zone1                                                               '+ "\n"
Report = Report + '='.center(70,'=')+ "\n"

f = open('d:\helloworld.html','w')
message = """<html>
<head></head>
<body><p>Report</p></body>
</html>"""
f.write(message)
f.close()



#pdfkit.from_string(Report,'d:\helloworld.pdf')
# print(Report)
# c = canvas.Canvas('d:\ex1.pdf')
# c.drawString(70,100,Report)
# c.showPage()
# c.save()


#
# f = open('d:\helloworld.txt','a')
# f.write('\n' + Report)
# f.close()



#
#
# import os
# os.remove("ChangedFile.csv")
# print("File Removed!")
#
# import os.path
# >>> os.path.exists('mydirectory/myfile.txt')
# True
# >>> os.path.exists('does-not-exist.txt')
# False
# >>> os.path.exists('mydirectory')
# True