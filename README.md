# Python Aim Trainer Bot

This Python bot is designed to automate an aim trainer game, allowing the player to improve their aiming skills. The bot uses computer vision techniques to detect and track targets on the screen, and then moves the mouse to accurately aim and shoot at the targets.

## Features

- Automatic target detection: The bot uses image processing algorithms to detect targets within the game's window.
- Target tracking: Once a target is detected, the bot tracks its movement and predicts its future position.
- Mouse control: The bot moves the mouse cursor to accurately aim at the targets.
- Shooting: When the target is in the desired position, the bot automatically triggers a click event to simulate shooting.

## Prerequisites

Install these libraries from an administrator terminal (windows):

pip install pygame
pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python
