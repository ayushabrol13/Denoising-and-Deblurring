import main
import matplotlib.pyplot as plt


'''

Comparing the Signals x1[n] and x2[n].
x1[n]->First Removing Noise(Denoising) and then Sharpening(Deblurring).
x2[n]->First Sharpening(Deblurring) and then Removing Noise(Denoising).

'''
yn = main.denoising(main.y, 8)
Blur = main.deblurring(yn, main.h)
blur = main.inverse_DTFT(Blur, 193)

Yb = main.deblurring(main.y, main.h)
yb = main.inverse_DTFT(Yb, 193)
L = main.denoising(yb, 8)

plt.title('Comparison between x1[n] and x2[n] and their deviation from x[n]')
plt.plot(blur, color='black', label='Denoised then Deblurred (x1[n])')
plt.plot(L, color='b', label='Deblurred then Denoised (x2[n])')
plt.plot(main.x, color='r', label='Original x[n]')
plt.legend(loc='upper right')
plt.savefig('plots/x1[n]_x2[n]_comparison.png')
plt.show()
