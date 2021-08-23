import bs4, requests

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip()

price = getEbayPrice('https://www.ebay.com/itm/402776470298?epid=201642099&hash=item5dc759331a:g:IM4AAOSwNFdgaEAT')
print('The price is ' + price)
