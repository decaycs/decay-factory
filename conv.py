#!/usr/bin/env python3

import signal
import argparse
import sys
import os

from pathlib import Path
from ImageGoNord import GoNord
from rich.console import Console
from rich.panel import Panel

mypath=str((Path(os.path.expanduser('~')) / 'Pictures' / 'decay').absolute())


def main():
    signal.signal(signal.SIGINT, signal_handler)
    console = Console()

    decay_factory = GoNord()
    decay_factory.reset_palette()
    add_decay_palette(decay_factory)

    # Checks if there's an argument
    if len(sys.argv) > 1:
        image_paths = fromCommandArgument(console)
    else:
        image_paths = fromTui(console)

    for image_path in image_paths:
        if os.path.isfile(image_path):
            process_image(image_path, console, decay_factory)
        else:
            console.print(
                f"❌ [red]We had a problem in the pipeline! \nThe image at '{image_path}' could not be found! \nSkipping... [/]"
            )
            continue


# Gets the file path from the Argument
def fromCommandArgument(console):
    command_parser = argparse.ArgumentParser(
        description="A simple cli to manufacture Decay themed wallpapers."
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
            "🏭 [bold magenta] Decay Factory [/] 🏭", expand=False, border_style="magenta"
        )
    )

    return [
        os.path.expanduser(path)
        for path in console.input(
            "🖼️ [bold yellow]Which image(s) do you want to manufacture? (image paths separated by spaces):[/] "
        ).split()
    ]


def process_image(image_path, console, decay_factory):
    image = decay_factory.open_image(image_path)
    
    console.print(f"🔨 [blue]manufacturing '{os.path.basename(image_path)}'...[/]")

    # TODO: might be a better idea to save the new Image in the same directory the command is being run from
    save_path = os.path.join(
        mypath, "decay_" + os.path.basename(image_path)
    )

    decay_factory.convert_image(image, save_path=(save_path))
    console.print(f"✅ [bold green]Done![/] [green](saved at '{save_path}')[/]")


def add_decay_palette(decay_factory):
    decayPalette = ["#13171b","#171B20","#1a1e24","#21262e","#242931","#485263","#76b97f","#70a5eb","#c68aee","#74bee9","#dee1e6","#a9b1d6","#171a1f","#1c252c","#384148","#e05f65","#fc7b81","#78dba9","#94f7c5","#f1cf8a","#ffeba6","#8cc1ff","#e2a6ff","#90daff","#fafdff","#f5f5f5","#22262e"]

    for color in decayPalette:
        decay_factory.add_color_to_palette(color)


## handle CTRL + C
def signal_handler(signal, frame):
    print()
    sys.exit(0)


if __name__ == "__main__":
    main()
