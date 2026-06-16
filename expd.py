import pandas as pd

players = {
    "player":["dhoni","rohit","virat"],
    "run": [100,50,45]

}

df = pd.DataFrame(players)

print(df)
print(df["player"])

print(df[df["run"]>30])
