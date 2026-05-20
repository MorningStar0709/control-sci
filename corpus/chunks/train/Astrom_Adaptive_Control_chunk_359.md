$$
\frac {d e}{d t} = \left( \begin{array}{c c} 0 & 1 \\ - a _ {2} & - a _ {1} \end{array} \right) e + \binom{f (\xi_ {1})}{\hat {\theta} f (\xi_ {1}) f ^ {\prime} (\xi_ {1})} \tilde {\theta} = A e + B \tilde {\theta}
$$

where

$$
A = \left( \begin{array}{c c} 0 & 1 \\ - a _ {2} & - a _ {1} \end{array} \right) \quad B = \binom{f (\xi_ {1})}{\hat {\theta} f (\xi_ {1}) f ^ {\prime} (\xi_ {1})}
$$

The matrix A has all eigenvalues in the left half-plane if $a_{1} > 0$ and $a_{2} > 0$ . It is then possible to find a matrix P such that

$$\boldsymbol {A} ^ {T} \boldsymbol {P} + \boldsymbol {P A} = - \boldsymbol {I}$$

Choosing the Lyapunov function

$$V = e ^ {T} P e + \frac {1}{\gamma} \tilde {\theta} ^ {2}$$

we find that

$$\frac {d V}{d t} = e ^ {T} (A ^ {T} P + P A) e + 2 \tilde {\theta} B ^ {T} P e + \frac {2}{\gamma} \tilde {\theta} \frac {d \tilde {\theta}}{d t}$$

If the law for updating the parameters is chosen to be

$$\frac {d \hat {\theta}}{d t} = \gamma B ^ {T} P e$$

we find that

$$\frac {d \hat {\theta}}{d t} = \frac {d}{d t} (\theta - \hat {\theta}) - \frac {d \hat {\theta}}{d t} = - \gamma B ^ {T} P e$$

and the derivative of the Lyapunov function becomes

$$\frac {d V}{d t} = - e ^ {T} e$$

This function is negative as long as any component of the error vector is different from zero. With the control law given by (5.89) and (5.90) the tracking error will thus always go to zero.
