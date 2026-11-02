import xml.dom.minidom as minidom

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read() #файл считывается в строку

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
currencies = []

for node in elements: #перебор всех валют
    nominal = None
    name = None
    for child in node.childNodes: #перебор информации о валюте
        if child.nodeType == 1: #работа с элементом
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3: #работа с текстом
                    nominal = int(child.firstChild.data)
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    name = child.firstChild.data
    if nominal == 1:
        currencies.append(name)

xml_file.close()

print(currencies)