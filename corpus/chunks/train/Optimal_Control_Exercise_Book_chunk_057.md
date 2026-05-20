$$
\left\{ \begin{array}{l} x ^ {*} (t) = \frac {1}{1 + e ^ {2}} e ^ {t} + \frac {e ^ {2}}{1 + e ^ {2}} e ^ {- t} \\ p ^ {*} (t) = \frac {1}{1 + e ^ {2}} e ^ {t} - \frac {e ^ {2}}{1 + e ^ {2}} e ^ {- t} \\ u ^ {*} (t) = \frac {p ^ {*} (t)}{P} = \frac {1}{P (1 + e ^ {2})} e ^ {t} - \frac {e ^ {2}}{P (1 + e ^ {2})} e ^ {- t} \end{array} \right. \tag {207}
$$

where $t \in [ 0 , 1 ]$ . We will now discuss about the influence of the weighting value P on the control input.

1. Case $P  0 \mathrm { : }$ :

$$\lim _ {P \rightarrow \infty} u ^ {*} (t) = \lim _ {P \rightarrow \infty} \frac {1}{P \left(1 + e ^ {2}\right)} \left(e ^ {t} - e ^ {2} e ^ {- t}\right) = \dots \tag {208}\dots = \lim _ {P \rightarrow \infty} \frac {e ^ {t}}{P (1 + e ^ {2})} (1 - e ^ {2 (1 - t)}) = - \infty , \quad t \in [ 0, 1 ] \tag {209}$$

In this case, we can deduce that the weighting P going to zero makes the control input diverge: intuitively, the more the input is muffled, the larger the control input will be in its absolute value to obtain the optimal trajectory.

2. Case $P \to \infty :$

$$\lim _ {P \rightarrow \infty} u ^ {*} (t) = \lim _ {P \rightarrow \infty} \frac {1}{P \left(1 + e ^ {2}\right)} \left(e ^ {t} - e ^ {2} e ^ {- t}\right) = \dots \tag {210}\dots = \lim _ {P \to \infty} \frac {e ^ {t}}{P (1 + e ^ {2})} \left(1 - e ^ {2 (1 - t)}\right) = 0, \quad t \in [ 0, 1 ] \tag {211}$$

In this case, we can deduce that the weighting P going to infinity makes the control input go to zero: this means that, the more the input is amplified, the smaller the control input’s absolute value will be to obtain the optimal trajectory.
