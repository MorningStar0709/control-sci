$${\frac {d}{d s}} \left({\frac {1}{s + 1}}\right) = - {\frac {1}{(s + 1) ^ {2}}}$$

Points in the s plane at which the function $G ( s )$ is analytic are called ordinary points, while points in the s plane at which the function $G ( s )$ is not analytic are called singular points. Singular points at which the function $G ( s )$ or its derivatives approach infinity are called poles. Singular points at which the function $G ( s )$ equals zero are called zeros.

If $G ( s )$ approaches infinity as s approaches $- p$ and if the function

$$G (s) (s + p) ^ {n}, \quad \text { for } n = 1, 2, 3, \dots$$

has a finite, nonzero value at $s = - p ,$ , then $s = - p$ is called a pole of order n. If $n = 1$ , the pole is called a simple pole. If $n = 2 , 3 , \ldots$ , the pole is called a second-order pole, a third-order pole, and so on.

To illustrate, consider the complex function

$$G (s) = \frac {K (s + 2) (s + 1 0)}{s (s + 1) (s + 5) (s + 1 5) ^ {2}}$$

$G ( s )$ has zeros at $s = - 2 , s = - 1 0$ , simple poles at $s = 0 , s = - 1 , s = - 5$ , and a double pole (multiple pole of order 2) at s=–15. Note that $G ( s )$ becomes zero at $s = \infty .$ . Since for large values of s

$$G (s) \doteq \frac {K}{s ^ {3}}$$

$G ( s )$ possesses a triple zero (multiple zero of order 3) at $s = \infty .$ . If points at infinity are included, $G ( s )$ has the same number of poles as zeros.To summarize, $G ( s )$ has five zeros $( s = - 2 , s = - 1 0 , s = \infty , s = \infty , s = \infty )$ and five poles $( s = 0 , s = - 1 , s = - 5$ , $s = - 1 5 , s = - 1 5 )$ .

Laplace Transformation. Let us define

$$
f (t) = \text { a function of time } t \text { such that } f (t) = 0 \text { for } t < 0s = \text { a complex variable }
\begin{array}{l} \mathcal {L} = \text { an   operational   symbol   indicating   that   the   quantity   that   it   prefixes   is   to } \\ \text { be   transformed   by   the   Laplace   integral   } \int_ {0} ^ {\infty} e ^ {- s t} d t \end{array}
F (s) = \text { Laplace transform of } f (t)
$$

Then the Laplace transform of $f ( t )$ is given by

$$\mathscr {L} [ f (t) ] = F (s) = \int_ {0} ^ {\infty} e ^ {- s t} d t [ f (t) ] = \int_ {0} ^ {\infty} f (t) e ^ {- s t} d t$$

The reverse process of finding the time function $f ( t )$ from the Laplace transform $F ( s )$ is called the inverse Laplace transformation.The notation for the inverse Laplace transformation is $\mathcal { L } ^ { - 1 }$ , and the inverse Laplace transform can be found from $F ( s )$ by the following inversion integral:

$$\mathscr {L} ^ {- 1} [ F (s) ] = f (t) = \frac {1}{2 \pi j} \int_ {c - j \infty} ^ {c + j \infty} F (s) e ^ {s t} d s, \quad \text { for } t > 0$$
