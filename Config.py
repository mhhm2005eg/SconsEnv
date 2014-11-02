import os
import SCons

#Env = Environment()

ProjectName="MFC400"

OutFile="./Out\\"+ProjectName # name of the final executable.
LibFile="./Lib\\"+ProjectName # name of the final executable.
DllFile="./Dll\\"+ProjectName # name of the final executable.
ObjDir=str("./Obj/")          # Directory for the obj files.
IncDir=str("./Inc/")

RecursiveSourceFolders=[] #Folders which will be scanned recursivly for the extensions *.c
SourceFolders=[] #Folders which will be scanned for the extensions *.c
SourceFiles=["./Src/objectTrackingTut.cpp"] #specific files to be built

RecursiveHeaderFolders=["./Inc/","C:\\opencv\\build\\include"] #Folders which will be scanned recursivly for the extensions *.h
HeaderFolders=["C:\\opencv\\build\\include\\opencv"] #Folders which will be scanned for the extensions *.h

RecursiveLibFolders=["C:/opencv/build/x64/vc10/lib"] #Folders which will be scanned recursivly for the extensions *.lib
LibFolders=[] #Folders which will be scanned for the extensions *.lib
LibFiles=[] #specific files to be linked