import json
import xlsxwriter

with open("output.json") as f:
    data = json.load(f)

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

row = 1
col = 1

header = list(data.values())[0]
worksheet.write(row - 1, col, "P1")
if header.get("P1") is not None:
    for element in header["P1"]:
        worksheet.write(row, col, element)
        col += 1
worksheet.write(row - 1, col, "P2")
if header.get("P2") is not None:
    for element in header["P2"]:
        worksheet.write(row, col, element)
        col += 1

# for d in data:
#     col = 1
    # if data[d].get("P1") is not None:
    #     for element in data[d]["P1"]:
    #         worksheet.write(row, col, element)
    #         col += 1
    # if data[d].get("P2") is not None:
    #     for element in data[d]["P2"]:
    #         worksheet.write(row, col, element)
    #         col += 1
#     break

row += 1
for d in data:
    col = 0
    worksheet.write(row, col, d)
    col += 1
    print(data[d])
    if data[d].get("P1") is not None:
        for element in data[d]["P1"].values():
            worksheet.write(row, col, element)
            col += 1
    if data[d].get("P2") is not None:
        for element in data[d]["P2"].values():
            worksheet.write(row, col, element)
            col += 1
    row += 1

workbook.close()
