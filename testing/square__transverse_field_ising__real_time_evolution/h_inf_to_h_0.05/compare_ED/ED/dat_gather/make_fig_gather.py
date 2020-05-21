#!/usr/bin/env python

# coding:utf-8
from __future__ import print_function
#import sys
import re
import glob
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

all_files = glob.glob('../dat_L*/dat')

list_L = []
list_N = []
list_mx = []
list_mz0mz1 = []
list_time_steps_pi = []
for file_name in all_files:
#    N = file_name.replace("dat_L","")
    L = re.sub(".*dat_L","",file_name)
    L = int(L.replace("/dat",""))
    N = L**2
    list_L.append(L)
    list_N.append(N)
    print(file_name,L,N)
#    file = open(sys.argv[1])
#    file = open('dat_L3_tau_inf')
    file = open(file_name)
    lines = file.readlines()
    file.close()
    for line in lines:
        if line.startswith("mx ["):
            line_mx = line[:-1]
            line_mx = line_mx.replace("mx [","")
            line_mx = line_mx.replace("]","")
            list_mx.append(np.fromstring(line_mx,dtype=np.float,sep=','))
        if line.startswith("mz0mz1 ["):
            line_mz0mz1 = line[:-1]
            line_mz0mz1 = line_mz0mz1.replace("mz0mz1 [","")
            line_mz0mz1 = line_mz0mz1.replace("]","")
            list_mz0mz1.append(np.fromstring(line_mz0mz1,dtype=np.float,sep=','))
        if line.startswith("time_steps_pi ["):
            line_time_steps_pi = line[:-1]
            line_time_steps_pi = line_time_steps_pi.replace("time_steps_pi [","")
            line_time_steps_pi = line_time_steps_pi.replace("]","")
            list_time_steps_pi.append(np.fromstring(line_time_steps_pi,dtype=np.float,sep=','))

for i in range(len(list_L)):
    print("L mx",list_L[i],list_mx[i])
    print("L mz0mz1",list_L[i],list_mz0mz1[i])
    print("L time_steps_pi",list_L[i],list_time_steps_pi[i])


list_time = list_time_steps_pi
for i in range(len(list_L)):
    Nsteps = len(list_time[i])
    output_file="dat_L"+str(list_L[i])
    f = open(output_file,'w')
    f.write('# time/pi mx mz0mz1\n')
    for step in range(Nsteps-1):
        f.write('{} {} {}\n'.format(\
            list_time[i][step],list_mx[i][step],list_mz0mz1[i][step]))
    f.close()


fig0 = plt.figure()
fig0.suptitle("mx")
for i in range(len(list_L)):
    plt.plot(list_time_steps_pi[i],list_mx[i],label=list_L[i])
plt.xlabel("$t/\pi$")
plt.legend(bbox_to_anchor=(1,1),loc='upper right',borderaxespad=1)
#plt.gca().invert_xaxis()
fig0.savefig("fig_mx.png")

fig1 = plt.figure()
fig1.suptitle("mz0mz1")
for i in range(len(list_L)):
    plt.plot(list_time_steps_pi[i],list_mz0mz1[i],label=list_L[i])
plt.xlabel("$t/\pi$")
plt.legend(bbox_to_anchor=(1,1),loc='upper right',borderaxespad=1)
#plt.gca().invert_xaxis()
fig1.savefig("fig_mz0mz1.png")
