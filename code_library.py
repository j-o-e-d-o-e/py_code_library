import os
import readline


def setup_lib():
    os.chdir("library")
    lib = []
    for fn in os.listdir():
        if os.path.isfile(fn):
            with open(fn, "r") as f:
                entry = {"path": fn, "title": f.readline().replace("\n", "")}
                f.readline()
                entry["tags"] = f.readline().replace("\n", "")
                lib.append(entry)
    lib = sorted(lib, key=lambda entry: entry["title"])
    count = 1
    for entry in lib:
        entry["index"] = count
        count += 1
    return lib


def print_toc(lib):
    print(ansi_format(" PYTHON CODE LIBRARY ".center(60, "="), bold=True))
    for i, entry in enumerate(lib):
        tmp = " " if entry["index"] < 10 else ""
        tmp = tmp + str(entry["index"]) + " - " + entry["title"] + " " * (35 - len(entry["title"])) + entry["tags"]
        print(ansi_format(tmp, color=CYAN if i % 2 != 0 else GREEN, color_bg=i % 2 != 0))


def print_entry(entry):
    print(ansi_format("\n----------------------------------------"))
    color = GREEN if not entry["index"] % 2 == 0 else CYAN
    print(ansi_format(str(entry["index"]) + " - " + str(entry["title"]), color=color, bold=True, underline=True))
    with open(entry["path"], "r") as f:
        f.readline()
        f.readline()
        f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            elif line == "EXAMPLE\n":
                print(ansi_format(line.replace("\n", ""), color=color, bold=True))
            else:
                print(ansi_format(line.replace("\n", ""), color=color))
    print(ansi_format("----------------------------------------"))


ANSI_ESC = "\033["
RED = 91  # text colors
GREEN = 92
CYAN = 96
BLACK = 40  # background color


def ansi_format(txt, color=RED, color_bg=False, bold=False, underline=False):
    tmp = ANSI_ESC + str(color)
    if color_bg:
        tmp = tmp + ";" + str(BLACK)
    if bold:
        tmp = tmp + ";1"
    if underline:
        tmp = tmp + ";4"
    return tmp + "m" + txt + ANSI_ESC + "0m"


def main():
    readline.clear_history()  # adds arrow-up/-down functionality
    lib = setup_lib()
    print_toc(lib)
    while True:
        user_input = input(ansi_format("\nWhat would you like to read? "))
        if user_input.startswith('s:'):
            search_term = user_input[2:]
            print("\n")
            print_toc([entry for entry in lib if search_term in entry["tags"].lower()])
            continue
        try:
            user_input = int(user_input)
            if user_input < 0 or (user_input > len(lib) and user_input != 667):
                print(ansi_format("Out of range."))
                continue
        except ValueError:
            print(ansi_format("No valid input."))
            continue
        if user_input == 0:
            print("\n")
            print_toc(lib)
        elif user_input == 667:
            print(ansi_format("Devil's neighbour wishes you a good day."))
            break
        else:
            print_entry(lib[user_input - 1])


if __name__ == "__main__":
    main()
