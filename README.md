<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/assembly-city/master/game/gui/window_icon.png" alt="Assembly City" width="250">
</p>

# Assembly City

![release](https://img.shields.io/github/v/release/remarkablegames/assembly-city)
[![build](https://github.com/remarkablegames/assembly-city/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/assembly-city/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/assembly-city/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/assembly-city/actions/workflows/lint.yml)

⚖️ Welcome to Assembly City!

Play the game on:

- [remarkablegames](https://remarkablegames.org/assembly-city)

## Credits

### Art

- [Sraye](https://sraye.itch.io/mature-male-character-sprites)
- [Tainara-P](https://tainara-p.itch.io/)
- [smashingstocks](https://www.flaticon.com/free-icon/justice-scale_6744071)
- [sutemo](https://sutemo.itch.io/)

### Audio

- [Kenney](https://kenney.nl/assets/interface-sounds)

### Music

- [Hizumi Tail](https://hizumi-tail.itch.io/)

## Ideation

- [Excalidraw](https://excalidraw.com/#json=6czVMRbr8qxWM-nVA6Zlt,Zd68FBkx9bQ8ZplCWGlyBg)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/assembly-city.git
cd assembly-city
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```

## Resources

- [POV: a cynic's guide to Citizens' Assembly](https://oneworldornone.world/the-comic-book-explainer)
- [Citizens' Assembly Explained](https://assemblyexplainer.com/)
- [Assembling an Assembly Guide](https://assemblyguide.demnext.org/)

## License

[MIT](LICENSE)
