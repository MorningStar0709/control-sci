# 4.2 Integrals

The integral is the inverse operation of the derivative and calculates the area under a curve. Here is an example of one based on table 4.2.

$$\int e ^ {a t} d t \frac {1}{a} e ^ {a t} + C$$

The arbitrary constant C is needed because when you take a derivative, constants are discarded because vertical offsets don’t affect the slope. When performing the inverse operation, we don’t have enough information to determine the constant.

However, we can provide bounds for the integration.

$$
\begin{array}{l} \int_ {0} ^ {t} e ^ {a t} d t \\ \left(\frac {1}{a} e ^ {a t} + C\right) \bigg | _ {0} ^ {t} \\ \left(\frac {1}{a} e ^ {a t} + C\right) - \left(\frac {1}{a} e ^ {a \cdot 0} + C\right) \\ \left(\frac {1}{a} e ^ {a t} + C\right) - \left(\frac {1}{a} + C\right) \\ \frac {1}{a} e ^ {a t} + C - \frac {1}{a} - C \\ \end{array}
\frac {1}{a} e ^ {a t} - \frac {1}{a}
$$

When we do this, the constant cancels out.
