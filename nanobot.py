#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, random, time, string
from time import gmtime, strftime

botnick		= "NanoBot"
channel		= "#python"
nickpass  	= "******"
server		= "smirnoff.vodka.whocares.ws"
port		= 6667
hater 		= "32143DDB"
owner		= "ins3c7"
VERSION		= "NanoBot v1.0.3b - Coded by ins3c7"
CEREBRO 	= "cerebro.txt"

def ping():
	sock.send("PONG :Pong\n")

def privmsg(chan, msg):
	sock.send("PRIVMSG " + chan + " :" + msg + "\n")

def joinchan(chan):
	sock.send("JOIN " + chan + "\n")

def identify():
	sock.send("PRIVMSG NickServ :identify " + passwd + "\n")

def quit():
	sock.send("QUIT :" + VERSION + "\n")
	time.sleep(2)
	exit()
#
def log(logg):
	 fl = open("logfile.txt", "a")
	 fl.write(logg + " \n")
	 fl.close()

def _cmp(x, y):
        return cmp(x[-1], y[-1])

def topnicks():
	f = open("logfile.txt", "r")
	text = f.readline()
	nickdic = {}
	while len(text) is not 0:
		if len(text) > 10:
			text = text.split("!")[0]
			if text not in nickdic:
				nickdic[text] = 1
			else:
				nickdic[text] += 1
		text = f.readline()
	ord = sorted(nickdic.items(), _cmp)
	diclen = len(nickdic)
	nicktop = diclen - 3
	top10 = ord[nicktop:]
	toplen = len(top10) - 1
	
	privmsg(channel, "# Top mais falantes:\n")
	for i in enumerate(top10):
		privmsg(channel, "%s = %d" % (top10[toplen][0], top10[toplen][1]))
		toplen -= 1
	f.close()

def topwords():
	f = open("cerebro.txt", "r")
	text = f.readline()
	dic = {}
	while len(text) is not 0:
			if len(text) > 10:
					text = text.lower()
					text = text.replace(".", " ")
					text = text.replace(",", " ")
#					text = text.split("=")[1] # descomentar se for pra ler livros.
					text = text.split()
					for p in text:
							if p not in dic:
									dic[p] = 1
							else:
									dic[p] += 1
			text = f.readline()
	ord = sorted(dic.items(), _cmp)
	diclen = len(dic)
	dictop = diclen - 10
	top10 = ord[dictop:]
	toplen = len(top10) - 1

	privmsg(channel, "# Palavras encontradas:\n")
	x = 1
	for i, prog in enumerate(top10):
			privmsg(channel, "%.2d. %s = %d\n" % (x, top10[toplen][0], top10[toplen][1]))
			toplen -= 1
			x += 1
	privmsg(channel, "A palavra mais digitada foi '%s', repetida %d vezes.\n" % (top10[toplen][0], top10[toplen][1]))
	f.close()

def aprender():
	words = []
	linhas = 0
	tempoinicial = time.time()

	privmsg(channel, "Carregando livro...")

	f = open(CEREBRO, 'r')
	text = f.readline()

	while len(text) is not 0:
		text = text.lower().split()
		for p in text:
			if p.isdigit() == False:
				if p.isalpha():
					if p not in words:
						words.append(p)
		text = f.readline()
		linhas += 1

	
	f.close()
	
	tempofinal = time.time()
	tempototal = tempofinal - tempoinicial

	privmsg(channel, "Total: %d linhas lidas. Concluído em %.2f segundos.\n" % (linhas, tempototal))
	privmsg(channel, "O livro aprendido possúi %d palavras.\n" % len(words))

def falar():
	words = []

	f = open(CEREBRO, 'r')
	text = f.readline()

	while len(text) is not 0:
		text = text.lower().split()
		for p in text:
			if p.isdigit() == False:
#				if p.isalpha():
				if p not in words:
					words.append(p)
		text = f.readline()
	
	f.close()

	w1 = []
	w2 = []
	w3 = []
	w4 = []
	
	frase = []

	for word in words:
		if 1 <= len(word) <= 2:
			w1.append(word)
		elif 3 <= len(word) <= 4:
			w2.append(word)
		elif 5 <= len(word) <= 6:
			w3.append(word)
		else:
			w4.append(word)

	ww1 = random.choice(w1)
	ww2 = random.choice(w2)
	ww3 = random.choice(w3)
	ww4 = random.choice(w4)

	while ww3[-1] != 's':
		ww3 = random.choice(w3)
	while ww1[-1] != 's':
		ww1 = random.choice(w1)
		print "ww1"
	while ww4[-1] != 's':
		ww4 = random.choice(w4)
		print "ww4", ww4[-2], ww1[-2]

	incl = ['são', 'podem ser', 'não são', 'um dia serão', 'parecem ser', 'individualmente são', 'particulamente são', 'vão ser']
	print "<<< PASSOU >>>"
	privmsg(channel, "%s %s %s %s.\n" % (ww1.capitalize(), ww4, random.choice(incl), ww3))

#
from operator import itemgetter

def read():
	f = open("cerebro.txt", "r")

	text = f.readline()
	dic = {}
	lines = 0

	while len(text) is not 0:
		if len(text) > 10:
				text = text.lower()
				text = text.replace(".", " ")
				text = text.replace(",", " ")
				text = text.split()
				for p in text:
						if p.isdigit() == False:
							if p.isalpha():
								if p not in dic:
										dic[p] = 1
								else:
										dic[p] += 1
		lines += 1
		text = f.readline()

#	print "\n", lines, "linhas lidas.\n"
	return dic

def orde(max):
	dic = read()
	sor = sorted(dic.items(), key=itemgetter(1), reverse=True)

	x = 0
	top = []

	for w in sor:
		if x < max:
			top.append(w)
			x += 1
		else:
			return top

