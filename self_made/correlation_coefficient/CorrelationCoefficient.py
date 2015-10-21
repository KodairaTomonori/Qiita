# !/usr/bin/python
# coding:utf8

import Kendall, Pearson, Spearman



def all_eval(tuple_list):
   return Spearman.Spearman(tuple_list), \
       Pearson.Pearson(tuple_list), Kendall.Kendall(tuple_list)



# ---------------test---------------------
if __name__ == '__main__':
   sample_tuple_list = [(1, 1), (2, 6), (3, 8), (4, 7), (5, 9), \
       (6, 4), (7, 3), (8, 5), (9, 2), (10, 4)]
   #sample_tuple_list = [(1, 2), (2, 1), (1, 2)]
   print all_eval(sample_tuple_list)
