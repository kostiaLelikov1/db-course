import sys
import json
import re


def main():
    words = {}
    words_quantity = 0
    tweetfile = open(sys.argv[1])
    for tweet in tweetfile:
        parsed_tweet = json.loads(tweet)
        if "text" in parsed_tweet:
            text = parsed_tweet["text"].rstrip("\n")
            splited_text = re.split(r"[\s\.\,\?\:\!\n]+", text)

            for word in splited_text:
                if word != '':
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
                        words_quantity += 1
                    

    for word in words.keys():
        word_frequency = str(round(float(words[word])/words_quantity, 4))
        print(word + " " + word_frequency)


if __name__ == '__main__':
    main()
