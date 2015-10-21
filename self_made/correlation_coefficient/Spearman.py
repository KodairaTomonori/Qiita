# !/usr/bin/python
# coding:utf8
# Reference Page: 
#   en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient


import collections
# -------Spearman function------------
# ρ = 1 - [(6 * ∑D^2) / (N^3 - N) ]
# D = the difference between ranks
def normal_spearman(tuple_list, N):
   return 1 - ((6 * sum([(rank_a - rank_b) ** 2 \
       for rank_a, rank_b in tuple_list]) ) / float(N ** 3 - N) )


#　T = (N^3 - N - Σ(t^3 - t) ) / 12 
def sigma(counter, N, sigma_sum = 0):
    for rank, num in sorted(counter.items(), key = lambda x: -x[1]):
        if num == 1: break
        sigma_sum += num ** 3 - num
    return (N ** 3 - N - sigma_sum) / 12


# consider the same order 
# ρ = (Tx + Ty - ΣD^2) / (2 * √(Tx * Ty) )
# T = (N^3 - N - Σ(t^3 - t) ) / 12
def same_order_spearman(tuple_list, N):
    counter_a = collections.Counter(); counter_b = counter_a.copy()
    sum_d = 0
    for rank_a, rank_b in tuple_list:
       sum_d += (rank_a - rank_b) ** 2
       counter_a[rank_a] += 1; counter_b[rank_b] += 1
    ta = sigma(counter_a, N); tb = sigma(counter_b, N)
    if ta == 0 or tb == 0:
        return 0
    return (ta + tb - sum_d) / (2 * ((ta ** .5) * (tb ** .5) ) )


# if exist same_rank, change the rank to the average 
def change_rank_num(list_x):
    return [len([1 for rank in list_x if rank < x]) + \
        float(list_x.count(x) - 1) / 2 + 1 for x in list_x]

# -------------main-----------------
# tuple = (rank_a, rank_b)
def Spearman(tuple_list):
   list_length = len(tuple_list)
   ranks_a, ranks_b = zip(*tuple_list)
   pattern = 0
   if max(ranks_a) != list_length: ranks_a = change_rank_num(ranks_a)
   else: pattern += 1
   if max(ranks_b) != list_length: ranks_b = change_rank_num(ranks_b)
   else: pattern += 1
   if pattern == 2: return normal_spearman(tuple_list, list_length)
   else: return same_order_spearman(zip(ranks_a, ranks_b), list_length)



# ---------------test---------------------
if __name__ == '__main__':
   sample_tuple_list = [(1, 2), (2, 1), (3, 4), (4, 4), (5, 4)]
   print '--------Spearman-------'
   print Spearman(sample_tuple_list)

   
