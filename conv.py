#!/bin/python
import signal
import argparse
import sys
import os
from pathlib import Path

from ImageGoNord import GoNord

from rich.console import Console
from rich.panel import Panel

# CHANGE pirate TO YOUR OWN USER NAME, DO NOT CHANGE THE DIRECTORY ITSELF
mypath="/home/pirate/Pictures/odf/"

def main():

    signal.signal(signal.SIGINT, signal_handler)
    console = Console()

    od_factory = GoNord()
    od_factory.reset_palette()
    add_od_palette(od_factory)

    # Checks if there's an argument
    if len(sys.argv) > 1:
        image_paths = fromCommandArgument(console)
    else:
        image_paths = fromTui(console)

    for image_path in image_paths:
        if os.path.isfile(image_path):
            process_image(image_path, console, od_factory)
        else:
            console.print(
                f"❌ [red]We had a problem in the pipeline! \nThe image at '{image_path}' could not be found! \nSkipping... [/]"
            )
            continue

# Gets the file path from the Argument
def fromCommandArgument(console):
    command_parser = argparse.ArgumentParser(
        description="A simple cli to manufacture OneDark themed wallpapers."
    )
    command_parser.add_argument(
        "Path", metavar="path", nargs="+", type=str, help="The path(s) to the image(s)."
    )
    args = command_parser.parse_args()

    return args.Path

# Gets the file path from user input
def fromTui(console):

    console.print(
        Panel(
            "🏭 [bold magenta] OneDark Factory [/] 🏭", expand=False, border_style="magenta"
        )
    )

    return [
        os.path.expanduser(path)
        for path in console.input(
            "🖼️ [bold yellow]Which image(s) do you want to manufacture? (image paths separated by spaces):[/] "
        ).split()
    ]

def process_image(image_path, console, od_factory):
    image = od_factory.open_image(image_path)
    
    console.print(f"🔨 [blue]manufacturing '{os.path.basename(image_path)}'...[/]")

    # TODO: might be a better idea to save the new Image in the same directory the command is being run from
    save_path = os.path.join(
        mypath, "od_" + os.path.basename(image_path)
    )

    od_factory.convert_image(image, save_path=(save_path))
    console.print(f"✅ [bold green]Done![/] [green](saved at '{save_path}')[/]")

def add_od_palette(od_factory):

    odPalette = ["#1e222a","#353b45","#3e4451","#545862","#565c64","#abb2bf","#b6bdca","#c8ccd4","#e06c75","#d19a66","#e5c07b","#98c379","#56b6c2","#61afef","#c678dd","#be5046"]

    for color in odPalette:
        od_factory.add_color_to_palette(color)

## handle CTRL + C
def signal_handler(signal, frame):
    print()
    sys.exit(0)

if __name__ == "__main__":
    main()
