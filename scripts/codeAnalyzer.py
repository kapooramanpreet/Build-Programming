import os
import json
import platform
import glob
from turtle import st
import xlsxwriter
from pprint import pprint
from clang.cindex import Index, Config, TokenKind
import pandas as pd

# Works on macOS, to find the path, execute "mdfind libclang.dylib" in terminal to find folder path
if platform.system().startswith("Darwin"):
    Config.set_library_path("/Library/Developer/CommandLineTools/usr/lib/")
elif platform.system().startswith("Win"):
    Config.set_library_path("/Program Files/LLVM/bin")
else:
    print("Please configure the library path for your system here")
    exit(1)


def writeOutput(data):
    workbook = xlsxwriter.Workbook('result.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    for d in data:
        col = 0
        for item in d:
            worksheet.write(row, col, item)
            col += 1
        row += 1
    workbook.close()


'''
Parses a single .cpp file for code metrics:
- lines of code
- # single comments
- # block comments
- # block comment lines
- avg line length
- avg identifers per line
'''


def parseCPP(filePath) -> dict:
    print(filePath)

    numOfSingleComments = 0
    numOfBlockComments = 0
    linesOfBlockComments = 0
    numberOfIdentifiers = 0
    numParenthesisAndBraces = 0
    numDots = 0

    with open(filePath, 'rb') as file:
        lines = file.readlines()

    averageLinelength = sum([len(line.strip()) for line in lines]) / len(lines)
    maxLineLength = max([len(line.strip()) for line in lines])

    # Identifiers
    idx = Index.create()
    tu = idx.parse(filePath, args=['-std=c++11'])
    for t in tu.get_tokens(extent=tu.cursor.extent):
        if t.kind is TokenKind.IDENTIFIER:
            numberOfIdentifiers += 1
        elif t.kind is TokenKind.COMMENT:
            commentLines = 1
            try:
                commentLines = len(t.spelling.split('\n'))
            except UnicodeDecodeError:
                pass
            if commentLines == 1:
                numOfSingleComments += 1
            else:
                numOfBlockComments += 1
                linesOfBlockComments += commentLines
        elif t.kind is TokenKind.PUNCTUATION:
            if t.spelling == '(' or t.spelling == '{':
                numParenthesisAndBraces += 1
            elif t.spelling == '.' or t.spelling == '->':
                numDots += 1

    averageIdentifiersPerLine = numberOfIdentifiers / len(lines)

    result = {
        "lines of code": len(lines), 
        "# single comments": numOfSingleComments / len(lines),
        "# block comments": numOfBlockComments / len(lines),
        "# block comment lines": linesOfBlockComments / len(lines),
        "avg comment lines": (linesOfBlockComments + numOfSingleComments) / len(lines),
        "avg line length": averageLinelength,
        "max line length": maxLineLength,
        "avg identifers per line": averageIdentifiersPerLine,
        "avg '(' and '{'": numParenthesisAndBraces / len(lines),
        "avg '.'": numDots / len(lines)
    }
    
    #pprint(result)

    return result


def main():
    fileTypes = ["**/consent/**.hpp", "**/consent/**.cpp"]
    students_with_no_response = ["S2", "S59", "S109", "S124", "S215"]

    projectFiles = []
    for fileType in fileTypes:
        projectFiles += glob.glob(fileType, recursive=True)
        print(len(projectFiles))

    data = {}
    for projectFile in projectFiles:
        projectFile = projectFile.replace("\\", "/")
        projectId, studentId = projectFile.split("/")[-1].split(".")[0].split("_")
        # get rid of students who didn't submit the survey response
        if studentId in students_with_no_response:
            continue
        if data.get(studentId) is None:
            data[studentId] = {projectId: parseCPP(projectFile)}
        else:
            data[studentId][projectId] = parseCPP(projectFile)

    with open("output.json", "w") as outfile:
        json.dump(data, outfile, indent=4)



if __name__ == "__main__":
    main()
