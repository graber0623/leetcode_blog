class Codec:
    def __init__(self):
        self.encodeUrl = {}
        self.decodeUrl = {}
        self.baseurl = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        # """
        # Encodes a URL to a shortened URL.
        # """
        if longUrl not in self.encodeUrl:
            tinyurl = self.baseurl + str(len(self.encodeUrl)+1)
            self.encodeUrl[longUrl] = tinyurl
            self.decodeUrl[tinyurl] = longUrl

        return self.encodeUrl[longUrl]

        

    def decode(self, shortUrl: str) -> str:
        # """
        # Decodes a shortened URL to its original URL.
        # """
        return self.decodeUrl[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))