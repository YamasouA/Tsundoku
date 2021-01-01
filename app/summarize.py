from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

from pysummarization.nlp_base import NlpBase
from pysummarization.similarityfilter.tfidf_cosine import TfIdfCosine


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

document = '人間がお互いにコミュニケーションを行うための自然発生的な言語である。「自然言語」に対置される語に「形式言語」「人工言語」がある。形式言語との対比では、その構文や意味が明確に揺るぎなく定められ利用者に厳格な規則の遵守を強いる（ことが多い）形式言語に対し、話者集団の社会的文脈に沿った曖昧な規則が存在していると考えられるものが自然言語である。自然言語には、規則が曖昧であるがゆえに、話者による規則の解釈の自由度が残されており、話者が直面した状況に応じて規則の解釈を変化させることで、状況を共有する他の話者とのコミュニケーションを継続する事が可能となっている。'


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

# 出力
for sentence in result_dict["summarize_result"]:
    print(sentence)