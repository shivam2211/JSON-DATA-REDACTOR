import random
import json

raw_json = {}

def loop(data):
  # print("data = ", data, type(data))
  
  def inner_loop(innerd):
    if isinstance(innerd, dict):
      return loop(innerd)
    else:
      if isinstance(innerd, list):
        new_list_data = []
        for j in innerd:
          new_list_data.append(inner_loop(j))
        return new_list_data
      elif isinstance(innerd, int):
        innerd = random.randint(0, 1000)
        return innerd
      elif isinstance(innerd, str):
        innerd = "*"*len(innerd)
        return innerd
  
  for k in data.keys():
    data[k] = inner_loop(data[k])

  return data

converted_data = loop(raw_json)
print(json.dumps(converted_data))
