import sys
import json
import re


def main():
    afinnfile = open(sys.argv[1])

    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweetfile = open(sys.argv[2])
    for tweet in tweetfile:
        parsed_tweet = json.loads(tweet)
        if "text" in parsed_tweet:
            text = parsed_tweet["text"]
            splited_text = re.split(r"[\s\.,\?\:]+", text)
            sentiment = 0

            for word in splited_text:
                if word in scores:
                    sentiment = sentiment + scores[word]

            print(sentiment)


if __name__ == '__main__':
    main()
