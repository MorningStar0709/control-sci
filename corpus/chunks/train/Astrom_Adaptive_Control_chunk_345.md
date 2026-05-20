$$u = - P _ {1} \left(\varphi^ {T} \theta^ {0}\right) = - P _ {1} \left(\left(\theta^ {0}\right) ^ {T} \varphi\right) = - \left(\theta^ {0}\right) ^ {T} \left(P _ {1} \varphi\right) \tag {5.74}$$

where $P_{1}$ is a polynomial in the differential operator. Let $\theta$ denote the adjustable controller parameters. The feedback law

$$u = - P _ {1} (\varphi^ {T} \theta)$$

would give the desired error model. However, this control law is not realizable if $P_{1}$ has a degree greater than 1 because the term $P_{1}(\varphi^{T}\theta)$ contains derivatives of the parameters. However, the control law

$$u = - \theta^ {T} (P _ {1} \varphi) \tag {5.75}$$

is realizable because of Eq. (5.69). If we use this control law, it follows from Eq. (5.70) that the filtered error can be written as

$$
\begin{array}{l} e _ {f} = \frac {b _ {0} Q}{A _ {o} A _ {m}} \left(\varphi^ {T} \theta^ {0} - \frac {1}{P _ {1}} \theta^ {T} \left(P _ {1} \varphi\right)\right) \\ = \frac {b _ {0} Q}{A _ {o} A _ {m}} \left(\varphi^ {T} \theta^ {0} - \varphi^ {T} \theta - \frac {1}{P _ {1}} \theta^ {T} \left(P _ {1} \varphi\right) + \varphi^ {T} \theta\right) \\ \end{array}
$$

Introduce the signals $\eta$ and $\varepsilon$ , defined by

$$\eta = \frac {1}{P _ {1}} \theta^ {T} \left(P _ {1} \varphi\right) - \varphi^ {T} \theta = - \left(\frac {1}{P _ {1}} u + \varphi^ {T} \theta\right) \tag {5.76}\varepsilon = e _ {f} + \frac {b _ {0} Q}{A _ {o} A _ {m}} \eta = \frac {b _ {0} Q}{A _ {o} A _ {m}} \varphi^ {T} (\theta^ {0} - \theta)$$

The signal $\varepsilon$ is called the augmented error, and $\eta$ is called the error augmentation. The augmented error is computed as follows:

$$\varepsilon = \frac {Q}{P} (y - y _ {m}) + \frac {b _ {0} Q}{A _ {o} A _ {m}} \eta \tag {5.77}$$
