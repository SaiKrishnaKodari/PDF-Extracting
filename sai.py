import PyPDF2  

pdfFileObj = open('1.pdf', 'rb')  
    

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
    
 
#print(pdfReader.numPages)  

pageObj = pdfReader.getPage(0)  
    
print(pageObj.extractText())  
 
pdfFileObj.close()
