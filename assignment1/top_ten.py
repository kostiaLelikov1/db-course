import sys
import json
import operator


def main():
    tweetfile = open(sys.argv[1])
    hashtags_dict = {}
    for tweet in tweetfile:
        parsed_tweet = json.loads(tweet)
        if "entities" in parsed_tweet:
            hashtags = parsed_tweet["entities"]["hashtags"]

            for hashtag in hashtags:
                text = hashtag["text"]
                if text in hashtags_dict.keys():
                    hashtags_dict[text] += 1
                else:
                    hashtags_dict[text] = 1
                    
    top_hashtags = sorted(hashtags_dict.items(), key=operator.itemgetter(1), reverse=True)
    hashtags_to_print = 10
    for hashtag_pair in top_hashtags:
        hashtags_to_print -= 1
        if hashtags_to_print < 0:
            return
        print(hashtag_pair[0] + ' ' + str(hashtag_pair[1]))



if __name__ == '__main__':
    main()
