$$\dot {x} _ {1} = x _ {2} + \beta_ {1} u\dot {x} _ {2} = x _ {3} + \beta_ {2} u$$

(2–36)

$$\dot {x} _ {n - 1} = x _ {n} + \beta_ {n - 1} u\dot {x} _ {n} = - a _ {n} x _ {1} - a _ {n - 1} x _ {2} - \dots - a _ {1} x _ {n} + \beta_ {n} u$$

where $\beta _ { n }$ is given by

$$\beta_ {n} = b _ {n} - a _ {1} \beta_ {n - 1} - \dots - a _ {n - 1} \beta_ {1} - a _ {n - 1} \beta_ {0}$$

[To derive Equation (2–36), see Problem A–2–6.] In terms of vector-matrix equations, Equation (2–36) and the output equation can be written as

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \cdot \\ \cdot \\ \cdot \\ \dot {x} _ {n - 1} \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n - 1} \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} \beta_ {1} \\ \beta_ {2} \\ \cdot \\ \cdot \\ \cdot \\ \beta_ {n - 1} \\ \beta_ {n} \end{array} \right] u

y = \left[ \begin{array}{l l l l} 1 & 0 & \dots & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + \beta_ {0} u
$$

or

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {2-37}y = \mathbf {C} \mathbf {x} + D u \tag {2-38}$$

where

$$
\begin{array}{l} \mathbf {x} = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n - 1} \\ x _ {n} \end{array} \right], \\ \mathbf {A} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ . & . & . & & . \\ . & . & . & & . \\ . & . & . & & . \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right] \\ \mathbf {B} = \left[ \begin{array}{c} \beta_ {1} \\ \beta_ {2} \\ . \\ . \\ . \\ \beta_ {n - 1} \\ \beta_ {n} \end{array} \right], \quad \mathbf {C} = [ 1 \quad 0 \quad \dots \quad 0 ], \quad D = \beta_ {0} = b _ {0} \\ \end{array}
$$

In this state-space representation, matrices A and C are exactly the same as those for the system of Equation (2–30).The derivatives on the right-hand side of Equation (2–33) affect only the elements of the B matrix.

Note that the state-space representation for the transfer function

$$\frac {Y (s)}{U (s)} = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n - 1} s + b _ {n}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}}$$

is given also by Equations (2–37) and (2–38).

There are many ways to obtain state-space representations of systems. Methods for obtaining canonical representations of systems in state space (such as controllable canonical form, observable canonical form, diagonal canonical form, and Jordan canonical form) are presented in Chapter 9.

MATLAB can also be used to obtain state-space representations of systems from transfer-function representations, and vice versa.This subject is presented in Section 2–6.
