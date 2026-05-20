we see that the common complex functions $U ( j \omega )$ and $Y ( j \omega )$ can be factored out of all of the right- and left-hand-side terms. Consequently, the I/O equation (9.6) becomes

$$\left(a _ {3} (j \omega) ^ {3} + a _ {2} (j \omega) ^ {2} + a _ {1} j \omega + a _ {0}\right) Y (j \omega) e ^ {j \omega t} = \left(b _ {1} j \omega + b _ {0}\right) U (j \omega) e ^ {j \omega t}$$

Finally, forming the ratio of output/input yields

$$\frac {Y (j \omega)}{U (j \omega)} = \frac {b _ {1} j \omega + b _ {0}}{a _ {3} (j \omega) ^ {3} + a _ {2} (j \omega) ^ {2} + a _ {1} j \omega + a _ {0}} = G (j \omega) \tag {9.9}$$

The complex function $G ( j \omega )$ is the sinusoidal transfer function. Note that the transfer function of the thirdorder I/O system (9.6) is

$$G (s) = \frac {Y (s)}{U (s)} = \frac {b _ {1} s + b _ {0}}{a _ {3} s ^ {3} + a _ {2} s ^ {2} + a _ {1} s + a _ {0}} \tag {9.10}$$

Comparing Eqs. (9.9) and (9.10) we see that the sinusoidal transfer function $G ( j \omega )$ is simply the transfer function $G ( s )$ with s replaced by j??, or $s = j \omega$ . Figure 9.3 shows the frequency response in a block diagram format where the steady-state output sinusoid is

$$y (t) = G (j \omega) U (j \omega) e ^ {j \omega t} \tag {9.11}$$

In general, $G ( j \omega ) , \ : U ( j \omega )$ , and $e ^ { j \omega t }$ are complex functions of the input frequency ??. Although we have not yet derived a simple expression for the frequency response, Eq. (9.11) shows that it depends on the sinusoidal transfer function $G ( j \omega )$ .
