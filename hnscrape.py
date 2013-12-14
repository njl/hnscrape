import requests
from lxml import html

def _yield_tr_rows(trs):
    rv = []
    for tr in trs:
        if 'style' in tr.keys():
            yield rv
            rv = []
        else:
            rv.append(tr)
    if rv:
        yield rv

def _scrape_from_string(s):
    rv = []
    t = html.fromstring(s)
    trs = t.cssselect('center > table > tr')[2].cssselect('table > tr')
    trs = trs[:-2]
    for first, second in _yield_tr_rows(trs):
        result = {}
        result['rank'] = int(first.cssselect('td')[0].text_content()[:-1])
        title_link = first.cssselect('td')[2].cssselect('a')[0]
        result['title'] = title_link.text_content()
        result['url'] = title_link.attrib['href']

        #skip, points/id/user/timestamp/comments
        second = second.cssselect('.subtext')[0]
        result['points'] = int(second.text_content().split()[0])
        if not second.cssselect('a'):
            result['id'] = 0
            result['user'] = None
            result['time'] = None
            result['points'] = None
            rv.append(result)
            continue

        discussion = second.cssselect('a')[-1]
        if discussion.text_content() == 'discuss':
            result['comments'] = 0
        else:
            result['comments'] = int(discussion.text_content().split()[0])
        result['id'] = int(discussion.attrib['href'].split('=')[-1])
        result['user'] = second.cssselect('a')[0].text
        time = second.cssselect('a')[0].tail
        result['time'] = time.strip().strip('|').strip().strip('ago').strip()
        result['points'] = int(second.cssselect('span')[0].text_content().split()[0])
        rv.append(result)
    return rv

_urls = ('https://news.ycombinator.com/',
            'https://news.ycombinator.com/news2')

def get_results():
    rv = []
    for url in _urls:
        r = requests.get(url)
        r.raise_for_status()
        rv.extend(_scrape_from_string(r.text))
    return rv
