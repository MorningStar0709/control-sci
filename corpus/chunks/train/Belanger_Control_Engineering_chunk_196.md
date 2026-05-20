# 4.3.4 Effect of RHP Zeros on Frequency Response

The presence of RHP zeros in the plant transfer function cuts down on our freedom to assign a transfer function and limits our choices to those that have the same RHP zeros. The impact of this on performance—particularly on frequency response—is now made explicit.

now made explicit. Rather than work with $H_{d}$ , it proves easier to work with $W(s) = 1 - H_{d}$ , the set-point to error-transfer function. With

$$e = y _ {d} - y= y _ {d} - H _ {d} y _ {d} \tag {4.20}$$

we have

$$\frac {e}{y _ {d}} = 1 - H _ {d} (s) = W (s). \tag {4.21}$$

Clearly, making $|W(j\omega)|$ small is the same as requiring $H_{d}(j\omega) \approx 1$ . The technical advantage of working with $W$ rather than with $H_{d}$ is that we need not worry about its phase, as long as its magnitude is small. Note that the poles of $W(s)$ are the same as those of $H_{d}(s)$ , so that $W(s)$ is a stable transfer function. We shall also assume that $W(s)$ is proper and has no zeros in the open RHP. The following is derived from the theory of complex variables [3].

Let $W(s)$ be proper, analytic, and nonzero in the open RHP. Then, at each RHP point $z_0 = x_0 + jy_0$ , $x_0 > 0$ ,

$$\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \log | W (j \omega) | \frac {x _ {0}}{x _ {0} ^ {2} + (y _ {0} - \omega) ^ {2}} d \omega = \log | W (z _ {0}) |. \tag {4.22}$$

Now, suppose $H_{d}(s)$ has an RHP zero at $s = z_0$ . Then, by Equation 4.20,

$$W (z _ {0}) = 1 - H _ {d} (z _ {0}) = 1. \tag {4.23}$$

From Equation 4.22,

$$\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \log | W (j \omega) | f (z _ {0}, \omega) d \omega = \log 1 = 0 \tag {4.24}$$

where $f(z_0, \omega) = x_0 / [x_0^2 + (y_0 - \omega)^2]$ .

Figure 4.12 illustrates the weighting function $f(z_0, \omega)$ . It is positive for all $\omega$ and has its maximum at $\omega = y_0$ . The peak is high and narrow if $x_0$ is small (the RHP zero is close to the $j$ -axis), and low and broad if $x_0$ is large (an RHP zero is farther from the $j$ -axis).
