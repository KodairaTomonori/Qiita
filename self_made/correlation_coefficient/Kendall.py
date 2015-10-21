# !/usr/bin/python
# coding:utf8
# Reference Page: 
#   en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient

import collections


def check_concordant_pairs(sub_a, sub_b):
    if (sub_a < 0 and sub_b < 0) or (sub_a > 0 and sub_b > 0): return 1
    if sub_a == 0 or sub_b == 0: return 0
    return -1

get_ties_nums = lambda ranks: [ranks.count(rank) for rank in set(ranks) \
    if ranks.count(rank) > 1]


culc_ties = lambda nums: sum([num * float(num - 1) / 2 for num in nums])


# τ = nc - nd  / √(n0 - n1)(n0 - n2)
def Kendall(tuple_list):
    pair = 0; list_length = len(tuple_list)
    for num, (rank_a1, rank_b1) in enumerate(tuple_list[:-1]):
        for rank_a2, rank_b2 in tuple_list[num + 1:]:
            pair += check_concordant_pairs(rank_a1 - rank_a2, rank_b1 - rank_b2)
    n0 = list_length * (list_length - 1) * .5
    if (lambda x, y: x * y) \
        (*map(lambda x: max(x) == list_length, zip(*tuple_list))):
        return float(pair) / (n0)
    else: 
        n = [culc_ties(get_ties_nums(x) )for x in zip(*tuple_list)]
        if n0 == n[0] or n0 == n[1]:
             return float(pair) / (n0)
        return pair / (((n0 - n[0]) * (n0 - n[1]) ) ** .5)


def all_eval(tuple_list):
   return Spearman(tuple_list), Pearson(tuple_list), Kendall(tuple_list)



# ---------------test---------------------
if __name__ == '__main__':
   sample_tuple_list = [(1, 1), (2, 6), (3, 8), (4, 7), (5, 9), \
       (6, 4), (7, 3), (8, 5), (9, 2), (10, 9)]
   print '-------Kendall------'
   print Kendall(sample_tuple_list)
