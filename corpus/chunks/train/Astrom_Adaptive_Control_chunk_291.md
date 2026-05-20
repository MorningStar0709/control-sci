# THEOREM 5.2 Lyapunov functions for linear systems

Assume that the linear system

$$\frac {d x}{d t} = A x \tag {5.22}$$

is asymptotically stable. Then for each symmetric positive definite matrix $Q$ there exists a unique symmetric positive definite matrix $P$ such that

$$\boldsymbol {A} ^ {T} \boldsymbol {P} + \boldsymbol {P A} = - \boldsymbol {Q} \tag {5.23}$$

Furthermore, the function

$$V (x) = x ^ {T} P x \tag {5.24}$$

is a Lyapunov function for Eq. (5.22).

Proof: Let $Q$ be a symmetric positive definite matrix. Define

$$P (t) = \int_ {0} ^ {t} e ^ {A ^ {T} (t - s)} Q e ^ {A (t - s)} d s$$

The matrix P is symmetric and positive definite because an integral of positive definite matrices is positive definite. The matrix P also satisfies

$$\frac {d P}{d t} = A ^ {T} P + P A + Q$$

Since the matrix $A$ is stable, the limit

$$P _ {o} = \lim _ {t \rightarrow \infty} P (t)$$

exists. This matrix satisfies Eq. (5.23). It can also be shown that the solution to Eq. (5.23) is unique, which completes the argument.

For a stable linear system we can thus always find a quadratic Lyapunov function. To use Theorem 5.2 to construct a Lyapunov function, we simply choose a positive matrix Q and solve the linear equation (5.23) for P. The following example shows how it can be done.
