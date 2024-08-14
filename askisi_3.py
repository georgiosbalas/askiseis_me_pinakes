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

class pinakas_elegxos_kai_praxeis:

    def __init__(self, pinakas1, pinakas2):
        self.pinakas1 = pinakas1
        self.pinakas2 = pinakas2
        self.n = len(pinakas1.pinakas)
        self.elegxos_pinaka()
        if not self.elegxos_pinaka():
            print("Η αρχικοποίηση απέτυχε λόγω ανισότητας στα μεγέθη των πινάκων.")
            return

    def elegxos_pinaka(self):
        if len(self.pinakas1.pinakas) != len(self.pinakas2.pinakas):
            print("Σφάλμα: Οι πίνακες δεν έχουν το ίδιο μέγεθος.")
            return False
        for i in range(self.n):
            if len(self.pinakas1.pinakas[i]) != len(self.pinakas2.pinakas[i]):
                print("Σφάλμα: Οι πίνακες δεν έχουν το ίδιο μέγεθος.")
                return False
        return True
    
    def prosthesi(self):
        apotelesma = []
        for i in range(self.n):
            grammi = []
            for j in range(self.n):
                grammi.append(self.pinakas1.pinakas[i][j] + self.pinakas2.pinakas[i][j])
            apotelesma.append(grammi)
        print("Πρόσθεση των πινάκων:")
        for grammi in apotelesma:
            print(grammi)

    def afairesi(self):
        apotelesma = []
        for i in range(self.n):
            grammi = []
            for j in range(self.n):
                grammi.append(self.pinakas1.pinakas[i][j] - self.pinakas2.pinakas[i][j])
            apotelesma.append(grammi)
        print("Αφαίρεση των πινάκων:")
        for grammi in apotelesma:
            print(grammi)

    def pollaplasiasmos(self):
        apotelesma = []
        for i in range(self.n):
            grammi = []
            for j in range(self.n):
                athr_stoix = 0
                for k in range(self.n):
                    athr_stoix = athr_stoix + self.pinakas1.pinakas[i][k] * self.pinakas2.pinakas[k][j]
                grammi.append(athr_stoix)
        apotelesma.append(grammi)
        print("Πολλαπλασιασμός των πινάκων:")
        for grammi in apotelesma:
            print(grammi)

    def tensor_product(self):
        apotelesma = []
        for i in range(self.n):
            for j in range(self.n):
                temp_grammi = []
                for x in range(self.n):
                    for y in range(self.n):
                        temp_grammi.append(self.pinakas1.pinakas[i][x] * self.pinakas2.pinakas[y][j])
                apotelesma.append(temp_grammi)
        print("Tensor Product των πινάκων:")
        for grammi in apotelesma:
            print(grammi)

def main():

    pinakas1 = praxeis_pinakwn(5, tyxaiopoihsi=True)
    pinakas2 = praxeis_pinakwn(5, tyxaiopoihsi=True)
    print("Πρώτος Πίνακας:")
    pinakas1.ektypwsi_pinaka()
    print("Δεύτερος Πίνακας:")
    pinakas2.ektypwsi_pinaka()
    prakseis = pinakas_elegxos_kai_praxeis(pinakas1, pinakas2)
    prakseis.prosthesi()
    prakseis.afairesi()
    prakseis.pollaplasiasmos()
    prakseis.tensor_product()

if __name__ == "__main__":
    main()

     