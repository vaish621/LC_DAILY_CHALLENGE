class Bank:

    def __init__(self, balance: List[int]):

        self.hash=defaultdict(int)
        for i in range(len(balance)):
            self.hash[i+1]=balance[i]
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.hash or account2 not in self.hash:
            return False
        
        if self.hash[account1]>=money:
            self.hash[account1]-=money
            self.hash[account2]+=money
            return True
        
        return False
        

        

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.hash:
            return False
        
        self.hash[account]+=money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.hash:
            return False
        
        if self.hash[account]>=money:
            self.hash[account]-=money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)