# !/usr/bin/python
# coding:utf8
# Reference Page: 
#   en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient


def get_average(list_tuple, length):
    return map(lambda x: sum(x) / float(length), list_tuple)


# tuple = (rank_a, rank_b)
# ρ = Σ(xi - x^)(yi - y^) / [√Σ(xi - x^)^2 * √Σ(yi - x^)^2] 
#        numer                 denom_a         denom_b
def Pearson(tuple_list):
    ave_a, ave_b = get_average(zip(*tuple_list), len(tuple_list) )
    numer = .0; denom_a = .0; denom_b = .0
    for a, b in tuple_list:
        sub = (a - ave_a, b - ave_b)
        numer += sub[0] * sub[1]
        denom_a += sub[0] ** 2; denom_b += sub[1] ** 2
    if numer == 0:
        return 0
    return numer / ((denom_a ** .5) * (denom_b ** .5) ) 


# ---------------test---------------------
if __name__ == '__main__':
   
   sample_tuple_list = [(1, 2), (2, 1), (3, 4), (4, 4), (5, 4)]
   print '-------Pearson------'
   print Pearson(sample_tuple_list)
