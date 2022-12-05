max_calories = 0
with open("./input.txt") as file:
    current_elf_calories = 0
    for line in file:
        if len(line.strip()) == 0:
            if current_elf_calories > max_calories:
                max_calories = current_elf_calories
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

print(max_calories)
