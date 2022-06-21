import main
import matplotlib.pyplot as plt

'''

First Sharpening(Deblurring) and then Removing Noise(Denoising).
Resulting Signal is x2[n]. 

'''
Yb = main.deblurring(main.y, main.h)
yb = main.inverse_DTFT(Yb, 193)
L = main.denoising(yb, 8)


plt.title('Deviation of x2[n] from Original x[n]')
plt.plot(L, color='b', label='Deblurred then Denoised (x2[n])')
plt.plot(main.x, color='r', label='Original x[n]')
plt.legend(loc='upper right')
plt.savefig('plots/x2[n].png')
plt.show()
