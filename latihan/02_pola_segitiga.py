# Latihan 2: Pola Segitiga

n = int(input("Masukkan n: "))

while n <= 0:
    print("n harus bilangan positif.")
    n = int(input("Masukkan n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()