import os
import Config
import Common

from os.path import basename


Env = Environment()
FileList=['HelloWorld.c', 'Hello.c' ]
ObjectList=[]

ExtensionsToBuild='*.cpp'
#FilesToBuild=Glob( '.\\Src\\' +ExtensionsToBuild) # Return file objects
FilesToBuild=[]

#Program(OutFile, FileList) # Produce .exe file

#Env.CCFLAGS.append('-DHELLO') #Otions for the compiler
#-------------------------------------------------------------------
# H files Dirs
#-------------------------------------------------------------------

HfilesDirs = Common.Getfolders(Config.RecursiveHeaderFolders, Config.HeaderFolders)

print(HfilesDirs, 'HfilesDirs')
#-------------------------------------------------------------------
# C files Dirs
#-------------------------------------------------------------------
FilesToBuild=Common.Getfiles(Config.RecursiveSourceFolders, Config.SourceFolders, Config.SourceFiles, ExtensionsToBuild)
print(FilesToBuild, 'FilesToBuild')
#-------------------------------------------------------------------
# Lib files Dirs
#-------------------------------------------------------------------
Libfiles=Common.Getfiles(Config.RecursiveLibFolders, Config.LibFolders, Config.LibFiles, '*.lib')
print(Libfiles, 'Libfiles')
#-------------------------------------------------------------------
# Compiling the C files
#-------------------------------------------------------------------
for Cfile in FilesToBuild:
	Objfile=str(Cfile).replace('.c','.o')
	print(str(Cfile))
	Objfile1 = basename(Objfile)
	print(Objfile)
	ObjectList.append(Object(target=File(str(Config.ObjDir)+Objfile1),source=Cfile, CPPPATH=HfilesDirs))

print (str(Config.ObjDir)+Objfile1)

#if Libfiles:
    #LibOption= " LIBS="+Libfiles+", LIBPATH="+Getfolders(Config.RecursiveLibFolders, Config.LibFolders)
Program(target = Config.OutFile, source = ObjectList, LIBS=Libfiles, LIBPATH=Common.Getfolders(Config.RecursiveLibFolders, Config.LibFolders))
#StaticLibrary(target = Config.LibFile, source = ObjectList)	
#SharedLibrary(target = Config.DllFile, source = ObjectList)

##########################################################
### Help
##########################################################
#Program(target = OutFile, source = FilesToBuild) # Produce .exe file from a patern

#Library(target = LibFile, source = FilesToBuild) #lib

#StaticLibrary(target = LibFile, source = FilesToBuild) #lib

#SharedLibrary(target = DllFile, source = FilesToBuild) # DLL
#Object(FileList) # Produce the obj files only


