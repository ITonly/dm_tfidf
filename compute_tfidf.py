# encoding:utf-8
__author__ = "li shi di"

if __name__ == "__main__":
    inputs_idf = open('./data/compute_idf.txt', 'r', encoding='utf-8')
    idf_dict = {}
    for line in inputs_idf:
        idf_arr = line.split(' ')
        idf_dict[idf_arr[0]] = float(idf_arr[1])
    # compute tf
    inputs_words = open('./data/split_words.txt', 'r', encoding='utf-8')
    o_tf_idf = open('./data/o_tf_idf.txt', 'w', encoding='utf-8')
    each_percent = []
    each_words = []
    count = 0
    files_name= []
    for line in inputs_words:
        count += 1
        dict_tf = {}
        words = line.split(' ')
        for word in words:
            if word.startswith('C'):
                continue
            if word in dict_tf:
                dict_tf[word] += 1
            else:
                dict_tf[word] = 1

        tf_idf_dict = {}
        for k, v in dict_tf.items():
            if k in idf_dict:
                tf_idf_dict[k] = idf_dict[k]*v/len(words)

        o_tf_idf.write('文档' + words[0]+ ' 开始' + '\n')
        for k in tf_idf_dict.items():
            w = k[0]
            v = k[1]
            o_tf_idf.write(w + ' ' + str(v) + '\n')
    inputs_idf.close()
    inputs_words.close()
    o_tf_idf.close()
