# encoding:utf-8
__author__ = "li shi di"

import math
from collections import Counter

if __name__ == "__main__":
    df_dict = {}
    inputs = open('./data/split_words.txt', 'r', encoding='utf-8')
    count = 0
    # 数组的查找速度为o(n)，set的查找速度为o(1)。line.split('')
    # 一行一行的处理，而不是把所有的新闻一次全部加载到内存。
    # for line in inputs:
    #     count += 1
    #     counter = {}
    #     for word in line.split(' '):
    #         if word.startswith('C'):
    #             continue
    #         if word not in counter:
    #             counter[word] = 1
    #             if word in df_dict:
    #                 df_dict[word] += 1
    #             else:
    #                 df_dict[word]=1
    # inputs.close()

    result = []
    for line in inputs:
        count += 1
        doc_words = line.spilt(' ')
        result += list(set(doc_words[1:]))
    inputs.close()
    result = Counter(result)
    outputs = open('./data/compute_idf.txt', 'w', encoding='utf-8')

    for key, value in result.items():
        outputs.write(key + ' ' + str(math.log(count/(value+1)))+'\n')


    # n = count
    # print('number', n)
    # # for k in df_dict:
    # #     v = df_dict[k]
    # #     idf =math.log(n/(v+1.0))
    # #     outputs.write(k +' '+ str(idf) + ' ' + str(v) +  '\n')
    # # print('ddd',df_dict.items())
    # print('dict', df_dict)
    # for k in sorted(df_dict.items(), key=lambda a: a[1], reverse=True):
    #     w = k[0]
    #     v = k[1]
    #     idf = math.log(n/(v+1.0))
    #     print('yui')
    #     print(w + ' ' + str(idf) + ' ' + str(v) + '\n')
    #     outputs.write(w + ' ' + str(idf) + ' ' + str(v) + '\n')

    outputs.close()








