import os
from io import TextIOWrapper
from shutil import copyfile


class MarkdownManager():

    def __init__(self, path: str, projectPath: str):
        self.path = path
        self.projectPath = projectPath

        myLines = self.__readFile()
        if (myLines[0] != -1):
            self.lines = myLines
        else: 
            raise ValueError()


    # This method open and read lines of file in path
    def __readFile(self):
        try:
            file = open(self.path, "r")   
            return file.readlines()
            
        except IOError:
            print("Error: wrong path.")
            return [-1]


    # This method get all image paths on markdown
    def __modifyImgsPath(self):
        newLines = []

        # Searching for images in the lines
        for line in self.lines:
            if(line.find("![") != -1):
                imgPath = line[line.find("](") + 2 : line.rfind(")")]
                line = self.__replaceImgPath(line, imgPath)

            newLines.append(line)

        self.lines = newLines


    # This method replace image paths to folder of markdown project
    def __replaceImgPath(self, line: str, imgPath: str):
        # Replacing path
        imgName = imgPath[imgPath.rfind("/"):]
        newPath = "./img" + imgName

        line = line.replace(imgPath, newPath)

        # Copying image
        newPath = self.projectPath + "/img" + imgName
        copyfile(imgPath, newPath)

        # Return line with new image path
        return line

    # This method construct the markdown folder to new files
    def __constructMdFolder(self):
        os.makedirs(self.projectPath)
        os.makedirs(self.projectPath + "/img")
  
    # This method write a new markdown file to constructed folder
    def __writeNewMdFile(self):
        fileName = self.path[self.path.rfind("/"):]
        file = open( self.projectPath + "/" + fileName, 'w' )
        file.writelines(self.lines)
        
    # Static Methods
    def confirm(path):
        return path.endswith(".md")

    # Create a markdown folder with file and images
    def createMdFolder(self):
        self.__constructMdFolder()
        self.__modifyImgsPath()
        self.__writeNewMdFile()