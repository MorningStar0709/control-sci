$$
\begin{array}{l} J _ {1} = \int_ {0} ^ {\infty} [ \mathbf {x} ^ {T} (\mathbf {b} _ {1}, t) C _ {1} ^ {T} C _ {1} \mathbf {x} (\mathbf {b} _ {1}, t) + \mathbf {x} ^ {T} (\mathbf {b} _ {1}, t) C _ {1} ^ {T} D _ {1 2} \mathbf {u} (\mathbf {b} _ {1}, t) \\ + \mathbf {u} ^ {T} (\mathbf {b} _ {1}, t) D _ {1 2} ^ {T} C _ {1} \mathbf {x} (\mathbf {b} _ {1}, t) + \mathbf {u} ^ {T} (\mathbf {b} _ {1}, t) D _ {1 2} ^ {T} D _ {1 2} \mathbf {u} (\mathbf {b} _ {1}, t) ] d t. \tag {8.63} \\ \end{array}
$$

Equations 8.61 and 8.63 form an LQ problem, even with the inclusion of cross terms (mixed x and u) in $J_{1}$ . The solution of that problem is of the form $u = -Kx$ and is independent of the initial state. The same control law minimizes every term of the sum in Equation 8.60, and hence minimizes the sum itself.

To remove the cross terms, define a new input v,

$$\mathbf {v} = \mathbf {u} + (D _ {1 2} ^ {T} D _ {1 2}) ^ {- 1} D _ {1 2} ^ {T} C _ {1} \mathbf {x}. \tag {8.64}$$

It is easy to show that

$$\dot {\mathbf {x}} = [ A - B _ {2} (D _ {1 2} ^ {T} D _ {1 2}) ^ {- 1} D _ {1 2} ^ {T} C _ {1} ] \mathbf {x} + B _ {2} \mathbf {v} \tag {8.65}J _ {1} = \int_ {0} ^ {\infty} \left\{\mathbf {x} ^ {T} C _ {1} ^ {T} \left[ I - D _ {1 2} \left(D _ {1 2} ^ {T} D _ {1 2}\right) ^ {- 1} D _ {1 2} ^ {T} \right] C _ {1} \mathbf {x} + \mathbf {v} ^ {T} \left(D _ {1 2} ^ {T} D _ {1 2}\right) \mathbf {v} \right\} d t. \tag {8.66}$$

Equations 8.65 and 8.66 present a standard LQ problem. Its solution is calculated by the methods of Chapter 7. With $v = -\kappa x$ ,

$$\mathbf {u} = - [ \kappa + (D _ {1 2} ^ {T} D _ {1 2}) ^ {- 1} D _ {1 2} ^ {T} C _ {1} ] \mathbf {x} = - K \mathbf {x}. \tag {8.67}$$

It is usually not necessary to work out these transformations, since most packages will solve the LQ problem for an integrand with cross terms.

If the state is not directly available, it is necessary to use a state estimator. We assume a control law $u = -\kappa \widehat{x}$ , simply replacing the state with its estimate in Equation 8.67. The problem is to choose the observer gain G so as to minimize $\|T_{wz}\|_{2}$ . We define

$$\widetilde {\mathbf {x}} = \mathbf {x} - \widehat {\mathbf {x}}$$

and

$$\nu = \mathbf {u} + K \mathbf {x} = K \widetilde {\mathbf {x}}. \tag {8.68}$$

We write

$$
\begin{array}{l} \dot {\mathbf {x}} = A \mathbf {x} + B _ {1} \mathbf {w} + B _ {2} \mathbf {u} \\ = (A - B _ {2} K) \mathbf {x} + B _ {1} \mathbf {w} + B _ {2} \nu (8.69) \\ \mathbf {z} = C _ {1} \mathbf {x} + D _ {1 2} \mathbf {u} \\ = (C _ {1} - D _ {1 2} K) \mathbf {x} + D _ {1 2} \nu . (8.70) \\ \end{array}
$$

Also,
