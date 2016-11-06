import os
import sys
import pdfkit

#setting up file names
inputfile = sys.argv[1]+'.txt'
htmlfile = sys.argv[1]+'.html'

#opening files
print("Creating the HTML File")
txt = open(inputfile,'r') #file
html = open(htmlfile,'w')
css = 'styles.css'

#file proprities
title = ""
subject = ""

#WRITING THE HTML FILE
html.write('<html>\n<head>\n')
html.write('<meta charset="utf-8">\n')
html.write('<link rel="stylesheet" href="styles.css">\n')
html.write('<link href="https://fonts.googleapis.com/css?family=Roboto|Space+Mono" rel="stylesheet">')
html.write('</head>\n<body>\n')
for word in txt :
    if word[0] == '/' and word[2] == ' ' :
        if word[1] == 't' :
            title = word[3:len(word)-1]
            word = '<h1>\n'+word[3:]+'</h1>\n'
        elif word[1] == 's' :
            word = '<div class="subtitle">\n'+word[3:]+'</div>\n'
        elif word[1] == '1' :
            word = '<h2>\n'+word[3:]+'</h2>\n'
        elif word[1] == '2' :
            word = '<h3>\n'+word[3:]+'</h3>\n'
        elif word[1] == '3' :
            word = '<h4>\n'+word[3:]+'</h4>\n'
        elif word[1] == 'd' :
            word = '<div class="definition">\n <b>Definition :</b></br>'+word[3:]+'</div></br>\n'
        elif word[1] == 'r' :
            word = '<div class="remark">\n <font color="#009124">Remark :&nbsp;</font>'+word[3:]+'</div>\n'
        elif word[1] == 'm' :
            subject = word[3:len(word)-1]
    else :
        word = '<p>'+word+'</p>\n'
    html.write(word)
html.write("</body>\n</html>")

txt.close()
html.close()
print("HTML Created")
if title != "" :
    outputfile = title+'.pdf'
else :
    outputfile = sys.argv[1]+'.pdf'
if subject != "" :
    os.mkdir(subject)
    outputfile = subject+'/'+outputfile
pdfkit.from_file(htmlfile,outputfile)
#os.remove(html)
