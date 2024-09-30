import numpy as np
import matplotlib.pyplot as plt

V0 = 0  
g = 9.8 
h0 = 10 


t_fall = np.sqrt(2 * h0 / g)
print("Waktu Jatuh =", t_fall, "s")
v_final = g * t_fall
print("Kecepatan Akhir =", v_final, "m/s")
h_final = h0 - 0.5 * g * t_fall**2
print("Ketinggian Akhir =", h_final, "m") 


t = np.linspace(0, t_fall, 1000)
v = g * t 
h = h0 - 0.5 * g * t**2  


fig, ax = plt.subplots()
ax.plot(t, v)
ax.set(xlabel='Waktu (s)', ylabel='Kecepatan (m/s)', title='Grafik Kecepatan sebagai Fungsi Waktu selama Benda Jatuh')
ax.grid()


fig, ax = plt.subplots()
ax.plot(t, h)
ax.set(xlabel='Waktu (s)', ylabel='Ketinggian (m)', title='Grafik Posisi Benda sebagai Fungsi Waktu selama Benda Jatuh')
ax.grid()

plt.show()
