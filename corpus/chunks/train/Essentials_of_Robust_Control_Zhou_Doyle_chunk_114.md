| frequency (rad/sec) | The largest singular value | The smallest singular value |
| --- | --- | --- |
| 0.1 | ~1.0 | ~0.1 |
| 1.0 | ~10.0 | ~0.5 |
| 10.0 | ~0.01 | ~0.01 |
</details>

Figure 4.3: $\| G \| _ { \infty }$ is the peak of the largest singular value of $G ( j \omega )$

with

$$
A = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ - \frac {k _ {1}}{m _ {1}} & \frac {k _ {1}}{m _ {1}} & - \frac {b _ {1}}{m _ {1}} & \frac {b _ {1}}{m _ {1}} \\ \frac {k _ {1}}{m _ {2}} & - \frac {k _ {1} + k _ {2}}{m _ {2}} & \frac {b _ {1}}{m _ {2}} & - \frac {b _ {1} + b _ {2}}{m _ {2}} \end{array} \right], B = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ \frac {1}{m _ {1}} & 0 \\ 0 & \frac {1}{m _ {2}} \end{array} \right].
$$

Suppose that $G ( s )$ is the transfer matrix from $( F _ { 1 } , F _ { 2 } )$ to $( x _ { 1 } , x _ { 2 } )$ ; that is,

$$
C = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right], D = 0,
$$

and suppose $k _ { 1 } = 1 , k _ { 2 } = 4 , b _ { 1 } = 0 . 2 , b _ { 2 } = 0 . 1 , m _ { 1 } = 1$ , and $m _ { 2 } = 2$ with appropriate units. The following Matlab commands generate the singular value Bode plot of the above system as shown in Figure 4.3.

G=pck(A,B,C,D);   
hinfnorm(G,0.0001) or linfnorm(G,0.0001) % relative error $\leq 0 . 0 0 0 1$   
w=logspace(-1,1,200); % 200 points between $1 = 1 0 ^ { - 1 }$ and $1 0 = 1 0 ^ { 1 }$ ;   
$\scriptstyle \mathbf { G f } = \mathbf { f r s p } ( \mathbf { G } , \mathbf { w } )$ ; % computing frequency response;   
$[ \mathbf { u } , \mathbf { s } , \mathbf { v } ] { = } \mathbf { v s v d } ( \mathbf { G f } )$ ; % SVD at each frequency;

vplot(0 liv, lm0 , s), grid % plot both singular values and grid.

Then the $\mathcal { H } _ { \infty }$ norm of this transfer matrix is $\| G ( s ) \| _ { \infty } = 1 1 . 4 7$ , which is shown as the peak of the largest singular value Bode plot in Figure 4.3. Since the peak is achieved at $\omega _ { \mathrm { m a x } } = 0 . 8 4 8 3$ , exciting the system using the following sinusoidal input

$$
\left[ \begin{array}{l} F _ {1} \\ F _ {2} \end{array} \right] = \left[ \begin{array}{l} 0. 9 6 1 4 \sin (0. 8 4 8 3 t) \\ 0. 2 7 5 3 \sin (0. 8 4 8 3 t - 0. 1 2) \end{array} \right]
$$

gives the steady-state response of the system as

$$
\left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] = \left[ \begin{array}{l} 1 1. 4 7 \times 0. 9 6 1 4 \sin (0. 8 4 8 3 t - 1. 5 4 8 3) \\ 1 1. 4 7 \times 0. 2 7 5 3 \sin (0. 8 4 8 3 t - 1. 4 2 8 3) \end{array} \right].
$$
