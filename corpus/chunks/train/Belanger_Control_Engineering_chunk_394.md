To derive the necessary condition, we examine the effect on J of small perturbations of K from $K^{*}$ . We argue that, if J is indeed minimized by $K^{*}$ , any perturbation of gain must lead to an increase in J; otherwise, some value of K would result in a lower value of J than $K^{*}$ . The fact that infinitesimal perturbations are used means that we are checking $J(K^{*})$ against values of $J(K)$ in a neighborhood of $K^{*}$ ; i.e., we verify that $K^{*}$ yields a local minimum. But, since the global minimum we are seeking must also be a minimum in its own neighborhood, it must also satisfy the condition for a local minimum. We let

$$K = K ^ {*} + \epsilon \delta K$$

where $\epsilon$ is infinitesimally small. The matrix $P$ will change. It can be shown that $P$ is an analytic function of the elements of $K$ , so that

$$P = P ^ {*} + \epsilon \delta P _ {1} + \epsilon^ {2} \delta P _ {2} + \dots .$$

We insert this in Equation 7.30:

$$
\begin{array}{l} (A - B K ^ {*} - \epsilon B \delta K) ^ {T} \left(P ^ {*} + \epsilon \delta P _ {1} + \epsilon^ {2} \delta P _ {2}\right) \\ + \left(P ^ {*} + \epsilon \delta P _ {1} + \epsilon^ {2} \delta P _ {2}\right) \left(A - B K ^ {*} - \epsilon B \delta K\right) \\ = - Q - \left(K ^ {*} + \epsilon \delta K\right) ^ {T} R \left(K ^ {*} + \epsilon \delta K\right) \\ \end{array}
$$

or

$$
\begin{array}{l} (A - B K ^ {*}) ^ {T} P ^ {*} (A - B K ^ {*}) + \epsilon [ - \delta K ^ {T} B ^ {T} P ^ {*} + (A - B K ^ {*}) ^ {T} \delta P _ {1} \\ + \delta P _ {1} (A - B K ^ {*}) ^ {T} - P ^ {*} B \delta K ] + 0 (\epsilon^ {2}) \\ = - Q - K ^ {* ^ {T}} R K ^ {*} + \epsilon [ - \delta K ^ {T} R K ^ {*} - K ^ {* ^ {T}} R \delta K ] + 0 (\epsilon^ {2}). \\ \end{array}
$$

Here, the notation $0(\epsilon^2)$ refers to terms of order two or more in $\epsilon$ . Matching powers of order zero gives back Equation 7.31. Matching terms in $\epsilon$ gives

$$
\begin{array}{l} \delta K ^ {T} \left(B ^ {T} P ^ {*} - R K ^ {*}\right) + \left(P ^ {*} B - K ^ {* T} R\right) \delta K \\ + (A - B K ^ {*}) ^ {T} \delta P _ {1} + \delta P _ {1} (A - B K ^ {*}) = 0. \tag {7.32} \\ \end{array}
$$

We go back to Equation 7.29 and write

$$
\begin{array}{l} J (K ^ {*} + \epsilon \delta K) = \mathbf {x} ^ {T} (0) P \mathbf {x} (0) \\ = \mathbf {x} ^ {T} (0) P ^ {*} \mathbf {x} (0) + \epsilon \mathbf {x} ^ {T} (0) \delta P _ {1} \mathbf {x} (0) + \epsilon^ {2} \mathbf {x} ^ {T} (0) \delta P _ {2} \mathbf {x} (0) + \dots . \\ \end{array}
$$
