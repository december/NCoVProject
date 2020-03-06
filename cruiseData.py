import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
sns.set()
sns.set_style('white')

time = [5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18]
examine = [31, 102, 273, 273, 330, 1723, 1723, 1723, 1723, 1723, 1723, 2404]
confirm = [10, 20, 61, 64, 70, 135, 174, 218, 285, 355, 454, 542]

time = np.array(time)
examine = np.array(examine)
confirm = np.array(confirm)
rate = confirm * 1.0 / examine * 100

#plt.xscale('log')
#plt.yscale('log')
#plt.xticks(fontsize=14)
#plt.yticks(fontsize=14)
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#plt.set_xticks([0, 20000, 40000, 60000, 80000])
#plt.yticks(fontsize=14)
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
#plt.plot(ourx, oury, 'b', label='SCM', linewidth=2.5)
#plt.plot(bs, bn, 'k', label='Poisson', linewidth=2.5)
#plt.xlabel(u'Days', fontsize=14)
#plt.ylabel(u'PDF', fontsize=14)
#plt.title('PDF on a log scale', fontsize=25)
#plt.legend(fontsize=20);
#plt.savefig('pdf_loglog.eps')
#plt.cla()