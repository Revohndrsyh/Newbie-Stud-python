print("Welcome to the tip calculator!")
bill = float(input("Berapa total harganya? $"))
tip = int(input("kamu mau kasih tip berapa? 10, 12, 15 "))
people = int(input("Berapa orang yang akan bayar? "))

# Validasi input tip
if tip not in [10, 12, 15]:
    print("kamu mau kasih tip berapa? 10, 12, 15 ")
else:
    tip_persen = tip / 100
    total_bayar_tip = bill * tip_persen
    total_semua = bill + total_bayar_tip
    berapa_orang = total_semua / people

    hasil_akhir = round(berapa_orang, 2)
    print(f"Jadi per-satu orang bayar: ${hasil_akhir}")
