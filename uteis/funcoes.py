import calendar
from datetime import datetime,date

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


def dictToString(dicionario):
    string = u''
    cabecalho = dicionario.keys()
    for cb in cabecalho:
        string = string + cb + ';'
    string = string + '\n'
    valores = list(dicionario.values())
    for i in range(len(valores[0])):
        for j in range(len(valores)):
            valor = str(valores[j][i])
            string = string + valor + ';'
        string = string + '\n' 
        
    return string

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return date(year, month, day)

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def separa_anos(data):
    arrayData = data.split('-')
    return arrayData[2]

def numero_horas_ano(ano):
    inicio = date(int(ano),1,1)
    fim = date(int(ano) + 1,1,1)
    numeroHoras = (fim - inicio).days * 24
    return numeroHoras

def transforma_data(string):
    return datetime.strptime(string, "%d-%m-%Y").strftime("%b/%Y").capitalize()

