Proof. Use of the definition of a convolution allows the left-hand side of (7.35) to be written as

$$(f * g ^ {*}) ^ {*} (t) = m (t) \int_ {- x} ^ {x} f (t - \tau) g ^ {*} (\tau) d \tau = \int_ {- x} ^ {x} m (t) f (t - \tau) m (\tau) g (\tau) d \tau$$

Similarly, the right-hand side of Eq. (7.36) can be written as

$$
\begin{array}{l} \left(f ^ {*} * g ^ {*}\right) (t) = \int_ {- x} ^ {x} m (t - \tau) f (t - \tau) m (\tau) g (\tau) d \tau \\ = \int_ {- x} ^ {x} m (t) f (t - \tau) m (\tau) g (\tau) d \tau \\ \end{array}
$$

The last equality holds because $m(\tau) \neq 0$ only for $\tau = nh$ and $m(t - nh) = m(t)$ .

Remark 1. The Laplace transformation of (7.35) gives

$$\left(F (s) G ^ {*} (s)\right) ^ {*} = F ^ {*} (s) G ^ {*} (s) \tag {7.37}$$

Remark 2. Notice that the multiplication by m outside the brace in (7.35) can be interpreted as introduction of a fictitious sampler.
