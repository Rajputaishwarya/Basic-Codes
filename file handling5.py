# creating file

# open ("file name","permission")
s="this is my file handlin program"
file=open("demo1.txt","w")
file.write(s)
print("file created")
file.close()


# read file
file=open("demo1.txt","r")
filecontent=file.read()
print(filecontent)


# write a list into file
l1=["python","java","php","angular"]
file=open("demo1.txt","w")
file.writelines(l1)
print("file created")
file.close()


# read a list into file
file=open("demo1.txt","r")
filelist=file.readlines()
print(filelist)