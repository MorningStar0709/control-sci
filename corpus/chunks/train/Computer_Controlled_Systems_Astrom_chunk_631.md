# Example 10.5 Spectral factorization

Consider the process $y(k)$ of Examples 10.3 and 10.4. This process has the spectral density

$$
\begin{array}{l} \phi_ {y} (\omega) = \frac {1}{2 \pi} \left(r _ {2} + \frac {r _ {1}}{(z - a) (z ^ {- 1} - a)}\right) _ {z = e ^ {i \omega}} \\ = \frac {1}{2 \pi} \left(\frac {r _ {1} + r _ {2} (1 + a ^ {2}) - r _ {2} a (z + z ^ {- 1})}{(z - a) (z ^ {- 1} - a)}\right) _ {z = e ^ {i \omega}} \\ \end{array}
$$

The denominator is already in factored form. To factor the numerator, we observe that it can be written as

$$\lambda^ {2} (z - b) \left(z ^ {- 1} - b\right) \equiv r _ {1} + r _ {2} \left(1 + a ^ {2}\right) - r _ {2} a \left(z + z ^ {- 1}\right)$$

Identification of coefficients of equal powers of z gives

$$
\begin{array}{l} z ^ {0}: \quad \lambda^ {2} (1 + b ^ {2}) = r _ {1} + r _ {2} (1 + a ^ {2}) \\ z ^ {1}: \quad \lambda^ {2} b = r _ {2} a \\ \end{array}
$$

Elimination of $\lambda$ gives a second-order algebraic equation for $b$ . This equation has the solution

$$b = \frac {r _ {1} + r _ {2} (1 + a ^ {2}) - \sqrt {\left(r _ {1} + r _ {2} (1 + a) ^ {2}\right) \left(r _ {1} + r _ {2} (1 - a) ^ {2}\right)}}{2 a r _ {2}}$$

The other root is discarded because it is outside the unit disc. Furthermore, the variable $\lambda$ is given by

$$\lambda^ {2} = \frac {1}{2} \left(r _ {1} + r _ {2} (1 + a ^ {2}) + \sqrt {\left(r _ {1} + r _ {2} (1 + a) ^ {2}\right) \left(r _ {1} + r _ {2} (1 - a) ^ {2}\right)}\right)$$

![](image/ee7e111f3c1fb319d1944222496b03ce950bfc78c74d77c47f256100f1fe55b9.jpg)

<details>
<summary>line</summary>

| Frequency | Magnitude |
| --- | --- |
| -4 | 0 |
| -2 | 0 |
| 0 | 0.5 |
| 2 | 0 |
| 4 | 0 |
</details>

Figure 10.6 The spectral density (10.20) as function of $\omega$ , that is, when $z = e^{i\omega}$ .
