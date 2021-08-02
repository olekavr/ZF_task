#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ' '.join(text)


def save(text):
    f = open("new.txt", "w")
    f.write(text)
    f.close()


def count(text):
    world_dict = {}
    clear_text = text.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
    worlds_list = clear_text.split(" ")
    print('Worlds in text - {}'.format(len(worlds_list)))
    for world in worlds_list:
        if world in world_dict.keys():
            world_dict[world] += 1
        else:
            world_dict[world] = 1
    print('Unique worlds in text - {}'.format(len(world_dict)))
    list_dict = list(world_dict.items())
    list_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(10):
        print('{} - world "{}" has appeared {} times'.format(i+1, list_dict[i][0], list_dict[i][1]))
    print('World "whale" has appeared {} times'.format(world_dict['whale']))


def task(fname):
    book = epub.read_epub(fname)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    text = ''
    for c in items[1:]:
        text += chapter_to_str(c)
    save(text)
    count(text)
    return text


if __name__ == "__main__":
    task('pg2701.epub')
