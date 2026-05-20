The stability of the closed-loop system can be investigated from the Nyquist plot of $H(z)$ . For discrete-time systems, the stability area in the $z$ -plane is the unit disc instead of the left half-plane. Figure 3.6 shows the path $\Gamma_c$ encircling the area outside the unit disc. The small indentation at $z = 1$ is to exclude the integrators in the open-loop system. The mapping of the infinitesimal semicircle at $z = 1$ with decreasing arguments from $\pi/2$ to $-\pi/2$ is mapped into the $H(z)$ -plane as an infinitely large circle from $-n\pi/2$ to $n\pi/2$ , where $n$ is the number of integrators in the open-loop system. If there are poles on the unit circle other than for $z = 1$ , those have to be excluded with small semicircles in the same way as for $z = 1$ . The map of the unit circle is $H(e^{i\omega h})$ for $\omega h \in (0,2\pi)$ .

The stability of the closed-loop system now can be determined by investigating how the path $\Gamma_{c}$ is mapped by $H(z)$ . The principle of arguments states that the number of encirclements N in the positive direction around $(-1,0)$ by the map of $\Gamma_{c}$ is equal to

$$N = Z - P$$

where Z and P are the number of zeros and poles, respectively, of $1 + H(z)$ outside the unit disc. Notice that if the open-loop system is stable, then P = 0 and thus $N = Z$ . The stability of the closed-loop system is then ensured if the map of $\Gamma_c$ does not encircle the point $(-1,0)$ . If $H_{cl}(z) \to 0$ when $z \to \infty$ , the parallel lines III and V do not influence the stability test, and it is sufficient to find the map of the unit circle and the small semicircle at $z = 1$ . The Nyquist criterion can be simplified further if the open-loop system and its inverse are stable. Stability of the closed-loop system is then ensured if the point $(-1,0)$ in the $H(z)$ -plane is to the left of the map of $H(e^{i\omega h})$ for $\omega h = 0$ to $\pi$ —that is, to the left of the Nyquist curve.

![](image/5d448587c6efc6cfa33910ab61626925275b71950a4993059fd6fa9eb36071de.jpg)

<details>
<summary>text_image</summary>

Im
IV
Γc
I
1
II
III
VI
V
Re
R→∞
VII
</details>

Figure 3.6 The path $\Gamma_{c}$ encircling the area outside the unit disc.

![](image/a9e20ed95a55e27693acb11b12edd2376c1e9461d351e2786efbfd187d0e3e41.jpg)

<details>
<summary>text_image</summary>

Im
1
VI
VII
V
-1
IV
III
Re
I
II
</details>

Figure 3.7 The map of $\Gamma_{c}$ into the $H(z)$ -plane of the system in Example 3.4, when $K = 1$ . The solid line is the Nyquist curve.
