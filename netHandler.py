import urllib.request


class Reader:
    @staticmethod
    def loadCatgories(id):
        #print('http://shop.lego.com/de-DE/catalog/productListing.jsp?categoryIds=' + id)
        req = urllib.request.Request('http://shop.lego.com/de-DE/catalog/productListing.jsp?categoryIds=' + id)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        return the_page.decode('utf-8')
