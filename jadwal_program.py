jadwal = {
    "A1": {"guru": "Syifa Abdul Lathif, S.Pd I", "mata_pelajaran": "Pendidikan Agama Islam"},
    "A2": {"guru": "Nurjanah S.P.I", "mata_pelajaran": "Pendidikan Agama Islam"},
    "A3": {"guru": "Rina Astusi, S.Pd.", "mata_pelajaran": "Pendidikan Agama Islam"},
    "A4": {"guru": "Enoh Danang Dwi Saputra, M.Th.", "mata_pelajaran": "Pendidikan Agama Kristen"},
    "A5": {"guru": "Yohanes Dimas Nugroho, S.Pd.", "mata_pelajaran": "Pendidikan Agama Kristen"},
    "A6": {"guru": "Marnaka, S.Ag", "mata_pelajaran": "Pendidikan Agama Hindu"},
    "B1": {"guru": "Gelis Wahjuti, S.Pd", "mata_pelajaran": "PPKn"},
    "B2": {"guru": "Aprilia Slamet Arifah, S.Pd.", "mata_pelajaran": "PPKn"},
    "C1": {"guru": "Sri Endang Sugiyanti", "mata_pelajaran": "Bahasa Indonesia"},
    "C2": {"guru": "Dwi Astuti Indriati, S.Pd, M.Hum", "mata_pelajaran": "Bahasa Indonesia"},
    "C3": {"guru": "Pipit Ristiana Anggraini, S.Pd", "mata_pelajaran": "Bahasa Indonesia"},
    "D1": {"guru": "Aris Widaryanti, S.Pd. M.Hum.", "mata_pelajaran": "Bahasa Inggris"},
    "D2": {"guru": "Gema Galgani Jumi S, S.Pd. M.Pd", "mata_pelajaran": "Bahasa Inggris"},
    "D3": {"guru": "Alfira Fanny Kuswandari S.Pd.", "mata_pelajaran": "Bahasa Inggris"},
    "E1": {"guru": "Yunarsih, S.Pd.", "mata_pelajaran": "Matematika"},
    "E2": {"guru": "Drs. Suwardi", "mata_pelajaran": "Matematika"},
    "E3": {"guru": "Desi Rahmawati, S.Pd.", "mata_pelajaran": "Matematika"},
    "E4": {"guru": "Parsana, S.Pd.", "mata_pelajaran": "Matematika"},
    "E5": {"guru": "Dwi Ningsih, S.Pd.Si", "mata_pelajaran": "Matematika"},
    "F1": {"guru": "Bimo Susetyo, S.Si. M.Pd.", "mata_pelajaran": "Fisika"},
    "F2": {"guru": "Drs. Dul Rohman Ary Yunanta", "mata_pelajaran": "Fisika"},
    "F3": {"guru": "Umi Fadilah, M.Pd.Si", "mata_pelajaran": "Fisika"},
    "F4": {"guru": "Rizal Irfandi Setiawan, S.Pd.", "mata_pelajaran": "Fisika"},
    "G1": {"guru": "Drs. Kunarka", "mata_pelajaran": "Kimia"},
    "G2": {"guru": "Dra Uin Supratiwi", "mata_pelajaran": "Kimia"},
    "G3": {"guru": "Wiwid Pungki Ningrum, S.Pd.", "mata_pelajaran": "Kimia/TIK"},
    "H1": {"guru": "Supardi, S.Pd.", "mata_pelajaran": "Biologi"},
    "H2": {"guru": "Monik Anesia Widyaningrum, S.Pd.", "mata_pelajaran": "Biologi"},
    "I1": {"guru": "Tutik Kundarwanti, S.Pd.", "mata_pelajaran": "Sejarah"},
    "I2": {"guru": "Anggita Tiana Rachmawati, S.Pd.", "mata_pelajaran": "Sejarah"},
    "J1": {"guru": "Sri Suramti, S.Pd.", "mata_pelajaran": "Geografi"},
    "J2": {"guru": "Suharyanti, S.Pd.", "mata_pelajaran": "Geografi"},
    "K1": {"guru": "Vita Fadliana, S.Pd. M.Pd.", "mata_pelajaran": "Ekonomi"},
    "K2": {"guru": "Patmiatun Retno Hardiyanti, S.Pd. M.Pd.", "mata_pelajaran": "Ekonomi"},
    "K3": {"guru": "Nur Isni Atun, S.Pd.", "mata_pelajaran": "Ekonomi"},
    "L1": {"guru": "Urip Sadewo, S.Sos.", "mata_pelajaran": "Sosiologi"},
    "L2": {"guru": "Putri Astini, S.Pd.", "mata_pelajaran": "Sosiologi"},
    "M1": {"guru": "Harno Handoyo, S.Pd. M.Pd.", "mata_pelajaran": "Seni Budaya"},
    "M2": {"guru": "Puspa Limpat Lelawati, S.Sn.", "mata_pelajaran": "Seni Budaya"},
    "N1": {"guru": "Muhammad Marjuki, S.Pd.", "mata_pelajaran": "Penjasorkes"},
    "N2": {"guru": "Asep Santoso, S.Pd.", "mata_pelajaran": "Penjasorkes"},
    "O1": {"guru": "Arief Budiman, S.Pd. M.Kom.", "mata_pelajaran": "Informatika/TIK"},
    "O2": {"guru": "Suprana Indarta, S.Pd.", "mata_pelajaran": "Prakarya dan KWU"},
    "P1": {"guru": "Nauli Trisnainy Siregar, S.S., M.Pd.", "mata_pelajaran": "Bahasa Prancis"},
    "Q1": {"guru": "Ririn Sulistiyani, S.Pd.", "mata_pelajaran": "Bahasa Jawa"},
    "Q2": {"guru": "Dewi Astutiningsih S, S.Pd.", "mata_pelajaran": "Bahasa Jawa"},
    "R1": {"guru": "Teti Nur'aeti, S.Pd.", "mata_pelajaran": "BK"},
    "R2": {"guru": "Prahesti Khasanah, S.Pd.", "mata_pelajaran": "BK"},
    "R3": {"guru": "Ramadhani Febriana Suryadewi, S.Pd.", "mata_pelajaran": "BK"},
    "R4": {"guru": "Musdalifah Amini", "mata_pelajaran": "BK"},
    "R5": {"guru": "Lyvia Choira, S.Pd.", "mata_pelajaran": "BK"},
    # Revisi Jadwal mulu TAIIIIII (Masih Lanjut Code nya)
}
hari = input("Masukkan hari (contoh: Senin): ")

kode_jadwal_list = []

while True:
    kode_jadwal = input("Masukkan kode guru (contoh: E4) atau ketik 'selesai' untuk menampilkan hasil: ")
    if kode_jadwal.lower() == 'selesai':
        break
    kode_jadwal_list.append(kode_jadwal)

print(f"\nHasil akhir untuk hari {hari}:")
for kode in kode_jadwal_list:
    if kode in jadwal:
        info = jadwal[kode]
        print(f"Kode {kode} - Guru: {info['guru']}, Mata Pelajaran: {info['mata_pelajaran']}")
    else:
        print(f"Kode {kode} tidak ditemukan.")
