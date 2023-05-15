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
    print(f"\n")
    # Get input from the user for each Paket element
    namaPengirimPaket = input("Masukkan nama pengirim: ")
    jenisBarang = input("Masukkan jenis barang: ")
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
    paket = Paket(paketID, namaPengirimPaket, jenisBarang, durasiPaket, priority)
    priorityQueue.put((priority[paket.durasiPaket], paket))

    # Print a success message with the new Paket ID
    print(f'\nProses pengiriman paket Anda berhasil! ID paket Anda adalah: {paketID}')

def printPaket(): 
    print(f"\n")
    # Print the contents of the queue in order of priority
    if priorityQueue.empty():
        print("Tidak ada antrian paket")
        return
    else:
        tempQueue = queue.PriorityQueue(maxsize=0)
        print("Antrian paket sekarang:\n")
        while not priorityQueue.empty():
            # Get the package and put it in the temporary queue
            priority_value, paket = priorityQueue.get()
            tempQueue.put((priority_value, paket))
            
            print(f"ID Paket: {paket.id}, Nama pengirim: {paket.namaPengirimPaket}, Jenis barang: {paket.jenisBarang}, Durasi: {paket.priority[paket.durasiPaket]}")

        # Copy the contents of the temporary queue back to the original queue
        while not tempQueue.empty():
            priorityQueue.put(tempQueue.get())

def searchPaket():
    print(f"\n")
    inputID = input("Masukkan ID paket yang ingin dicari: ")
    paket_ditemukan = False
    tempQueue = queue.PriorityQueue(maxsize=0)

    while not priorityQueue.empty():
        priority_value, paket = priorityQueue.get()
        tempQueue.put((priority_value, paket))

        if paket.id == inputID:
            paket_ditemukan = True
            print(f"Detail paket: {paket.id}")
            print(f"Nama Pengirim Paket: {paket.namaPengirimPaket}")
            print(f"Jenis barang: {paket.jenisBarang}")
            print(f"Durasi: {duration_options[paket.durasiPaket]}")

    # Copy the contents of the temporary queue back to the original queue
    while not tempQueue.empty():
        priorityQueue.put(tempQueue.get())

    if not paket_ditemukan:
        print(f"Paket dengan ID {inputID} tidak ditemukan.")

def batalkanPaket():
    print(f"\n")
    inputID = input("Masukkan ID paket yang ingin dibatalkan: ")
    tempQueue = queue.PriorityQueue(maxsize=0)
    paket_ditemukan = False

    while not priorityQueue.empty():
        _, paket = priorityQueue.get()
        if paket.id == inputID:
            paket_ditemukan = True
        else:
            tempQueue.put((priority[paket.durasiPaket], paket))

    # Copy the contents of the temporary queue back to the original queue
    while not tempQueue.empty():
        priorityQueue.put(tempQueue.get())

    if paket_ditemukan:
        print(f"Paket dengan ID {inputID} telah dibatalkan.")
    else:
        print(f"Paket dengan ID {inputID} tidak ditemukan.")

# Initial menu
while True:
    print("\nSelamat datang di layanan pengiriman paket. Ada yang bisa saya bantu hari ini?\n")
    print("1. Kirim paket")
    print("2. Cari paket")
    print("3. Batalkan paket")
    print("4. Cek antrian paket")
    print("5. Tidak ada, terima kasih!")
    choice = int(input("Masukkan pilihan Anda: "))
    if choice == 1:
        addPaket()
    elif choice == 2:
        searchPaket()
    elif choice == 3:
        batalkanPaket()
    elif choice == 4:
        printPaket()
    elif choice == 5:
        print("Terima kasih!")
        sys.exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    # Subsequent menu after adding a package
    while True:
        print("======================================")
        print("\nAda yang bisa kami bantu lagi?\n")
        print("1. Kirim paket")
        print("2. Cari paket")
        print("3. Batalkan paket")
        print("4. Cek antrian paket")
        print("5. Tidak ada, terima kasih!")
        choice = int(input("Masukkan pilihan Anda: "))
        if choice == 1:
            addPaket()
        elif choice == 2:
            searchPaket()
        elif choice == 3:
            batalkanPaket()
        elif choice == 4:
            printPaket()
        elif choice == 5:
            print("Terima kasih!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
