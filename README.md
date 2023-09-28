# BUKU BIRU OTOMATIS

## ABOUT

Project ini dibuat dengan tujuan memudahkan mahasiswa informatika dalam menyusun foto selfie ukuran 3x4 untuk ditempel dibuku biru. Project ini dibuat dengan agar memaksikmalkan halaman dan disusun dengan rapi agar mudah dipotong sekaligus. Adapun beberapa fitur:

##### 1. Hasil Rapi sehingga mudah dipotong

##### 2. 140 foto dalam 25 detik

##### 3. Terdapat source code untuk compression foto sehingga tidak terlalu besar

## Penggunaan

1. Clone repository

```sh
   git clone https://github.com/github_username/repo_name.git
```

2. Install requirements.txt

```sh
pip install -r requirements.txt
```

3. Edit variable image_folder dan output sesuai dengan folder gambar.
   Install requirements.txt

```python
pdf_filename = "output.pdf"
image_path = "folder_kalian"
```

4. Jalankan dengan menggunakan python

```sh
python pdf.py
```

## Compress Image

1. Edit variable image_folder sesuai dengan folder kalian

```python
image_folder = "gambar"
```

2. Jalankan python

```sh
python image_compress.py
```

## Note

1. Semua gambar yang digunakan disarankan sudah memiliki ratio 3:4 dengan tujuan kerapian.
2. Kecepatan eksekusi diujikan pada laptop i3-2310M CPU dengan ram 4 GB pada sistem operasi Ubuntu 22.04.3 LTS
3. Pada 140 Foto ukurang pdf file masih dikisaran 150mb (cukup besar)
