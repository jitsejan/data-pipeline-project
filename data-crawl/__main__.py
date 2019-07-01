from dateutil import parser
import lxml.html
import pandas as pd
import requests

BASE_URL = "https://mario.nintendo.com"
CHARACTER_URL = f"{BASE_URL}/characters/"
HISTORY_URL = f"{BASE_URL}/history/"

def get_characters():
    """ Retrieve the Mario characters from nintendo.com """
    resp = requests.get(CHARACTER_URL)
    tree = lxml.html.fromstring(resp.content)
    for elem in tree.cssselect("ul.characters li.characters__item"):
        yield {
            'name': elem.cssselect('h2.characters__name')[0].text_content(),
            'description': elem.cssselect('p.characters__description')[0].text_content(),
            'image-headshot': BASE_URL + elem.cssselect('img.img-headshot')[0].get('src'),
            'image-action': BASE_URL + elem.cssselect('img.img-action')[0].get('src'),
            'copyright': tree.cssselect('div.footer-main__links__legal p')[0].text_content(),
        }

def get_history():
    """ Retrieve the Mario history from nintendo.com """
    resp = requests.get(HISTORY_URL)
    tree = lxml.html.fromstring(resp.content)
    for elem in tree.cssselect("div.history-tile"):
        yield {
            'year': elem.cssselect('div.history-tile__desc h1.history-tile__yr')[0].text_content(),
            'name': elem.cssselect('h4.history-tile__name')[0].text_content(),
            'release_date': elem.cssselect('span.history-tile__date')[0].text_content().replace("Released: ", ""),
            'platform': elem.cssselect('span.history-tile__platform')[0].text_content(),
            'story': ' '.join([par.text_content() for par in elem.cssselect('div.history-tile__story p')]),
        }

def _clean_history_frame(df):
    """ Correct the history dataframe """
    expand_df = df[['release_date', 'platform']].apply(lambda x: x.str.split('/'))
    result_df = pd.DataFrame.from_items([(index, zipped) for index, row in expand_df.iterrows() for zipped in zip(*row)],
                                    orient='index',
                                    columns=expand_df.columns)
    return df.drop(['release_date', 'platform'], axis=1).join(result_df)
    
def main():
    """ Main functionality """
    char_df = pd.DataFrame(get_characters())
    history_df = _clean_history_frame(pd.DataFrame(get_history()))

if __name__ == "__main__":
    main()