# Nama : Rifky Muafy
# NIM : 24028438
# Kelas : 1C

students = {
    'Alice': {'age': 20, 'major': 'Computer Science'},
    'Bob': {'age': 21, 'major': 'Mathematics'},
    'Charlie': {'age': 19, 'major': 'Physics'}
}

def get_student_info(name):
    if name in students:
        student = students[name]
        print(f"Umur {name} adalah {student['age']} dan Prodi nya adalah {student['major']}")
    else:
        print(f"Data untuk {name} tidak ditemukan.")

name = input("Inputkan nama siswa: ")
get_student_info(name)

