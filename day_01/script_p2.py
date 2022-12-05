calories_per_elf = []
with open("./input.txt") as file:
    current_elf_calories = 0
    for line in file:
        if len(line.strip()) == 0:
            calories_per_elf.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

calories_per_elf.sort(reverse=True)
print(calories_per_elf[:3])
print(sum(calories_per_elf[:3]))
