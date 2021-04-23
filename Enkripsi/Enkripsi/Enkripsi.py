abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = int(input('Masukkan key yang diinginkan : '))

def encode(kalimat,cipher_key):
  kalimat = kalimat.lower()
  hasil_encode = ''
  for karakter in kalimat:
    if karakter in abjad:
      index_lama = abjad.index(karakter)
      index_baru = (index_lama + cipher_key ) % len(abjad)
      abjad_baru = abjad[index_baru]
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode

kalimat = input('Masukkan kata atau kalimat : ')
# ENKRIPSI
kalimat_hasil = encode(kalimat,key)
print('Kata atau kalimat yang dimasukkan adalah : ',kalimat)
print('Hasil Enkripsi dengan key :',key, 'adalah ', kalimat_hasil)
# DEKRIPSI (dengan enkripsi ulang menggunakan nilai minus key)
kalimat_awal = encode(kalimat_hasil,-key)
print('Hasil Dekripsi ulang menggunakan nilai negatif dari key: ',-key, 'adalah ', kalimat_awal)
