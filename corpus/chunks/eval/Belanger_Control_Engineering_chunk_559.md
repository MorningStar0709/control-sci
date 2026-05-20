# 9.7.2 Discretization of Continuous-Time Controllers

It is natural to discretize a differential equation by replacing the derivative operation with a backward finite difference, i.e.,

$$
\begin{array}{l} \frac {d}{d t} y (t) = \frac {y (t) - y (t - T _ {s})}{T _ {s}} \\ = \frac {\widehat {y} (k) - \widehat {y} (k - 1)}{T _ {s}}. \tag {9.34} \\ \end{array}
$$

In the transform variables, this is equivalent to replacement of $s$ with $(1 - z^{-1}) / T_s$ or, solving for $z$ , replacement of $z$ with $1 / (1 - T_s s)$ .

The controller is designed by replacing s with $(z-1)/zT_{s}$ in the transfer function $F_{c}(s)$ . Recall from the preceding section that we need to satisfy $F(e^{sT_{s}}) \approx F_{c}(s)$ for $s = j\omega$ over as much of the range 0 to $\pi/T_{s}$ as possible. In this case,

$$F (z) = F _ {c} \left(\frac {z - 1}{z T _ {s}}\right) = F _ {c} \left(\frac {1 - z ^ {- 1}}{T _ {s}}\right)$$

and

$$F (e ^ {s T _ {s}}) = F _ {c} \left(\frac {1 - e ^ {- s T _ {s}}}{T _ {s}}\right). \tag {9.35}$$

Now,

$$
\begin{array}{l} \frac {1 - e ^ {- s T _ {s}}}{T _ {s}} = \frac {1 - 1 + s T _ {s} - \frac {1}{2} (s T _ {s}) ^ {2} + \cdots}{T _ {s}} \\ = s \left(1 - \frac {1}{2} s T _ {s} + \frac {1}{3 !} s ^ {2} T _ {s} - \dots\right). \tag {9.36} \\ \end{array}
$$

The condition $F(e^{j\omega T_{s}}) \approx F_{c}(j\omega)$ is satisfied at low frequencies, i.e., for $\frac{1}{2}\omega T_{s} \ll 1$ . Since the approximation must hold up to frequencies where the magnitude of the loop gain is small, we require that $\omega_{c}T_{s} \ll 2$ , in line with the conclusion already expressed in Equation 9.33.

The Tustin approximation consists in replacing $s$ with $(2 / T_s)[(z - 1) / (z + 1)]$ ; i.e.,

$$F (z) = F _ {c} \left(\frac {2}{T _ {s}} \frac {z - 1}{z + 1}\right)$$

and

$$F (e ^ {s T _ {s}}) = F _ {c} \left(\frac {2}{T _ {s}} \frac {e ^ {s T _ {s}} - 1}{e ^ {s T _ {s}} + 1}\right). \tag {9.37}$$

Now,

$$\frac {2}{T _ {s}} \frac {e ^ {s T _ {s}} - 1}{e ^ {s T _ {s}} + 1} = \frac {2}{T _ {s}} \frac {- 1 + 1 + s T _ {s} + \frac {1}{2} (s T _ {s}) ^ {2} + \cdots}{2 + s T _ {s} + \frac {1}{2} (s T _ {s}) ^ {2} + \cdots}.$$

By long division, the leading terms of the series are

$$
\begin{array}{l} \frac {2}{T _ {s}} \frac {e ^ {s T _ {s}} - 1}{e ^ {s T _ {s}} + 1} = \frac {2}{T _ {s}} \frac {1}{2} s T _ {s} - \frac {1}{8} (s T _ {s}) ^ {3} \\ = s \left(1 - \frac {1}{4} s ^ {2} T _ {s} ^ {2}\right). \tag {9.38} \\ \end{array}
$$
