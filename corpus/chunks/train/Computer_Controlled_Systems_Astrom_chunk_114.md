# Solution of the System Equation

To analyze discrete-time systems it is necessary to solve the system equation (2.16). Assume that the initial condition $x(k_{0})$ and the input signals $u(k_{0}), u(k_{0}+1), \ldots$ are given. How is the state then evolving? It is possible to solve (2.16) by simple iterations.

$$
\begin{array}{l} x \left(k _ {0} + 1\right) = \Phi x \left(k _ {0}\right) + \Gamma u \left(k _ {0}\right) \\ x \left(k _ {0} + 2\right) = \Phi x \left(k _ {0} + 1\right) + \Gamma u \left(k _ {0} + 1\right) \\ = \Phi^ {2} x (k _ {0}) + \Phi \Gamma u (k _ {0}) + \Gamma u (k _ {0} + 1) \\ \vdots \tag {2.17} \\ \end{array}
x (k) = \Phi^ {k - k _ {0}} x \left(k _ {0}\right) + \Phi^ {k - k _ {0} - 1} \Gamma u \left(k _ {0}\right) + \dots + \Gamma u (k - 1)= \Phi^ {k - k _ {0}} x (k _ {0}) + \sum_ {j = k _ {0}} ^ {k - 1} \Phi^ {k - j - 1} \Gamma u (j)
$$

The solution consists of two parts: One depends on the initial condition, and the other is a weighted sum of the input signals. Equation (2.17) clearly shows that the eigenvalues of $\Phi$ will determine the properties of the solution. The eigenvalues are obtained from the characteristic equation

$$\det (\lambda I - \Phi) = 0$$
