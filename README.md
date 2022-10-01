# 🗼Decay Factory 🏭

A simple cli to convert any image to a Decay themed wallpaper

![example1](./1.jpg)
![example2](./2.jpg)
decay on the right.

## Alternatives

- [dye](https://github.com/Infinitybeond1/dye): Dye is an ultrafast image colorizer tool that supports decay palette, you can try it too!

## Installation

### AUR

You can install decay-factory using our AUR decay-factory package:

```sh
yay -S decay-factory
```

> You can use any AUR helper :)

### Manually

You can install decay-factory manually

1. Clone the repo.
2. Install the required packages using pip as shown below:
```
pip3 install -r requirements.txt
```
3. Install it with:
```
sudo make install
```
## Installing on NixOS
In order to install decay-factory on NixOS, add to your packages list in configuration.nix in order to be able to run decay-factory
```
python310Packages.rich
python310Packages.image-go-nord
```



## Usage
from your terminal run:
```
decayFactory
```
or
```
decayFactory /path/to/image/
```

 All the outputs will be in ~/Pictures/decay

 ## UNINSTALL
 1. ```cd``` into the repo folder.
 2. Uninstall it with:
 ```
 sudo make uninstall
 ```


 ## Credits
- **Made** with [Schrodinger-Hat's ImageGoNord](https://github.com/Schrodinger-Hat), but with the Decay palette
- **Text User Interface (TUI)** made with [rich](https://github.com/willmcgugan/rich)
