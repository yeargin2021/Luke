luke = {
    "Han": "Scoundrel",
    "Chewie": "Wookie",
    "Threepio": "Droid",
    "Vader": "father"
}

def Luke(character):
    for i, j in luke.items():
        if character == i:
            return "Luke, I am your " + j + "."
    return "Not here!"

print(Luke("Han"))
print(Luke("Leia"))
print(Luke("Vader"))