import main
import matplotlib.pyplot as plt

ans = main.DTFT(main.h, 193)


plt.title('DTFT of h[n]')
plt.plot(ans, color='b', label='DTFT of [n]')
plt.legend(loc='upper right')
plt.savefig('plots/DTFT_of_h[n].png')
plt.show()
