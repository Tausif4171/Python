#2.
#open the files in binary mode
f1=open('cat.jpg','rb')
f2=open('new.png','wb')
#read bytes from f1 and write into f2
bytes=f1.read()
f2.write(bytes)

#close the files
f1.close()
f2.close()
