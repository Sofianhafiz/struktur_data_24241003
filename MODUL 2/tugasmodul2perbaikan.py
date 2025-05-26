# Node class untuk double linked-list
class Node:
    def __init__(self, data):# Saya membuat implementasi struktur data Double Linked List menggunakan Python.
        self.data = data #Kodenya mencakup operasi dasar seperti menambahkan node menghapus dari awal, akhir
        self.prev = None # dan berdasarkan nilai."
        self.next = None

# Double Linked List class
class DoubleLinkedList: #Struktur program terdiri dari dua kelas:
    def __init__(self): # Kelas Node, yang menyimpan data serta pointer ke node sebelumnya dan sesudahnya.
        self.head = None #Kelas DoubleLinkedList, yang menyimpan referensi ke head 
                          # dan menyediakan metode untuk manipulasi data."


    # Menambahkan node di akhir
    def append(self, data):  #Fungsi-fungsi yang Diimplementasikan
        new_node = Node(data)  #append(data): untuk Menambahkan node di akhir list. 
        if self.head is None:  #display():untuk Menampilkan semua data dalam list.
            self.head = new_node # delete_first():untuk Menghapus node paling awal. 
            return                #delete_last(): untuk Menghapus node paling akhir.
        cur = self.head         #delete_by_value(value): Menghapus node dengan nilai tertentu."
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    # Menampilkan isi list
    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> " if cur.next else "\n")
            cur = cur.next

    # 1. Menghapus node awal
    def delete_first(self):
        if self.head is None:
            print("List kosong")
            return
        print(f"Menghapus node awal: {self.head.data}")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # 2. Menghapus node akhir
    def delete_last(self):
        if self.head is None:
            print("List kosong")
            return
        cur = self.head
        if cur.next is None:
            print(f"Menghapus node terakhir: {cur.data}")
            self.head = None
            return
        while cur.next:
            cur = cur.next
        print(f"Menghapus node terakhir: {cur.data}")
        cur.prev.next = None

    # 3. Menghapus node berdasarkan nilai data
    def delete_by_value(self, value):
        if self.head is None:
            print("List kosong")
            return
        cur = self.head
        while cur:
            if cur.data == value:
                print(f"Menghapus node dengan nilai: {value}")
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                return
            cur = cur.next
        print(f"Data {value} tidak ditemukan dalam list.")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Isi awal:")
dll.display()

dll.delete_first()
dll.display()

dll.delete_last()
dll.display()

dll.delete_by_value(20)
dll.display()

dll.delete_by_value(99)  # Kasus data tidak ditemukan

#Menambahkan empat data: 10, 20, 30, 40.

#Menghapus node awal → hasilnya 20, 30, 40.

#Menghapus node akhir → hasilnya 20, 30.

#Menghapus data 20 → hasilnya tinggal 30.

#Terakhir, mencoba hapus data 99 yang tidak ada → muncul pesan bahwa data tidak ditemukan."

