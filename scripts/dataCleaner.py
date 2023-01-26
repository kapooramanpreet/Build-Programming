import os
import os.path
import shutil
import fileReader as fr

folderPath = "Data/Project 2"
destinationFileName = "consent"

projectFiles = [f for f in os.listdir(
    folderPath) if os.path.isfile(os.path.join(folderPath, f))]

for projectFile in projectFiles:
    projectFileNameSub = projectFile.split("_")
    if any(x in projectFileNameSub for x in map(str, fr.ids)):
        # create folder
        if not os.path.isdir(os.path.join(folderPath, destinationFileName)):
            os.mkdir(os.path.join(folderPath, destinationFileName))

        # copy file
        shutil.copy(
            os.path.join(folderPath, projectFile),
            os.path.join(folderPath, destinationFileName, projectFile),
        )


def redo():
    if os.path.isdir(os.path.join(folderPath, destinationFileName)):
        shutil.rmtree(os.path.join(folderPath, destinationFileName))
