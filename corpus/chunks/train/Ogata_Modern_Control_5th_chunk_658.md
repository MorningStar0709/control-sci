$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} \tag {9-28}$$

where x = n-vector

$$\mathbf {A} = n \times n \text { constant matrix }$$

By analogy with the scalar case, we assume that the solution is in the form of a vector power series in t, or

$$\mathbf {x} (t) = \mathbf {b} _ {0} + \mathbf {b} _ {1} t + \mathbf {b} _ {2} t ^ {2} + \dots + \mathbf {b} _ {k} t ^ {k} + \dots \tag {9-29}$$

By substituting this assumed solution into Equation (9–28), we obtain

$$
\begin{array}{l} \mathbf {b} _ {1} + 2 \mathbf {b} _ {2} t + 3 \mathbf {b} _ {3} t ^ {2} + \dots + k \mathbf {b} _ {k} t ^ {k - 1} + \dots \\ = \mathbf {A} \left(\mathbf {b} _ {0} + \mathbf {b} _ {1} t + \mathbf {b} _ {2} t ^ {2} + \dots + \mathbf {b} _ {k} t ^ {k} + \dots\right) \tag {9-30} \\ \end{array}
$$

If the assumed solution is to be the true solution, Equation (9–30) must hold for all t. Thus, by equating the coefficients of like powers of t on both sides of Equation (9–30), we obtain

$$
\begin{array}{l} \mathbf {b} _ {1} = \mathbf {A b} _ {0} \\ \mathbf {b} _ {2} = \frac {1}{2} \mathbf {A b} _ {1} = \frac {1}{2} \mathbf {A} ^ {2} \mathbf {b} _ {0} \\ \mathbf {b} _ {3} = \frac {1}{3} \mathbf {A b} _ {2} = \frac {1}{3 \times 2} \mathbf {A} ^ {3} \mathbf {b} _ {0} \\ \mathbf {b} _ {k} = \frac {1}{k !} \mathbf {A} ^ {k} \mathbf {b} _ {0} \\ \end{array}
$$

By substituting t=0 into Equation (9–29), we obtain

$$\mathbf {x} (0) = \mathbf {b} _ {0}$$

Thus, the solution x(t) can be written as

$$\mathbf {x} (t) = \left(\mathbf {I} + \mathbf {A} t + \frac {1}{2 !} \mathbf {A} ^ {2} t ^ {2} + \dots + \frac {1}{k !} \mathbf {A} ^ {k} t ^ {k} + \dots\right) \mathbf {x} (0)$$

The expression in the parentheses on the right-hand side of this last equation is an $n \times n$ matrix. Because of its similarity to the infinite power series for a scalar exponential, we call it the matrix exponential and write

$$\mathbf {I} + \mathbf {A} t + \frac {1}{2 !} \mathbf {A} ^ {2} t ^ {2} + \dots + \frac {1}{k !} \mathbf {A} ^ {k} t ^ {k} + \dots = e ^ {\mathbf {A} t}$$

In terms of the matrix exponential, the solution of Equation (9–28) can be written as

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) \tag {9-31}$$

Since the matrix exponential is very important in the state-space analysis of linear systems, we shall next examine its properties.

Matrix Exponential. It can be proved that the matrix exponential of an $n \times n$ matrix A,

$$e ^ {\mathbf {A} t} = \sum_ {k = 0} ^ {\infty} \frac {\mathbf {A} ^ {k} t ^ {k}}{k !}$$
