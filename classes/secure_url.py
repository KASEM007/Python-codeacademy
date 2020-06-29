class SearchEngineEntry:
    secure_prefix = "https://"

    def __init__(self, url):
        self.url = url

    def secure(self):
        return f"{self.secure_prefix}{self.url}"


codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"
print(wikipedia.url)
# prints "www.wikipedia.org"

