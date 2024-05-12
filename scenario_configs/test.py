import pickle
import pprint

with open('scenario_1.pkl', 'rb') as f:
    data = pickle.load(f)

with open("out.txt", "a") as f:
    pprint.pprint(data, stream=f)