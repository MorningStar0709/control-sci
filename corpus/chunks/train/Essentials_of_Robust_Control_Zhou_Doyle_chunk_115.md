This shows that the system response will be amplified 11.47 times for an input signal at the frequency $\omega _ { \mathrm { m a x } }$ , which could be undesirable if $F _ { 1 }$ and $F _ { 2 }$ are disturbance force and $x _ { 1 }$ and $x _ { 2 }$ are the positions to be kept steady.

Example 4.3 Consider a two-by-two transfer matrix

$$
G (s) = \left[ \begin{array}{c c} \frac {1 0 (s + 1)}{s ^ {2} + 0 . 2 s + 1 0 0} & \frac {1}{s + 1} \\ \frac {s + 2}{s ^ {2} + 0 . 1 s + 1 0} & \frac {5 (s + 1)}{(s + 2) (s + 3)} \end{array} \right].
$$

A state-space realization of G can be obtained using the following Matlab commands:

G11=nd2sys([10,10],[1,0.2,100]);   
G12=nd2sys(1,[1,1]);   
G21=nd2sys([1,2],[1,0.1,10]);   
G22=nd2sys([5,5],[1,5,6]);   
G=sbs(abv(G11,G21),abv(G12,G22));

Next, we set up a frequency grid to compute the frequency response of $G$ and the singular values of $G ( j \omega )$ over a suitable range of frequency.

w=logspace(0,2,200); % 200 points between $1 = 1 0 ^ { \mathbf { 0 } }$ and $1 0 0 = 1 0 ^ { 2 }$ ;   
$\gg \bf { G f } \mathrm { = f r s p ( \bf { G } , \bf { w } ) }$ ; % computing frequency response;   
[u,s,v]=vsvd(Gf); % SVD at each frequency;

vplot(0 liv, lm0 , s), grid % plot both singular values and grid;   
pkvnorm(s) % find the norm from the frequency response of the singular values.

The singular values of $G ( j \omega )$ are plotted in Figure 4.4, which gives an estimate of $\| G \| _ { \infty } \approx 3 2 . 8 6 1$ . The state-space bisection algorithm described previously leads to $\| G \| _ { \infty } ^ { - } = 5 0 . 2 5 \pm 0 . 0 1$ and the corresponding Matlab command is

hinfnorm(G,0.0001) or linfnorm(G,0.0001) % relative error $\leq 0 . 0 0 0 1$ .

![](image/8d28bd9f6a784206ff724825fc827f8032efa27786563cbaa8eb569c2c8e2743.jpg)

<details>
<summary>line</summary>

| x | Solid Line | Dashed Line |
| --- | --- | --- |
| 10^0 | 1.0 | 0.1 |
| 10^1 | 50.0 | 0.5 |
| 10^2 | 0.1 | 0.05 |
</details>

Figure 4.4: The largest and the smallest singular values of $G ( j \omega )$

The preceding computational results show clearly that the graphical method can lead to a wrong answer for a lightly damped system if the frequency grid is not sufficiently dense. Indeed, we would get $\| G \| _ { \infty }$ ≈ 43.525, 48.286 and 49.737 from the graphical method if 400, 800, and 1600 frequency points are used, respectively.

Related MATLAB Commands: linfnorm, vnorm, getiv, scliv, var2con, xtract, xtracti
