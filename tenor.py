import requests
import json


def tenor(token, word, limit):
    # set the apikey and limit
    apikey = token  # test value
    lmt = limit

    # our test search
    search_term = word

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gif_json = json.loads(r.content)
        return gif_json["results"][0]["media"][0]["gif"]["url"]
    else:
        gif_json = None
        return None

def tenor_multiple(token, word, limit):
    # set the apikey and limit
    apikey = token  # test value
    lmt = limit
    result = []

    # our test search
    search_term = word

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gif_json = json.loads(r.content)
    else:
        gif_json = None
    for i in range(limit):
        result.append(gif_json["results"][limit]["media"][0]["gif"]["url"])
    return result