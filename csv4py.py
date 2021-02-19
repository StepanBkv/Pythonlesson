import csv
from prettytable import PrettyTable

with open("1.csv", encoding="utf-8") as f:
    long = list()
    for row in csv.reader(f):
        long.append([row[0], row[1], row[10], row[11], row[12]])

table = PrettyTable()
result = list()
basic = 0
econom = 0
for i in long[1:29]:
    result.append(i)
    if(i[2] == '0,00') and (i[3] == '0,00'):
        basic += 2
    elif(i[3] == '0,00') or (i[2] == '0,00'):
        basic += 1
    if(i[4] == '0,00'):
        econom = econom + 1
table.field_names = long[0]
for elem in result:
    table.add_row(elem)
print(table)
print(f"Количество: {len(result)}"
      f"\nКоличество неверных ответов по теме «Основы законодательства РФ в области образования»:{basic}"
      f"\nКоличество неверных ответов по теме «Экономико-правовое регулирование педагогической деятельности»:{econom}")
