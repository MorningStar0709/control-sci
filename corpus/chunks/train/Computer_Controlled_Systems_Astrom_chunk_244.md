Hence if $K$ is chosen so that the system (4.30) is asymptotically stable, the error $\tilde{x}$ will always converge to zero. By introducing a feedback from the measurements in the reconstruction, it is thus possible to make the error go to zero even if the system of (4.23) is unstable. The system in (4.28) is called an observer for the system of (4.23) because it produces the state of the system from measurements of inputs and outputs. It now remains to find a suitable way to choose the matrix $K$ so that the system (4.28) is stable. Given the matrices $\Phi$ and $C$ , the problem is to find a matrix $K$ such that the matrix $\Phi - KC$ has prescribed eigenvalues. Because a matrix and its transpose have the same eigenvalues, the problem is the same as finding a matrix $K^T$ such that $\Phi^T - C^T K^T$ has prescribed eigenvalues. However, this problem was solved in Sec. 4.3 in connection with the pole-placement problem; see Theorem 4.1. If those results are translated, we find then that the problem can be solved if the matrix

$$
W _ {o} ^ {T} = \left( \begin{array}{l l l l} C ^ {T} & \Phi^ {T} C ^ {T} & \dots & (\Phi^ {n - 1}) ^ {T} C ^ {T} \end{array} \right)
$$

has full rank. Notice that $W_{o}$ is the observability matrix for the system of (4.23). The result can be expressed by the following.

THEOREM 4.2 OBSERVER DYNAMICS Consider the discrete system given by Eq. (4.23). Let $P(z)$ be a polynomial of degree $n$ , where $n$ is the order of the system. Assuming that the system is completely observable, then there exists a matrix $K$ such that the matrix $\Phi - KC$ of the observer (4.28) has the characteristic polynomial $P(z)$ .
