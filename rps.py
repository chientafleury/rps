import random

choices = ["gunting", "batu", "kertas"]
computer = random.choice(choices)
player = input("Pilih (gunting/batu/kertas): ").lower()

print(f"Komputer memilih: {computer}")

if player == computer:
    print("Seri!")
elif (player == "batu" and computer == "gunting") or \
     (player == "gunting" and computer == "kertas") or \
     (player == "kertas" and computer == "batu"):
    print("Kamu menang!")
else:
    print("Komputer menang!")