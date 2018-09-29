# encoding:utf-8
__author__ = "li shi di"

import jieba
import os
import sys
import math


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return set(stopwords)


# 对句子进行分词
def seg_sentence(sentence):
    sentence = sentence.split('==')
    outstr = sentence[0]+' '
    sentence_seged = jieba.cut(sentence[1].strip())
    stopwords = stopwordslist('./data/stop_words.txt')  # 这里加载停用词的路径

    for word in sentence_seged:
        if word.strip() not in stopwords and check_contain_chinese(word):
                outstr += word
                outstr += " "
    return outstr


def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        else:
            return False


if __name__ == "__main__":
    inputs = open('./data/news/news_data.txt', 'r', encoding='utf-8')
    outputs = open('./data/split_words.txt', 'w', encoding='utf-8')
    for line in inputs:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()


