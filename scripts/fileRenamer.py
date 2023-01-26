import os
import os.path
import shutil
import pandas as pd


def readConsentFile(path, stuIdCol, subIdCol):
    data = pd.read_excel(path, engine="openpyxl")
    stuIds = map(str, data[stuIdCol].tolist())
    subIds = data[subIdCol].tolist()

    zip_iterator = zip(stuIds, subIds)
    return dict(zip_iterator)


def renameFile(file, idMapping, projectNum, folderName):
    projectFileNameSubparts = file.split("_")

    # print(projectFileNameSubparts)
    for subpart in projectFileNameSubparts:
        try:
            subpart = str(float(subpart))
        except ValueError:
            continue
        if idMapping.get(subpart) is not None:
            extension = file.split(".")[-1]
            if extension == "h": extension = "hpp"
            newName = projectNum + "_" + idMapping[subpart] + "." + extension
            print(newName)
            os.rename(file, os.path.join(folderName, newName))


def main():
    folderName = "Data/Project 2/consent"
    consentFileName = "consent.xlsx"

    projectNum = "P2"

    idMaps = readConsentFile(consentFileName, "ID", "Student2")

    studentFiles = [f for f in os.listdir(
        folderName) if os.path.isfile(os.path.join(folderName, f))]

    for sf in studentFiles:
        renameFile(os.path.join(folderName, sf),
                   idMaps, projectNum, folderName)


if __name__ == "__main__":
    main()
