import pornhub
from NHentai import NHentai


def pornhub_search(word1, word2):
    keywords = [word1, word2]
    client = pornhub.PornHub(keywords)
    result = []
    for video in client.getVideos(10, page=2):
        result.append(video["url"])
        result.append(video["name"])
        result.append(video["duration"])
        result.append(video["rating"])
        result.append(video["background"])
    return result


def nhentai_search(keyword):
    nhentai = NHentai()
    SearchPage = nhentai.search(query=keyword, sort='popular', page=1)
    result = SearchPage.doujins[0]
    return result
