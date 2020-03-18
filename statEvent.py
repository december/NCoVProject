import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
import datetime
import time
sns.set()
sns.set_style('white')

def calcDateDelta(date1, date2):
	date1 = time.strptime(date1, '%Y%m%d')
	date2 = time.strptime(date2, '%Y%m%d')
	date1 = datetime.datetime(date1[0],date1[1],date1[2])
	date2 = datetime.datetime(date2[0],date2[1],date2[2])
	return (date2 - date1).days 	

name = ['Numbers', 'Views', 'Likes', 'Comments', 'Shares']
category = ['All', 'Celebrity', 'Company', 'Government', 'Media', 'Organization']
infodic = list() #from different kinds of users to date to the number of videos, views, likes, comments, shares
earliest = '20200101'

for i in range(6): #all, celebrity, company, government
	infodic.append({})

provincedic = {} #from date to province to the number of videos, views, likes, comments, shares

path = '../../../data/'
event = 'zns'
dt = '20200313'
fr = open(path+'aweme_event_'+event+'_'+dt+'.text', 'r')
data = fr.readlines()
fr.close()
for line in data:
	temp = line[:-1].split('\t')
	#print len(temp)
	if len(temp) < 15:
		continue
	#print temp
	date = temp[2]
	provc = temp[3]
	if not provincedic.has_key(date):
		provincedic[date] = {}
	if not provincedic[date].has_key(provc):
		provincedic[date][provc] = [0, 0, 0, 0, 0]
	provincedic[date][provc][0] += 1
	wrongline = False
	for i in range(4):
		if temp[7+i].isdigit():
			provincedic[date][provc][i+1] += int(temp[7+i])
		else:
			wrongline = True
	if not infodic[0].has_key(date):
		infodic[0][date] = [0, 0, 0, 0, 0]
	infodic[0][date][0] += 1
	for i in range(4):
		if temp[7+i].isdigit():		
			infodic[0][date][i+1] += int(temp[7+i])
		else:
			wrongline = True
	#if temp[5] == 'null' or wrongline:
	if not temp[5].isdigit():
		continue
	ct = int(temp[5])
	if ct == 0:
		if not infodic[1].has_key(date):
			infodic[1][date] = [0, 0, 0, 0, 0]
		infodic[1][date][0] += 1
		for i in range(4):
			infodic[1][date][i+1] += int(temp[7+i])
	if not temp[6].isdigit():
		continue			
	cc = int(temp[6])
	if ct == 1 and cc == 0:
		if not infodic[2].has_key(date):
			infodic[2][date] = [0, 0, 0, 0, 0]
		infodic[2][date][0] += 1
		for i in range(4):
			infodic[2][date][i+1] += int(temp[7+i])
	if ct == 1 and cc == 2:
		if not infodic[3].has_key(date):
			infodic[3][date] = [0, 0, 0, 0, 0]
		infodic[3][date][0] += 1
		for i in range(4):
			infodic[3][date][i+1] += int(temp[7+i])
	if ct == 1 and cc == 1:
		if not infodic[4].has_key(date):
			infodic[4][date] = [0, 0, 0, 0, 0]
		infodic[4][date][0] += 1
		for i in range(4):
			infodic[4][date][i+1] += int(temp[7+i])
	if ct == 1 and cc == 3:
		if not infodic[5].has_key(date):
			infodic[5][date] = [0, 0, 0, 0, 0]
		infodic[5][date][0] += 1
		for i in range(4):
			infodic[5][date][i+1] += int(temp[7+i])

