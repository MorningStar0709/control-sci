# Case 4: two imaginary roots

If the coefficients $a _ { 1 } = 0$ and $a _ { 0 } > 0$ , then the radicand in Eq. (7.51) is negative, and the two roots are purely imaginary numbers (no real part, or $\alpha = 0 )$

$$r _ {1} = j \beta \quad \text { and } \quad r _ {2} = - j \beta \tag {7.59}$$

The homogeneous solution has the form

$$
\begin{array}{l} y _ {H} (t) = c _ {1} e ^ {j \beta t} + c _ {2} e ^ {- j \beta t} \\ = c _ {1} (\cos \beta t + j \sin \beta t) + c _ {2} (\cos \beta t - j \sin \beta t) \\ = (c _ {1} + c _ {2}) \cos \beta t + j (c _ {1} - c _ {2}) \sin \beta t \tag {7.60} \\ \end{array}
$$

Constants $c _ { 1 }$ and $c _ { 2 }$ are complex conjugates (just as in Case 3), and therefore the free response can be written in the same form as Eq. (7.58), but without the exponential function

$$y _ {H} (t) = K \cos (\beta t + \phi) \tag {7.61}$$

![](image/331dfd64978f8727ec62f7f3a5f257e27eaaaa54fc69b4374b27ec8b9a867de1.jpg)  
Figure 7.15 Second-order system root locations and a typical corresponding free response: complex roots (Case 3).

Figure 7.16 shows an example of the imaginary root locations in the complex plane and the corresponding free response. The free response is a purely harmonic (sinusoidal) function, which oscillates with constant amplitude. Therefore, the free response is marginally stable.

The consequences of the root locations for a second-order system can be summarized as follows:

• If the two roots are real, nonzero numbers, the free response will be the sum of two exponential functions. If both roots are negative, the free response decays to zero at steady state and the system is stable. If either root is positive, the free response diverges to infinity and the system is unstable.   
• If one root is equal to zero, part of the free response will be a constant, and therefore the system is marginally stable if the other root is negative. If the two roots are both equal to zero, the free response changes at a linear rate with time (provided $\dot { y } _ { 0 } \neq 0 )$ , and the system is unstable.

![](image/a52c61d81bdad91632e89d64ff60c68ae7d0dba9df510506b93bd937e2bbc7a1.jpg)

<details>
<summary>text_image</summary>

Imaginary
jβ
0
Real
-jβ
r₁,₂ = ± jβ
yₕ(t)
0
Marginally
stable
t
</details>

Figure 7.16 Second-order system root locations and a typical corresponding free response: imaginary roots (Case 4).

• If the two roots are complex numbers, they appear as complex conjugate pairs. The free response will oscillate at frequency ?? rad/s, where $\beta$ is the imaginary part of the complex roots. If the real part of the two roots (??) is negative, the free response is a damped sinusoid that decays to zero at steady state (stable). If ?? is positive, the free response is a diverging sinusoid (unstable).

• If the two roots are purely imaginary numbers, the free response is a sinusoid function that oscillates at frequency ?? rad/s. The system is marginally stable because the amplitude remains constant.
