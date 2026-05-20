# E.3.4 Laplace transform definition

The Laplace transform of a function f(t) is defined as

$$\mathcal {L} \{f (t) \} = F (s) = \int_ {0} ^ {\infty} f (t) e ^ {- s t} d t$$

We won’t be computing any Laplace transforms by hand using this formula (everyone in the real world looks these up in a table anyway). Common Laplace transforms (assuming zero initial conditions) are shown in table E.1. Of particular note are the Laplace transforms for the derivative, unit step,[5] and exponential decay. We can see that a derivative is equivalent to multiplying by s, and an integral is equivalent to multiplying by $\textstyle { \frac { 1 } { s } }$ .

<table><tr><td></td><td>Time domain</td><td>Laplace domain</td></tr><tr><td>Linearity</td><td> $af(t) + bg(t)$ </td><td> $aF(s) + bG(s)$ </td></tr><tr><td>Convolution</td><td> $(f*g)(t)$ </td><td> $F(s)G(s)$ </td></tr><tr><td>Derivative</td><td> $f'(t)$ </td><td> $sF(s)$ </td></tr><tr><td> $n^{th}$  derivative</td><td> $f^{(n)}(t)$ </td><td> $s^nF(s)$ </td></tr><tr><td>Unit step</td><td> $u(t)$ </td><td> $\frac{1}{s}$ </td></tr><tr><td>Ramp</td><td> $tu(t)$ </td><td> $\frac{1}{s^2}$ </td></tr><tr><td>Exponential decay</td><td> $e^{-\alpha t}u(t)$ </td><td> $\frac{1}{s+\alpha}$ </td></tr></table>

Table E.1: Common Laplace transforms and Laplace transform properties with zero initial conditions
