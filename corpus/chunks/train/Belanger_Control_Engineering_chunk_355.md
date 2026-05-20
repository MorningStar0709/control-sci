If $\tau/T$ is large (the delay is small with respect to the time constant), then the upper limit for stable k is also large. This is what we expect, because, with no delay at all $(T=0)$ , the first-order system is stable for all k. As $\tau/T$ decreases (delay becomes more important), the stability limit also decreases. The following table lists a few values.

<table><tr><td> $\tau/T$ </td><td> $\omega_0 T$ </td><td>Limit on  $k$ </td></tr><tr><td>.1</td><td>2.86</td><td>1.04</td></tr><tr><td>.5</td><td>2.29</td><td>1.52</td></tr><tr><td>1</td><td>2.03</td><td>2.26</td></tr><tr><td>2</td><td>1.84</td><td>3.81</td></tr><tr><td>5</td><td>1.69</td><td>8.50</td></tr><tr><td>10</td><td>1.63</td><td>16.35</td></tr></table>

Unfortunately, many of the techniques we have studied so far (such as the Routh criterion and the Root Locus) and the state methods still to come require finite-state representation. This motivates us to approximate the delay with a rational transfer function called a Padé approximation. The idea is to match the leading terms of the series for $e^{-sT}$ . Since $e^{-sT}$ is all-pass, we try the all-pass transfer function

$$H (s) = \frac {- a s + 1}{a s + 1}, \quad a > 0.$$

The reader is invited to show, by long division, that

$$H (s) = 1 - 2 a s + 2 a ^ {2} s ^ {2} - 2 a ^ {3} s ^ {3} + \dots .$$

Compare this to

$$e ^ {- s T} = 1 - s T + \frac {1}{2} s ^ {2} T ^ {2} - \frac {1}{6} s ^ {3} T ^ {3} + \dots .$$

With $a = T / 2$ , the two series match up to and including the term in $s^2$ . The first-order Padé approximation is

$$H (s) = \frac {(- T / 2) s + 1}{(T / 2) s + 1}. \tag {6.53}$$

![](image/b44821d19b08a97eb32fcc3d9b724e6a25948cc1e54dbd0a8a2cc8591b51a730.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) - Pade approx. | Phase (deg) - Delay |
| --- | --- | --- |
| 0.1 | 0 | - |
| 1 | -100 | - |
| 10 | -200 | -500 |
</details>

Figure 6.35 Phase curves for the pure delay, Padé delay, and Padé approximation

For comparison, the phases for $e^{-sT}$ and for the Padé approximation are shown in Figure 6.35 for T = 1. (In both cases the magnitudes are unity at all frequencies.) In those (frequent) cases where the delay multiplies a rational transfer function, the replacement of $e^{-sT}$ by the Padé approximation can be assessed by the method of Chapter 5, Section 5.6, using the concept of an unstructured uncertainty.
