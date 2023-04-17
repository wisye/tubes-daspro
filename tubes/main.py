import func
import os

user_array = func.csv_reader('user.csv')
user = func.csv_parser(user_array, ';', 103, 3)

candi_array = func.csv_reader('candi.csv')
candi = func.csv_parser(candi_array, ';', 101, 5)

bahan_bangunan_array = func.csv_reader('bahan_bangunan.csv')
bahan_bangunan = func.csv_parser(bahan_bangunan_array, ';', 4, 3)
bahan_bangunan[1][0], bahan_bangunan[2][0], bahan_bangunan[3][0] = 'pasir', 'batu', 'air'
bahan_bangunan[1][1], bahan_bangunan[2][1], bahan_bangunan[3][1] = 'pasir', 'batu', 'air'
bahan_bangunan[1][2], bahan_bangunan[2][2], bahan_bangunan[3][2] = 0, 0, 0

# bahan_bangunan = [['nama', 'deskripsi', 'jumlah'], ['pasir', '', 0], ['batu', '', 0], ['air', '', 0]]

# print(user)
# print(candi)
# print(bahan_bangunan)

def main():
    command = input('>>> ')
    if command == 'login':
        login()
    elif command == 'help':
        help_main()
    elif command == 'exit':
        confirm = 'p'
        while confirm != 'Y' and confirm != 'N':
            confirm = input("Apakah anda ingin men-save progress (Y/N)?: ")
        if confirm == 'N': 
            exit()
        else:
            save()
    elif command == 'printu':
        printu()
    elif command == 'printb':
        printb()
    elif command == 'printc':
        printc()
    elif command == 'save':
        save()
    elif command == 'load':
        load()
    else:
        print('Command tidak terdaftar')
        return main()


def menu_bondowoso():
    command = input('>>> ')
    if command == 'help':
        help_bondowoso()
    elif command == 'logout':
        logout()
    elif command == 'exit':
        confirm = 'p'
        while confirm != 'Y' and confirm != 'N':
            confirm = input("Apakah anda ingin men-save progress (Y/N)?: ")
        if confirm == 'N': 
            exit()
        else:
            save()
    elif command == 'summonjin':
        summonjin()
    elif command == 'hapusjin':
        hapusjin()
    elif command == 'ubahjin':
        ubahjin()
    elif command == 'batchkumpul':
        batch_kumpul()
    elif command == 'batchbangun':
        batch_bangun()
    elif command == 'laporanjin':
        laporanjin()
    elif command == 'laporancandi':
        laporancandi()
    elif command == 'save':
        save()
    else:
        print('Command tidak terdaftar')
        return menu_bondowoso()


def menu_roro():
    command = input('>>> ')
    if command == 'help':
        help_roro()
    elif command == 'logout':
        logout()
    elif command == 'exit':
        confirm = 'p'
        while confirm != 'Y' and confirm != 'N':
            confirm = input("Apakah anda ingin men-save progress (Y/N)?: ")
        if confirm == 'N': 
            exit()
        else:
            save()
    elif command == 'hancurkancandi':
        hancurkancandi()
    elif command == 'ayamberkokok':
        ayamberkokok()
    elif command == 'save':
        save()
    else:
        print('Command tidak terdaftar')
        return menu_roro()


def menu_pembangun():
    command = input('>>> ')
    if command == 'bangun':
        bangun()
    elif command == 'help':
        help_pembangun()
    elif command == 'logout':
        logout()
    elif command == 'hancurkancandi':
        hancurkancandi()
    elif command == 'exit':
        confirm = 'p'
        while confirm != 'Y' and confirm != 'N':
            confirm = input("Apakah anda ingin men-save progress (Y/N)?: ")
        if confirm == 'N': 
            exit()
        else:
            save()
    else:
        print('Command tidak terdaftar')
        return menu_pembangun()
    

def menu_pengumpul():
    command = input('>>> ')
    if command == 'kumpul':
        kumpul()
    elif command == 'help':
        help_pengumpul()
    elif command == 'logout':
        logout()
    elif command == 'exit':
        confirm = 'p'
        while confirm != 'Y' and confirm != 'N':
            confirm = input("Apakah anda ingin men-save progress (Y/N)?: ")
        if confirm == 'N': 
            exit()
        else:
            save()
    else:
        print('Command tidak terdaftar')
        return menu_pengumpul()


def help_main():
    print('1. login : untuk masuk ke akun')
    print('2. exit : untuk keluar dari program')
    print('3. printu : print user')
    print('4. printb : print bahan bangunan')
    print('5. printc : print candi')
    return main()


