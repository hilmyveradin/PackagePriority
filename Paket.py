class Paket:
  


  def __init__(self, paketID, namaPengirimPaket, jenisBarang, durasiPaket, priority):
    self.id = paketID
    self.namaPengirimPaket = namaPengirimPaket
    self.jenisBarang = jenisBarang
    self.durasiPaket = durasiPaket
    self.priority = priority

    # add kerjaan baru
    #abc

  def __lt__(self, other):
    return self.priority[self.durasiPaket] < self.priority[other.durasiPaket]
