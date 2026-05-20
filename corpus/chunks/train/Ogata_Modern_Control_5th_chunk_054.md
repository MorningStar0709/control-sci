The dynamic system must involve elements that memorize the values of the input for $t \geq t _ { 1 }$ . Since integrators in a continuous-time control system serve as memory devices, the outputs of such integrators can be considered as the variables that define the internal state of the dynamic system. Thus the outputs of integrators serve as state variables. The number of state variables to completely define the dynamics of the system is equal to the number of integrators involved in the system.

Assume that a multiple-input, multiple-output system involves n integrators.Assume also that there are r inputs $u _ { 1 } ( t ) , u _ { 2 } ( t ) , \ldots , u _ { r } ( t )$ and m outputs $y _ { 1 } ( t ) , y _ { 2 } ( t ) , \ldots , y _ { m } ( t )$ . Define n outputs of the integrators as state variables: $x _ { 1 } ( t ) , x _ { 2 } ( t ) , \ldots , x _ { n } ( t )$ Then the system may be described by

$$
\begin{array}{l} \dot {x} _ {1} (t) = f _ {1} \left(x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t\right) \\ \dot {x} _ {2} (t) = f _ {2} \left(x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t\right) \\ \dot {x} _ {n} (t) = f _ {n} \left(x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t\right) \\ \end{array}
$$

The outputs $y _ { 1 } ( t ) , y _ { 2 } ( t ) , \ldots , y _ { m } ( t )$ of the system may be given by

$$
y _ {1} (t) = g _ {1} \left(x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t\right)y _ {2} (t) = g _ {2} \left(x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t\right)
\begin{array}{l} \cdot \\ \cdot \\ \cdot \end{array} \tag {2-9}
y _ {m} (t) = g _ {m} \left(x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t\right)
$$

If we define

$$
\mathbf {x} (t) = \left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \\ . \\ . \\ . \\ x _ {n} (t) \end{array} \right], \quad \mathbf {f} (\mathbf {x}, \mathbf {u}, t) = \left[ \begin{array}{c} f _ {1} \bigl (x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t \bigr) \\ f _ {2} \bigl (x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t \bigr) \\ . \\ . \\ . \\ f _ {n} \bigl (x _ {1}, x _ {2}, \dots , x _ {n}; u _ {1}, u _ {2}, \dots , u _ {r}; t \bigr) \end{array} \right],
