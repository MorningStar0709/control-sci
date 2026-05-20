# E.3.3 Laplace transform

The Laplace domain is a generalization of the frequency domain that has the frequency (jω) on the imaginary y-axis and a real number on the x-axis, yielding a two-dimensional coordinate system. We represent coordinates in this space as a complex number s = $\sigma + j \omega$ . The real part σ corresponds to the x-axis and the imaginary part jω corresponds to the y-axis (see figure E.12).

To extend our analogy of each coordinate being represented by some basis, we now have the y coordinate representing the oscillation frequency of the system response (the frequency domain) and also the x coordinate representing the speed at which that

![](image/54a1fc184b92cbe9f9b5d6a59533d3dd0da0221c2c1de65ddd88f218a3c6d4fe.jpg)  
Figure E.10: Frequency decomposition of Fmajor4 chord

![](image/061a941fe6d1a57f3d40c6978925ebbe1a74e99cbdfdc10b39a1c1b56f1b6ff8.jpg)

<details>
<summary>bar</summary>

| Frequency (Hz) | Value |
| -------------- | ----- |
| 270            | 1.0   |
| 350            | 1.0   |
| 440            | 1.0   |
</details>

Figure E.11: Fourier transform of Fmajor4 chord

![](image/d74a63ed12cb65b7788934fd2374fc3e0d6b01b105d1b8d208f989754044871d.jpg)

<details>
<summary>text_image</summary>

Im(jω)
Re(σ)
</details>

Figure E.12: Laplace domain

oscillation decays and the system converges to zero (i.e., a decaying exponential). Figure E.2 shows this for various points.

If we move the component frequencies in the Fmajor4 chord example parallel to the real axis to $\sigma = - 2 5$ , the resulting time domain response attenuates according to the decaying exponential $e ^ { - 2 5 t }$ (see figure E.13).

Note that this explanation as a basis isn’t exact because the Laplace basis isn’t orthogonal (that is, the x and y coordinates affect each other and have cross-talk). In the frequency domain, we had a basis of sine waves that we represented as delta functions in the frequency domain. Each frequency contribution was independent of the others. In the Laplace domain, this is not the case; a pure exponential is $\frac { 1 } { s - a }$ (a rational function −where a is a real number) instead of a delta function. This function is nonzero at points that aren’t actually frequencies present in the time domain. Figure E.14 demonstrates this, which shows the Laplace transform of the Fmajor4 chord plotted in 3D.
