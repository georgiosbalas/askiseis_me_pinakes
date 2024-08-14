import random
class praxeis_pinakwn:
    def __init__(self, n, tyxaiopoihsi = False):
        self.n = n
        self.pinakas = self.dimiourgia_pinaka(tyxaiopoihsi)
    
    def dimiourgia_pinaka(self, tyxaiopoihsi):
        pinakas = []
        for i in range(self.n):
            grammi = []
            for j in range(self.n):
                if tyxaiopoihsi:
                    grammi.append(random.randint(1, 100))
                else:
                    grammi.append(j + i * self.n + 1)
            pinakas.append(grammi)
        return pinakas
    
    def ektypwsi_pinaka(self):
        for grammi in self.pinakas:
            print(grammi)

    def athroisma_grammwn(self):
        for i, grammi in enumerate(self.pinakas):
            athr_gram = sum(grammi)
            print("Άθροισμα γραμμής", i + 1, ":", athr_gram)

    def athroisma_stilwn(self):
        for j in range(self.n):
            athr_stil = 0
            for i in range(self.n):
                athr_stil = athr_stil + self.pinakas[i][j]
            print("Άθροισμα στήλης", j + 1, ":", athr_stil)

    def aristeri_diagwnios(self):
        athr_ar_diag = 0
        for i in range(self.n):
            athr_ar_diag = athr_ar_diag + self.pinakas[i][i]
        print("Άθροισμα αριστερής διαγωνίου:", athr_ar_diag)

    def dexia_diagwnios(self):
        athr_de_diag = 0
        for i in range(self.n):
            athr_de_diag = athr_de_diag + self.pinakas[i][self.n - 1 - i]
        print("Άθροισμα δεξιάς διαγωνίου:", athr_de_diag)
    

def main():
    pinakes = [
        praxeis_pinakwn(5, tyxaiopoihsi = False),
        praxeis_pinakwn(5, tyxaiopoihsi = True),
        praxeis_pinakwn(5, tyxaiopoihsi = True)
    ]

    for pinakas in pinakes:
        print("Πίνακας:")
        pinakas.ektypwsi_pinaka()
        pinakas.athroisma_grammwn()
        pinakas.athroisma_stilwn()
        pinakas.aristeri_diagwnios()
        pinakas.dexia_diagwnios()
        print()

if __name__ == "__main__":
    main()