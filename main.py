import cmath
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


''' 
Reading temperature Data from the Excel File using Pandas Module Dataframe
'''

df = pd.read_csv('data.csv')

''' 
Importing Signals x[n] and y[n] from Excel File 
And Defining them as their list forms.
'''

x = df['x[n]']  # x[n] Signal
y = df['y[n]']  # y[n] Signal

h = [1/16, 1/4, 3/8, 1/4, 1/16]  # Given h[n]

'''
Defining the DTFT Function which contributes to Deblurring later.
'''


def DTFT(func, N):
    DTFT_Signal = []

    for k in range(N):
        term = 0
        for n in range(0, len(func)):
            term += ((cmath.exp(complex(0, ((k)*(-2)*(math.pi)*(n-2)/N)))
                      )*func[n])
        DTFT_Signal.append(term)
    return DTFT_Signal


'''
Defining the Inverse DTFT Function which also contributes to Deblurring later.
'''


def inverse_DTFT(func, N):
    inverse_DTFT_Signal = []
    for n in range(N):
        term = 0
        for k in range(N):
            term += func[k]*(cmath.exp(complex(0, (k*2*math.pi*n)/N))
                             )*((2*math.pi)/N)
        term = term/((math.pi)*2)
        inverse_DTFT_Signal.append(term)
    return inverse_DTFT_Signal


'''
Defining the Denoising Function using the Method of Average 
of corresponding values of three consecutive Samples of the Signal.
And using Recurssion for Denoising Multiple times.
'''


def denoising(func, times):
    denoised_signal = []
    i = 1
    denoised_signal.append(func[0])
    while i < len(func)-1:
        denoised_signal.append((func[i-1]+func[i+1]+func[i])/3)
        i += 1
    denoised_signal.append(func[192])
    if times > 0:
        return denoising(denoised_signal, times-1)
    else:
        return denoised_signal


'''

Defining the Deblurring FUnction using the DTFT and Inverse DTFT Functions
defined before. 
As we know,
->x[n]*h[n]=y[n]
->X(Z).H(Z)=Y(Z) -----(DTFT of x,h,y)
->X(Z)=Y(Z)/H(Z) -----(Mathematical Manipulation)
->inverse_DTFT(X(Z))=x[n]-----(Getting x[n] from X(Z) using inverse_DTFT)

'''


def deblurring(func1, func2):
    deblurred_signal = []

    Func1 = DTFT(func1, 193)
    Func2 = DTFT(func2, 193)
    for i in range(193):
        if abs(Func2[i]) <= 0.4:
            term = Func2[i]/0.4
            deblurred_signal.append(term)
        else:
            term = Func1[i]/Func2[i]
            deblurred_signal.append(term)

    return deblurred_signal
