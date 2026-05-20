$$
\begin{array}{l} \widehat {\mathbf {x}} (1) = A \mathbf {v} = z _ {i} \mathbf {v} _ {i} \\ \widehat {\mathbf {x}} (2) = A \widehat {\mathbf {x}} (1) = z _ {i} ^ {2} \mathbf {v} _ {i} \\ \widehat {\mathbf {x}} (k) = z _ {i} ^ {k} \mathbf {v} _ {i}. \tag {9.23} \\ \end{array}
$$

•
•
•

We see that $z_{i}^{k}$ plays the same role in discrete-time systems as $e^{s_{i}t}$ does in continuous-time systems.

The zero-state response is also easily derived, by recursion:

$$
\begin{array}{l} \widehat {\mathbf {x}} _ {z _ {s}} (1) = B \widehat {\mathbf {x}} (0) \\ \widehat {\mathbf {x}} _ {z _ {s}} (2) = A B \widehat {\mathbf {x}} (0) + B \widehat {\mathbf {u}} (1) \\ \widehat {\mathbf {x}} _ {z _ {s}} (3) = A ^ {2} B \widehat {\mathbf {x}} (0) + A B \widehat {\mathbf {u}} (1) + B \widehat {\mathbf {u}} (2) \\ \widehat {\mathbf {x}} _ {z _ {s}} (k) = \sum_ {i = 0} ^ {k - 1} A ^ {k - 1 - i} B \widehat {\mathbf {u}} (i) \tag {9.24} \\ \end{array}
$$

•
•
•

and

$$\widehat {\mathbf {y}} _ {z _ {s}} (k) = \sum_ {i = 0} ^ {k - 1} C A ^ {k - 1 - i} B \widehat {\mathbf {u}} (i) + D \widehat {\mathbf {u}} (k). \tag {9.25}$$

Preceding the transform of the state equations, we apply the advance theorem to Equation 9.21:

$$z \widehat {\mathbf {x}} (z) = z \widehat {\mathbf {x}} (0) + A \widehat {\mathbf {x}} (z) + B \widehat {\mathbf {u}} (z)$$

or

$$\widehat {\mathbf {x}} (z) = (z I - A) ^ {- 1} z \widehat {\mathbf {x}} (0) + (z I - A) ^ {- 1} B \widehat {\mathbf {u}} (z) \tag {9.26}$$

and

$$\widehat {\mathbf {y}} (z) = C (z I - A) ^ {- 1} z \widehat {\mathbf {x}} (0) + [ C (z I - A) ^ {- 1} B + D ] \widehat {\mathbf {u}} (z). \tag {9.27}$$

Comparing to Equation 9.22, we see that

$$\mathcal {Z} [ A ^ {k} ] = (z I - A) ^ {- 1} z. \tag {9.28}$$

The matrix pulse transfer function is seen to be

$$G (z) = C (z I - A) ^ {- 1} B + D. \tag {9.29}$$

This last equation is, with $z$ replacing $s$ , the same as in the continuous-time case. This implies that any software that generates $G(s)$ from $(A, B, C, D)$ also generates $G(z)$ .

To pursue the parallel, the poles of the pulse transfer functions are the eigenvalues of A in discrete time, as they are in continuous time.

![](image/78dd4673c4e3b0ca63117e732502b045440dee8566e9ee5dad277ec611a0c891.jpg)
