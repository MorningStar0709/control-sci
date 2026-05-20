Let us multiply each side by a vector as follows:

$$
\mathbf {k} ^ {T} T \left[ \begin{array}{c} 1 \\ s \\ \vdots \\ s ^ {n - 2} \\ s ^ {n - 1} \end{array} \right] = \kappa^ {T} \left[ \begin{array}{c} 1 \\ s \\ \vdots \\ s ^ {n - 2} \\ s ^ {n - 1} \end{array} \right]. \tag {7.17}
$$

From Equation 7.15, we see that the right-hand side (RHS) is

$$\kappa_ {1} + \kappa_ {2} s + \dots + \kappa_ {n} s ^ {n - 1} = p _ {c} (s) - p _ {0} (s)$$

where $p_{0}(s)$ is the open-loop characteristic polynomial; i.e., $p_{0}(s) = \det(sI - A)$ . As for the left-hand side (LHS) of Equation 7.17, recall that, in Lemma 7.1, T was formed by extracting each row from the corresponding row of the numerator of the transfer function. For example, given a fourth-order system, the row $2s^{3} + 3s^{2} + s + 1$ would, according to the rule for the controllable canonical form, correspond to the C vector [1 1 3 2]. The multiplication on the left-hand side (LHS) of Equation 7.17 simply restores the transfer-function numerator. Then

$$
T \left[ \begin{array}{c} 1 \\ s \\ \vdots \\ s ^ {n - 1} \\ s ^ {n - 1} \end{array} \right] = \det (s I - A) \mathbf {h} (s) = A d j (s I - A) \mathbf {b}.
$$

We may therefore write Equation 7.17 as

$$p _ {c} (s) = \det (s I - A) + \mathbf {k} ^ {T} A d j (s I - A) \mathbf {b}. \tag {7.18}$$
