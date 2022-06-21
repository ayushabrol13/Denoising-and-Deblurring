# Signals and Systems EEL2010 Deblurring and Denoising

## Steps to follow to run the code:

- Install Python 3.9.5 or above.

      sudo apt-get install python3

- Install the dependencies.

      pip install -r requirements.txt

- For x1[n], First Denoising and then Deblurring.

      python3 x1\[n\].py

- For x2[n], First Deblurring and then Denoising.

      python3 x2\[n\].py

- For comparison between x1[n] and x2[n].

      python3 comparison.py

- For viewing the plot of DTFT of y[n]

      python3 DTFT_of_y\[n\].py

- For viewing the plot of DTFT of h[n]

      python3 DTFT_of_h\[n\].py

## Results

- x1[n] is the signal, first denoised and then deblurred.

  <img src="https://raw.githubusercontent.com/ayushabrol13/Denoising-and-Deblurring/master/plots/x1%5Bn%5D.png">

- x2[n] is the signal, first deblurred and then denoised.

  <img src="https://raw.githubusercontent.com/ayushabrol13/Denoising-and-Deblurring/master/plots/x2%5Bn%5D.png">

- Comparison between x1[n] and x2[n].

  <img src="https://raw.githubusercontent.com/ayushabrol13/Denoising-and-Deblurring/master/plots/x1%5Bn%5D_x2%5Bn%5D_comparison.png">

- DTFT of y[n]

  <img src="https://raw.githubusercontent.com/ayushabrol13/Denoising-and-Deblurring/master/plots/DTFT_of_y%5Bn%5D.png">

- DTFT of h[n]

  <img src="https://raw.githubusercontent.com/ayushabrol13/Denoising-and-Deblurring/master/plots/DTFT_of_h%5Bn%5D.png">

## Contributors

[Ayush Abrol](https://github.com/ayushabrol13)

[Abhishek Rajora](https://github.com/brillard1)
