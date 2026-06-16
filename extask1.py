f= open("test.txt" ,"w")
f.write("helloew wored")
f.close()
print("file created")



f = open("test.txt","r")
conter= f.read()
print(conter)
f.close()



f= open("test.txt" ,"a")
f.write("\n new line added")
f.close
print("file added")