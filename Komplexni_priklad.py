# Komplexni priklad - battle
# cast 1
file_in_lines = []

with open("battles.tsv", mode="r", encoding="utf-8") as file:
    for line in file:
        text_split = line.split("\t")
        file_in_lines.append(text_split)

headline = file_in_lines[0]
rows = file_in_lines[1:]
attacker_dict = {}

index_start = headline.index("attacker_1")
index_end = headline.index("attacker_4") + 1

for clan in rows:
    for x in range(index_start, index_end):
        if clan[x] not in attacker_dict.keys():
            attacker_dict[clan[x]] = 1
        else:
            attacker_dict[clan[x]] += 1

attacker_dict.pop("")

with open("attackers.csv", mode="w", encoding="utf-8") as output_file:
    write_headline = "attacker;count"
    print(write_headline,file=output_file)
    for write_row in attacker_dict.items():
        name, count = write_row
        one_row = name + ";" + str(count)
        print(one_row, file=output_file)


# cast 2
index_attacker_size = headline.index("attacker_size")
index_defender_size = headline.index("defender_size")
index_attacker_outcome = headline.index("attacker_outcome")
index_attacker_comm = headline.index("attacker_commander")

attacker_commanders_win = list()
attacker_commanders_loss = list()

for battle in rows:
    if battle[index_attacker_outcome] == "win":
        if battle[index_attacker_size] > battle[index_defender_size]:
            attacker_commanders_win.append(battle[index_attacker_comm])
    if battle[index_attacker_outcome] == "loss":
        if battle[index_attacker_size] < battle[index_defender_size]:
            attacker_commanders_loss.append(battle[index_attacker_comm])

count_wins = len(attacker_commanders_win)
count_loss = len(attacker_commanders_loss)

print(attacker_commanders_win)
print(count_wins)
print(attacker_commanders_loss)
print(count_loss)