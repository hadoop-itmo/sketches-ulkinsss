class HyperLogLog:
    def __init__(self, b):
        self.b = b
        self.m = 1 << b
        self.M = [0] * self.m

    def put(self, s):
        
        x = mmh3.hash(s, signed=False)
        x_bin = bin(x)[2:].zfill(32)
        j = int(x_bin[:self.b], 2)
        w = x_bin[self.b:]

        r = next((i + 1 for i, bit in enumerate(w) if bit == '1'), len(w) + 1)
        
        self.M[j] = max(self.M[j], r)

    def est_size(self):
        z = sum(2 ** (-m) for m in self.M)
        Z = 1 / z
        
        alpha_m = 0.7213 / (1 + 1.079 / self.m) if self.m >= 128 else \
                   (self.m * quad(lambda x: math.log2((2+x)/(1+x))**self.m, 0, float('+inf'))[0]) ** (-1)
        
        E = alpha_m * self.m**2 * Z
        
        if E <= 2.5 * self.m:
            V = sum(1 for m in self.M if m == 0)
            if V > 0:
                E = self.m * math.log(self.m / V)
        elif E > (1/30) * (1 << 32):
            E = -(1 << 32) * math.log(1 - E / (1 << 32))
        
        return round(E)
