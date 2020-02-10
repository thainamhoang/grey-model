class ADJ_R2:
        def __init__(self, r2, n, k):
                self.r2 = r2
                self.n = n
                self.k = k
        
        def ADJ_R2(self):
                return 1 - ((1 - self.r2) * ((self.n - 1) / (self.n - self.k - 1)))