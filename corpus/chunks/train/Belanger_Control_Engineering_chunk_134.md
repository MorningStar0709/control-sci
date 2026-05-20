# Diagonal Form

A special similarity transformation generates the so-called Jordan form. A special case of the Jordan form, the diagonal form, is considered first. It can be generated in cases where the $A$ matrix has $n$ independent eigenvectors, as when its eigenvalues are distinct. Let these eigenvectors be $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ , and let

$$
T = \left[ \begin{array}{l l l l} \mathbf {v} _ {1} & \mathbf {v} _ {2} & \dots & \mathbf {v} _ {n} \end{array} \right]. \tag {3.58}
$$

Then,

$$\mathbf {x} = T \mathbf {z} = z _ {1} \mathbf {v} _ {1} + z _ {2} \mathbf {v} _ {2} + \dots + z _ {n} \mathbf {v} _ {n}. \tag {3.59}$$

The state vector $\mathbf{x}$ is seen to be expressed in terms of its components along each eigenvector.

The inverse of T is written in terms of rows, as

$$
T ^ {- 1} = \left[ \begin{array}{c} \mathbf {w} _ {1} ^ {T} \\ \mathbf {w} _ {2} ^ {T} \\ \vdots \\ \mathbf {w} _ {n} ^ {T} \end{array} \right]. \tag {3.60}
$$

Since $T^{-1}T = I$ , it follows that

$$
T ^ {- 1} T = \left[ \begin{array}{c c c c} \mathbf {w} _ {1} ^ {T} \mathbf {v} _ {1} & \mathbf {w} _ {1} ^ {T} \mathbf {v} _ {2} & \ldots & \mathbf {w} _ {1} ^ {T} \mathbf {v} _ {n} \\ \mathbf {w} _ {2} ^ {T} \mathbf {v} _ {1} & \mathbf {w} _ {2} ^ {T} \mathbf {v} _ {2} & \ldots & \mathbf {w} _ {2} ^ {T} \mathbf {v} _ {n} \\ \vdots & \vdots & \vdots & \vdots \\ \mathbf {w} _ {n} ^ {T} \mathbf {v} _ {1} & \mathbf {w} _ {n} ^ {T} \mathbf {v} _ {2} & \ldots & \mathbf {w} _ {n} ^ {T} \mathbf {v} _ {n} \end{array} \right] = I
$$

and hence

$$
\mathbf {w} _ {i} ^ {T} \mathbf {v} _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   } j = i \\ 0 & \text { if   } j \neq i. \end{array} \right. \tag {3.61}
$$

It turns out that $w_{i}$ is an eigenvector of $A^{T}$ , corresponding to the eigenvalue $s_{i}$ . We may now calculate $T^{-1}AT$ , as needed by Equation 3.55. We have

$$
\begin{array}{l} A T = A \left[ \begin{array}{l l l l} \mathbf {v} _ {1} & \mathbf {v} _ {2} & \dots & \mathbf {v} _ {n} \end{array} \right] = \left[ \begin{array}{l l l l} A \mathbf {v} _ {1} & A \mathbf {v} _ {2} & \dots & A \mathbf {v} _ {n} \end{array} \right] \\ = \left[ s _ {1} \mathbf {v} _ {1} \quad s _ {2} \mathbf {v} _ {2} \quad \dots \quad s _ {n} \mathbf {v} _ {n} \right] \\ \end{array}
$$

and, using Equation 3.60,
