# 3.6.3 Controllability Tests

In parallel with the case of observability, controllability can be ascertained by showing that a system has no uncontrollable states. Duality between controllability and observability is now established to apply the observability tests to controllability.

The transpose of Equation 3.48 yields

$$B ^ {T} e ^ {A ^ {T} t} \mathbf {x} ^ {*} = \mathbf {0} \tag {3.50}$$

which is precisely the condition for $\mathbf{x}^*$ to be an unobservable state of the dual system

$$\dot {\mathbf {x}} = A ^ {T} \mathbf {x}\mathbf {y} = B ^ {T} \mathbf {x}. \tag {3.51}$$

The problem of looking for uncontrollable states of the system $\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}$ is reduced to that of seeking unobservable states of the dual system of Equation 3.51. The tests are thus directly transferable. From Equation 3.39, an uncontrollable state satisfies

$$
\left[ \begin{array}{c} B ^ {T} \\ B ^ {T} A ^ {T} \\ B ^ {T} (A ^ {T}) ^ {2} \\ \vdots \\ B ^ {T} (A ^ {T}) ^ {n - 1} \end{array} \right] \mathbf {x} ^ {*} = \mathbf {0}
$$

or, transposing,

$$\mathbf {x} ^ {* T} [ B \quad A B \quad A ^ {2} B \quad \dots \quad A ^ {n - 1} B ] = 0. \tag {3.52}$$

The system is controllable if no $x^{*} \neq 0$ satisfies Equation 3.56, i.e., if

$$\operatorname{rank} \mathcal {C} = \operatorname{rank} \left[ B \quad A B \quad A ^ {2} B \quad \dots \quad A ^ {n - 1} B \right] = n \tag {3.53}$$

where C is called the controllability matrix.

The eigenvector test is also applicable. The system $(A, B)$ is uncontrollable if, and only if, there exists an eigenvector w of the matrix $A^{T}$ such that $B^{T}w = 0$ . If $B^{T}w_{i} = 0$ , the mode corresponding to $w_{i}$ is called an uncontrollable mode.

This last sentence deserves some elaboration. Starting from

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u}$$

we premultiply each side by $\mathbf{w}_i^T$ to get

$$\mathbf {w} _ {i} ^ {T} \dot {\mathbf {x}} = \mathbf {w} _ {i} ^ {T} A \mathbf {x} + \mathbf {w} _ {i} ^ {T} B \mathbf {u}.$$

Now, $\mathbf{w}_i^T A = (A^T\mathbf{w}_i)^T = (s_i\mathbf{w}_i)^T = \mathbf{w}_i^T s_i$ . Thus,

$$\mathbf {w} _ {i} ^ {T} \dot {\mathbf {x}} = \frac {d}{d t} (\mathbf {w} _ {i} ^ {T} \mathbf {x}) = s _ {i} \mathbf {w} _ {i} ^ {T} \mathbf {x} + \mathbf {w} _ {i} ^ {T} B \mathbf {u}.$$

If the mode $s_i$ is uncontrollable, $\mathbf{w}_i^T B = \mathbf{0}$ and

$$\frac {d}{d t} (\mathbf {w} _ {i} ^ {T} \mathbf {x}) = s _ {i} (\mathbf {w} _ {i} ^ {T} \mathbf {x})$$
