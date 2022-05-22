print('''Название блюда
Количество ингредиентов в блюде
Название ингредиента | Количество | Единица измерения
Название ингредиента | Количество | Единица измерения''')
file = open('cooke.txt', 'r', encoding='UTF8')
data_file = file.read()
data_file = data_file.split('\n')

import pandas as pd
import numpy as np
# data_file = pd.read_csv('cooke.txt')
# print((pd.DataFrame(data_file).iat[0, 0]))
# print((pd.DataFrame(data_file).rename_axis))

df = pd.DataFrame(data_file)
df = df[df != ''].fillna(0)
df = (df[(df[0] != 0)].values).tolist()

class structure_default():
  def __init__(self, name_foode, person, enredients):
    self.name_foode = name_foode
    self.person = person
    self.enredients = enredients
    self.my_dict = {}
    self.new_list = []

  def list_ingredients(self):
    # print(self.enredients)
    # for i in range(len(self.enredients)):
    list_ = {'ingredient_name' : self.enredients[0], 'quantity' : self.enredients[1],'measure' : self.enredients[2]}

    return list_

  def dict_ingredients(self, list_):
    # self.new_list = list_
    self.my_dict = { self.name_foode : list_ }

    return self.my_dict
class foode_colcul(structure_default):


  def get_shop_list_by_dishes(self, pieces): # list_foode, list_person, enredients
    # print(self.new_dict[0])
    # print('111', self.name_foode)
    list_ = {}
    self.unit = pieces

    # self.enredients
    # self.name_foode

    for f in enredients:
      # print(f)
      quantity = str(f[1]).strip('][')
      # print('----',(str(self.name_foode).strip("'][")).replace('"', '').strip("]['")  )
      # for i in range(len(f)):
      # print('000 f:', (f[0]).strip("'[]"))
      # print('111 quantity:', str(f[1]).strip(']['))
      # print('222 person: ', (self.person))
      # print('333 (pieces): ', (pieces))
      # print('444 measure: ', str(f[2]).strip(']['))

      list_.update({(str(self.name_foode).strip("'][")).replace('"', '').strip("]['") : {(f[0]).strip("']["): {'measure': str(f[2]).strip(']['),'quantity': int(quantity) * int(self.person) * int(self.unit)}}})

      # print(f'list_: {list_}')

      # print(list_)
      return list_

enredients = []
new_dict = {}
new_list = []

print('ЗАДАЧА 1 - cook_book ')
print('''Задача имеет 2 версии - "Задача 1" и "Задача 2.3"''')
def table(data):
  list_ = []
  s = pd.DataFrame(pd.Series(data)).copy()
  for i in range(len(s)):
    list_ += [i]
  # print((list_))
  s.insert(0, 'index', list_)
  ss = s.reset_index()
  ss = ss.rename(columns={'level_0' : 'Блюдо', 0 : 'Ингредиенты'})
    # .set_index('index')
  return ss

def cooke_list(df):
  for one in df:
    if len(one[0]) < 2:
      person = int(one[0])
      # print(len(one[0]), ' ', one)
    else:

      new_ = str(one[0]).strip("][").split(' | ')

      if len(new_) == 1:


        name_foode = new_[0]
        # print(name_foode)
        enredients = []
      else:

        # print(new_)

        my_dict = structure_default(name_foode, person, new_)

        my_list = my_dict.list_ingredients()

        # print((my_list))
        enredients.append(my_list)


        # print(enredients)
        # print('enredients', len(enredients))
        # if len(enredients) == 3:

        # print(my_dict.dict_ingredients(enredients))
        # new_dict{name_foode : new_list}
      if np.array(enredients).size > 0:
        # print(np.array(enredients).size)
        l = np.array(enredients).tolist()
        new_dict.update({name_foode: l})
  return new_dict # print(new_dict)
print(cooke_list(df))
print(' ')
data = cooke_list(df)
data_ = pd.DataFrame(pd.Series(df))

print('ЗАДАЧА 2.3 - Рабочая версия ')
print('''В реализацию данной задачи по умолчанию вшиты
 вшити кол-во персон за столом (согласно базовой версии предоставленного файла "cooke.txt") и кол-во блюд на персону. Просто 
 в задаче не было указано - как поступить с персонами.
 
 Для реализации ввода данных, по персоне при запуске функции, необходимо лишь разместить int(input) и константы по 
 персонам изменить на переменные. 
  
 ''' )
person_food = 1 # Кол-во блюд на человека
person = 1
dishes = []
def dishes(cook_book):
  print('''Перечислите блюда через запятую''')
  dishes = input('Блюдо_1, ..., Блюдо 3:' )
  print('111', dishes)
  print()
  print('2222', cook_book)
  print()
  # print('3333', cook_book[dishes])
  dishes = dishes.split(', ')

  for i in range(len(dishes)):
    print(type(str(dishes[i]).strip("][").strip("'")))
    print(cook_book[dishes[i]])
  # cook_book

