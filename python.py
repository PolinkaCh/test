import re

#Создаём функцию, которая будет проверять каждый элемент исходного массива 
#на наличие русских букв. В условие записываем проверку на количество найденных букв.
def checkArray(el):
    filterEl = re.findall(r'[А-Яа-яЁё]', el, re.I)
    if filterEl and len(filterEl)>1:
        return True
    else:
        return False

#Исходный массив со строками, которые нужно отфильтровать
array = ["ghvbjnk","vgпbhnj", "пр ито", "cfvgbhjn", "пмриото", "GHBРПHGJH", "GHBПоGJH", "56bhирbhbn"]

#Отфильтровываем исходный массив, используя встроенную функцию filter
result = filter(checkArray, array)  

#Выводим результат
print (list(result))

