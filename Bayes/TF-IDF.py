import io
import numpy as np
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

stopwords = [line.strip() for line in io.open('./data/english.txt', encoding='utf-8').readlines()]

documents = [
    'this is the bayes document',
    'this is the second second document',
    'and the third one',
    'is this the document'
]

# token_pattern 默认为r"(?u)\b\w\w+\b"，其中两个\w 决定了其匹配长度至少为 2 的单词
# max_df/min_df: [0.0, 1.0]内浮点数或正整数, 默认值=1.0
# 当设置为浮点数时，过滤出现在超过 max_df, 低于 min_df 比例的句子中的词语；正整数时, 则是超过 max_df 句句子。
# 这样可以过滤掉出现太多的无意义词语。
tfidf_vec = TfidfVectorizer(stop_words=stopwords, token_pattern=r"(?u)\b\w+\b")
tfidf_matrix = tfidf_vec.fit_transform(documents)
tfidf_matrix = np.round(tfidf_matrix, 2)

print(tfidf_vec.stop_words)
print(tfidf_vec.get_feature_names())
print(tfidf_matrix.toarray())

