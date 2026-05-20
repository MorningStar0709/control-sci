# 4.7 Particle Filtering

Theorem 4.35 (Resampling). Consider a sampled density $p ( x )$ with s samples at $x = x _ { i }$ and associated weights $w _ { i }$

$$p (x) = \sum_ {i = 1} ^ {s} w _ {i} \delta (x - x _ {i}) \quad w _ {i} \geq 0, \quad \sum_ {i = 1} ^ {s} w _ {i} = 1$$

Consider the resampling procedure that gives a resampled density

$$\tilde {p} (x) = \sum_ {i = 1} ^ {s} \tilde {w} _ {i} \delta (x - \tilde {x} _ {i})$$

in which the $\tilde { x } _ { i }$ are chosen according to resample probability $p _ { \mathrm { r e } }$

$$
p _ {\mathrm{re}} (\tilde {x} _ {i}) = \left\{ \begin{array}{l l} w _ {j} & \tilde {x} _ {i} = x _ {j} \\ 0 & \tilde {x} _ {i} \neq x _ {j} \end{array} \right.
$$

and with uniform weights $\tilde { \boldsymbol { w } } _ { i } = 1 / s$ . Consider a function $f ( \cdot )$ defined on a set X containing the points $x _ { i }$ .

With this resampling procedure, the expectation over resampling of any integral of the resampled density is equal to that same integral of the original density

$$\mathcal {E} _ {\mathrm{re}} \left(\int f (x) \tilde {p} (x) d x\right) = \int f (x) p (x) d x \quad a l l f$$

The proof of this theorem is discussed in Exercise 4.16. To get a feel for why this resampling procedure works, however, consider the case $s = 2$ . There are four possible outcomes of $\tilde { x } _ { 1 } , \tilde { x } _ { 2 }$ in resampling. Because of the resampling procedure, the random variables $\widetilde { \boldsymbol { x } } _ { i }$ and $\tilde { x } _ { j }$ , $j \neq i$ are independent, and their joint density is

$$
p _ {\mathrm{re}} (\widetilde {x} _ {1}, \widetilde {x} _ {2}) = \left\{ \begin{array}{l l} w _ {1} ^ {2} & \widetilde {x} _ {1} = x _ {1}, \widetilde {x} _ {2} = x _ {1} \\ w _ {1} w _ {2} & \widetilde {x} _ {1} = x _ {1}, \widetilde {x} _ {2} = x _ {2} \\ w _ {2} w _ {1} & \widetilde {x} _ {1} = x _ {2}, \widetilde {x} _ {2} = x _ {1} \\ w _ {2} ^ {2} & \widetilde {x} _ {1} = x _ {2}, \widetilde {x} _ {2} = x _ {2} \end{array} \right.
$$

The values of the integral of f for each of these four outcomes is

$$
\sum_ {i = 1} ^ {2} \widetilde {w} _ {i} f (\widetilde {x} _ {i}) = \left\{ \begin{array}{l l} \frac {1}{2} (f _ {1} + f _ {1}) & \widetilde {x} _ {1} = x _ {1}, \widetilde {x} _ {2} = x _ {1} \\ \frac {1}{2} (f _ {1} + f _ {2}) & \widetilde {x} _ {1} = x _ {1}, \widetilde {x} _ {2} = x _ {2} \\ \frac {1}{2} (f _ {2} + f _ {1}) & \widetilde {x} _ {1} = x _ {2}, \widetilde {x} _ {2} = x _ {1} \\ \frac {1}{2} (f _ {2} + f _ {2}) & \widetilde {x} _ {1} = x _ {2}, \widetilde {x} _ {2} = x _ {2} \end{array} \right.
$$
