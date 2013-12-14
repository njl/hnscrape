import hnscrape


def test_basic_parse():
    items = hnscrape._scrape_from_string(open('test_one.html').read())
    assert items[0] == {'comments': 109,
            'id': 6903450,
            'points': 131,
            'rank': 1,
            'time': '2 hours',
            'title': "SteamOS: It's here",
            'url': 'http://steamdb.info/blog/35/',
            'user': 'xPaw'}

def test_job_offer_parse():
    items = hnscrape._scrape_from_string(open('test_two.html').read())
    assert not items[17]['user']
