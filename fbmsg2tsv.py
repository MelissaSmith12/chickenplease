#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup
from textblob import TextBlob

def get_text(L):
    return ' '.join(x.get_text() for x in L)

def flatten_text(L):
    return ' '.join(x if isinstance(x, str) else '[]' for x in L).strip().replace('\n', ' ')

def get_chat_msgs(soup):
        sender = 'foo'
        dt = 'beginning of time'
        for thread in soup.find_all('div', 'thread'):
        #   print(thread.prettify())
           for elem in thread.find_all(['div', 'p']):
              if elem.name == 'div':
                  if 'message_header' in elem['class']:
                      sender = get_text(elem.find_all('span', 'user'))
                      dt = get_text(elem.find_all('span', 'meta'))
              else:  # must be p
                  txt = flatten_text(elem.contents)
                  if txt and txt != 'You are now connected on Messenger.':
                      yield sender, dt, txt


def main_full():
        print('\t'.join(['sender','timestamp','polarity', 'subjectivity', 'contents']))
        for fn in sys.argv[1:]:
            soup = BeautifulSoup(open(fn).read(), "lxml")

            for sender, dt, txt in get_chat_msgs(soup):
                tb = TextBlob(txt)
                polarity, subjectivity = tb.sentiment
                print('\t'.join([sender,dt, str(polarity), str(subjectivity), txt]))

def main_words():
        print('\t'.join(['sender','timestamp','word']))
        for fn in sys.argv[1:]:
            soup = BeautifulSoup(open(fn).read(), "lxml")

            for sender, dt, txt in get_chat_msgs(soup):
                tb = TextBlob(txt)
                for w in tb.words:
                    print('\t'.join([sender,dt,w]))

def main_participants():
        print('\t'.join(['id','participant', 'num_participants']))
        for fn in sys.argv[1:]:
            soup = BeautifulSoup(open(fn).read(), "lxml")

            senders = set([sender for sender, dt, txt in get_chat_msgs(soup)])
            for sender in senders:
                print('\t'.join([fn, sender, str(len(senders))]))

main_full()
#main_words()
#main_participants()