def filtr():
	top = orde(5000)
	lists = []
	
	for w in top:
		lists.append(w[0])

	return lists

def make():
	lists = filtr()
	frase = []

	f = open('lero.txt', 'r')

	get = f.readlines()
	get = get[0].split('. ')[0].replace(', ', ' ')
	get = get.split()

	w1 = []
	w2 = []
	w3 = []
	w4 = []
	w5 = []
	w6 = []
	w7 = []
	w8 = []
	w9 = []


	for x in lists:
		if x[-2:] == 'ia':
			w1.append(x)
		elif x[-2:] == 'ar':
			w2.append(x)
		elif x[-3:] == 'omo':
			w3.append(x)
		elif x[-2:] == 'ei':
			w4.append(x)
		elif x[-3:] == 'uma':
			w5.append(x)
		elif x[-2:] == 'de':
			w6.append(x)
		elif x[-1] == 'o':
			w7.append(x)
		elif x[-2:] == 'el':
			w8.append(x)

	falaa = "Eu até", random.choice(w1), random.choice(w2), "mas não", random.choice(w7) + ".", "Eu", random.choice(w1), random.choice(w2), random.choice(w3), random.choice(w4) + ", mas", random.choice(w1), "de", random.choice(w2), random.choice(w5), random.choice(w6) + "."
	falaa = str(falaa)	

	privmsg(channel, falaa)

	
def falar2():
	f = open("cerebro.txt", "r")
	g = open("cerebro.txt", "r")
	
	text2 = f.readlines()
	g.close()

	text = f.readline()
	dic = {}

	print text2

	while len(text) is not 0:
		if len(text) > 10:
				text = text.lower()
				text = text.replace(".", " ")
				text = text.replace(",", " ")
				text = text.split()
				for p in text:
						if p.isdigit() == False:
							if p.isalpha():
								if p not in dic:
										dic[p] = 1
								else:
										dic[p] += 1
		text = f.readline()
	
	ord = sorted(dic.items(), _cmp)
	diclen = len(dic)
	dictop = diclen - 2000
	top = ord[dictop:]
	toplen = len(top) - 1

	w1 = []
	w2 = []
	w3 = []
	w4 = []

	for i, prog in enumerate(top):
		
		word = top[toplen][0]

		if 1 <= len(word) <= 2:
			w1.append(word)
		elif 3 <= len(word) <= 4:
			w2.append(word)
		elif 5 <= len(word) <= 6:
			w3.append(word)
		else:
			w4.append(word)
		toplen -= 1

	def dizer():

		ww1 = random.choice(w1)
		ww2 = random.choice(w2)
		ww3 = random.choice(w3)
		ww4 = random.choice(w4)

		privmsg(channel, "%s %s %s %s, %s %s." % (
			ww1.capitalize(),
			ww2,
			random.choice(w1),
			ww4,
			random.choice(w4),
			random.choice(w3)
			)
		)

		ww1 = random.choice(w1)
		ww2 = random.choice(w2)
		ww3 = random.choice(w3)
		ww4 = random.choice(w4)

		if ww3[-1] == 's':
			while ww1[-1] != 's':
				ww1 = random.choice(w1)

		privmsg(channel, "%s %s %s." % (
			ww4.capitalize(),
			ww1,
			ww3
			)
		)



def lerolero():
	f = open("lerolero.txt", "r")
	tudo = f.readlines()
	text = random.choice(tudo)
	privmsg(channel, text)

def info():
    infotext = "NaNoBoT v1.0.2 - Coded in #Nosafe by ins3ct"
	#privmsg(channel, str(infotext))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, port))
sock.send("USER " + botnick + " " + botnick + " " + botnick + " :" + VERSION + "\n")
sock.send("NICK " + botnick + "\n")

while 1:
	ff = sock.recv(2048)
	ff = ff.strip("\n\r")

	print(ff)

	if ff.find("PING :") != -1:
		ping()

	if ff.find("To connect type /QUOTE PONG") != -1:
		exit()

	if ff.find("This nickname is registered and protected") != -1 or ff.find("registrado e protegido.  Se este for seu") != -1:
			privmsg("NICKSERV", "identify %s" % nickpass)

	if ff.find(":Senha aceita - voc") != -1:
			joinchan(channel)

	if ff.find(":.rehash") != -1:
		if ff.split("!")[0].split(":")[1] == owner:
			quit()
		else:
			privmsg(channel, "You are not autorized.")
#
	if ff.find("PRIVMSG " + channel) != -1:
		brut = ff.split(":")[1]
		text = brut.split()[0] + " " + ff.split()[2] + " = " + ff.split(":")[2]
		log(text)
		
		if ff.find(":.topnicks") != -1:
			if str(ff.split()[0].split("@")[1].split(".")[0]) != hater:
				topnicks()
			else:
				privmsg(channel, "You are in blacklist.")

		if ff.find(":.topwords") != -1:
			if str(ff.split()[0].split("@")[1].split(".")[0]) != hater:
				topwords()
			else:
				privmsg(channel, "You are in blacklist.")

		if ff.find(":.lerolero") != -1:
			if str(ff.split()[0].split("@")[1].split(".")[0]) != hater:
				lerolero()
			else:
				privmsg(channel, "You are in blacklist.")

		if ff.find(":.ajuda") != -1:
			if str(ff.split()[0].split("@")[1].split(".")[0]) != hater:
				ajuda()
			else:
				privmsg(channel, "You are in blacklist.")

		if ff.find(":.info") != -1:
			info()

		if ff.find(":.say") != -1:
			make()

		if ff.find(":.aprender") != -1:
			aprender()
