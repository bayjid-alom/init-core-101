#

players = ["Shakib", "Tamim", "Mustafizz", "Masrafee", "Tanjid", "Riyad", 420]
print(players)

players.remove(420)
print(players)

players.remove("Tamim")
print(players)


# Pop (specific index remove)
players.pop(3)
print(players)


# delete last item of lists
players.pop()
print(players)


# del keyword  (delete specified item)
del players[2]
print(players)


# clear method (all items delete)
players.clear()
print(players)    # []


