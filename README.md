# snake
This is game of Snake developed in `python=3.6` using `pygame`.

## Installation

### For UBUNTU and its variants

#### Within `anaconda` environment (Recommended)

1. Create anaconda environment from terminal
```
conda env create -f environment.yml
```
This will install `python=3.6` compatible version of `pygame` within an anaconda environment called `snake`.

2. Activate the anaconda environment from terminal
```
conda activate snake
```

3. Run the game from terminal
```
python main.py
```
This will open a window with the game. Enjoy!

#### Install `python-pygame` package directly

```
sudo apt-get install python-pygame
```
afterwards you can start the game by executing the command `python main.py` from terminal
or from any python IDE, e.g., spyder, visual studio code, etc.<br>
**Note**: If you're running the script from IDE, make sure you current working directory is on the `current` path.

## Game play
<img align="right" src="images/temptation.png" height="100">

- The game consists, as of now, two versions:
    + Simple
    + Slither
- The simple version has the most basic logical version without much complications. If you're a developer or someone who wants to get into how to program basic games using `pygame`, this version would serve an a good example.
- Slither consists of slightly more elaborate graphics and gameplay strategies. Play this version for awesome gaming experience.

## Feedback
If you want to contribute to the repository to improve the code, feel free to submit a pull request.
