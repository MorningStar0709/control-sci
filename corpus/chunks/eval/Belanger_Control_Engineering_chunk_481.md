where $\mathbf{w}$ is a complex vector of appropriate dimensions and $L = PF$ is the loop-gain matrix. The approximation $(I + L) \approx L$ is valid if, for any vector $\mathbf{w}$ , $(I + L)\mathbf{w} \approx L\mathbf{w}$ . From Equation 8.16, that is true if $\|L\mathbf{w}\|_2 \gg \| \mathbf{w}\|_2$ . Since $\|L\mathbf{w}\|_2$ is, at minimum, equal to $\underline{\sigma}(L)\|\mathbf{w}\|_2$ , the approximation holds if $\underline{\sigma}[L(j\omega)] \gg 1$ . This is precisely what is meant by “large loop gain.” In such a case,

$$S (j \omega) \approx L ^ {- 1} (j \omega)T (j \omega) \approx L ^ {- 1} (j \omega) L (j \omega) = I.$$

On the other hand, $(I + L) \approx I$ if $\|L\mathbf{w}\|_2$ is small compared to $\|\mathbf{w}\|_2$ . That is so for all $\mathbf{w}$ if $\overline{\sigma}(L) \ll 1$ ; this is the precise meaning of "small loop gain." In such a case,

$$S (j \omega) \approx IT (j \omega) \approx L (j \omega).$$

Example 8.1 The loop-gain matrix for a two-input, two-output system is

$$
L (s) = \left[ \begin{array}{c c} \frac {1}{s} & - \frac {. 5}{s + 1} \\ 1 & \frac {1}{s (s + 1)} \end{array} \right].
$$

(a) Compute and display $\overline{\sigma}[L(j\omega)]$ and $\underline{\sigma}[L(j\omega)]$ .   
(b) Calculate $S(s)$ and $T(s)$ .   
(c) Compute and display $\overline{\sigma}[S(j\omega)]$ .

Solution (a) The maximum and minimum singular values of $L$ are shown in Figure 8.2 (MATLAB sigma).

(b) We have

$$
S (s) = [ I + L (s) ] ^ {- 1} = \left[ \begin{array}{c c} \frac {s + 1}{s} & - \frac {. 5}{s + 1} \\ 1 & \frac {s ^ {2} + s + 1}{s (s + 1)} \end{array} \right] ^ {- 1}.
$$

We calculate

$$
\begin{array}{l} \det [ I + L (s) ] = \frac {(s + 1) (s ^ {2} + s + 1)}{s ^ {2} (s + 1)} + \frac {. 5}{s + 1} \\ = \frac {s ^ {2} + 2 . 5 s ^ {2} + 2 s + 1}{s ^ {2} (s + 1)} \\ \end{array}
$$

and

$$
S = \frac {1}{s ^ {3} + 2 . 5 s ^ {2} + 2 s + 1} \left[ \begin{array}{c c} s (s ^ {2} + s + 1) & . 5 s ^ {2} \\ - s ^ {2} (s + 1) & s (s + 1) ^ {2} \end{array} \right].
$$

![](image/167b4eed606ea5dc7242c650aca0a0f7c5b2c164e9448d2cd2a5b75ad14bf1e9.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Singular Values (dB) |
| --- | --- |
| 0.1 | 20 |
| 1 | -20 |
| 10 | -25 |
</details>

Figure 8.2 Singular values of the loop gain

![](image/a54f40feb606f6e6d4f6c7d952fc1b549a502b12d272eaf034e79b30f2a5f811.jpg)

<details>
<summary>line</summary>
