# Example 7.5 Ramp-invariant sampling of a double integrator

Consider a system with the transfer function $G(s) = 1/s^{2}$ . This system has the realization

$$
\begin{array}{l} \frac {d x}{d t} = \left( \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right) x + \binom{0}{1} u \\ y = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x \\ \end{array}
$$

for the matrix

$$
\tilde {A} = \left( \begin{array}{c c c} A & B & 0 \\ 0 & 0 & I \\ 0 & 0 & 0 \end{array} \right) = \left( \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right)
$$

and its matrix exponential

$$
e ^ {\dot {A} h} = \left( \begin{array}{c c c c} 1 & h & h ^ {2} / 2 & h ^ {3} / 6 \\ 0 & 1 & h & h ^ {2} / 2 \\ 0 & 0 & 1 & h \\ 0 & 0 & 0 & 1 \end{array} \right)
$$

Hence from (7.17)

$$
\Phi = \left( \begin{array}{c c} 1 & h \\ 0 & 1 \end{array} \right) \quad \Gamma = \binom{h ^ {2} / 2}{h} \quad \Gamma_ {1} = \binom{h ^ {3} / 6}{h ^ {2} / 2}
$$

The pulse-transfer function is now obtained from (7.16), that is,

$$
\begin{array}{l} H (z) = \left( \begin{array}{l l} 1 & 0 \end{array} \right) \left( \begin{array}{c c} z - 1 & - h \\ 0 & z - 1 \end{array} \right) ^ {- 1} \left(\binom {h ^ {2} / 6} {h / 2} z + \binom {h ^ {2} / 2} {h} - \binom {h ^ {2} / 6} {h / 2}\right) \\ = \frac {h ^ {2}}{6} \frac {z ^ {2} + 4 z + 1}{(z - 1) ^ {2}} \\ \end{array}
$$

![](image/074cf4fc97bc0a4b186d0bcc72610d0735133f5a50e33f8f6fb4775716079428.jpg)

<details>
<summary>line</summary>

| t | y |
| --- | --- |
| 0 | 0 |
| 1 | 0.5 |
| 2 | 1 |
| 3 | 0.5 |
| 4 | 1 |
| 5 | 0.5 |
</details>

![](image/0ab8aaadcb96b39ce23c65c69edd80c68c483ad37527560d58145726dc6e82a7.jpg)

<details>
<summary>line</summary>

| t | u |
| --- | --- |
| t_{k-1} | Low |
| t_k | High |
| t_{k+1} | Medium |
| t_{k+2} | High |
</details>

Figure 7.14 Inputs and outputs of a process with predictive first-order-hold sampling.