def help_bondowoso():
    print('1. logout : untuk keluar dari akun')
    print('2. exit : untuk keluar dari program')
    print('3. summonjin : untuk memanggil jin')
    print('4. hapusjin: untuk menghapus jin')
    print('5. ubahjin: untuk mengubah tipe jin')
    print('6. batchkumpul: untuk mengerahkan seluruh jin pengumpul')
    print('7. batchbangun: untuk mengerahkan seluruh jin pembangun')
    print('8. laporanjin: untuk mengambil laporan jin')
    print('9. laporancandi: untuk mengambil laporan candi')
    return menu_bondowoso()


def help_roro():
    print('1. logout : untuk keluar dari akun')
    print('2. exit : untuk keluar dari program')
    print('3. hancurkancandi: untuk menghancurkan candi')
    print('4. ayamberkokok: untuk menyelesaikan permainan')
    return menu_roro()


def help_pembangun():
    print('1. logout : untuk keluar dari akun')
    print('2. bangun: untuk membangun candi')
    return menu_pembangun()


def help_pengumpul():
    print('1. logout : untuk keluar dari akun')
    print('2. kumpul: untuk mengumpulkan bahan')
    return menu_pengumpul()
    

def login():
    username = input('Username : ')
    password = input('Password : ')
    if func.checkm(user, username, 103, 1, 1) == True:
        for i in range (1, 103):
            if user[i][0] == username:
                if user[i][1] == password:
                    global current_user
                    current_user = username
                    print('Selamat datang, ',username,'!')
                    print('Masukkan command “help” untuk daftar command yang dapat kamu panggil.')
                    if user[i][2] == 'bandung_bondowoso':
                        return menu_bondowoso()
                    elif user[i][2] == 'roro_jonggrang':
                        return menu_roro()
                    elif user[i][2] == 'Jin_pembangun':
                        return menu_pembangun()
                    elif user[i][2] == 'Jin_pengumpul':
                        return menu_pengumpul()
                else:
                    print('Password salah!')
                    return main()
    else:
        print('Username tidak terdaftar!')
        return main()


def summonjin():
    breaker = 0
    for i in range (103):
        if user[i] == ['', '', '']:
            breaker += 1
    if breaker == 0:
        print('Bondowoso tidak dapat mensummon jin')
        menu_bondowoso()
    else:
        print('Jenis jin yang dapat dipanggil:')
        print(' (1) Pengumpul - Bertugas mengumpulkan bahan bangunan')
        print(' (2) Pembangun - Bertugas membangun candi')
        jenis_jin = 0
        pass_check = 0
        while jenis_jin != '1' and jenis_jin != '2':
            jenis_jin = input('Masukkan nomor jenis jin yang ingin dipanggil: ')
            if jenis_jin != '1' and jenis_jin != '2':
                print('Tidak ada jenis jin bernomor ', jenis_jin, '!')
        if jenis_jin == '1':
            print('Memilih jin “Pengumpul”')
            while jenis_jin !='-1':
                user_jin = input('Masukkan username jin: ')
                if func.checkm(user, user_jin, 103, 3, 0) == True:
                    print('Username “', user_jin,'” sudah diambil!')
                else:
                    while pass_check != -1:
                        pass_jin = input('Masukkan password jin: ')
                        if 5 <= func.str_len(pass_jin) <= 25:
                            pass_check = -1
                        else:
                            print("Password panjangnya harus 5-25 karakter!")
                    for i in range (103):
                        if user[i] == ['', '', '']:
                            user[i] = [user_jin, pass_jin, 'Jin_pengumpul']
                            break
                    print('Mengumpulkan sesajen...')
                    print('Menyerahkan sesajen...')
                    print('Membacakan mantra...')
                    print('Jin ', user_jin, ' berhasil dipanggil!')
                    return menu_bondowoso()
        else:
            print('Memilih jin “Pembangun”')
            while jenis_jin != '-1':
                user_jin = input('Masukkan username jin: ')
                if func.checkm(user, user_jin, 103, 3, 0) == True:
                    print('Username “', user_jin,'” sudah diambil!')
                else:
                    while pass_check != -1:
                        pass_jin = input('Masukkan password jin: ')
                        if 5 <= func.str_len(pass_jin) <= 25:
                            pass_check = -1
                        else:
                            print("Password panjangnya harus 5-25 karakter!")
                    for i in range (103):
                        if user[i] == ['', '', '']:
                            user[i] = [user_jin, pass_jin, 'Jin_pembangun']
                            break
                    print('Mengumpulkan sesajen...')
                    print('Menyerahkan sesajen...')
                    print('Membacakan mantra...')
                    print('Jin ', user_jin, ' berhasil dipanggil!')
                    return menu_bondowoso()


