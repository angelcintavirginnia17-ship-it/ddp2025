import math
def kubus(sisi):
    hasil = math.pow(sisi,3)
    return hasil

def balok(p,l,t):
    hasil = p * l * t
    return hasil

def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas *tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil

def volume_tabung(jari_jari, tinggi):
  return math.pi * (jari_jari ** 2) * tinggi

def volume_kerucut(jari_jari, tinggi):
  return (1/3) * math.pi * (jari_jari ** 2) * tinggi

print(prisma(3,3,3))

    

print(balok(3,3,3))


print (kubus(3))