# Komplexni priklad - battle
# cast 1
file_in_lines = []

with open("battles.tsv", mode="r", encoding="utf-8") as file:
    for line in file:
        text_split = line.strip("\n").split("\t")
        file_in_lines.append(text_split)

headline = file_in_lines[0]
rows = file_in_lines[1:]
attacker_dict = {}

index_start = headline.index("attacker_1")
index_end = headline.index("attacker_4")

for clan in rows:
    for x in range(index_start, index_end + 1):
        if clan[x] != "":
            if clan[x] not in attacker_dict.keys():
                attacker_dict[clan[x]] = 1
            else:
                attacker_dict[clan[x]] += 1

with open("attackers.csv", mode="w", encoding="utf-8") as output_file:
    write_headline = "attacker;count"
    print(write_headline, file=output_file)
    for name, count in attacker_dict.items():
        print(f"{name};{count}", file=output_file)


# cast 2
index_attacker_size = headline.index("attacker_size")
index_defender_size = headline.index("defender_size")
index_attacker_outcome = headline.index("attacker_outcome")
index_attacker_comm = headline.index("attacker_commander")
index_defender_comm = headline.index("defender_commander")

attacker_commanders_win = list()
attacker_commanders_loss = list()
count_wins = 0
count_loss = 0

for battle in rows:
    if (battle[index_attacker_size] and battle[index_defender_size]) != "":
        if battle[index_attacker_outcome] == "win":
            if float(battle[index_attacker_size]) < float(battle[index_defender_size]):
                count_wins += 1
                commander = battle[index_attacker_comm].split(", ")
                for com in commander:
                    attacker_commanders_win.append(com)
        if battle[index_attacker_outcome] == "loss":
            if float(battle[index_attacker_size]) > float(battle[index_defender_size]):
                count_loss +=1
                commander = battle[index_defender_comm].split(", ")
                for com in commander:
                    attacker_commanders_loss.append(com)

print(attacker_commanders_win)
print(count_wins)
print(attacker_commanders_loss)
print(count_loss)