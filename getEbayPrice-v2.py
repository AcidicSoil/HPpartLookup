Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bs4
>>> import requests
>>> res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
>>> res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\requests\models.py", line 940, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url: https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994
>>> res = requests.get('https://www.ebay.com/itm/402776470298?epid=201642099&hash=item5dc759331a:g:IM4AAOSwNFdgaEAT')
>>> res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
>>> res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\requests\models.py", line 940, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url: https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994
>>> res = requests.get('https://www.ebay.com/itm/402776470298?epid=201642099&hash=item5dc759331a:g:IM4AAOSwNFdgaEAT')
>>> res.raise_for_status()
>>> soup = bs4.BeautifulSoup(res.text)
>>> soup = bs4.BeautifulSoup(res.text, 'html.parser')
>>> soup.select('#prcIsum')
[<span class="notranslate" content="11.66" id="prcIsum" itemprop="price" style="text-decoration:none">US $11.66</span>]
>>> elems = soup.select('[<span class="notranslate" content="11.66" id="prcIsum" itemprop="price" style="text-decoration:none">US $11.66</span>]')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    elems = soup.select('[<span class="notranslate" content="11.66" id="prcIsum" itemprop="price" style="text-decoration:none">US $11.66</span>]')
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\bs4\element.py", line 1869, in select
    results = soupsieve.select(selector, self, namespaces, limit, **kwargs)
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\soupsieve\__init__.py", line 98, in select
    return compile(select, namespaces, flags, **kwargs).select(tag, limit)
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\soupsieve\__init__.py", line 62, in compile
    return cp._cached_css_compile(pattern, namespaces, custom, flags)
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\soupsieve\css_parser.py", line 211, in _cached_css_compile
    CSSParser(pattern, custom=custom_selectors, flags=flags).process_selectors(),
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\soupsieve\css_parser.py", line 1058, in process_selectors
    return self.parse_selectors(self.selector_iter(self.pattern), index, flags)
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\soupsieve\css_parser.py", line 909, in parse_selectors
    key, m = next(iselector)
  File "C:\Users\biven\AppData\Roaming\Python\Python39\site-packages\soupsieve\css_parser.py", line 1051, in selector_iter
    raise SelectorSyntaxError(msg, self.pattern, index)
soupsieve.util.SelectorSyntaxError: Malformed attribute selector at position 0
  line 1:
[<span class="notranslate" content="11.66" id="prcIsum" itemprop="price" style="text-decoration:none">US $11.66</span>]
^
>>> soup.select('#prcIsum')
[<span class="notranslate" content="11.66" id="prcIsum" itemprop="price" style="text-decoration:none">US $11.66</span>]
>>> elems = soup.select('#prcIsum')
>>> elems[0].text
'US $11.66'
>>> elems[0].text.strip()
'US $11.66'
>>> 