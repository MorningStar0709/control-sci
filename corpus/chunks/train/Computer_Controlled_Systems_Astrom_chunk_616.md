where $\ell$ is an arbitrary linear operator that is not identically zero. This means that completely deterministic random processes can be predicted exactly with linear predictors for almost all $\omega$ . (Almost all $\omega$ means all $\omega$ except for possibly a set of points with zero measure.)

![](image/32422e0bbf2bfa4e555688f6df53048c51da49ea30cd88dc894cd8dfacdf8493.jpg)

<details>
<summary>line</summary>

| t | x(·, ω₁) | x(·, ω₂) | x(·, ω₃) | x(·, ω₄) |
| --- | --- | --- | --- | --- |
| 0 | ~0 | ~0 | ~0 | ~0 |
| t₁ | ~0 | ~0 | ~0 | ~0 |
</details>

Figure 10.3 A stochastic process and a finite-dimensional distribution function.

The completely deterministic random processes are closely related to the classical disturbance signals discussed in Sec. 3.5. These signals will be completely deterministic random processes if the initial conditions to the dynamic systems are chosen as random processes. The completely deterministic processes are normally excluded because they are too regular to be of interest.

Concepts. Some important concepts for random processes will now be given. The values of a random process at n distinct times are n-dimensional random variables. The function

$$F (\xi_ {1}, \dots , \xi_ {n}; t _ {1}, \dots , t _ {n}) = P \{x (t _ {1}) \leq \xi_ {1}, \dots , x (t _ {n}) \leq \xi_ {n} \}$$

where P denotes probabilities, is called the finite-dimensional distribution function of the random process. An illustration is given in Fig. 10.3. A random process is called Gaussian, or normal, if all finite-dimensional distributions are normal. The mean-value function of a random process x is defined by

$$m (t) = \operatorname{Ex} (t) = \int_ {- \infty} ^ {\infty} \xi d F (\xi ; t)$$

The mean-value function is an ordinary time function. Higher moments are defined similarly. The covariance function of a process is defined by

$$
\begin{array}{l} r _ {x x} (s, t) = \operatorname{cov} (x (s), x (t)) \\ = \mathrm{E} \left(\left(x (s) - m (s)\right) \left(x (t) - m (t)\right) ^ {T}\right) \\ = \iint (\xi_ {1} - m (s)) (\xi_ {2} - m (t)) ^ {T} d F (\xi_ {1}, \xi_ {2}; s, t) \\ \end{array}
$$

A Gaussian random process is completely characterized by its mean-value function and its covariance function. The cross-covariance function

$$r _ {x y} (s, t) = \operatorname{cov} \left(x (s), y (t)\right)$$

of two stochastic processes is defined similarly.
