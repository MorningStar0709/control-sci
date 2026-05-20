is fitted by least squares, it is desirable that $A(q)v_{f}(t)$ be white noise. Since filtering with A implies that high frequencies are amplified, it means that $v_{f}(t)$ should not contain high frequencies. The data filter will therefore typically have band-pass character, as shown in Fig. 11.7. The center frequency is typically around the crossover frequency of the system.

In Section 3.5 we suggested using a filter with the transfer function

$$H _ {f} (z) = \frac {1}{A _ {o} (z ^ {- 1}) A _ {m} (z ^ {- 1})}$$

This filter is a typical low-pass filter that does not attenuate low frequencies. In Section 11.7 we will present other ways to choose the data filter. A typical data filter is given by

$$H _ {f} (q) = \frac {(1 - \alpha) (q - 1)}{q - \alpha}$$

Some ways to choose the data filter will be discussed later.

It has been emphasized many times that it is necessary for the input signal to be persistently exciting of sufficiently high order to estimate parameters reliably. Taking into account that we are fitting low-order models to high-order systems, it is also necessary that persistency of excitation be achieved with signals in a frequency band where model accuracy is required.
