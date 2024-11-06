# Nama : Rifky Muafy
# NIM : 24028438
# Kelas : 1C

students = {
    'Alice': 'Computer Science',
    'Bob': 'Mathematics',
    'Charlie': 'Physics',
    'David': 'Computer Science',
    'Eva': 'Mathematics'
}

# Dictionary baru untuk menghitung jumlah siswa di setiap jurusan
deez_nuts = {}

# Menghitung jumlah siswa di setiap jurusan
for student, major in students.items():
    if major in deez_nuts:
        deez_nuts[major] += 1
    else:
        deez_nuts[major] = 1

# Menampilkan hasil
for major, count in deez_nuts.items():
    print(f"Prodi {major} sebanyak {count}")