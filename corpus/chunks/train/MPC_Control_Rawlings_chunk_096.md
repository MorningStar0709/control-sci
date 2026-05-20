in which $V _ { T - N } ^ { - } ( \cdot )$ is the arrival cost at time T − N. Comparing these two objective functions, it is clear that the simplest form of MHE is equivalent to setting up a full least squares problem, but then setting the arrival cost function $V _ { T - N } ^ { - } ( \cdot )$ to zero.

MHE in terms of conditional density. Because we have established the close connection between least squares and conditional density in (1.32), we can write the full least squares problem also as an equivalent conditional density maximization

$$\max _ {x (T)} p _ {x (T) | \mathbf {y} _ {N} (T)} (x (T) | \mathbf {y} _ {N} (T))$$

with prior density

$$p _ {x (T - N) | \mathbf {y} (T - N - 1)} (x | \mathbf {y} (T - N - 1)) = c \exp (- V _ {T - N} ^ {-} (x)) \tag {1.35}$$

in which the constant c can be found from (1.20) if desired, but its value does not change the solution to the optimization. We can see from (1.35) that setting $V _ { T - N } ^ { - } ( \cdot )$ to zero in the simplest form of MHE is equivalent to giving infinite variance to the conditional density of $x ( T - N ) | \mathbf { y } ( T - N - 1 )$ . This means we are using a noninformative prior for the state $x ( T - N )$ and completely discounting the previous measurements $\mathbf { y } ( T - N - 1 )$ .

To provide a more flexible MHE problem, we therefore introduce a penalty on the first state to account for the neglected data $\mathbf { y } ( T - N - 1 )$

$$
\begin{array}{l} \hat {V} _ {T} (\mathbf {x} _ {N} (T)) = \Gamma_ {T - N} (x (T - N)) + \\ \frac {1}{2} \left(\sum_ {k = T - N} ^ {T - 1} | x (k + 1) - A x (k) | _ {Q ^ {- 1}} ^ {2} + \sum_ {k = T - N} ^ {T} | y (k) - C x (k) | _ {R ^ {- 1}} ^ {2}\right) \\ \end{array}
$$

For the linear Gaussian case, we can account for the neglected data exactly with no approximation by setting Γ equal to the arrival cost, or, equivalently, the negative logarithm of the conditional density of the state given the prior measurements. Indeed, there is no need to use

MHE for the linear Gaussian problem at all because we can solve the full problem recursively. When addressing nonlinear and constrained problems in Chapter 4, however, we must approximate the conditional density of the state given the prior measurements in MHE to obtain a computationally tractable and high-quality estimator.
