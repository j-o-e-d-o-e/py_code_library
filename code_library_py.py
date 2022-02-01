import os


def setup_lib():
    os.chdir("library")
    lib = []
    for fn in os.listdir():
        if os.path.isfile(fn):
            with open(fn, "r") as f:
                entry = {"title": f.readline().replace("\n", "")}
                f.readline()
                entry["tags"] = f.readline().replace("\n", "")
                f.readline()
                entry["body"] = f.readlines()
                lib.append(entry)
    return sorted(lib, key=lambda entry: entry["title"])


def print_toc(lib):
    print("PYTHON CODE LIBRARY".center(80, "="))
    toc = []
    for entry in lib:
        temp = [str((lib.index(entry) + 1)) + " - " + entry["title"]]
        if entry["tags"]:
            temp.append("->(" + str((lib.index(entry) + 1)) + ") " + entry["tags"])
        toc.append(temp)
    col_width = max(len(word) for row in toc for word in row) - 6
    for row in toc:
        print("".join(word.ljust(col_width) for word in row))


def print_entry(lib, num):
    print("\n----------------------------------------")
    print(str(num) + " - " + str(lib[num - 1]["title"]) + "\n")
    for line in lib[num - 1]["body"]:
        print(line.replace("\n", ""))
    print("----------------------------------------")
    print("----------------------------------------")


def main():
    lib = setup_lib()
    print_toc(lib)
    user_input = None
    while True:
        try:
            user_input = int(input("\nWhat would you like to read? "))
        except ValueError:
            print("No valid input.")
            continue
        if user_input == 0:
            print("\n")
            print_toc(lib)
        elif user_input == 667:
            break
        else:
            print_entry(lib, user_input)


if __name__ == "__main__":
    main()
