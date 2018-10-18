#!/usr/bin/env python3

# Build dictionary

fav_dic = { 'book' : 'Crime and Punishment' , 'movie' : 'Lord of the Rings' , 'food' : 'risoto' }
print(fav_dic['book'])

# Printing Favorite thing
fav_thing = 'book'
print(fav_dic[fav_thing])
print(fav_dic['food'])

# Adding new keys to dictionary
fav_dic['organism'] = 'arabidopsis'
print(fav_dic)
fav_thing = 'organism'
print(fav_dic[fav_thing])

#
fav_thing = input('My favorite things: book, movie, food and organism. Which one?');
print(fav_thing, 'is', fav_dic[fav_thing])

