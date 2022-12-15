import functools


class Directory:
    def __init__(self, name, parent_dir, sub_directories, sub_files, path, totalSize):
        self.name = name
        self.parent_dir = parent_dir
        self.sub_directories = sub_directories
        self.sub_files = sub_files
        self.path = path
        self.totalSize = totalSize

    def __str__(self):
        return f"{self.path} - {self.totalSize}"


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def get_system(data):
    commands_and_results = [command.strip().split("\n") for command in data.split("$ ") if command]
    # print(commands_and_results)

    root = Directory("/", None, [], [], "/", None)
    current_dir = root
    for command in commands_and_results[1:]:
        args = command[0].split()
        ls_results = command[1:]
        if args[0] == "ls":
            entities_in_ls = [line.split() for line in ls_results]
            files_in_ls = [File(b, a) for a, b in entities_in_ls if a != "dir"]
            direc_in_ls = [Directory(b, current_dir, [], [], current_dir.path + b + "/", 0) for a, b in entities_in_ls
                           if
                           a == "dir"]
            current_dir.sub_files = files_in_ls  # risky
            current_dir.sub_directories = direc_in_ls
        else:  # is cd
            cd_folder = args[1]  # could be foler or ..
            if cd_folder == "..":
                current_dir = current_dir.parent_dir
            else:
                new_dir = [item for item in current_dir.sub_directories if item.name == cd_folder][0]
                current_dir = new_dir
    return root


def sum_files(files: File):
    return functools.reduce(lambda acc, x: acc + int(x.size), files, 0)


def compute_total(directory: Directory):
    if len(directory.sub_directories) == 0:
        sum_current = sum_files(directory.sub_files)
        # print(str(directory.path) + ">" + str(sum_current))
        directory.totalSize = sum_current
        return sum_current
    else:
        sum_dir = [compute_total(dir) for dir in directory.sub_directories]
        sum_files_current = sum_files(directory.sub_files)
        total = sum(sum_dir) + sum_files_current
        # print(str(directory.path) + ">" + str(total))
        directory.totalSize = total
        return total


def get_all_directories(directory: Directory):
    if len(directory.sub_directories) == 0:
        return [directory]
    else:
        sub_directories = [get_all_directories(sub_dir) for sub_dir in directory.sub_directories]
        flat_list = [item for sublist in sub_directories for item in sublist]
        flat_list.append(directory)  # not great
        return flat_list


if __name__ == "__main__":
    f = open("input.txt")
    data = f.read()

    system = get_system(data)
    compute_total(system)  # it transform

    # print(system.name)
    all = get_all_directories(system)

    # Part-1
    sorted_by_size = sorted(all, key=lambda x: x.totalSize, reverse=True)
    criteria_1 = [dir for dir in sorted_by_size if dir.totalSize <= 100000]
    total = functools.reduce(lambda acc, x: acc + int(x.totalSize), criteria_1, 0)
    print(total)

    #for dir in sorted_by_size: print(dir)

    # Part-2
    to_find = 30000000 - (70000000 - sorted_by_size[0].totalSize)
    criteria_2 = [dir for dir in sorted_by_size if dir.totalSize >= to_find]
    print(criteria_2[-1].totalSize)


    # print(all)
    # biggest = sorted(ut, key=lambda x: x.count, reverse=True)