def hapusjin():
    jin = input('Masukkan username jin: ')
    confirm = 'p'
    if func.checkm(user, jin, 103, 3, 3) == True:
        for i in range (3, 103):
            if user[i][0] == jin:
                while confirm != 'Y' and confirm != 'N':
                    confirm = input('Apakah anda yakin ingin menghapus jin dengan username '+jin+' (Y/N)? ')
                if confirm == 'Y':
                    for j in range (101):
                        if candi[j][1] == jin:
                            candi[j] = ['', '', '', '', '']
                    user[i] = ['', '', '']        
                    print('Jin telah berhasil dihapus dari alam gaib.')
                    return menu_bondowoso()
                elif confirm == 'N':
                    return menu_bondowoso()
    else:
        print('Tidak ada jin dengan username tersebut.')
        return menu_bondowoso()
    

def ubahjin():
    jin = input('Masukkan username jin: ')
    confirm = 'p'
    if func.checkm(user, jin, 103, 3, 3) == True:
        for i in range (3, 103):
            if user[i][0] == jin:
                if user[i][2] == 'Jin_pembangun':
                    while confirm != 'Y' and confirm != 'N':
                        confirm = input('Jin ini bertipe pembangun. Yakin ingin mengubah ke tipe pengumpul (Y/N)? ')
                    if confirm == 'Y':
                        user[i][2] = 'Jin_pengumpul'
                        print("Jin telah berhasil diubah.")
                elif user[i][2] == 'Jin_pengumpul':
                    while confirm != 'Y' and confirm != 'N':
                        confirm = input('Jin ini bertipe pengumpul. Yakin ingin mengubah ke tipe pembangun (Y/N)? ')
                    if confirm == 'Y':
                        user[i][2] = 'Jin_pembangun'
                        print("Jin telah berhasil diubah.")
    else:
        print('Tidak ada jin dengan username tersebut.')
    return menu_bondowoso()


def bangun():
    pasir = func.randomize(); batu = func.randomize(); air = func.randomize()
    sisa = 0
    for i in range (1, 101):
        if candi[i] == ['', '', '', '', '']:
            sisa += 1
    if bahan_bangunan[1][2] >= pasir and bahan_bangunan[2][2] >= batu and bahan_bangunan[3][2] >= air:
        print('Candi berhasil dibangun.')
        print('Sisa candi yang perlu dibangun: ', sisa)
        bahan_bangunan[1][2] -= pasir; bahan_bangunan[2][2] -= batu; bahan_bangunan[3][2] -= air
        for i in range (101):
            if candi[i] == ['', '', '', '', '']:
                candi[i] = [i, current_user, pasir, batu, air]
                break
    elif sisa == 0:
        print('Candi tidak bisa dibangun!')
        print('Sisa candi yang perlu dibangun: 0.')
    else:
        print('Bahan bangunan tidak mencukupi.')
        print('Candi tidak bisa dibangun!')
    return menu_pembangun()


def kumpul():
    pasir = func.randomize(); batu = func.randomize(); air = func.randomize()
    bahan_bangunan[1][2] += pasir; bahan_bangunan[2][2] += batu; bahan_bangunan[3][2] += air
    print('Jin menemukan ', pasir, 'pasir, ', batu ,' batu, dan ', air, ' air.')
    return menu_pengumpul()


def batch_kumpul():
    pasir = 0; batu = 0; air = 0
    delimiter = 0; counter = 0
    for i in range (3, 103):
        if user[i][2] == 'Jin_pengumpul':
            counter += 1
            current_pasir = func.randomize(); current_batu = func.randomize(); current_air= func.randomize()
            bahan_bangunan[1][2] += current_pasir; bahan_bangunan[2][2] += current_batu; bahan_bangunan[3][2] += current_air
            pasir += current_pasir; batu += current_batu; air += current_air
        else:  
            delimiter += 1
    if delimiter == 100:
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')
    else:
        print('Mengerahkan ', counter ,' jin untuk mengumpulkan bahan.')
        print('Jin menemukan total ', pasir, ' pasir, ', batu ,' batu, dan ', air, ' air.')
    return menu_bondowoso()


