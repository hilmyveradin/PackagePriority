class Paket:
  
  def __init__(self, paketID, namaPengirimPaket, jenisBarang, jenisPaket, durasiPaket, priority):
    self.id = paketID
    self.namaPengirimPaket = namaPengirimPaket
    self.jenisBarang = jenisBarang
    self.jenisPaket = jenisPaket
    self.durasiPaket = durasiPaket
    self.priority = priority

  def __lt__(self, other):
    return self.priority[self.durasiPaket] < self.priority[other.durasiPaket]
