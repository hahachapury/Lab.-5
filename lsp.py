import re
import csv

print('task1')

text = open('task1-ru.txt', encoding='utf-8').read()

print(re.findall(r'\bс[а-яё]+', text, flags=re.I))
print(re.findall(r'\bи\s+([а-яё]+)', text, flags=re.I))

print('task2')

html = open('task2.html', encoding='utf-8').read()
print(re.findall(r"font-family\s*:\s*'([^']+)'", html)
)

print('task3')
st = open('task3.txt',encoding='utf-8').read()
date = re.findall(r'\d{4}-\d{2}-\d{2}',st)
email = re.findall(r'[\w\.-]+@[\w\.-]+',st)
url =  re.findall( r'https?://[^\s]+', st)
surname = re.findall(r'[A-Z][a-z]+',st)

with open('task3.csv', mode = 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID','Фамилия','Почта','Дата','Сайт'])
    for i in range(len(date)):
        writer.writerow([str(i+1),surname[i],email[i],date[i],url[i]])

print('file done')