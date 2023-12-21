class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.pages = self.pages[:self.i+1]
        self.pages.append(url)
        self.i += 1

    def back(self, steps: int) -> str:
        if steps > self.i:
            self.i = 0
        else:
            self.i -= steps
        return self.pages[self.i]

    def forward(self, steps: int) -> str:
        if steps > len(self.pages) - 1 - self.i:
            self.i = len(self.pages) - 1
        else:
            self.i += steps
        return self.pages[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)