#!/bin/python
#encoding:utf-8


import os
import sys


file_1=sys.argv[1]
file_2=sys.argv[2]
join_cond=sys.argv[3]

join_cond_list = join_cond.split("&")
join_cond_dict = dict();
for join_cond_cell in join_cond_list:
   join_cond_cell = join_cond_cell.split("=")
   join_cond_dict[int(join_cond_cell[0])] = join_cond_cell[1]

fp_1=open(file_1,'rb')
fp_2=open(file_2,'rb')
f1_line_len = 0;
index_str = ''
f_1_ret = {}
f_2_ret = {}

while True :
    line = fp_1.readline().replace("\n","").rstrip()
    if not line:
        break;

    index_list = []
    line_list = line.split("\t")
    for k,v in join_cond_dict.items():
        index_list.append(line_list[k-1])
    index = "_".join(index_list).rstrip();
    f_1_ret[index] = line
    f1_line_len = len(line_list)

while True:
    line = fp_2.readline().replace("\n","").rstrip()
    if not line:
        break;
        
    index_list = []
    line_list = line.split("\t")
    for k,v in join_cond_dict.items():
        index_list.append(line_list[k-1])
    index = "_".join(index_list).rstrip()
    f_2_ret[index] = line
    f2_line_len = len(line_list)
    if index in f_1_ret:
        print "%s\t%s" % (f_1_ret[index],line)
    else:
        f_1_empty = [ '0' for n in range(0,f1_line_len)]
        print "%s\t%s" % ("\t".join(f_1_empty),line)

f_2_empty = [ '0' for n in range(0,f2_line_len)]

for index in f_1_ret:
    if index not in f_2_ret:
         print "%s\t%s" % (f_1_ret[index],"\t".join(f_2_empty))


