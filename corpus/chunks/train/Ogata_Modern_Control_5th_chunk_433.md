$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 5 & - 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 2 5 \end{array} \right] u

y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

This system has one input u and one output y. By using the command

$$\operatorname{bode} (A, B, C, D)$$

and entering MATLAB Program 7–4 into the computer, we obtain the Bode diagram shown in Figure 7–24.

<table><tr><td>MATLAB Program 7-4</td></tr><tr><td>A = [0 1;-25 -4];B = [0;25];C = [1 0];D = [0];bode(A,B,C,D)title(&#x27;Bode Diagram&#x27;)</td></tr></table>

If we replace the command bode $\scriptstyle \cdot ( \mathsf { A } , \mathsf { B } , \mathsf { C } , \mathsf { D } )$ in MATLAB Program 7–4 with

$\mathrm { b o d e ( A , B , C , D , 1 ) }$

then MATLAB will produce the Bode diagram identical to that shown in Figure 7–24.

![](image/e022ab3c5f0a8118fd8c600d859699395a283e79ea65d110f19905ad2e9ef708.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 1 | 0 | 0 |
| 10 | -150 | -150 |
| 100 | -60 | -60 |
</details>

Figure 7–24 Bode diagram of the system considered in Example 7–7.
