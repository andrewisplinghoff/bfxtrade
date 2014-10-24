#!/usr/bin/env python

from bitfinex import *
import json
import pickle
import os.path
import datetime

bfx = Bitfinex()
new_book = bfx.book({
	'limit_bids': 50,
	'limit_asks': 50,
	'group': 1
})
cur_time = datetime.datetime.now().isoformat()

date = str(datetime.date.today())
file_name = 'orderbooks_' + date + '.pickle'
if os.path.isfile(file_name):
	# Opening our object dumpfile.
	fh = open(file_name, 'r')
	 
	# Creating the unpickler object.
	unpk = pickle.Unpickler(fh)
	 
	# Re-load the books object from our dumpfile.
	books = unpk.load()

else:
	books = {}

#print books.keys()
books[cur_time] = new_book

fh = open(file_name, 'w') 

pickler = pickle.Pickler(fh)
pickler.dump(books)
