$$L = (B ^ {T} B) ^ {- 1} B ^ {T} (A - A _ {m}) = (B _ {m} ^ {T} B) ^ {- 1} B _ {m} ^ {T} (A - A _ {m})M = (B ^ {T} B) ^ {- 1} B ^ {T} B _ {m} = (B _ {m} ^ {T} B) ^ {- 1} B _ {m} ^ {T} B _ {m}$$

The error equation Introduce the error defined as

$$e = x - x _ {m}$$

Subtracting Eq. (5.30) from Eq. (5.29) gives

$$\frac {d e}{d t} = \frac {d x}{d t} - \frac {d x _ {m}}{d t} = A x + B u - A _ {m} x _ {m} - B _ {m} u _ {c}$$

Adding and subtracting $A_{m}x$ from the right-hand side give

$$
\begin{array}{l} \frac {d e}{d t} = A _ {m} e + (A - A _ {m} - B L) x + (B M - B _ {m}) u _ {c} \\ = A _ {m} e + \left(A _ {c} (\theta) - A _ {m}\right) x + \left(B _ {c} (\theta) - B _ {m}\right) u _ {c} \\ = A _ {m} e + \Psi (\theta - \theta^ {0}) \tag {5.34} \\ \end{array}
$$

To obtain the last equality, it has been assumed that the conditions for exact model-following are satisfied. This is required for $\theta^{0}$ to exist. To derive a parameter adjustment law, we introduce the Lyapunov function

$$V (e, \theta) = \frac {1}{2} \left(\gamma e ^ {T} P e + (\theta - \theta^ {0}) ^ {T} (\theta - \theta^ {0})\right)$$

where $P$ is a positive definite matrix. The function $V$ is positive definite. To find out whether it can be a Lyapunov function, we calculate its total time derivative

$$
\begin{array}{l} \frac {d V}{d t} = - \frac {\gamma}{2} e ^ {T} Q e + \gamma (\theta - \theta^ {0}) \Psi^ {T} P e + (\theta - \theta^ {0}) ^ {T} \frac {d \theta}{d t} \\ = - \frac {\gamma}{2} e ^ {T} Q e + (\theta - \theta^ {0}) ^ {T} \left(\frac {d \theta}{d t} + \gamma \Psi^ {T} P e\right) \\ \end{array}
$$

where Q is positive definite and such that

$$A _ {m} ^ {T} P + P A _ {m} = - Q$$

Notice that it follows from Theorem 5.2 that a pair of positive definite matrices $P$ and $Q$ with this property always exist if $A_{m}$ is stable.

If the parameter adjustment law is chosen to be

$$\frac {d \theta}{d t} = - \gamma \Psi^ {T} P e \tag {5.35}$$

we get

$$\frac {d V}{d t} = - \frac {\gamma}{2} e ^ {T} Q e$$

The time derivative of the Lyapunov function is negative semidefinite. By using Lemma 5.1 in the same way as in Example 5.7 it can be shown that the error goes to zero. Notice that we have assumed that all states x are measurable.
