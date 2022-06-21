import main
import matplotlib.pyplot as plt

ans = main.DTFT(main.y, 193)


plt.title('DTFT of y[n]')
plt.plot(ans, color='b', label='DTFT of y[n]')
plt.legend(loc='upper right')
plt.savefig('plots/DTFT_of_y[n].png')
plt.show()
