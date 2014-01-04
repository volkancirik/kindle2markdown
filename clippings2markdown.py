#! /usr/bin/python

__author__="Volkan Cirik <volkan.cirik@gmail.com>"
__date__ ="$January, 2014"

import sys
"""
convert kindle clippings to markdown format
"""

class book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.clippings = []
    def addClippings(self,clip):
        self.clippings.append(clip)


rawclips = [line.strip(' \t\n\r') for line in open(sys.argv[1])]

L = len(rawclips)
i = 0
id = 1
bookshelf = {}
id2book = {}

while True:
    title = rawclips[i].split('(')[0].lstrip()
    author = rawclips[i].split('(')[-1].split(')')[0]
    if (title,author) not in bookshelf:
        bookshelf[(title,author)] = book(author,title)
        id2book[id] = (title,author)
        id +=1
    i += 3
    while i<L and not("===" in rawclips[i]):
        clip = rawclips[i]
        i +=1
        bookshelf[(title,author)].addClippings(clip)
    i +=1
    if i == L:
        break;
print "books and clippings are loaded!"
for i in id2book:
    title,author = id2book[i]
    print i,title,author
while True:
    print "Choose a book among above with the id",(1,id-1)
    i = int(raw_input())
    if i not in id2book:
        print "there is no such id, choose among",(1,id-1)
    else:
        break

title,author = id2book[i]
f=open(title+"-"+author+"-comments.md","w")

print "initial words before commenting the book",title,"from",author
print "press enter to skip"
comment = raw_input()
if len(comment) > 0:
    f.write(comment+"\n\n")

for clip in bookshelf[id2book[i]].clippings:
    if len(clip) == 0:
        continue
    print clip
    print "_______________________"
    print "any comment to above clip? press enter to skip"
    comment = raw_input()
    if len(comment) > 0:
       f.write("> "+clip+"\n\n")
       f.write(comment+"\n\n")

print "final words about the book",title,"from",author
print "press enter to skip"
comment = raw_input()
if len(comment) > 0:
    f.write(comment+"\n\n")


f.close()
