Because the integrand is the magnitude squared of a vector, $\mathbf{x}_0^T M(T)\mathbf{x}_0 \geq 0$ . For the integral to be zero, the integrand must be zero everywhere, except possibly at isolated time points, in the interval 0 to $T$ . If that is so, there is at least one interval of nonzero duration over which $\|Ce^{At}\mathbf{x}_0\|^2 = 0$ . But $Ce^{At}\mathbf{x}_0$ is an analytic function (a sum of exponentials). If it is zero over a nonzero time interval, all its derivatives are zero at some interior point of the interval. By Taylor's theorem, $Ce^{At}\mathbf{x}_0$ must be zero for all $t$ . Therefore, $\mathbf{x}_0^T M(T)\mathbf{x}_0 = 0$ only if $Ce^{At}\mathbf{x}_0 = \mathbf{0}$ for all $t$ . Since $\mathbf{x}_0 \neq \mathbf{0}$ and since there are no unobservable states, that is not possible, so

$$\mathbf {x} _ {0} ^ {T} M (T) \mathbf {x} _ {0} > 0 \quad \text { for any } \quad \mathbf {x} _ {0} \neq \mathbf {0}.$$

This shows that $M(T)$ is positive definite and hence nonsingular. From Equation 3.37,

$$\mathbf {x} _ {0} = M ^ {- 1} (T) \int_ {0} ^ {T} \left(C e ^ {A t}\right) ^ {T} \mathbf {y} (t) d t \tag {3.38}$$

and $\mathbf{x}_0$ is uniquely determined, so the system is observable.