def get_shop_list_by_dishes(df, person_food, person ):
  name_foode = ''
  ingredients = {}
  cook_book  = {}

  # print(df)
  print('''Вывести рецепты "r" или Блюда "d" для стола?''')
  t = input('r или d: ')

  for single_list in df:
    single_list_str = (str(single_list).strip("][")).strip("'")

    cleaner_single_list = single_list_str.split(' | ')

    if len(cleaner_single_list) < 2 and len(cleaner_single_list[0]) >= 4:
      if ingredients != {}:
        cook_book.update({name_foode: ingredients})
        ingredients = {}

      name_foode = str(cleaner_single_list).strip("][").strip("'")


    elif len(cleaner_single_list) < 2 and len(cleaner_single_list[0]) < 4:
      person = int(str(cleaner_single_list).strip("][").strip("'"))
    else:

      one_enredient = str(cleaner_single_list[0]).strip("][").strip("'")
      quantity =  int(str(cleaner_single_list[1]).strip("][").strip("'")) * person * person_food
      measure = str(cleaner_single_list[2]).strip("][").strip("'")
      ingredients.update({one_enredient: {'measure': quantity, 'quantity': measure}})
      # print(ingredients)
  cook_book.update({name_foode: ingredients})


  if t == 'r':
    return cook_book
  elif t == 'd':
    dishes(cook_book)
print(get_shop_list_by_dishes(df, person_food, person) )
print(' ')
# print('ЗАДАЧА 2.1')
#
# # print((data_))
# person = []  # Количество ингредиентов в блюде
# # print('data_', len(data))
# # print(data_)
# name_foode = []
# ingredients = []
# dict_foode = {}
#
# pieces = 1 #  Кол-во блюд на персону
# t = len(list(data.values())[0])
# # print(f'data_: {t}, {list(data.values())[0]}')
# # print(f'data_: {t}, {data_}')
# for i in range(len(data_)):
#   # print('data_.iat[i,0]', data_.iat[i,0])
#   e = data_.iat[i,0]
#   # print(f'e: {e}')
#   if len(e[0]) < 2:
#     # print('e[0]', e[0], 'и len(e[0]): ', len(e[0]))
#     # if len(e[0]) < 2:
#     #   ee = e[0]
#     #   person = ee
#     #   print(f'---person {person}')
#
#     ee = e[0]
#     person = ee
#     # print(f'---person {person}')
#   else:
#     # print(str(e))
#
#     eee = str(e).split(' | ')
#
#     if len(eee) < 2:
#       name_foode = eee
#       # print('name_foode: ', name_foode)
#       if ingredients != []:
#         # print(f'name_foode: {name_foode}, person: {person}, ingredients: {ingredients}')
#
#
#
#
#         ingredients = []
#
#     elif len(eee) > 1:
#
#       ingredients += [eee]
#       b = foode_colcul(name_foode, person, ingredients)
#       dict_foode.update(b.get_shop_list_by_dishes(pieces))
#
# print('ЗАДАЧА 2.2')
# data_ = pd.DataFrame(pd.Series(df))
# print(len(list(np.array((data).values()).tolist())))
# categ = np.array((data).keys())
# foode = (list(np.array((data).values()).tolist()))
# # print(foode)
# print()
# print()
# for e in foode:
#   # print(e)
#   pass
#



      # id = [id for id in range(len(data))]
      # for i in id:
      #   print(f'name_foode {name_foode} ingredients: {(ingredients)}, id {i}')
      #


      # p = (dict_foode)
      # print(dict_foode)
# print(pd.Categorical(pd.DataFrame(dict_foode)))
      # print(f'name_foode: {name_foode}')
  # break


      # print(name_foode)


        #
      #   ingredients = []


  # print(e)

# list_
# for e in data_:
#   ee = str(e[0]).strip().split(' | ')
#   if len(ee) < 2:
#     # print(ee)
#     if len(ee[0]) < 2:
#       list_person += ee[0]
#     else:
#       list_foode += [ee[0]]
#   else:
#     ingredients += ee

# print('222', ingredients)

    # print(ee)
# print(table(data).head())
# new_dict = {}
# new_list = []
#
# def get_shop_list_by_dishes(data):
#   for str_ in data.keys():
#
#     for i in range(len(data[str_])):
#       if i < len(data[str_]):
#         # print('111', str_)
#
#         my_dict = foode_colcul(list(data[str_][i].values()))
#         my_dict.get_shop_list_by_dishes()

    # print(len(data[str_]))
# foode_colcul(data)

# get_shop_list_by_dishes(data)




