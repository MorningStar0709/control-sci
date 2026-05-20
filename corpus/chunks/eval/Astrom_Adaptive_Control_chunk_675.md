# Directional Forgetting

Another way to forget old data is based on the fact that one observation gives a projection of the parameter on the regression vector. Exponential forgetting can then be done only in the "direction" of the regression vector. This approach is called directional forgetting. To derive the equations, we observe that the inverse of the $P$ -matrix with exponential forgetting is given by

$$\boldsymbol {P} ^ {- 1} (t + \mathbf {1}) = \lambda \boldsymbol {P} ^ {- 1} (t) + \varphi (t) \boldsymbol {\varphi} ^ {T} (t)$$

In directional forgetting we start with the formula

$$P ^ {- 1} (t + 1) = P ^ {- 1} (t) + \varphi (t) \varphi^ {T} (t)$$

The matrix $P^{-1}(t)$ is decomposed as

$$P ^ {- 1} (t) = \tilde {P} ^ {- 1} (t) + \gamma (t) \varphi (t) \varphi^ {T} (t) \tag {11.22}$$

where $\tilde{P}^{-1}(t)\varphi (t) = 0$ . This gives

$$\gamma (t) = \frac {\varphi^ {T} (t) P ^ {- 1} (t) \varphi (t)}{(\varphi^ {T} (t) \varphi (t)) ^ {2}}$$

Exponential forgetting is then applied only to the second term of Eq. (11.22), which corresponds to the direction where new information is obtained. This gives

$$P ^ {- 1} (t + 1) = \tilde {P} ^ {- 1} (t) + \lambda \gamma (t) \varphi (t) \varphi^ {T} (t) + \varphi (t) \varphi^ {T} (t)$$

which can be written as

$$P ^ {- 1} (t + 1) = P ^ {- 1} (t) + \left(1 + (\lambda - 1) \frac {\varphi^ {T} (t) P ^ {- 1} (t) \varphi (t)}{(\varphi^ {T} (t) \varphi (t)) ^ {2}}\right) \varphi (t) \varphi^ {T} (t)$$

There are several variations of the algorithms. The forgetting factor is sometimes made a function of the data. One method has the property that the P-matrix is driven toward a matrix proportional to the identity matrix when there is poor excitation.
