from sty import fg, bg
from random import randrange

Scene = []

itemcolor = {"?": fg(232), "#": fg(randrange(238, 242)), " ": fg(236), "0": fg(20), "±": fg(15), "≈": fg(94),
             "+": fg(94), "-": fg(94), "|": fg(94), "Λ": fg(203), ",": fg(34), ";": fg(28), "~": fg(45) + bg(26),
             "д": fg(11), "=": fg(94), "─": fg(94), "┃": fg(94), "E": fg(1), "R": fg(1), "O": fg(1), "M": fg(1),
             "!": fg(1), "\\": fg(241), "/": fg(randrange(239, 241)), "^": fg(randrange(239, 241)),
             "⁄": fg(randrange(239, 241)), "T": fg(41), "@":fg(3)}

# 1   2   3   4   5   6   7   8   9  10   11 12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32
Dungeon1 = [
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "#", "#", "#",
     " ", "#", "#", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "#", " ", " ", " ", " ", "#", "#", "#",
     "#", "#", "#", "#", "#", "#", "#", "#", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "#", " ", " ", " ", " ", "#", "#", " ",
     " ", " ", " ", " ", " ", " ", " ", "#", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "#", " ", " ", " ", " ", "#", "#", " ",
     "±", " ", "±", " ", "±", " ", " ", "#", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "#", "#", "#", "#", "#", " ", " ", " ", " ", "#", "#", " ",
     "≈", " ", "≈", " ", "≈", " ", " ", "#", "?"],
    ["?", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ",
     " ", " ", " ", " ", " ", " ", " ", "#", "?"],
    ["?", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ",
     " ", " ", " ", " ", " ", " ", " ", "#", "?"],
    ["?", "#", " ", "+", "-", "-", "-", "-", "+", " ", "#", "#", " ", " ", ";", " ", " ", " ", " ", " ", "#", "#", "#",
     "#", "#", "#", "#", "#", " ", "#", "#", "?"],
    ["?", "#", " ", "|", " ", " ", " ", " ", "|", " ", "#", "#", " ", ",", ";", ",", " ", " ", " ", " ", "#", "#", " ",
     " ", " ", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "#", " ", "|", " ", " ", " ", " ", "|", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ",
     " ", "д", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "#", " ", "+", "-", "-", " ", "-", "+", " ", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", "#", "#", " ",
     " ", " ", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "?", "?", "?", "#", " ", " ", " ", " ", " ", "#", "#", " ",
     " ", " ", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "?", "?", "?", "#", "#", "#", " ", "#", "#", "#", "#", " ",
     " ", " ", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "#", "#", "#", "#", "#", "#", " ", " ", "#", "#", "?", "?", "?", "?", "?", "#", " ", "#", "?", "?", "#", " ",
     " ", " ", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "?", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "─", "#", "#", "#", "#", " ",
     " ", " ", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "?", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "~", "~", " ", " ", " ", "#", "#", " ",
     " ", " ", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "?", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", "#", "~", "~", " ", " ", " ", "┃", " ", " ",
     " ", " ", " ", " ", "#", " ", "#", "?", "?"],
    ["?", "?", "#", "Λ", "Λ", "Λ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", "#", "#", "#",
     "#", "#", "#", "#", "#", " ", "#", "?", "?"],
    ["?", "?", "#", " ", " ", "Λ", " ", " ", " ", " ", " ", " ", " ", "┃", " ", " ", " ", " ", " ", " ", "┃", " ", " ",
     " ", " ", " ", " ", " ", " ", "#", "?", "?"],
    ["?", "?", "#", " ", " ", "Λ", " ", " ", " ", " ", " ", "#", " ", "#", "#", " ", " ", " ", " ", " ", "#", "#", "#",
     "#", "#", "#", "#", "#", "#", "#", "?", "?"],
    ["?", "?", "#", " ", " ", "Λ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ",
     "#", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", ",",
     "#", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "#", ";",
     "#", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "#",
     " ", "#", "?", "?", "?", "?", "?", "?", "?", "?"],
]

WaterRoom = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "~", " ", " ", " ", " ", " ", "~", "#"],
    ["#", "~", "~", " ", " ", " ", "~", "~", "#"],
    ["#", " ", "~", "~", "~", "~", "~", " ", "#"],
    ["#", ",", ",", " ", " ", " ", " ", " ", "#"],
    ["#", ";", ",", " ", " ", ",", ",", ";", "#"],
    ["#", ",", " ", ";", " ", ";", " ", " ", "#"],
    ["#", "#", "#", "#", " ", "#", "#", "#", "#"]]

ErrorLevel = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "E", "R", "R", "O", "R", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "R", "O", "O", "M", "!", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

GrassField = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "/", "/", "⁄", "^", "\\", "\\", "\\", "\\", "#", " ", " ", "T", " ", "±", "T", " ", "#"],
    ["#", "⁄", "/", "/", "^", "\\", "\\", "\\", "#", "#", " ", " ", "T", " ", "≈", "T", " ", "#"],
    ["#", "#", "⁄", "/", "^", "\\", "\\", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", "#"],
    ["#", " ", "T", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", "T", " ", " ", "T", "T", "T", " ", " ", " ", "T", "T", " ", "#"],
    ["#", " ", " ", " ", "T", "T", " ", " ", " ", "T", "T", "T", " ", " ", " ", "T", " ", "#"],
    ["#", " ", " ", " ", "T", "T", " ", " ", " ", "T", "T", "T", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", ",", " ", "T", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "~", "~", "~", " ", " ", ";", ",", ";", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "~", "~", "~", "~", " ", " ", ";", ";", " ", " ", " ", " ", "T", "T", " ", " ", "#"],
    ["#", "~", "~", "~", "~", " ", " ", ",", ",", " ", " ", " ", "T", "T", "T", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", "T", "T", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


