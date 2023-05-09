from Paket import Paket
import queue
import sys

paketCounter = 0
priorityQueue = queue.PriorityQueue(maxsize=0)

def generatePaketID(): 
    global paketCounter
    paketCounter += 1
    return f'PAKET{str(paketCounter).zfill(3)}'
    

# Define the duration-to-priority mapping
global priority
duration_options = {1: 'hari yang sama', 2: 'besok', 3: '2-3 hari', 4: '3-5 hari'}
priority = {1: 1, 2: 2, 3: 3, 4: 4}

# Prompt the user for package information and add to queue
def addPaket():
    # Get input from the user for each Paket element
    namaPengirimPaket = input("Masukkan nama pengirim: ")
    jenisBarang = input("Masukkan jenis barang: ")
    jenisPaket = input("Masukkan jenis paket: ")
    # Prompt the user to enter the duration of the package
    print("Masukkan durasi pengiriman:")
    print("1. Hari yang sama")
    print("2. Besok")
    print("3. 2-3 hari")
    print("4. 3-5 hari")
    durasiPaket = int(input())

    # Generate a new Paket ID
    paketID = generatePaketID()

    # Create a new Paket object with the user input and the new ID
    paket = Paket(paketID, namaPengirimPaket, jenisBarang, jenisPaket, durasiPaket, priority)
    priorityQueue.put((priority[paket.durasiPaket], paket))

    # Print a success message with the new Paket ID
    print(f'Proses pengiriman paket Anda berhasil! ID paket Anda adalah: {paketID}')

def printPaket(): 
    # Print the contents of the queue in order of priority
    if priorityQueue.empty():
      print("Tidak ada antrian paket")
      return
    else:
      print("Antrian paket sekarang:")
      while not priorityQueue.empty():
          # need to turn this paket as Paket class
          _, paket = priorityQueue.get()
          print(f"ID Paket: {paket.id}, Nama pengirim: {paket.namaPengirimPaket}, Jenis barang: {paket.jenisBarang}, Jenis paket: {paket.jenisPaket}, Durasi: {paket.priority[paket.durasiPaket]}")

# Initial menu
while True:
    print("\n\nSelamat datang di layanan pengiriman paket. Ada yang bisa saya bantu hari ini?\n")
    print("1. Kirim paket")
    print("2. Cari paket")
    print("3. Cek antrian paket")
    print("4. Tidak ada, terima kasih!")
    choice = int(input("Masukkan pilihan Anda: "))
    if choice == 1:
        addPaket()
    elif choice == 2:
        print("Menu cari paket belum tersedia.")
    elif choice == 3:
        printPaket()
    elif choice == 4:
        print("Terima kasih!")
        sys.exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    # Subsequent menu after adding a package
    while True:
        print("\n\nAda yang bisa kami bantu lagi?\n")
        print("1. Kirim paket")
        print("2. Cari paket")
        print("3. Cek antrian paket")
        print("4. Tidak ada, terima kasih!")
        choice = int(input("Masukkan pilihan Anda: "))
        if choice == 1:
            addPaket()
        elif choice == 2:
            print("Menu cari paket belum tersedia.")
        elif choice == 3:
            printPaket()
        elif choice == 4:
            print("Terima kasih!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#test