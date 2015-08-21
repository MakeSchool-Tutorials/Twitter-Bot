import requests

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'

def get_article(article_url, token):
    # set request params for API request
    params = { 'token': token,
               'url': article_url,
               'discussion': 'false' }

    res = requests.get(DIFFBOT_API_URL, params) # hit the Diffbot API
    res_obj = res.json()['objects'][0]          # parse the response object

    return res_obj['text']                      # pull out the text

if __name__ == '__main__':
    import sys
    dev_token = sys.argv[2]
    urls_file = open(sys.argv[1])
    output_file = open('corpus.txt', 'w')

    corpus = ''

    for line in urls_file:
        url = line.strip() # remove leading/trailing whitespace
        article = get_article(url, token)
        corpus += article

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))
