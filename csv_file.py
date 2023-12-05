import csv
import pandas as pd

class Target:
    def __init__(self,mail,name,company):
        if name=='':
            name="Sir/Ma'am"
        if company=="":
            company="your company"
        self.mail=mail
        self.name=name
        self.company=company

# excel_file_path = 'excel.xlsx'
# df = pd.read_excel(excel_file_path)
# csv_file_path = 'file.csv'
# df.to_csv(csv_file_path, index=False)


with open('file.csv','r') as csv_file:
    csvReader= csv.reader(csv_file)
    next(csvReader,None)
    target=[]
    for line in csvReader:
        t=Target(line[0],line[1],line[2])
        target.append(t)