import pandas as pd

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
    list_ = {'ingredient_name' : self.enredients[0], 'quantity' : self.enredients[1],
     'measure' : self.enredients[2]}

    return list_

  def dict_ingredients(self, list_):
    # self.new_list = list_
    self.my_dict = { self.name_foode : list_ }

    return self.my_dict
enredients = []
# print(df)
new_dict = {}
new_list = []

print('ЗАДАЧА 1')
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
print(new_dict)










str_data = ''
# print(len(df[3]), ' ', len(df[3][0]), ' ', df[3][0])
# print((str(str(df[3][0]).split(' | '))).strip(' ]['))
data = []
for i in range(len(df)):
  if len(df[i][0]) < 2:
    # print(df[i][0])
    # print('11: ', (((str(str(df[i][0]).split(' | '))).strip(' ][') + '\n').strip(" ")).rstrip("'"))
    str_data += ((str(str(df[i][0]).split(' | '))).strip(' ][') + '\n').strip(" ").replace("'", '')
  elif len(df[i][0]) > 1:
    # print('22: ', df[i])
    data = (str(df[i][0]).split(' | '))
    # print(data, " : ", len(data))
    if len(data) == 1:

      str_data += '\n'
      str_data += str(data).strip('][').strip().replace("'", '') + '\n'
    else:
      # print(, " : ", len(data))
    # for id in range(len(df[i])):
      str_data += (str(data).strip('][')).strip("',").replace("', '", ' | ') + '\n'


# print(str_data)

# print(str_data)
# df = pd.DataFrame(pd.Series(data_file))[(pd.DataFrame(pd.Series(data_file))) != ''].values
# df = str((pd.DataFrame(data_file)[0][(pd.DataFrame(data_file)[0] != '')])[3]).split(' | ')
# df = (pd.DataFrame(data_file)[0][(pd.DataFrame(data_file)[0] != '')])
# df = pd.Series(data_file)

# print(df)
# df_list = []
# for i in range(len(df)):
#   print(df[i])
#   if df[i][0] == 'nan':
#     pass
#   else:
    # print(np.array(df[i]))



