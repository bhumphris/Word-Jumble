import random
birds = ["Macaw", "Toucan", "Pheasant", "Painted Bunting", "Cardinal", "Crane", "Flamingo", "Parakeet", "Love Bird", "Mallard", "Finch", "Robin", "Dove", "Hawk", "Eagle"]
selection = random.choice(birds)
answer = selection
jumble = list(selection)
for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,

guess = raw_input("\nWhat kind of bird is jumbled?")
guess = guess.upper()
if guess == answer:
    print("correct")
else:
    print(answer)
