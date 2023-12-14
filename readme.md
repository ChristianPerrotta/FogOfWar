<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TITLE -->
<br />
<div align="center">
  <h3 align="center">Fog of War</h3>
    <a href="https://github.com/ChristianPerrotta/FogOfWar/releases/tag/v1.1.1">
        <img src="./images/icon.ico" alt="Logo" width="20" height="20">
    </a>
  <p align="center">
    The classic minesweeper with a touch of the Fire Emblem experience!
    <br />
    <a href="https://github.com/ChristianPerrotta/FogOfWar/releases/tag/v1.1.1">Play now!</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About the Project

[![Fog of War Screenshot][project-screenshot]](https://github.com/ChristianPerrotta/FogOfWar/releases/tag/v1.1.1)

<i>Fog of War</i> is a classic minesweeper game, but remade using visual elements from the Fire Emblem franchise, more specifically the first 8 games.

For each play experience, you may choose:
* the tileset that will be used to render the map (from FE1 to FE8)
* choose the difficulty, which will define the number of enemies on each map

Each run is comprised of 5 chapters (5 maps), each one containing a selection of tiles from the chosen game.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built with

This game has been created with:
* [![Python][Python]][Python-url]
* [![Pygame][Pygame]][Pygame-url]
* [![Tkinter][Tkinter]][Tkinter-url]
* [![Pillow][Pillow]][Pillow-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, you can choose to clone the repository and run the scripts or you can download the `.exe` file from the [Release](https://github.com/ChristianPerrotta/FogOfWar/releases/tag/v1.1.1) page.

### Installation

Make sure you are using python version 3.11.0 for this.

1. Clone the repo
```sh
git clone https://github.com/ChristianPerrotta/FogOfWar.git
```

2. Install the packages. If you want to specifically use the versions I'm using, add the `==[VERSION NUMBER]` after the package name, as indicaded in the examples bellow. You may need to upgrade your `pip` as well.

* Pillow:
```sh
pip install Pillow==9.3.0
```

* Pygame:
```sh
pip install pygame==2.4.0
```

3. Run the main script
```sh
python .\main.py
```

If you choose to run the `.exe` file from the release page, you may need to manually allow your antivirus to execute the game. This happens because the executable was created with PyInstaller, which almost always triggers an alert from most antiviruses.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- HOW TO PLAY -->
## How to play

The game mostly follows standard [minesweeper rules](https://minesweepergame.com/strategy/how-to-play-minesweeper.php). The two main differences are:
* you always start with an open square, which contains your lord and is never surrounded by enemies
* instead of numbers, you get differents tiles; however, you may hover the cursor over each tile to check the corresponding number

Clicking with the right button of the mouse will change the tile into an emblem (flag), showing you believe that there is an enemy on that tile. Right-clicking on the same tile again will convert the emblem into a question mark. Right-clicking a third time will revert to the initial unopend tile.

You win the game by clearing 5 consecutive maps (chapters). You can check the chapter you are playing, the number of remaining enemies and tiles on the left column.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Christian Perrotta - chr.perrotta@gmail.com

Project Link: [https://github.com/ChristianPerrotta/FogOfWar](https://github.com/ChristianPerrotta/FogOfWar)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/ChristianPerrotta/FogOfWar/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/christian-perrotta-17422b114/
[project-screenshot]: ./images/screenshot.png
[Python]: https://img.shields.io/badge/python-3.11.0-3670A0?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://www.python.org/
[Pygame]: https://img.shields.io/badge/pygame-2.4.0-yellow?style=for-the-badge
[Pygame-url]: https://www.pygame.org/news
[Tkinter]: https://img.shields.io/badge/tkinter-8.6-purple?style=for-the-badge
[Tkinter-url]: https://docs.python.org/3/library/tkinter.html
[Pillow]: https://img.shields.io/badge/Pillow-9.3.0-green?style=for-the-badge
[Pillow-url]: https://pypi.org/project/Pillow/