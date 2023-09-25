import os 
# This program is used to change the extension of all the files in a directory to png

directory = str(input("Give the directory of all the files: "))
print(f"Total Number of files are: { len(os.listdir(directory))}")
directory2 = str(input("Give the directory to change the files into(Give the other directory as above): "))
for file in os.listdir(directory):
    if(os.path.isdir(file)):
        print("This is a directory")
    else:
        filename, file_extension = os.path.splitext(file)
        newFilename = filename + '.png'
        print(newFilename)
        os.rename(directory+'\\'+file, directory2+'\\'+newFilename) 
        print("The file has been changed to png")
