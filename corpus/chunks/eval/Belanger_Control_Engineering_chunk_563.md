# Solution

The design proceeds as in Example 9.13, with the discretization done on the computer (MATLAB c2dm). The Bode plots appear in Figure 9.17. The phase margins (MATLAB margin) are 55.8°, 51.8°, and 43.5°, respectively, for $T_{s} = 0.05$ ,

![](image/40fda78c4e372dc2c8dec829ad8cf85138a31cba8baf145c6b095967cc2003cb.jpg)

<details>
<summary>line</summary>

| ω·Ts | Phase (deg) for Ts = .05 | Phase (deg) for Ts = .1 | Phase (deg) for Ts = .2 |
| --- | --- | --- | --- |
| 0.1 | -100 | -100 | -100 |
| 1 | -200 | -250 | -150 |
| 10 | -350 | -350 | -350 |
</details>

![](image/3f5507f63fbcc37a8b24982f24079297d2c24af84ceb539e0c141ee5cc2bea57.jpg)

<details>
<summary>line</summary>

| ω·Ts | Magnitude (db) for Ts = .1 | Magnitude (db) for Ts = .05 | Magnitude (db) for Ts = .2 |
| --- | --- | --- | --- |
| 0.1 | ~0 | ~0 | ~15 |
| 1 | ~-30 | ~-15 | ~-5 |
| 10 | ~-55 | ~-40 | ~-30 |
</details>

Figure 9.17 Bode plot magnitudes for Example 9.14, for $T_{s} = 0.05, 0.1$ , and 0.2 a

0.1, and 0.2. Note that (i) the difference between $T_{s} = 0.05$ and $T_{s} = 0.1$ is much less than in the case of backward differences, and (ii) for all three values of $T_{s}$ , the phase margin is greater than with the backward-difference method.

Step responses are plotted in Figure 9.18. The dotted curves are the sampled-data responses. $^{2}$

The simplest method of discretizing a controller expressed in state form is the forward-difference method, where $\mathbf{x}$ is replaced by $[\widehat{\mathbf{x}}(k+1)-\widehat{\mathbf{x}}(k)]/T_s$ . State equations become

$$\widehat {\mathbf {x}} (k + 1) = \widehat {\mathbf {x}} (k) + T _ {s} A \widehat {\mathbf {x}} (k) + T _ {s} B \widehat {\mathbf {e}} (k)$$

or

$$\widehat {\mathbf {x}} (k + 1) = (I + T _ {s} A) \widehat {\mathbf {x}} (k) + T _ {s} B \widehat {\mathbf {e}} (k)\widehat {\mathbf {u}} (k) = C \widehat {\mathbf {x}} (k) + D \widehat {\mathbf {e}} (k). \tag {9.40}$$

Here, $\widehat{\mathbf{e}}(k)$ is the error signal and $\widehat{\mathbf{u}}(k)$ is the controller output, which is, of course, the plant input.

The Tustin transformation can also be used. We replace $s$ with $(2 / T_s)[(z - 1) / (z + 1)] = (2 / T_s)[(1 - z^{-1}) / (1 + z^{-1})]$ , which yields

$$1 - z ^ {- 1} \widehat {\mathbf {x}} (z) = \frac {T _ {s}}{2} (1 + z ^ {- 1}) [ A \widehat {\mathbf {x}} (z) + B \widehat {\mathbf {e}} (z) ].$$

In the time domain,
