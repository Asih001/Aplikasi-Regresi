import math
import statistics

# Data
durasi_waktu_belajar = [7, 4, 8, 5, 7, 3, 7, 8, 5, 4]
nilai_ujian = [91.0, 65.0, 45.0, 36.0, 66.0, 61.0, 63.0, 42.0, 61.0, 69.0]

# Transformasi logaritma
ln_TB = [math.log(x) for x in durasi_waktu_belajar]
ln_NT = [math.log(y) for y in nilai_ujian]

# Menghitung rata-rata
mean_ln_TB = statistics.mean(ln_TB)
mean_ln_NT = statistics.mean(ln_NT)

# Menghitung koefisien regresi b dan a
numerator = sum((ln_TB[i] - mean_ln_TB) * (ln_NT[i] - mean_ln_NT) for i in range(len(ln_TB)))
denominator = sum((ln_TB[i] - mean_ln_TB) ** 2 for i in range(len(ln_TB)))
b = numerator / denominator
ln_a = mean_ln_NT - b * mean_ln_TB
a = math.exp(ln_a)

# Mencetak hasil koefisien
print(f'a: {a}, b: {b}')

# Prediksi NT menggunakan model pangkat
NT_pred = [a * (x ** b) for x in durasi_waktu_belajar]

# Menghitung galat RMS
def calculate_rms_error(actual, predicted):
    error = sum((actual[i] - predicted[i]) ** 2 for i in range(len(actual)))
    mean_error = error / len(actual)
    rms_error = math.sqrt(mean_error)
    return rms_error

rms_error = calculate_rms_error(nilai_ujian, NT_pred)
print(f'RMS Error: {rms_error}')

# Visualisasi data asli dan hasil regresi menggunakan ASCII art
def plot_data(durasi_waktu_belajar, nilai_ujian, NT_pred):
    max_tb = max(durasi_waktu_belajar)
    max_nt = max(nilai_ujian)
    scale_tb = 50 / max_tb
    scale_nt = 20 / max_nt

    plot = [[' ' for _ in range(55)] for _ in range(22)]

    for tb, nt in zip(durasi_waktu_belajar, nilai_ujian):
        x = int(tb * scale_tb)
        y = int(nt * scale_nt)
        plot[20 - y][x] = 'o'

    for tb, nt in zip(durasi_waktu_belajar, NT_pred):
        x = int(tb * scale_tb)
        y = int(nt * scale_nt)
        if plot[20 - y][x] == 'o':
            plot[20 - y][x] = '*'
        else:
            plot[20 - y][x] = '+'

    print('Durasi Waktu Belajar vs Nilai Ujian')
    for row in plot:
        print(''.join(row))

plot_data(durasi_waktu_belajar, nilai_ujian, NT_pred)
