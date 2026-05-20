# Two Basic Theorems

To develop an algebra that allows formal manipulation of the systems, two theorems are needed. The first theorem tells how the z-transform of a continuous-time function is related to its Laplace transform.

THEOREM 7.2 Let the function $f$ have the Laplace transform $F$ and the $z$ -transform $\bar{F}$ , and let $F^*$ be the Laplace transform of the sampled representation $f^*$ of $f$ . Assume that for some $\varepsilon > 0, |F(s)| \leq |s|^{-1 - \varepsilon}$ for large $|s|$ then

$$F ^ {*} (s) = \bar {F} \left(e ^ {s h}\right) = \frac {1}{h} \sum_ {k = - \infty} ^ {\infty} F (s + i k \omega_ {s}) \tag {7.33}$$

where $\omega_{s} = 2\pi / h$ is the sampling frequency.

Proof. The definition of $F^{*}$ gives

$$
\begin{array}{l} F ^ {*} (s) = \int_ {0} ^ {\infty} e ^ {- s t} f ^ {*} (t) d t \\ = \int_ {0} ^ {\infty} e ^ {- s t} f (t) m (t) d t \\ = \int_ {0} ^ {\infty} e ^ {- a t} f (t) \left(\sum_ {k = - \infty} ^ {\infty} \delta (t - k h)\right) d t \\ \end{array}
$$

where the last equality is obtained from (7.26). Interchange the order of integration and summation gives

$$F ^ {*} (s) = \sum_ {- \infty} ^ {\infty} \int_ {0} ^ {\infty} e ^ {- s t} f (t) \delta (t - k h) d t= \sum_ {k = 0} ^ {\infty} \left(e ^ {s h}\right) ^ {- k} f (k h)= \tilde {F} (e ^ {s h})$$

The last equality follows from (7.32).

Because the Laplace transform of a product of two functions is a convolution of their transforms, it follows that

$$
\begin{array}{l} F ^ {*} (s) = F (s) * M (s) = \frac {1}{2 \pi i} \int_ {\gamma - i \infty} ^ {\gamma + i \infty} F (\nu) M (s - \nu) d \nu \tag {7.34} \\ = \frac {1}{2 \pi i} \int_ {\gamma - i \infty} ^ {\gamma + i \infty} F (v) \frac {1}{1 - e ^ {- h (s - v)}} d v \\ \end{array}
$$

The integration path should be to the right of all poles of $F$ and to the left of all poles of $M$ (see Fig. 7.28). If $F$ goes to zero faster than $|s|^{-1 - \varepsilon}$ as $|s| \to \infty$ , the integral of FM on a large semicircle will vanish. Upon completion of the integration path by a large semicircle to the right, the integral can be evaluated with residue calculus. In the domain enclosed by the contour the integrand has simple poles at the zeros of

![](image/f6783807d715fb95ae551e545a21ed8e6cc5a7731514b50f959c8afc71aa2993.jpg)

<details>
<summary>text_image</summary>

Poles of F
Im
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
⑧
</details>

Figure 7.28 Singularities of F and M and the integration contour Γ.

$$e ^ {h (s - \nu)} = 1$$

that is, at
