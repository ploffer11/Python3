class Underprime:
    def __init__(self):
        self.a, self.b = (
            map(int, input().split())
        )
    
    def prime_list(self):
        self.era = [True] * (self.b+1)
        self.era[0], self.era[1] = False, False 
        prime = []
        for i in range(2, int((self.b)**.5)+1):
            if not self.era[i]:
                continue
            for j in range(2, self.b // i + 1):
                self.era[i*j] = False
        for i in range(2, self.b+1):
            if self.era[i]:
                prime.append(i)
        return prime

    def underprime(self):
        ans = 0
        prime = self.prime_list()
        for i in range(self.a, self.b + 1):
            soinsu = 0
            j = 0
            while j < len(prime):
                if self.era[i]:
                    soinsu += 1
                    break
                elif i==1:
                    break 
                while i % prime[j] == 0:
                    i //= prime[j]
                    soinsu += 1                
                j += 1
            if self.era[soinsu]:
                ans += 1
        print(ans) 
            

up = Underprime()
up.underprime()