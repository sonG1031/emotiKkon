def kakaoUrlHandler(url: str): # url -> "List(http://domain.com, ...)"
    real_url = url[5:-1].split(',')[0]
    return real_url

