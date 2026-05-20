# Moving-Average Controller

The minimum-variance controller leads to a closed-loop system in which the output is a moving average of order $d_{0} - 1$ (see Eq. (4.15)). It is possible to design controllers such that the output is a moving average of higher order.

Instead of placing $d_0 - 1$ closed-loop poles at the origin, we may place $d - 1$ poles, where $d \geq d_0$ .

The moving-average controller can be derived as follows. Factor the B polynomial as

$$B (q) = B ^ {+} (q) B ^ {-} (q)$$

where $B^{+}$ corresponds to well-damped zeros. To obtain a unique factorization, it is assumed that $B^{-}$ is monic. Determine R and S from

$$q ^ {d - 1} B ^ {+} C = A R + B S \tag {4.18}$$

It follows that $B^{+}$ must be a factor of $R$ , that is, $R = R_{1}B^{+}$ . With the feedback law

$$u (t) = - \frac {S}{R} y (t)$$

we get

$$A y (t) = B \left(- \frac {S}{R}\right) y (t) + C e (t)$$

or

$$
\begin{array}{l} y (t) = \frac {C R}{A R + B S} e (t) = \frac {C B ^ {+} R _ {1}}{q ^ {d - 1} B ^ {+} C} e (t) \\ = \frac {R _ {1}}{q ^ {d - 1}} e (t) = \left(\mathbf {1} + r _ {1} q ^ {- 1} + \dots + r _ {d - 1} q ^ {- d + 1}\right) e (t) \\ \end{array}
$$

where $\deg R_1 = d - 1$ with

$$d = \deg A - \deg B ^ {+}$$

Since the controlled output is a moving-average process of order d-1, we call the strategy moving-average (MA) control. Notice that no zeros are canceled if

$$\boldsymbol {B} ^ {+} = 1$$

which means that

$$d = \deg A = n$$

The minimum-variance controller and the moving-average controller are similar. The only difference is the value of the integer d, which controls the number of process zeros that are canceled. With $d = d_{0}$ , all process zeros are canceled; with $d = \deg A = n$ , no process zeros are canceled.
