zakupy = {
    "Piekarnia": ["Chleb", "Paczek", "Bulki"],
    "Warzywniak": ["Marchew", "Seler", "Rukola"]
}
print("Lista zakupow")
a=0
for i in zakupy:
    print(f"Ide do {i}, kupuje tu nastepujace rzeczy: {zakupy[i]}")
    a=a+len(zakupy[i])
print(f"W sumie kupuje {a} elementow")
print ("commit1-test")
print ("commit2-test")