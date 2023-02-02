# %%
import random
import json

# %%
raw_json = {}

# %%
dict_no = 0
list_no = 0
int_no = 0
str_no = 0


# %%
def loop(data):
  global dict_no
  global list_no
  global int_no
  global str_no
  
  for k in data.keys():
    if isinstance(data[k], dict):
      dict_no += 1
      loop(data[k])
    else:
      if isinstance(data[k], list):
        list_no += 1
        for j in data[k]:
          loop(j)
      elif isinstance(data[k], int):
        data[k] = random.randint(0, 1000)
        int_no += 1
      elif isinstance(data[k], str):
        data[k] = "*"*len(data[k])
        str_no += 1
  
  return data


# %%
converted_data = loop(raw_json)
print(json.dumps(converted_data))


