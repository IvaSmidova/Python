import json

znaky_slovnik = {}

with open("alice.txt", mode="r", encoding="utf-8") as file:
    text = file.read()
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    for znak in text:
        if znak in znaky_slovnik:
            znaky_slovnik[znak] += 1
        else:
            znaky_slovnik[znak] = 1

serazeny_slovnik = dict(sorted(znaky_slovnik.items()))

with open("hw01_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(serazeny_slovnik, output_file, ensure_ascii=False, indent=4)
