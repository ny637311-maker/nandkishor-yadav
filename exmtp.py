import matplotlib.pyplot as plt

players=["rohit","rishab", "virat", "ishan"]
runs=[1000,500,900,600]

plt.bar(players,runs)
plt.title("player record")
plt.xlabel("players")
plt.ylabel("runs")
plt.show()

matches =[1,2,3,4,]
runs =[100,233,456,789]

plt.plot(matches,runs)
plt.show()

plt.pie([50,68,89],labels=["rohit","rishab", "virat"])
plt.show()