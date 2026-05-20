# 1.3 Laplace Transform Review

We will extensively use Laplace Transforms to manipulate the dierential equations of control systems. As a review, the Laplace transform is

$$\mathcal {L} \{f (t) \} = F (s) = \int_ {0} ^ {\infty} e ^ {- s t} f (t) d t$$

where s is a complex variable, $s = \sigma + j \omega$ . Technically this is the one sided Laplace Transform because the integral extends only to positive t. The inverse of the Laplace Transform is

$$f (t) = \mathcal {L} ^ {- 1} F (s) = \frac {1}{2 \pi j} \lim _ {T \to \infty} \int_ {\sigma - j T} ^ {\sigma + j T} F (s) e ^ {s t} d s$$

For this course, we will not need to evaluate these integrals, because all of the LODEs we study will result in just a few terms which have been worked out long ago and are widely available in tables (Table 1.1).

When using this table we need to keep in mind a few limitations and assumptions:

 We are only considering $t > 0$ . One way to do this is to consider functions to be multiplied by the Unit Step function, u(t)

$$
u (t) = \left\{ \begin{array}{l l} 0 & t <   0 \\ 1 & t > 0 \end{array} \right.
$$

 When using the dierentiation relationship (last two lines of Table 1.1) we must be careful about the initial conditions $( f ( 0 ) , { \dot { f } } ( 0 ) )$ . Most often, we assume that all initial conditions are zero, but it is your responsibility to verify that this assumption applies to a given problem.

<table><tr><td> $f(t)$  for  $t \geq 0$ </td><td> $\mathcal{L}(f)$ </td></tr><tr><td> $1u(t)$ </td><td> $\frac{1}{s}$ </td></tr><tr><td> $e^{at}$ </td><td> $\frac{1}{s - a}$ </td></tr><tr><td> $t^n$ </td><td> $\frac{n!}{s^{n+1}} (n = 0,1,\ldots)$ </td></tr><tr><td> $\sin at$ </td><td> $\frac{a}{s^2 + a^2}$ </td></tr><tr><td> $\cos at$ </td><td> $\frac{s}{s^2 + a^2}$ </td></tr><tr><td> $\dot{f}(t)$ </td><td> $s\mathcal{L}(f) - f(0)$ </td></tr><tr><td> $\ddot{f}(t)$ </td><td> $s^2\mathcal{L}(f) - sf(0) - \dot{f}(0)$ </td></tr></table>

(Where

$$u (t) = 0, t \leq 0= 1, t > 0\dot {f} (t) = \frac {d f (t)}{d t}\ddot {f} (t) = \frac {d ^ {2} f (t)}{d t ^ {2}}$$

)

Table 1.1: Table of some commonly used Laplace Transform pairs.
