#Fetch info from wikipedia
from mediawiki import MediaWiki
import re #this module provides functions to search,match and manipulate strings.
from collections import Counter

def pga_text():
    "get title and content from PGA Tour wikipedia page"
    wikipedia = MediaWiki()
    page = wikipedia.page("PGA Tour")
    return page.title, page.content


def remove_stop_words(words, stop_words):
    "eliminate common words like 'the','and','a' etc... from the wikipedia text"
    return[word for word in words if word not in stop_words]


def count_word_frequencies(text, stop_words=None):
    "Count frecuency of words after removing stop words"
    text= text.lower()#convert text to lowercase
    words=re.findall(r'\w+', text)#Excract alphanumerical words(regex)
    if stop_words:
        words=remove_stop_words(words,stop_words)
        return Counter(words)


if __name__=="__main__":
    stop_words={"the","and", "a", "an", "of", "to", "in", "for", "on", "with", "by",
        "is", "it", "that", "this", "as", "at", "from", "was","are","s"}
    title,content= pga_text()
    combine_text=title+""+content
    word_frequencies=count_word_frequencies(combine_text, stop_words=stop_words)
    top_10=word_frequencies.most_common(10)
    #print
    print("Top 10 words in the text:")
    for word, freq in top_10:
        print(f"{word}:{freq}")

