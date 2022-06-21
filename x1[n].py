import main
import matplotlib.pyplot as plt


'''

First Removing Noise(Denoising) and then Sharpening(Deblurring).
Resulting Signal is x1[n]. 

'''

yn = main.denoising(main.y, 8)
Blur = main.deblurring(yn, main.h)
blur = main.inverse_DTFT(Blur, 193)

plt.title('Deviation of x1[n] from Original x[n]')
plt.plot(blur, color='b', label='Denoised then Deblurred (x1[n])')
plt.plot(main.x, color='r', label='Original x[n]')
plt.legend(loc='upper right')
plt.savefig('plots/x1[n].png')
plt.show()
