# Completing the Squares

Quadratic functions will be minimized several times in the sequel. The loss functions will have the form

$$
J (x, u) = \left( \begin{array}{l l} x ^ {T} & u ^ {T} \end{array} \right) \left( \begin{array}{l l} Q _ {x} & Q _ {x u} \\ Q _ {x u} ^ {T} & Q _ {u} \end{array} \right) \binom{x}{u} \tag {11.11}
$$

and we want to find the minimum with respect to u. Then there exists an L satisfying

$$Q _ {u} L = Q _ {x u} ^ {T} \tag {11.12}$$

such that the loss function (11.11) can be written as

$$J (x, u) = x ^ {T} \left(Q _ {x} - L ^ {T} Q _ {u} L\right) x + (u + L x) ^ {T} Q _ {u} (u + L x) \tag {11.13}$$

This is easily shown by inserting (11.12) into (11.13). Rewriting (11.11) as in (11.13) is called completing the squares. Because (11.13) is quadratic in u and both terms are greater or equal zero, it is easily seen that (11.11) is minimized for

$$u = - L x \tag {11.14}$$

and that $L$ is unique if $Q_{\mu}$ is positive definite. The minimum is

$$J _ {\min} = x ^ {T} \left(Q _ {x} - L ^ {T} Q _ {u} L\right) x \tag {11.15}$$
