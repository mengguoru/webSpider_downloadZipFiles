import urllib,zipfile,io,re
from bs4 import BeautifulSoup

def download_from_zip_url(url):
    req = urllib.request.urlopen(url)
    file = zipfile.ZipFile(io.BytesIO(req.read()))
    file.extractall()
    print("Download success:",url)

def get_specific_urls(url):
    req = urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for link in soup.find_all(href=re.compile('zip')):
       links.append(link.get("href"))
    return links
    
if __name__ == "__main__":
    for link in get_specific_urls("http://www.wrox.com/WileyCDA/WroxTitle/Beginning-Visual-C-2012-Programming.productCd-1118314417,descCd-DOWNLOAD.html"):
        download_from_zip_url(link)
    print("finished")
