class BrowserHistory:
    def __init__(self,homepage):
        self.back = [homepage]
        self.forward = []
    def visit(self,url):
        self.back.append(url)
        self.forward.clear()
    def go_back(self):
        if len(self.back)>1:
            self.forward.append(self.back.pop())
            return self.back[-1]
    def go_forward(self):
        page=self.forward.pop()
        self.back.append(page)
        return page
# Demo
b = BrowserHistory("google.com")
b.visit("youtube.com")
b.visit("github.com")
print(b.back)
print(b.forward)
print(b.go_back())
print(b.forward)
print(b.go_forward())
print(b.forward)