def batch_bangun():
    pasir = 0; batu = 0; air = 0
    counter = 0; limiter1 = 0; limiter2 = 0; counter2 = 0
    for i in range (3, 103):
        if user[i][2] == 'Jin_pembangun':
            counter += 1
    bahan_holder = [['', '', '', ''] for i in range (counter)]
    if counter == 0:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
    else:
        for i in range (101):
            if user[i][2] == 'Jin_pembangun':
                current_user = user[i][0]
                current_pasir = func.randomize(); current_batu = func.randomize(); current_air= func.randomize()
                pasir += current_pasir; batu += current_batu; air += current_air
                if limiter1 <= counter:
                    bahan_holder[limiter1] = [current_user, current_pasir, current_batu, current_air]
                    limiter1 += 1
                else:
                    break
        for i in range (1, 101):
            if candi[i] == ['', '', '', '', '']:
                counter2 += 1
        if counter2 < counter:
            print('Tidak cukup ruangan untuk membangun candi oleh', counter, 'jin pembangun')
        else:
            if bahan_bangunan[1][2] >= pasir and bahan_bangunan[2][2] >= batu and bahan_bangunan[3][2] >= air:
                bahan_bangunan[1][2] -= pasir; bahan_bangunan[2][2] -= batu; bahan_bangunan[3][2] -= air
                for i in range (101):
                    if candi[i] == ['', '', '', '', ''] and limiter2 < counter:
                        candi[i] = [i, bahan_holder[limiter2][0], bahan_holder[limiter2][1], bahan_holder[limiter2][2], bahan_holder[limiter2][3]]
                        limiter2 += 1
                print('Mengerahkan ', counter, ' jin untuk membangun candi dengan total bahan ', pasir, ' pasir, ', batu, ' batu, dan ', air, ' air.')
                print('Jin berhasil membangun total ', counter, ' candi.')
            else:
                print('Mengerahkan ', counter, ' jin untuk membangun candi dengan total bahan ', pasir, ' pasir, ', batu, ' batu, dan ', air, ' air.')
                print('Bangun gagal. Kurang ', func.abso(pasir - bahan_bangunan[1][2]), ' pasir, ', func.abso(batu - bahan_bangunan[2][2]), ' batu, dan ', func.abso(air - bahan_bangunan[3][2]), ' air')
    return menu_bondowoso()


def laporanjin():
    total_pembangun = 0; total_pengumpul = 0; limiter1 = 0; limiter2 = 200
    for i in range (1, 103):
        if user[i][2] == 'Jin_pengumpul':
            total_pengumpul += 1
        elif user[i][2] == 'Jin_pembangun':
            total_pembangun += 1
    total_jin = total_pembangun + total_pengumpul
    # jin terajin
    jin_terajin = 'zuhair'
    for i in range (1,101):
        count = 0
        for j in range (1, 101):
            if candi[i][1] == candi[j][1] and candi[i][1] != '':
                count += 1
        if count > limiter1 and candi[i][1] != '':
            limiter1 = count
            if func.first_lettter_big(jin_terajin, candi[i][1]) == False:
                jin_terajin = candi[i][1]
    # jin termalas
    jin_termalas = 'athaullah'
    for i in range (1,101):
        count = 0
        for j in range (1, 101):
            if candi[i][1] == candi[j][1] and candi[i][1] != '':
                count += 1
        if count < limiter2 and candi[i][1] != '':
            limiter2 = count
            if func.first_lettter_small(jin_termalas, candi[i][1]) == False:
                jin_termalas = candi[i][1]
    print('Total jin: ', total_jin)
    print('Total jin pengumpul: ', total_pengumpul)
    print('Total jin pembangun: ', total_pembangun)
    print('Jin terajin: ', jin_terajin)
    print('Jin termalas: ', jin_termalas)
    print('Jumlah pasir: ', bahan_bangunan[1][2], ' unit')
    print('Jumlah batu: ', bahan_bangunan[2][2], ' unit')
    print('Jumlah air: ', bahan_bangunan[3][2], ' unit')
    return menu_bondowoso()


