# Paket.py
class Paket:
    def __init__(self, paketID, namaPengirimPaket, jenisBarang, durasiPaket, priority):
        self.id = paketID
        self.namaPengirimPaket = namaPengirimPaket
        self.jenisBarang = jenisBarang
        self.durasiPaket = durasiPaket
        self.priority = priority

    def __lt__(self, other):
        return self.priority[self.durasiPaket] < other.priority[other.durasiPaket]

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
