| x | q(x) |
| --- | --- |
| -8.0 | 0.001 |
| -7.5 | 0.002 |
| -7.0 | 0.003 |
| -6.5 | 0.005 |
| -6.0 | 0.008 |
| -5.5 | 0.012 |
| -5.0 | 0.018 |
| -4.5 | 0.025 |
| -4.0 | 0.035 |
| -3.5 | 0.050 |
| -3.0 | 0.070 |
| -2.5 | 0.095 |
| -2.0 | 0.125 |
| -1.5 | 0.155 |
| -1.0 | 0.185 |
| -0.5 | 0.210 |
| 0.0 | 0.220 |
| 0.5 | 0.215 |
| 1.0 | 0.205 |
| 1.5 | 0.190 |
| 2.0 | 0.170 |
| 2.5 | 0.145 |
| 3.0 | 0.120 |
| 3.5 | 0.095 |
| 4.0 | 0.075 |
| 4.5 | 0.055 |
| 5.0 | 0.035 |
| 5.5 | 0.020 |
| 6.0 | 0.010 |
| 6.5 | 0.005 |
| 7.0 | 0.002 |
| 7.5 | 0.001 |
| 8.0 | 0.001 |
</details>

Figure 4.17: Importance function $q ( x )$ and its histogram based on 5000 samples.   
![](image/36c4e8dd23dcdf3458fc8e9559d77c551b3032764efd4b8a6a1cc1262b2a0eba.jpg)

<details>
<summary>histogram</summary>

| x | p(x) |
| --- | --- |
| -8.0 | 0.001 |
| -7.5 | 0.003 |
| -7.0 | 0.006 |
| -6.5 | 0.012 |
| -6.0 | 0.025 |
| -5.5 | 0.045 |
| -5.0 | 0.075 |
| -4.5 | 0.115 |
| -4.0 | 0.195 |
| -3.5 | 0.210 |
| -3.0 | 0.205 |
| -2.5 | 0.160 |
| -2.0 | 0.105 |
| -1.5 | 0.055 |
| -1.0 | 0.025 |
| -0.5 | 0.010 |
| 0.0 | 0.001 |
| 0.5 | 0.003 |
| 1.0 | 0.015 |
| 1.5 | 0.035 |
| 2.0 | 0.065 |
| 2.5 | 0.110 |
| 3.0 | 0.165 |
| 3.5 | 0.215 |
| 4.0 | 0.210 |
| 4.5 | 0.195 |
| 5.0 | 0.170 |
| 5.5 | 0.135 |
| 6.0 | 0.085 |
| 6.5 | 0.045 |
| 7.0 | 0.025 |
| 7.5 | 0.010 |
| 8.0 | 0.001 |
</details>

Figure 4.18: Exact density $p ( x )$ and its histogram based on 5000 importance samples.

1992). First we express d(s) as

$$
\begin{array}{l} d (s) = \frac {1}{s} \sum_ {j} \frac {h \left(x _ {j}\right)}{q \left(x _ {j}\right)} \\ = \int_ {- \infty} ^ {\infty} \frac {1}{s} \sum_ {j} \frac {h (x _ {j})}{q (x _ {j})} \delta (x - x _ {j}) d x \\ = \int_ {- \infty} ^ {\infty} \frac {1}{s} \sum_ {j} \frac {h (x)}{q (x)} \delta \left(x - x _ {j}\right) d x \\ d (s) = \int_ {- \infty} ^ {\infty} h _ {s} (x) d x \\ \end{array}
$$

Exchanging the order of limit and integral and using (4.46) give

$$\lim _ {s \rightarrow \infty} d (s) = \int_ {- \infty} ^ {\infty} \lim _ {s \rightarrow \infty} h _ {s} (x) d x = \int_ {- \infty} ^ {\infty} h (x) d x$$

Next we take the limit in (4.47) to obtain

$$
\begin{array}{l} \lim _ {s \rightarrow \infty} \overline {{p}} _ {s} (x) = \lim _ {s \rightarrow \infty} \frac {q _ {s} (x)}{d (s)} \frac {h (x)}{q (x)} \\ = \frac {\lim _ {s \rightarrow \infty} q _ {s} (x)}{\lim _ {s \rightarrow \infty} d (s)} \frac {h (x)}{q (x)} \\ = \frac {q (x)}{\int h (x) d x} \frac {h (x)}{q (x)} \\ = \frac {h (x)}{\int h (x) d x} \\ \lim _ {s \rightarrow \infty} \overline {{p}} _ {s} (x) = p (x) \\ \end{array}
$$

Notice the unbiased property no longer holds for a finite sample size. We can readily show

$$\mathcal {E} _ {\text { is }} \left(\overline {{p}} _ {s} (x)\right) \neq p (x) \quad \text { for finite } s \tag {4.49}$$

For example, take s = 1. We have from (4.48) that $w _ { 1 } = 1$ , and therefore

$$
\begin{array}{l} \mathcal {E} _ {\mathrm{is}} \left(\overline {{p}} _ {s} (x)\right) = \int p _ {\mathrm{is}} (x _ {1}) w _ {1} \delta (x - x _ {1}) d x _ {1} \\ = \int q (x _ {1}) \delta (x - x _ {1}) d x _ {1} \\ \mathcal {E} _ {\text { is }} \left(\overline {{p}} _ {s} (x)\right) = q (x) \\ \end{array}
$$
