#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "li shi di"

"""
将文本整合到 news_data.txt 文件中
"""

import os
import jieba
import re


def _read_file(filename):
    """读取一个文件并转换为一行"""
    # with open(filename, 'rb')as f:
    #      return f.read()
    #     return f.read().repl
    with open(filename, 'rb') as f:
        return f.read()


def save_file(dir_name):
    """
    将多个文件整合并存到1个文件中
    dir_name: 原数据目录
    文件内容格式:  类别\t内容
    """
    f_train = open('data/news/news_data.txt', 'w', encoding='utf-8')

    for category in os.listdir(dir_name):   # 分类目录 返回指定路径下的文件和文件夹列表。
        cat_dir = os.path.join(dir_name, category)
        if not os.path.isdir(cat_dir):
            continue
        files = os.listdir(cat_dir)
        count = 0
        for cur_file in files:
            filename = os.path.join(cat_dir, cur_file)
            content = _read_file(filename)
            result = jieba.cut(content)
            result = ''.join(result)
            result1 = ''
            for line in result:
                line = line.strip()
                # line1 = re.sub(r'[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+',
                #                '', line)
                result1 = result1+line
            result = result1.replace('\n', '').replace('\t', '').replace('\u3000', '').replace('&nbsp','')
            # print('result',result)
            f_train.write(category+'_'+cur_file+ '=='+result + '\n')

        print('Finished:', category)

    f_train.close()


if __name__ == '__main__':
    save_file('../Reduced')

