"""dedicnost"""
class Zviratko:
    def __init__(self, meno):
        self.meno = meno
    def jedz(self, jedlo):
        print(f"{self.meno}: {jedlo} mi chutná")

class Macka(Zviratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Mňau")

    def jedz(self, jedlo):
        super().jedz(jedlo)
        print(f"{self.meno}: {jedlo} vypľula")

class Pes(Zviratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Had")

macka = Macka("Micka")
pes = Pes("Falko")

macka.jedz("Sunka")
macka.urob_zvuk()

pes.jedz("Mäsko")
pes.urob_zvuk()

"""polymorfismus"""
zvieratka = [Macka("Naginy"), Pes("Azor")]

for zvieratko in zvieratka:
    zvieratko.jedz("Granulka")
    zvieratko.urob_zvuk()
"""generalizacia"""