# Example 9.8

In Figure 9.9, the plant is $P(s) = 1 / [(s + 1)(s + 2)]$ . Calculate the discrete-time transfer function of the sampled-data plant.

Solution The step response is the inverse transform of

$$\frac {1}{s (s + 1) (s + 2)} = \frac {1 / 2}{s} - \frac {1}{s + 1} + \frac {1 / 2}{s + 2}$$

which is

$$y _ {\text { step }} (t) = \frac {1}{2} - e ^ {- t} + \frac {1}{2} e ^ {- 2 t}.$$

Sampling with period $T_{s}$ yields

$$\widehat {y} _ {\text { step }} (k) = \frac {1}{2} - (e ^ {- T _ {s}}) ^ {k} + \frac {1}{2} (e ^ {- 2 T _ {s}}) ^ {k}$$

whose $z$ -transform is

$$
\begin{array}{l} \widehat {y} _ {\text { step }} (z) = \frac {(1 / 2) z}{z - 1} - \frac {z}{z - e ^ {- T _ {s}}} + \frac {(1 / 2) z}{z - e ^ {- 2 T _ {s}}} \\ = \frac {z \left[ \left(1 / 2 - e ^ {- T _ {s}} + \frac {1}{2} e ^ {- 2 T _ {s}}\right) z + \frac {1}{2} e ^ {- T _ {s}} - e ^ {- 2 T _ {s}} + \frac {1}{2} e ^ {- 3 T _ {s}} \right]}{(z - 1) (z - e ^ {- T _ {s}}) (z - e ^ {- 2 T _ {s}})}. \\ \end{array}
$$

Dividing by $z / (z - 1)$ yields the discrete transfer function

$$P (z) = \frac {(1 / 2 - e ^ {- T _ {s}} + \frac {1}{2} e ^ {- 2 T _ {s}}) z + \frac {1}{2} e ^ {- T _ {s}} - e ^ {- 2 T _ {s}} + \frac {1}{2} e ^ {- 3 T _ {s}}}{(z - e ^ {- T _ {s}}) (z - e ^ {- 2 T _ {s}})}.$$
