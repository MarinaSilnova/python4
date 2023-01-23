 #В первой строке файла находится информация об ассортименте мороженного, 
 # во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.


# icecream = {'Каштан', 'Каприз', 'Эврика', 'Ваверачка', 'Фруктовое', 'Гоша', 'Ятис', 'Пингвин', 'Пломбир', 'Топ', 'Столичное', 'Солетто'}
# icecream_available = {'Каштан', 'Эврика', 'Гоша', 'Ятис', 'Пингвин', 'Топ', 'Столичное', 'Солетто'}
# print(icecream.difference (icecream_available))

icecream = 'Каштан Каприз Эврика Ваверачка Фруктовое Гоша Ятис Пингвин Пломбир Топ Столичное Солетто'
icecream_available = 'Каштан Эврика Гоша Ятис Пингвин Топ Столичное Солетто'
print(icecream)
print(icecream_available)
icecream = set(icecream.split())
icecream_available = set(icecream_available.split())
result = icecream.difference (icecream_available)
print(result)

