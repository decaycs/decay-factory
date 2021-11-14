import signal
import argparse
import sys
import os
from pathlib import Path

from ImageGoNord import GoNord

from rich.console import Console
from rich.panel import Panel

def main():

    signal.signal(signal.SIGINT, signal_handler)
    console = Console()

    tn_factory = GoNord()
    tn_factory.reset_palette()
    add_tn_palette(tn_factory)

    # Checks if there's an argument
    if len(sys.argv) > 1:
        image_paths = fromCommandArgument(console)
    else:
        image_paths = fromTui(console)

    for image_path in image_paths:
        if os.path.isfile(image_path):
            process_image(image_path, console, tn_factory)
        else:
            console.print(
                f"❌ [red]We had a problem in the pipeline! \nThe image at '{image_path}' could not be found! \nSkipping... [/]"
            )
            continue

# Gets the file path from the Argument
def fromCommandArgument(console):
    command_parser = argparse.ArgumentParser(
        description="A simple cli to manufacture Tokyo Night themed wallpapers."
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
            "🏭 [bold magenta] Tokyo-Night Factory [/] 🏭", expand=False, border_style="magenta"
        )
    )

    return [
        os.path.expanduser(path)
        for path in console.input(
            "🖼️ [bold yellow]Which image(s) do you want to manufacture? (image paths separated by spaces):[/] "
        ).split()
    ]

def process_image(image_path, console, tn_factory):
    image = tn_factory.open_image(image_path)
    
    console.print(f"🔨 [blue]manufacturing '{os.path.basename(image_path)}'...[/]")

    # TODO: might be a better idea to save the new Image in the same directory the command is being run from
    save_path = os.path.join(
        os.path.dirname(image_path), "tn_" + os.path.basename(image_path)
    )

    tn_factory.convert_image(image, save_path=(save_path))
    console.print(f"✅ [bold green]Done![/] [green](saved at '{save_path}')[/]")

def add_tn_palette(tn_factory):

    tnPalette = ["#16161E","#1a1b26","#24283b","#414868","#565f89","#cfc9c2","#9aa5ce","#a9b1d6","#c0caf5","#bb9af7","#7aa2f7","#7dcfff","#2ac3de","#b4f9f8","#9ece6a","#e0af68","#ff9e64","#f7768e"]

    for color in tnPalette:
        tn_factory.add_color_to_palette(color)

## handle CTRL + C
def signal_handler(signal, frame):
    print()
    sys.exit(0)

if __name__ == "__main__":
    main()
