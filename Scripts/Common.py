import os
import glob

def getSubdirs(abs_path_dir1) :
	abs_path_dir = os.path.abspath(abs_path_dir1)
	#print(abs_path_dir)
	#lst = [ name for name in os.listdir(abs_path_dir) if os.path.isdir(os.path.join(abs_path_dir, name)) and name[0] != '.' ]
	lst=[]
	for name in os.listdir(abs_path_dir):
		if os.path.isdir(os.path.join(abs_path_dir, name)) and name[0] != '.':
			if lst:
				lst.append(str(abs_path_dir)+'/'+str(name))
			else:
			    lst=[str(abs_path_dir)+'/'+str(name)]
			
	lst.sort()
	return lst

def ListAppend(MainList, SubList):
	x=0
	while x in range(len(SubList)):
		MainList.append(SubList[x])
		x=x+1
	return  MainList
	
	
def Getfiles(RecursiveFolders,DirectFolders,DirectFiles, ExtensionsToFind ):
	FilesFound=[]
	filesDirs=RecursiveFolders
	for Folder in RecursiveFolders:
		temp1=getSubdirs(Folder)
		filesDirs = ListAppend(filesDirs, temp1)
		
	if DirectFolders:
		filesDirs = ListAppend(filesDirs, DirectFolders)

	for Folder1 in filesDirs:
		if FilesFound:
			temp = glob.glob(str(Folder1)+'/'+ExtensionsToFind)
			FilesFound = ListAppend(FilesFound, temp)
			
		else:
			FilesFound = glob.glob(str(Folder1)+'/'+ExtensionsToFind)
		
	if 	DirectFiles:
		FilesFound = ListAppend(FilesFound, DirectFiles)
		
	return FilesFound
	
def Getfolders(RecursiveFolders,DirectFolders):
	filesDirs=['.']
	if RecursiveFolders:
		filesDirs=RecursiveFolders
		for Folder in RecursiveFolders:
			temp1=getSubdirs(Folder)
			filesDirs = ListAppend(filesDirs, temp1)
			
	if DirectFolders:
		filesDirs = ListAppend(filesDirs, DirectFolders)
	return filesDirs
	
	
def GetAbsPath(RelativePathlist):
	ReturnList=[]
	for x in RelativePathlist:
		ReturnList.append(os.path.abspath(x))
	