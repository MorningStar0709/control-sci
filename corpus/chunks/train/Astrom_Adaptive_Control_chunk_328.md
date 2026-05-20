# Test for Positive Realness

It is useful to have an algorithm to test whether a function is positive real. Theorem 5.7 can be used for this purpose. Condition (i) is easily tested by an ordinary Routh-Hurwitz test. Condition (ii) is a straightforward calculation. To test condition (iii), we proceed as follows:

$$G (s) = \frac {B (s)}{A (s)}$$

then

$$\operatorname{Re} G (i \omega) = \operatorname{Re} \frac {B (i \omega)}{A (i \omega)} = \operatorname{Re} \frac {B (i \omega) A (- i \omega)}{A (i \omega) A (- i \omega)}$$

Since the denominator is nonnegative and $G(i\omega)$ is symmetric with respect to the real axis, it suffices to investigate whether the function

$$f (\omega) = \operatorname{Re} (B (i \omega) A (- i \omega))$$

is nonnegative for $\omega \geq 0$ . Notice that f is an even function of $\omega$ . It is thus sufficient to investigate whether $f(\omega)$ has any real zeros. This can be verified directly by solving the equation $f(\omega) = 0$ . There is also an indirect procedure. To describe this, introduce the polynomial

$$g (x) = f (\sqrt {x})$$

The problem is thus to find whether the polynomial $g(x)$ has any zeros on the interval $(0, \infty)$ . This classical problem can be solved as follows:

1. Let $g_1(x) = g(x)$ , $g_2(x) = g'(x)$ . Form a sequence of functions $\{g_1(x), g_2(x), \ldots, g_n(x)\}$ by letting $-g_{k+2}(x)$ be the remainder when dividing $g_k(x)$ by $g_{k+1}(x)$ . Proceed until $g_n$ is a constant.

2. Let $V(x)$ be the number of sign changes in the sequence $\{g_1(x), g_2(x), \ldots, g_n(x)\}$ .

3. The number of real zeros of the function $g(x)$ in the interval $[a, b]$ is then $V(a) - V(b)$ .

The function sequence $\{g_1(x), g_2(x), \ldots, g_n(x)\}$ is called a Sturm sequence. The procedure is illustrated by an example.
