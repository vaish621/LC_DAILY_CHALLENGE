class BrowserHistory:

    def __init__(self, homepage: str):
        self.ba=[homepage]
        self.fo=[]
        

    def visit(self, url: str) -> None:
        self.ba.append(url)
        self.fo.clear()

        

    def back(self, steps: int) -> str:

        while len(self.ba)>1 and steps>0:
            self.fo.append(self.ba.pop())
            steps-=1
        
        return self.ba[-1]
        

    def forward(self, steps: int) -> str:
        while self.fo and steps>0:
            self.ba.append(self.fo.pop())
            steps-=1
        
        return self.ba[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)