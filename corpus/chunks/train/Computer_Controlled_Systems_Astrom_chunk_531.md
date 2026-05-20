# Different Representations of the Controller

The design methods of the previous chapters give control laws in the form of a discrete-time dynamic system. Different representations are obtained, depending on the approaches used. The design methods based on pole placement by state feedback in Sec. 4.5 give a controller of the form

$$\hat {x} (k | k) = \hat {x} (k | k - 1) + K (y (k) - \hat {y} (k | k - 1))u (k) = L \left(x _ {m} (k) - \hat {x} (k | k)\right) + L _ {c} u _ {c} (k)\hat {x} (k + 1 | k) = \Phi \hat {x} (k | k) + \Gamma u (k) \tag {9.1}x _ {m} (k + 1) = f \left(x _ {m} (k), u _ {c} (k)\right)\hat {y} (k + 1 | 1) = C \hat {x} (k + 1 | k)$$

In this representation the state of the controller is $\hat{x}$ and $x_{m}$ , where $\hat{x}$ is an estimate of the process state, and $x_{m}$ is the state of the model that generates the desired response to command signals $u_{c}$ . The form in (9.1) is called a state representation with an explicit observer because of the physical interpretation of the controller state. It is easy to include a nonlinear model for the desired state in this representation.

If the function f in (9.1) is linear, the controller is a linear system with the inputs y and $u_{c}$ and the output u. Such a controller may be represented as

$$
\begin{array}{l} x (k + 1) = F x (k) + G y (k) + G _ {c} u _ {c} (k) \\ \text {(9.2)} \end{array}
u (k) = C x (k) + D y (k) + D _ {c} u _ {c} (k)
$$

where x is the state of the controller (see Problem 4.7). Equation (9.2) is a general-state representation of a discrete-time dynamic system. This form is more compact than (9.1). The state does, however, not necessarily have a simple physical interpretation.

The design methods for single-input-single-output systems discussed in Chapter 5, which are based on external models, give a controller in the form of a general input-output representation

$$R (q) u (k) = T (q) u _ {c} (k) - S (q) y (k) \tag {9.3}$$

where $R(q)$ , $S(q)$ , and $T(q)$ are polynomials in the forward-shift operator q. There are simple transformations between the different representations (compare with Chapter 2).
