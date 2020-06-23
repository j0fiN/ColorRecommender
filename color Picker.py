import numpy as np
import sklearn
import requests
res = requests.get(url="http://127.0.0.1:5000/b7438d633dd9915c")
print(eval(res.content))