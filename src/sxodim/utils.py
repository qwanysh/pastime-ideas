import httpx
from bs4 import BeautifulSoup


def get_sxodim_popular_places():
    data = []

    soup = _get_soup_by_url('https://sxodim.com/almaty/events/week')
    slides_soup = soup.select('.swiper-wrapper > .swiper-slide')

    for slide_soup in slides_soup:
        data_wrapper_soup = slide_soup.select_one('.data_wrapper')

        title_soup = data_wrapper_soup.select_one('.info .title')
        description_soup = data_wrapper_soup.select_one('.descr')
        price_soup = data_wrapper_soup.select_one('.price')

        item = {
            'title': _beautify_text(title_soup.get_text()),
            'description': _beautify_text(description_soup.get_text()),
            'price': None,
        }

        if price_soup:
            item['price'] = _beautify_text(price_soup.get_text())

        data.append(item)

    return data


def _beautify_text(text: str):
    return text.strip()


def _get_soup_by_url(url: str):
    html = _get_html_from_url(url)
    return BeautifulSoup(html)


def _get_html_from_url(url: str):
    response = httpx.get(url)
    return response.content.decode()