#print infodic[0]
'''
for i in range(4):
	print i
	print infodic[i]
	datelist = sorted(infodic[i].keys())
	#print datelist
	start = max(min(datelist), earliest)
	n = len(datelist)
	x = list()
	ylist = list()
	rate1 = list()
	rate2 = list()
	for j in range(5):
		ylist.append(list())
	if i == 3:
		for j in range(5):
			rate2.append(list())
	if i == 3 or i == 2:
		for j in range(5):
			rate1.append(list())
	for j in range(n):
		if datelist[j] < start:
			continue
		unit = infodic[i][datelist[j]]
		for k in range(5):
			ylist[k].append(unit[k])
		x.append(calcDateDelta(start, datelist[j]))
		if i == 3:
			topunit = [0, 0, 0, 0, 0]
			if infodic[2].has_key(datelist[j]):
				topunit = infodic[2][datelist[j]]
			for k in range(5):
				rate2[k].append((topunit[k] + 1) * 1.0 / (unit[k] + 1))
		if i == 3 or i == 2:
			topunit = [0, 0, 0, 0, 0]
			if infodic[1].has_key(datelist[j]):
				topunit = infodic[1][datelist[j]]
			for k in range(5):
				rate1[k].append((topunit[k] + 1) * 1.0 / (unit[k] + 1))
	x = np.array(x)
	ylist = np.array(ylist)
	for j in range(5):
		plt.xlabel('Date')
		plt.ylabel(name[j])
		plt.yscale('log')
		plt.plot(x, ylist[j])
		plt.title(category[i]+'_'+start+'_'+event)
		plt.savefig('figs/'+category[i]+'_'+name[j]+'_'+dt+'_'+event+'_log.png')
		plt.clf()
	rate1 = np.array(rate1)
	rate2 = np.array(rate2)
	if i == 3:
		for j in range(5):
			plt.xlabel('Date')
			plt.ylabel('Rate on ' + name[j])
			plt.yscale('log')
			plt.plot(x, rate2[j])
			plt.title('Company / Government:'+start+'_'+event)		
			plt.savefig('figs/Company_Government_'+name[j]+'_'+dt+'_'+event+'_log.png')
			plt.clf()
	if i == 3 or i == 2:
		for j in range(5):
			plt.xlabel('Date')
			plt.ylabel('Rate on ' + name[j])
			plt.yscale('log')
			plt.plot(x, rate1[j])
			plt.title('Celebrity / '+category[i]+':'+start+'_'+event)		
			plt.savefig('figs/Celebrity_'+category[i]+'_'+name[j]+'_'+dt+'_'+event+'_log.png')
			plt.clf()
'''
datelist = sorted(infodic[0].keys())
start = max(min(datelist), earliest)
n = len(datelist)
x = list()
ylist = list()
for j in range(5):
	ylist.append(list())
for j in range(n):
	if datelist[j] < start:
		continue
	if len(datelist[j]) != 8:
		continue
	unit = infodic[0][datelist[j]]
	for k in range(5):
		ylist[k].append(unit[k])
	x.append(calcDateDelta(start, datelist[j]))
x = np.array(x)
ylist = np.array(ylist)
for j in range(5):
	plt.xlabel('Date')
	plt.ylabel(name[j])
	plt.grid()
	plt.plot(x, ylist[j])
	plt.title('All_'+start+'_'+event)
	#plt.savefig('figs/All_'+name[j]+'_'+dt+'_'+event+'.png')
	plt.yscale('log')
	plt.savefig('figs/All_'+name[j]+'_'+dt+'_'+event+'_log.png')
	plt.clf()	

color = ['b', 'k', 'r', 'g', 'y']
for j in range(5):
	plt.xlabel('Date')
	plt.ylabel(name[j])
	start = earliest
	for i in range(1, 6):
		x = list()
		y = list()		
		datelist = sorted(infodic[i].keys())
		n = len(datelist)
		if n == 0:
			continue
		#start = max(min(datelist), earliest)
		for k in range(n):
			if datelist[k] < start:
				continue
			if len(datelist[k]) != 8:
				continue		
			x.append(calcDateDelta(start, datelist[k]))
			y.append(infodic[i][datelist[k]][j])
		x = np.array(x)
		y = np.array(y)
		plt.plot(x, y, c=color[i-1], label=category[i])
	plt.title('Certification_'+start+'_'+event)
	plt.legend()
	plt.grid()
	#plt.savefig('figs/Sep_'+name[j]+'_'+dt+'_'+event+'.png')
	plt.yscale('log')
	plt.savefig('figs/Sep_'+name[j]+'_'+dt+'_'+event+'_log.png')
	plt.clf()

fw = open('data/province_'+dt+'_'+event+'.text', 'w')
datelist = sorted(provincedic.keys())
n = len(datelist)
for i in range(n):
	if datelist[i] < earliest:
		continue
	plist = sorted(provincedic[datelist[i]].keys())
	m = len(plist)
	#s = datelist[i]+'\t'
	for j in range(m):
		unit = provincedic[datelist[i]][plist[j]]
		s = datelist[i]+'\t'+plist[j]
		for k in range(5):
			s += '\t' + str(unit[k])
		fw.write(s+'\n')
fw.close()
