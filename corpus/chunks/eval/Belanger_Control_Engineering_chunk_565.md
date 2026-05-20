# Problems

9.1 A signal $y(t)$ has the spectrum shown in Figure 9.19 (the phase is zero and $Y(j1)=0$ ). Sketch the spectrum of the signal obtained by impulse sampling of $y(t)$ at 1 rad/s, 1.5 rad/s, and 2.5 rad/s.

![](image/b8a0f4a4486651a3bce4ef843d40c71df61a58192e6167479c3d7499c31e1d26.jpg)

<details>
<summary>text_image</summary>

-1
1
ω
</details>

Figure 9.19 Spectrum of $y$ , Problem 9.1

9.2 Repeat Problem 9.1 for the spectrum of Figure 9.20 (the phase is zero).

![](image/d2f7a93068afdcb76e1c4847220af92eef122ebbed89be3dfb42e3176fd94cfc.jpg)

<details>
<summary>text_image</summary>

-1
1
ω
</details>

Figure 9.20 Spectrum of $y$ , Problem 9.2

![](image/bb398382d345ce5ea590cb7128b52660f6e48a6c50d3674733d55fafe8113210.jpg)

9.3 A first-order hold performs, for $kT_{s} \leq t \leq (k + 1)T_{s}$ , a linear extrapolation from the values at $(k - 1)T_{s}$ and $kT_{s}$ .

a. Write the analytic expression in the time domain for the extrapolated waveforms.   
b. Calculate the response to a discrete-time impulse $u_{0}(k)$ .   
c. From (b), calculate the transfer function and plot its magnitude and phase. Compare with the magnitude and phase of the zero-order hold.

![](image/efe4d795592a7e3041d85af85634e29ccfe983ac33e441424fbfa956f39e9067.jpg)

9.4 Repeat Problem 9.3 for the second-order hold, where the extrapolation is done by passing a quadratic through the points at $(k - 2)T_s$ , $(k - 1)T_s$ , and $kT_s$ .

9.5 Compute the z-transforms of the following:

a. $\widehat{y}(k) = (0.5)^{k} - (2)^{k - 1}$ .   
b. $\widehat{y}(k)=3e^{-k}\cos(2k+45).$

9.6 Compute the $z$ -transforms of the following:

a. $\widehat{y}(k)=(0.5)^{k-4}\sin[3(k-2)].$   
b. $\widehat{y}(k)=k(.7)^{-k}.$

9.7 Invert the following z-transforms, assuming causal signals.

a. $\widehat{y}(z) = [z(z + 2)] / [(z - 1)(z - .5)].$   
b. $\widehat{y}(z)=1/[z^{2}(z-1)(z-2)].$

9.8 Invert the following z-transforms, assuming causal signals.

a. $\widehat{y}(z) = [z(z + 1)] / [(z - .5)^2 (z - 1)].$   
b. $\widehat{y}(z) = 1 / [z(z^2 + z + 1)]$ .

9.9 Use linearity to prove the discrete convolution theorem for causal, linear, time-invariant systems:

$$\widehat {y} (k) = \sum_ {n = 0} ^ {k} h (k - n) \widehat {u} (n)$$

where $\widehat{u}$ is a causal signal.

\* H i n t Assume $\widehat{y}(k)$ to be a linear function of present and past inputs, and invoke time invariance.
