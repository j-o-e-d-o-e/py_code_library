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
    print(ansi_format(" PYTHON CODE LIBRARY ".center(60, "="), bold=True))
    for entry in lib:
        i = lib.index(entry) + 1
        tmp = " " if i < 10 else ""
        tmp = tmp + str(i) + " - " + entry["title"] + " " * (35 - len(entry["title"])) + entry["tags"]
        print(ansi_format(tmp, color=CYAN if i % 2 == 0 else GREEN, color_bg=i % 2 == 0))


def print_entry(lib, num):
    print(ansi_format("\n----------------------------------------"))
    color = GREEN if not num % 2 == 0 else CYAN
    print(ansi_format(str(num) + " - " + str(lib[num - 1]["title"]) + "\n", color=color, bold=True, underline=True))
    for line in lib[num - 1]["body"]:
        if line == "EXAMPLE\n":
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
    lib = setup_lib()
    print_toc(lib)
    while True:
        try:
            user_input = int(input(ansi_format("\nWhat would you like to read? ")))
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
            print_entry(lib, user_input)


if __name__ == "__main__":
    main()
