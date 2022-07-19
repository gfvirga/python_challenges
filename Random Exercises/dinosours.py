import csv
import math
dinos = {}
g = 9.8
with open('dataset1.csv', "r") as dataset1, open('dataset2.csv', "r") as dataset2:
  reader1 = csv.reader(dataset1)
  next(reader1, None)
  for dino in reader1:
    dinos[dino[0]] = {
      "LEG_LENGTH" : float(dino[1]),
      "DIET" : dino[2]
    }
  reader2 = csv.reader(dataset2)
  next(reader2, None)
  for dino in reader2:
    if dino[0] in dinos.keys():
      dinos[dino[0]] |= {
        "STRIDE_LENGTH" : float(dino[1]),
        "STANCE": dino[2]
      }
      d = dinos[dino[0]]
      SPEED = ((d["STRIDE_LENGTH"] / d["LEG_LENGTH"]) - 1) * math.sqrt(d["LEG_LENGTH"] * g)
      dinos[dino[0]] |= {"SPEED":SPEED}

dinos_clean = {dino:skills for dino, skills in dinos.items() if "SPEED" in skills and skills["STANCE"] == "bipedal"}

dinos_sorted = sorted(dinos_clean, key=lambda x: dinos_clean[x]['SPEED'])
    
print("\n".join(dinos_sorted))