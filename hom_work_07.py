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

str_data = ''
# print(len(df[3]), ' ', len(df[3][0]), ' ', df[3][0])
# print((str(str(df[3][0]).split(' | '))).strip(' ]['))
data = []
for i in range(len(df)):
  if len(df[i][0]) < 2:
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


print(str_data)

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



