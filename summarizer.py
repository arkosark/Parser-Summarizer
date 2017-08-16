from nltk.corpus import stopwords
from string import punctuation
from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
from heapq import nlargest
import re

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars

class PointLangVars(PunktLanguageVars):
    sent_end_chars = ('.', '?', '!', '•',';')

class FrequencySummarizer:
    def __init__(self, min_cut=0.1, max_cut=0.9):
        self._min_cut = min_cut
        self._max_cut = max_cut
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ["'img"])

    def _compute_frequencies(self, word_sent):
        freq = defaultdict(int)
        for s in word_sent:
            for word in s:
                if (word not in self._stopwords) and ("'" not in word):
                    freq[word] += 1
        m = float(max(freq.values()))
        for w in list(freq):
            freq[w] = freq[w]/m
            if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                del freq[w]
        return freq

    def _rank(self, ranking, n):
        return nlargest(n, ranking, key=ranking.get)

    def summarize(self, text, n):

        tokenizer = PunktSentenceTokenizer(lang_vars = PointLangVars())
        #sents = tokenizer.tokenize(text) #text.split('.') #sent_tokenize(text)
        sents = re.split(r'\s*[!?.;]\s*', text)



        
        assert n <= len(sents)
        word_sent = [word_tokenize(s.lower()) for s in sents]


                self._freq = self._compute_frequencies(word_sent)
        print(self._freq)
        ranking = defaultdict(int)
        for i, sent in enumerate(word_sent):
            for w in sent:
                if w in self._freq:
                    ranking[i] += self._freq[w]
        sents_idx = self._rank(ranking,n)
        sents_idx.sort()
        print(sents_idx)
        return [sents[j] for j in sents_idx]