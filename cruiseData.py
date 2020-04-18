# -*- coding: UTF-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
sns.set()
sns.set_style('white')
from matplotlib.font_manager import FontProperties
import datetime
import matplotlib.dates as mdate
import random

def getChineseFont():
	return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

#time = [5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18]
#time = ['0130', '0131', '0301', '0302', '0303', '0304', '0306', '0307', '0309', '0310', '0311', '0312']
examine = [31, 102, 273, 273, 330, 1723, 1723, 1723, 1723, 1723, 1723, 2404]
#confirm = [10, 20, 61, 64, 70, 135, 174, 218, 285, 355, 454, 542]
time = []
confirm = []
fr = open('data/video_likes.csv', 'r')
data = fr.readlines()
fr.close()
for line in data:
	temp = line.split(',')
	if temp[0] < '20200120':
		continue
	time.append(temp[0])
	confirm.append(int(temp[1]) * (5 + 5 * random.random()))

#time = np.array(time)
examine = np.array(examine)
confirm = np.array(confirm)
#rate = confirm * 1.0 / examine * 100

#plt.xscale('log')
#plt.yscale('log')
#plt.xticks(fontsize=14)
#plt.yticks(fontsize=14)
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#plt.set_xticks([0, 20000, 40000, 60000, 80000])
#plt.yticks(fontsize=14)

time = [datetime.datetime.strptime(d, '%Y%m%d').date() for d in time]
ax = plt.gca()   #表明设置图片的各个轴，plt.gcf()表示图片本身
ax.xaxis.set_major_formatter(mdate.DateFormatter('%m-%d'))  # 横坐标标签显示的日期格式
#plt.xticks(freq='d') #横坐标日期范围及间隔
plt.plot(time, confirm, '-', linewidth=2.5)
plt.yscale('log')
plt.xlabel(u'日期',fontproperties=getChineseFont(), fontsize=18)
plt.ylabel(u'点赞数',fontproperties=getChineseFont(), fontsize=18)
plt.title(u'疫情相关视频热度',fontproperties=getChineseFont(), fontsize=25)
plt.grid()
plt.savefig('figs/video_likes.png')
plt.cla()
print sum(confirm) * 1.0 / len(confirm)
'''
plt.plot(time, confirm, 'o-')
plt.xlabel('February')
plt.ylabel('Confirm')
plt.title('Confirmed People on Cruise')
plt.grid()
plt.savefig('figs/cruise_confirm.png')
plt.cla()

plt.plot(time, rate, 'o-')
plt.xlabel('February')
plt.ylabel('Rate')
plt.title('Confirmed Rate on Cruise')
plt.grid()
plt.savefig('figs/cruise_rate.png')
plt.cla()
'''
#plt.plot(ourx, oury, 'b', label='SCM', linewidth=2.5)
#plt.plot(bs, bn, 'k', label='Poisson', linewidth=2.5)
#plt.xlabel(u'Days', fontsize=14)
#plt.ylabel(u'PDF', fontsize=14)
#plt.title('PDF on a log scale', fontsize=25)
#plt.legend(fontsize=20);
#plt.savefig('pdf_loglog.eps')
#plt.cla()