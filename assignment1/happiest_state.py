import sys
import json
import re

def main():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    afinnfile = open(sys.argv[1])

    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweetfile = open(sys.argv[2])
    index = 0
    states_sentiments = {}
    for tweet in tweetfile:
        parsed_tweet = json.loads(tweet)
        if "text" in parsed_tweet:
            user = parsed_tweet["user"]
            location = user["location"]
            
            text = parsed_tweet["text"].rstrip("\n")
            splited_text = re.split(r"[\s\.\,\?\:\!\n]+", text)
            sentiment = 0

            for word in splited_text:
                if word in scores:
                    sentiment = sentiment + scores[word]

            for state in states:
                if state in location or states[state] in location:
                    if state in states_sentiments:
                        states_sentiments[state] += sentiment
                    else:
                        states_sentiments[state] = sentiment

    happiest_state = ''
    for state in states_sentiments:
        if happiest_state == "" or states_sentiments[state] > states_sentiments[happiest_state]:
            happiest_state = state
    print(happiest_state)


if __name__ == '__main__':
    main()
