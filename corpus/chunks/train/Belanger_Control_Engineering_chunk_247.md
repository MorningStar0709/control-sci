# 5.4 THE ROOT LOCUS METHOD

Example 5.3 is typical of a large class of problems in which one seeks to ascertain the effect of variations in a single parameter. The Routh criterion yields only a yes-no answer with respect to stability. It tells us what values of the parameter result in closed-loop stability, but has nothing to say about the behavior or the closed-loop poles in response to changes in the parameter. The Root Locus, originally developed by Evans [2], fills this gap.

As its name suggests, the Root Locus is the geometric locus traced out in the complex plane by the roots of the closed-loop characteristic equation as a specific parameter k varies from 0 to $\infty$ . The Root Locus methods described here are applicable when the characteristic polynomial is of the form $D(s) + kN(s)$ , where $D(s)$ and $N(s)$ are coprime polynomials. This is satisfied notably, in the case of the pure-gain controller $F(s) = k$ , as in Example 5.3, since the closed-loop characteristic polynomial is then $D_{P}(s) + kN_{P}(s)$ .

The characteristic equation is

$$D (s) + k N (s) = 0. \tag {5.7}$$

With $G(s) = N(s) / D(s)$ , this is also written as

$$1 + k G (s) = 0. \tag {5.8}$$

Note that, in the case of pure-gain control, $N(s) = N_{P}(s)$ , $D(s) = D_{P}(s)$ , and $G(s) = P(s)$ . As we shall see, there are cases in which the Root Locus parameter is not the control gain k, and therefore $G(s) \neq P(s)$ .

Let $G(s)$ be a proper transfer function of degree $n$ . Then the left-hand side (LHS) of Equation 5.7 is a polynomial of order $n$ which, for a given value of $k$ , has $n$ roots. Those roots are plotted as points in the complex plane. If that is done for each value of $k$ as $k$ varies continuously from 0 to infinity, the result is a locus with $n$ branches, corresponding to the $n$ roots. This is clarified in Example 5.4.

Example 5.4 Let $P(s) = (s + 1) / (s^2 + s + 1)$ . Plot the locus of roots of $1 + kP(s)$ as $k$ varies from 0 to $\infty$ .

Solution The roots satisfy

$$1 + k \frac {s + 1}{s ^ {2} + s + 1} = 0$$

or

$$s ^ {2} + s + 1 + k s + k = 0.$$

This is solved analytically; the roots $s^{*}(k)$ are

$$s ^ {*} (k) = - \frac {1}{2} (k + 1) \pm \frac {1}{2} \sqrt {k ^ {2} - 2 k - 3}.$$

The roots are complex when $k^2 - 2k - 3 < 0$ , which occurs if $-1 < k < 3$ ; they are real for other values of $k$ .

For k = 0,

$$s ^ {*} (0) = - \frac {1}{2} \pm j \frac {\sqrt {3}}{2}$$

which happen (not by coincidence!) to be the roots of the denominator of $P(s)$ . For $k = 3$ , there is a double root at
