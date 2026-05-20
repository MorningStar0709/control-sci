# Diagonal Form

Assume that $\Phi$ has distinct eigenvalues. Then there exists a T such that

$$
T \Phi T ^ {- 1} = \left( \begin{array}{c c c} \lambda_ {1} & & 0 \\ & \ddots & \\ 0 & & \lambda_ {n} \end{array} \right)
$$

where $\lambda_{i}$ are the eigenvalues of $\Phi$ . The computation of T is discussed in Sec. 3.4. In this case a set of decoupled first-order difference equations is obtained.

$$
\begin{array}{l} z _ {1} (k + 1) = \lambda_ {1} z _ {1} (k) + \beta_ {1} u (k) \\ z _ {n} (k + 1) = \lambda_ {n} z _ {n} (k) + \beta_ {n} u (k) \\ y (k) = \gamma_ {1} z _ {1} (k) + \dots + \gamma_ {n} z _ {n} (k) \\ \end{array}
$$

:

The solution to the system of equations is now simple. Each mode will have the solution

$$z _ {i} (k) = \lambda_ {i} ^ {k} z _ {i} (0) + \sum_ {j = 0} ^ {k - 1} \lambda_ {i} ^ {k - j - 1} \beta_ {i} u (j) \tag {2.18}$$
