2.10 Figure 2.12 shows a system of two tanks, where the input signal is the flow to the first tank and the output is the level in the second tank. Use of the levels as state variables gives the system

$$
\frac {d x}{d t} = \left( \begin{array}{c c} - 0. 0 1 9 7 & 0 \\ 0. 0 1 7 8 & - 0. 0 1 2 9 \end{array} \right) x + \binom{0. 0 2 6 3}{0} u

y = \left( \begin{array}{c c} 0 & 1 \end{array} \right) x
$$

(a) Sample the system with the sampling period $h = 12$ .

(h) Verify that the pulse-transfer operator for the system is

$$H _ {0} (q) = \frac {0 . 0 3 0 q + 0 . 0 2 6}{q ^ {2} - 1 . 6 5 q + 0 . 6 8}$$

2.11 The normalized motor is described in Example A.2. Show that the sampled system is described by (A.6). Determine the following:

(a) The pulse-transfer function.

(b) The pulse response.

(c) A difference equation relating the input and the output.

(d) The variation of the poles and zeros of the pulse-transfer function with the sampling period.

![](image/80d5f7519ad2fb6bca9ce1b8aa94fd1de0941c3aa96b6aa3ae3ba97eef746c94.jpg)

<details>
<summary>text_image</summary>

u
x₁
x₂
</details>

Figure 2.12 The two-tank process.

2.12 A continuous-time system with the transfer function

$$G (s) = \frac {1}{s} e ^ {- s t}$$

is sampled with h = 1 when τ = 0.5.

(a) Determine a state-space representation of the sampled system. What is the order of the sampled system?   
(h) Determine the pulse-transfer function and the pulse response of the sampled system.   
(c) Determine the poles and zeros of the sampled system.

2.13 Solve Problem 2.12 with

$$G (s) = \frac {1}{s + 1} e ^ {- s t}$$

and $h = 1$ and $\tau = 1.5$ .

2.14 Consider the sampled system

$$y (k + 1) = a y (k) + b _ {3} u (k - 3) + b _ {4} u (k - 4)$$

where the sampling interval is 1 s. Show that the system may be obtained by sampling the system

$$\frac {d y (t)}{d t} = - \alpha y (t) + b u (t - \tau)$$

where

$$\tau = 3 - \frac {1}{\ln \alpha} \ln \frac {a b _ {3} + b _ {4}}{a (b _ {3} + b _ {4})}$$

2.15 Consider the system

$$y (k) - 0. 5 y (k - 1) = u (k - 9) + 0. 2 u (k - 1 0)$$

Determine the polynomials $A(q), B(q), A^{*}(q^{-1})$ , and $B^{*}(q^{-1})$ in the representations

$$A (q) y (k) = B (q) u (k)$$

and

$$A ^ {*} (q ^ {- 1}) y (k) = B ^ {*} (q ^ {- 1}) u (k - d)$$

What are d and the order of the system?

2.16 A filter with the pulse-transfer operator

$$\boldsymbol {H} ^ {*} (q ^ {- 1}) = b _ {0} + b _ {1} q ^ {- 1} + \dots + b _ {n} q ^ {- n}$$

is called a finite impulse-response (FIR) filter.
