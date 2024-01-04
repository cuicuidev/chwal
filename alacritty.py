import os

HOME = os.path.expanduser("~")
PYWAL_CONFIG = f"{HOME}/.cache/wal/colors"
TOML_CONFIG = f"{HOME}/.config/alacritty/alacritty.toml"

def main():
    normal_colors_range = range(0, 8)
    bright_colors_range = range(8, 16)

    color_names = [
            "black",
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "white"
            ]

    special_colors_indices = {
            "background": 0,
            "foreground": 7,
            "cursor": 15,
            "text": 0,
            }

    colors = read_colors()

    config = generate_colors_config(colors, normal_colors_range, bright_colors_range, color_names, special_colors_indices)

    # Write config to file
    beginning_line = get_beginning_line()
    ending_line = get_ending_line()

    print(f"Beginning line: {beginning_line}")
    print(f"Ending line: {ending_line}")

    if not beginning_line or not ending_line:
        print("Could not find beginning or ending line, appending to end of file")
        with open(TOML_CONFIG, 'a') as f:
            f.write("\n")
            f.write(config)
    elif beginning_line and ending_line:
        print("Found beginning and ending line, replacing config")
        with open(TOML_CONFIG, 'r') as f:
            lines = f.readlines()

        with open(TOML_CONFIG, 'w') as f:
            for i, line in enumerate(lines):
                if i == beginning_line - 1:
                    f.write(config)
                elif i >= beginning_line and i < ending_line:
                    continue
                else:
                    f.write(line)

    else:
        raise Exception("One of beginning or ending line was found, but not the other")
        

def generate_colors_config(colors, normal_colors_range, bright_colors_range, color_names, special_colors_indices):
    config = "# BEGINNING OF COLORS \n\n"
    config += "[colors.normal]\n"
    for i in normal_colors_range:
        config += f"{color_names[i]} = \"{colors[i].strip()}\"\n"
    config += "\n"

    config += "[colors.bright]\n"
    for i in bright_colors_range:
        config += f"{color_names[i-8]} = \"{colors[i].strip()}\"\n"
    config += "\n"

    config += "[colors.cursor]\n"
    config += f"cursor = \"{colors[special_colors_indices['cursor']].strip()}\"\n"
    config += f"text = \"{colors[special_colors_indices['text']].strip()}\"\n"
    config += "\n"

    config += "[colors.primary]\n"
    config += f"background = \"{colors[special_colors_indices['background']].strip()}\"\n"
    config += f"foreground = \"{colors[special_colors_indices['foreground']].strip()}\"\n"
    config += "\n"

    config += "# END OF COLORS \n"

    return config

def read_colors():
    with open(PYWAL_CONFIG) as f:
        colors = f.readlines()
    return colors

def get_beginning_line():
    with open(TOML_CONFIG) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line == "# BEGINNING OF COLORS \n":
            return i + 1
    return None

def get_ending_line():
    with open(TOML_CONFIG) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line == "# END OF COLORS \n":
            return i + 1
    return None

if __name__ == '__main__':
    main()
