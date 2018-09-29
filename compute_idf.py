# encoding:utf-8
__author__ = "li shi di"

import math


if __name__ == "__main__":
    df_dict = {}
    inputs = open('./data/split_words.txt', 'r', encoding='utf-8')
    count = 0
    # 一行一行的处理，而不是把所有的新闻一次全部加载到内存。
    for line in inputs:
        count += 1
        counter = {}
        for word in line.split(' '):
            if word.startswith('C'):
                continue
            if word not in counter:
                counter[word] = 1
                if word in df_dict:
                    df_dict[word] += 1
                else:
                    df_dict[word]=1
    inputs.close()
    outputs = open('./data/compute_idf.txt', 'w', encoding='utf-8')
    n=count
    print('number', n)
    # for k in df_dict:
    #     v = df_dict[k]
    #     idf =math.log(n/(v+1.0))
    #     outputs.write(k +' '+ str(idf) + ' ' + str(v) +  '\n')
    # print('ddd',df_dict.items())
    print('dict',df_dict)
    for k in sorted(df_dict.items(), key=lambda a: a[1], reverse=True):
        w = k[0]
        v = k[1]
        idf = math.log(n/(v+1.0))
        print('yui')
        print(w + ' ' + str(idf) + ' ' + str(v) + '\n')
        outputs.write(w + ' ' + str(idf) + ' ' + str(v) + '\n')

    outputs.close()








