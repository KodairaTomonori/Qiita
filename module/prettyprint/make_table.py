#usr/bin/python
#coding:utf8
import MeCab
import prettytable
import sys

def make_prettytable(header=None, others):
    if not header: header = range(len(list(others)[0]) )
    if len(header) != len(others[0]):
        print('incorrect length!')
        return 
    table = prettytable.PrettyTable(header)
    for other in others: table.add_row(other)
    return table

def make_mecab_info_table(sentence, output_info, \
        mecab_parser=MeCab.Tagger.parse):
    others = list(map(lambda x: x.split(','), \
        mecab_parser(sentence).replace('\t', ',').split('\n') ) )[:-2]
    return make_prettytable(output_info, others)


if __name__ == '__main__':
    mecab_output = '表層形,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音'
    parser = MeCab.Tagger().parse
    header = mecab_output.split(',')
    print(make_mecab_info_table(input(), header, parser) )
