<details>
<summary>line</summary>

| x | K=10000 | K=0.1 | K=0.00001 |
| --- | --- | --- | --- |
| 10^-3 | ~10^10 | ~10^8 | ~10^4 |
| 10^-2 | ~10^9 | ~10^7 | ~10^3 |
| 10^-1 | ~10^8 | ~10^6 | ~10^2 |
| 10^0 | ~10^6 | ~10^5 | ~10^1 |
| 10^1 | ~10^4 | ~10^3 | ~10^-2 |
| 10^2 | ~10^3 | ~10^2 | ~10^-4 |
| 10^3 | ~10^2 | ~10^1 | ~10^-6 |
</details>

Figure 16.9: Frequency response of $P _ { 6 }$ for $K = 1 0 ^ { - 5 } , 1 0 ^ { - 1 }$ and $1 0 ^ { 4 }$

The frequency responses of $P _ { 6 }$ with $K = 1 0 ^ { - 5 } , 1 0 ^ { - 1 }$ , and $1 0 ^ { 4 }$ are shown in Figure 16.9. It is clear that the slope of the frequency response near the crossover frequency for $K = 1 0 ^ { - 5 }$ is not too large, which implies a reasonably good loop shape. Thus we should expect $b _ { \mathrm { o p t } } ( P _ { 6 } )$ to be not too small. A similar conclusion applies to $K = 1 0 ^ { 4 }$ . On the other hand, the slope of the frequency response near the crossover frequency for $K = 0 . 1$ 1 is quite large which implies a bad loop shape. Thus we should expect $b _ { \mathrm { o p t } } ( P _ { 6 } )$ to be quite small. This is clear from the following table:

<table><tr><td>K</td><td> $10^{-5}$ </td><td> $10^{-3}$ </td><td>0.1</td><td>1</td><td>10</td><td> $10^{2}$ </td><td> $10^{4}$ </td></tr><tr><td> $b_{\text{opt}}(P_6)$ </td><td>0.3566</td><td>0.0938</td><td>0.0569</td><td>0.0597</td><td>0.0765</td><td>0.1226</td><td>0.4933</td></tr></table>

Based on the preceding discussion, we can give some guidelines for the loop-shaping design.

♥ The loop transfer function should be shaped in such a way that it has low gain around the frequency of the modulus of any right-half plane zero z. Typically, it requires that the crossover frequency be much smaller than the modulus of the right-half plane zero; say, $\omega _ { c } < | z | / 2$ for any real zero and $\omega _ { c } < | z |$ for any complex zero with a much larger imaginary part than the real part (see Figure 16.6).   
♥ The loop transfer function should have a large gain around the frequency of the modulus of any right-half plane pole.   
♥ The loop transfer function should not have a large slope near the crossover frequencies.

These guidelines are consistent with the rules used in classical control theory (see Bode [1945] and Horowitz [1963]).
