# Closed-Loop Systems with Guaranteed Exponential Stability

The control laws given by Theorems 12.2, 12.3, 12.4, and 12.5 give closed-loop systems with poles inside the unit disc. It is sometimes desirable to have control laws such that the closed-loop system has its poles inside a circle with radius $\bar{r}$ . It is straightforward to formulate optimization problems that give such control laws.

Introduce the criterion

$$J = \mathrm{E} \bar {r} ^ {- 2 k} \left(y ^ {2} (k) + \rho u ^ {2} (k)\right) \tag {12.72}$$

If a control law that minimizes this criterion can be found, the variables $y(k)$ and $u(k)$ must converge to zero at least as fast as $\bar{r}^{k}$ when k increases. To obtain such a result, it must be assumed that the model of (12.5) is such that the covariance of $e(k)$ also goes to zero as $\bar{r}^{k}$ .

Introduce the scaled variables $\eta$ , $\mu$ , and $\varepsilon$ defined by

$$
\begin{array}{l} y (k) = \bar {r} ^ {k} \eta (k) \\ u (k) = \bar {r} ^ {k} \mu (k) \\ e (k) = \bar {r} ^ {k} \varepsilon (k) \\ \end{array}
$$

Because

$$q ^ {l} y (k) = q ^ {l} \left(\bar {r} ^ {k} \eta (k)\right) = \bar {r} ^ {k + l} \eta (k + l) = \bar {r} ^ {k} (\bar {r} q) ^ {l} \eta (k)$$

it follows that

$$A (q) y (k) = A (q) \left(\bar {r} ^ {k} \eta (k)\right) = \bar {r} ^ {k} A (\bar {r} q) \eta (k)$$

Introducing the transformed polynomials

$$
\begin{array}{l} \tilde {A} (z) = A (\bar {r} z) \\ \tilde {B} (z) = B (\bar {r} z) \\ \tilde {C} (z) = C (\bar {r} z) \\ \end{array}
$$

the model of (12.5) can be written as

$$\tilde {A} (q) \eta (k) = \bar {B} (q) \eta (k) + \bar {C} (q) \varepsilon (k) \tag {12.73}$$

and the criterion of (12.72) becomes

$$J = E \left(\eta^ {2} (k) + \rho \mu^ {2} (k)\right) \tag {12.74}$$

The control law that minimizes (12.74) for the system of (12.73) is then given by Theorem 12.4. This control law gives a closed-loop system in which all the zeros of the characteristic equation

$$\tilde {P} (z) \bar {C} (z) = 0$$

are inside the unit disc. Going back to the original variables results in the characteristic equation

$$P (z) C (z) = \tilde {P} \left(\frac {z}{\bar {r}}\right) \tilde {C} \left(\frac {z}{\bar {r}}\right) = 0$$

All the zeros of this equation are inside the circle $|z| = \bar{r}$ .

A simple procedure for obtaining feedback laws that give closed-loop systems with all poles inside the circle $|z| = \bar{r}$ has thus been devised.
