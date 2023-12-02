import operator
import urllib.request as ur
from bs4 import BeautifulSoup as bs

def url_to_word_list(url):
    # 입력받은 url을 이용하여 span 에 해당하는 문자를 불러온 뒤 간단한 처리 후 set과 list에 각각 저장하는 함수
    words = []
    words_set = set()
    html = ur.urlopen(url)
    soup = bs(html.read(), 'html.parser')
    quotes = soup.find_all('div', {"class": "quote"})

    for quote_n in quotes:
        quote = quote_n.find('span', {"class": "text"})
        word = quote.text.strip().strip("\“").strip("\”").split()
        for i in word:
            words.append(i.lower())
            words_set.add(i)
    return words, words_set

def do_count(words, words_set):
    #for문을 통하여 집합 속 내용물을 딕셔너리 키값에 추가하고, 리스트를 돌며 횟수를 벨류값으로 추가하는 함수
    term_frequency_dict = {}
    for j in words_set:
        term_frequency_dict[j] = 0

    for k in words:
        if k in term_frequency_dict:
            term_frequency_dict[k] += 1
    return term_frequency_dict

def make_rank(term_frequency_dict):
    #내림차순으로 정렬 후, 1위부터 5위까지 빈도가 높은 단어를 출력하는 함수
    sortedList = sorted(term_frequency_dict.items(), key=operator.itemgetter(1), reverse=True)
    rank = 1
    for key, val in sortedList:
        print("(", rank, ")", key, val, "회")
        if rank == 5:
            break
        rank += 1

#추후 url변경시 해당 항목만 수정하면 가능
url = "https://quotes.toscrape.com/tag/life/"

#함수 실행
word_list, word_set = url_to_word_list(url)
word_dict = do_count(word_list, word_set)
make_rank(word_dict)
