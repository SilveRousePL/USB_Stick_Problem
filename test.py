#!/usr/bin/python3
from main import calculate

with open('test_file') as file:
    capacity = int(file.readline())
    memes = []
    for line in file:
        meme = line.split()
        meme[1] = int(meme[1])
        meme[2] = int(meme[2])
        meme = tuple(meme)
        memes.append(meme)

print(calculate(capacity, memes))
