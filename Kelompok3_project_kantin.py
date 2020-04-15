# pmbeli datang > kasir memberikan daftar meja kosong > pembeli pilih nomor meja (meja-=1)
# daftar warung tampil dan pilih warung > daftar menu dan pilih menu > bisa kembali atau konfir pemesanan
# setelah konfir pop up muncul di penjual > pesanan dibuat dan diantar >  meja dibersihkan pelayan (meja +=1)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

# ls > even = username, odd = pass
daf_pen,ls = [],['kevin','000','sofyan','123']
meja = 24

class Autentikasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Masukkan username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Masukkan password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_signin = QPushButton('Signin')
        label_sign = QLabel('<font size="4">Belum punya akun? </font>')
        button_login.clicked.connect(self.check_password)
        button_signin.clicked.connect(self.signin)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 30)
        layout.addWidget(label_sign, 3, 0)
        layout.addWidget(button_signin, 4, 0, 1, 2)
        layout.setRowMinimumHeight(2, 20)

        self.setLayout(layout)


    def check_password(self):
        msg = QMessageBox()
        if self.lineEdit_username.text() == '' or self.lineEdit_password.text() == '':
            msg.setText('isi semua kolom')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:

            if self.lineEdit_username.text() in ls :
                for i in range(len(ls)):
                    if self.lineEdit_username.text() == ls[i]:
                        indx = i
                        if self.lineEdit_password.text() == ls[indx+1]:
                            msg.setText('Sukses')
                            msg.setIcon(QMessageBox.Information)
                            msg.exec_()
                            app.quit()
                        else:
                            msg.setText('Password Salah')
                            msg.setStandardButtons(QMessageBox.Abort|QMessageBox.Retry)
                            msg.buttonClicked.connect(self.popup_btn)
                            msg.setIcon(QMessageBox.Critical)
                            msg.exec_()

            else:
                msg.setText('User Tidak Ditemukan')
                msg.setStandardButtons(QMessageBox.Abort|QMessageBox.Retry)
                msg.buttonClicked.connect(self.popup_btn)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def signin(self):
        msg = QMessageBox()
        ls.append(self.lineEdit_username.text())
        ls.append(self.lineEdit_password.text())
        msg.setText('Anda telah terdaftar')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def popup_btn(self, btn):
        if btn.text() == 'Abort':
            app.quit()


class transaksi:
    def __init__(self,waktu,no_trans,struk):
        self.waktu = waktu
        self.no_trans = no_trans
        self.struk = struk


class menu:
    def __init__(self,id_penjual,nama_menu,harga,stok):
        self.id_penjual = id_penjual
        self.nama_menu = nama_menu
        self.harga = harga
        self.stok = stok
        self.stokAwal = stok

    def __str__(self): #tampilan print
        return self.nama_menu + '\t\t\t' + str(self.harga) + '\t\t' + str(self.stok)


class penjual:
    def __init__(self,nomor,nama_warung,dmenu):
        self.nomor = nomor
        self.nama_warung = nama_warung
        self.dmenu = dmenu
        daf_pen.append(self)

    def getMenu(self):
        print('nama menu\t\tharga\t\tstok')
        for i in self.dmenu:
            print(i)

    def find_menu(self,target):
        for i in self.dmenu :
            if target == i.nama_menu:
                return i


class pembeli:
    def __init__(self,no_meja):
        assert 0 < no_meja <= 24, 'pilih nomor meja 1-24'
        self.no_meja = no_meja

    def pemesanan(self):
        daf_pesanan = []
        for i in daf_pen: #buat nampilkan daftar warung
            print(i.nomor, i.nama_warung)
        indx = int(input('pilih wrng : '))
        daf_pen[indx-1].getMenu()
        while True:
            pes = []
            pil = input('plih menu<koma>jumlah (jika selesai masukkan "sudah") : ')
            if pil == 'sudah':
                break
            else:
                pilmenu,jum = pil.split(',')
                pes.append(pilmenu);pes.append(jum)
                daf_pen[indx-1].find_menu(pilmenu).stok -= int(jum) #kurangi stok
                daf_pesanan.append(pes)

        return daf_pesanan


class notifikasi:
    def setDering(self):
        pass


class penghasilan:
    def __init__(self, tanggal):
        self.tanggal = tanggal

    def getLaporanKeuangan(self,id):
        for i in daf_pen:
            # print(type(i.nomor))
            if id == i.nomor:
                print(f'\n---------------Laporan keuangan {i.nama_warung}---------------')
                total = 0
                for i in i.dmenu:
                    terjual = i.stokAwal-i.stok
                    print(f'{i.nama_menu}\t\tstok terjual = stok awal - stok sisa\n\
                         = {i.stokAwal} - {i.stok} = {terjual} x {i.harga} = {terjual*i.harga}\n')
                    total += terjual*i.harga
                print(f'\t\t\ttotal penghasilan tanggal {self.tanggal} = Rp.{total}')


class pegawai:
    def __init__(self,nama,alamat,tgl_lahir,kontak):
        self.nama = nama
        self.alamat = alamat
        self.tgl_lahir = tgl_lahir
        self.kontak = kontak

    def getNama(self):
        return self.nama
    def getAlamat(self):
        return self.alamat
    def getTgl_lahir(self):
        return self.tgl_lahir
    def getKontak(self):
        return self.kontak

    def setNama(self, baru):
        self.nama = baru
    def setAlamat(self, baru):
        self.alamat = baru
    def setTgl_lahir(self, baru):
        self.tgl_lahir = baru
    def setKontak(self, baru):
        self.kontak = baru


class kasir(pegawai):
    def konfirmasi(self):
        pass
    def setMejaTerisi(self):
        pass
    def setBarang(self):
        pass
    def getBarang(self):
        pass
    def getDaftarMeja(self):
        return meja


class pelayan(pegawai):
    def setMejaKosong(self):
        pass


class titip:
    def __init__(self,id_barang):
        self.id_barang = id_barang
    def getIdPembeli(self):
        pass
    def setTitipBarang(self,nama_barang):
        pass


#### guistart demo ####
# app = QApplication(sys.argv)
# mulai = Autentikasi()
# mulai.show()
# app.exec_()

#### pegawai demo ####
# pegawai1 = kasir('budi', 'kp.timur','30 jan 1999','082233445566')
#
# print(pegawai1.getNama())
# print(pegawai1.getAlamat())
# print(pegawai1.getTgl_lahir())
# print(pegawai1.getKontak())
#
# print('\ndiupdate dulu..\n')
# pegawai1.setAlamat('jl kenangan')
# pegawai1.setKontak('081234567891')
#
# print(pegawai1.getNama())
# print(pegawai1.getAlamat())
# print(pegawai1.getTgl_lahir())
# print(pegawai1.getKontak())
#
# print(pegawai1.getDaftarMeja())


#### demo pemesanan ####
# n1 = penjual('1','mas gus',[menu(1,'geprek',15000,20),menu(1,'nasgor',12000,20),menu(1,'tahuu',5000,20)])
# n2 = penjual('2','mba boy',[menu(2,'mie gas',14000,20),menu(2,'salome',5000,20),menu(2,'tempe',3000,20)])
# n3 = penjual('3','dek dor',[menu(3,'wedank',7000,20),menu(3,'es the',4000,20),menu(3,'jeruk',5000,20)])
# # print(daf_pen)
# pm = pembeli(12)
# pm.pemesanan()

#### demo laporan ####
# lp1 = penghasilan('14 apr 2020')
# lp1.getLaporanKeuangan('2')
