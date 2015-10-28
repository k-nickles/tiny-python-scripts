import os 

#Iterate over the screenshot images in a folder and delete them

def tidyFolder():

	#create an output file for the deleted imgs 
	outputFile = open("output.txt", "w")

	for files in os.listdir(os.getcwd()): 
		if files.endswith(".png") and files.startswith('Screen') :
			outputFile.write(files + os.linesep)
			os.remove(files)
	print 'There are no screenshot images in this folder'

if __name__ == '__main__': 
	tidyFolder() 
