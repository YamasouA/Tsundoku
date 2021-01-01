from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

from pysummarization.nlp_base import NlpBase
from pysummarization.similarityfilter.tfidf_cosine import TfIdfCosine

from bs4 import BeautifulSoup
import requests

import time
import random

def summary(bookmark_bar):
    bookmark_bar = random.sample(bookmark_bar, k=4)

    for i in bookmark_bar:
        print('#######################################################################')
        response = requests.get(i['url'])
        soup = BeautifulSoup(response.text, "html.parser")
        document = soup.find('p', class_="single_article_contents")
        print(document.get_text())

        # NLPのオブジェクト
        nlp_base = NlpBase()

        # トークナイザーを設定します。 これは、MeCabを使用した日本語のトークナイザーです
        nlp_base.tokenizable_doc = MeCabTokenizer()

        # 「類似性フィルター」のオブジェクト。 
        #    このオブジェクトによって観察される類似性は、Tf-Idfベクトルのいわゆるコサイン類似性です
        similarity_filter = TfIdfCosine()

        # NLPのオブジェクトを設定します
        similarity_filter.nlp_base = nlp_base

        # 類似性がこの値を超えると、文は切り捨てられます
        similarity_filter.similarity_limit = 0.25

        # 自動要約のオブジェクト
        auto_abstractor = AutoAbstractor()

        # 日本語のトークナイザーを設定
        auto_abstractor.tokenizable_doc = MeCabTokenizer()

        # キュメントを抽象化およびフィルタリングするオブジェクト
        abstractable_doc = TopNRankAbstractor()

        # 変数を渡し文書を要約
        result_dict = auto_abstractor.summarize(document, abstractable_doc, similarity_filter)

        """result_dictは辞書型となっています。
        dict{
            "summarize_result": "要約された文のリスト。", 
            "scoring_data":     "スコアのリスト（重要度のランク）。"
        }
        """
        i['summary'] = result_dict["summarize_result"]
        time.sleep(1)
    
    return bookmark_bar