def laporancandi():
    total_candi = 0; pasir = 0; batu = 0; air = 0
    id_candi_termahal = 0; id_candi_termurah = 200
    harga_candi_termahal = 0; harga_candi_termurah = 163000 # paling mahal 5*pasir + 5*batu + 5*air
    for i in range (1, 101):
        if candi[i] != ['', '', '', '', ''] :
            total_candi += 1
            pasir += candi[i][2]; batu += candi[i][3]; air += candi[i][4]
            if (candi[i][2]*10000 + candi[i][3]*15000 + candi[i][4]*7500) > harga_candi_termahal:
                id_candi_termahal = candi[i][0]
                harga_candi_termahal = candi[i][2]*10000 + candi[i][3]*15000 + candi[i][4]*7500
            if (candi[i][2]*10000 + candi[i][3]*15000 + candi[i][4]*7500) < harga_candi_termurah:
                id_candi_termurah = candi[i][0]
                harga_candi_termurah = candi[i][2]*10000 + candi[i][3]*15000 + candi[i][4]*7500
    print('Total candi: ', total_candi)
    print('Total pasir yang digunakan: ', pasir)
    print('Total batu yang digunakan: ', batu)
    print('Total air yang digunakan: ', air)
    print('ID candi termahal: ', id_candi_termahal, ' (Rp ', harga_candi_termahal, ')')
    print('ID candi termurah: ', id_candi_termurah, ' (Rp ', harga_candi_termurah, ')')
    return menu_bondowoso()


def hancurkancandi():
    confirm = 'p'
    id_candi = int(input('Masukkan ID candi: '))
    if func.checkm(candi, str(id_candi), 101, 1, 1) == True:
        while confirm != 'Y' and confirm != 'N':
            confirm = input('Apakah anda yakin ingin menghancurkan candi ID: ' + str(id_candi) + ' (Y/N)? ')
        if confirm == 'Y':
            candi[id_candi] = ['', '', '', '', '']
            print('Candi telah berhasil dihancurkan.')
    else:
        print('Tidak ada candi dengan ID tersebut.')
    return menu_roro()


def ayamberkokok():
    print('Kukuruyuk.. Kukuruyuk..')
    total_candi = 0
    for i in range (1, 101):
        if candi[i] != ['', '', '', '', '']:
            total_candi += 1
    if total_candi == 100:
        print('Jumlah Candi: 100')
        print('Yah, Bandung Bondowoso memenangkan permainan!')
    else:
        print('Jumlah candi: ', total_candi)
        print('Selamat, Roro Jonggrang memenangkan permainan!')
        print('*Bandung Bondowoso angry noise*')
        print('Roro Jonggrang dikutuk menjadi candi.')


def logout():
    main()


def printu():
    print(user)
    return main()


def printb():
    print(bahan_bangunan)
    return main()


def printc():
    print(candi)
    return main()


def save():
    folder = input('Masukan nama folder: ')
    file1 = 'user1.csv'; file2 = 'bahan_bangunan1.csv'; file3 = 'candi1.csv'
    print('Saving...')
    if os.path.exists(folder) == False:
        print('Membuat folder ', folder)
        print('Berhasil menyimpan data di folder ', folder)
        os.mkdir(folder)
        os.chdir(folder)
        f1 = open(file1, 'x'); f2 = open(file2, 'x'); f3 = open(file3, 'x')
        for i in range (103):
            for j in range (3):
                f1.write(user[i][j])
                if j <= 1:
                    f1.write(';')
            f1.write('\n')
        for i in range (4):
            for j in range (3):
                f2.write(str(bahan_bangunan[i][j]))
                if j <= 1:
                    f2.write(';')
            f2.write('\n')
        for i in range (101):
            for j in range (5):
                f3.write(str(candi[i][j]))
                if j <= 3:
                    f3.write(';')
            f3.write('\n')
    else:
        print('Berhasil menyimpan data di folder ', folder)
        os.chdir(folder)
        f1 = open(file1, 'w'); f2 = open(file2, 'w'); f3 = open(file3, 'w')
        for i in range (103):
            for j in range (3):
                f1.write(user[i][j])
                if j <= 1:
                    f1.write(';')
            f1.write('\n')
        for i in range (4):
            for j in range (3):
                f2.write(str(bahan_bangunan[i][j]))
                if j <= 1:
                    f2.write(';')
            f2.write('\n')
        for i in range (101):
            for j in range (5):
                f3.write(str(candi[i][j]))
                if j <= 3:
                    f3.write(';')
            f3.write('\n')
    f1.close(); f2.close(); f3.close()
    os.chdir("../")


def load():
    folder = input('Masukan nama folder: ')
    if os.path.exists(folder) == False:
        print('Folder tidak ada')
    else:
        os.chdir(folder)
        global user
        user_array = func.csv_reader('user1.csv')
        user = func.csv_parser(user_array, ';', 103, 3)
        global candi
        candi_array = func.csv_reader('candi1.csv')
        candi = func.csv_parser(candi_array, ';', 101, 5)
        global bahan_bangunan
        bahan_bangunan_array = func.csv_reader('bahan_bangunan1.csv')
        bahan_bangunan = func.csv_parser(bahan_bangunan_array, ';', 4, 3)
    os.chdir("../")
    return main()


main()