$$
y = \left[ \begin{array}{c c c c} 1 & 0 & \dots & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ . \\ . \\ . \\ x _ {n} \end{array} \right]
$$

or

$$y = \mathbf {C x} \tag {2-32}$$

where

$$
\mathbf {C} = \left[ \begin{array}{c c c c} 1 & 0 & \dots & 0 \end{array} \right]
$$

[Note that D in Equation (2–24) is zero.] The first-order differential equation, Equation (2–31), is the state equation, and the algebraic equation, Equation (2–32), is the output equation.

Note that the state-space representation for the transfer function system

$$\frac {Y (s)}{U (s)} = \frac {1}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}}$$

is given also by Equations (2–31) and (2–32).

State-Space Representation of nth-Order Systems of Linear Differential Equations in which the Forcing Function Involves Derivative Terms. Consider the differential equation system that involves derivatives of the forcing function, such as

$$y ^ {(n)} + a _ {1} ^ {(n - 1)} y + \dots + a _ {n - 1} \dot {y} + a _ {n} y = b _ {0} ^ {(n)} u + b _ {1} ^ {(n - 1)} u + \dots + b _ {n - 1} \dot {u} + b _ {n} u \tag {2-33}$$

The main problem in defining the state variables for this case lies in the derivative terms of the input u. The state variables must be such that they will eliminate the derivatives of u in the state equation.

One way to obtain a state equation and output equation for this case is to define the following n variables as a set of n state variables:

$$
\begin{array}{l} x _ {1} = y - \beta_ {0} u \\ x _ {2} = \dot {y} - \beta_ {0} \dot {u} - \beta_ {1} u = \dot {x} _ {1} - \beta_ {1} u \\ x _ {3} = \ddot {y} - \beta_ {0} \dot {u} - \beta_ {1} \dot {u} - \beta_ {2} u = \dot {x} _ {2} - \beta_ {2} u \\ x _ {n} = \stackrel {(n - 1)} {y} - \beta_ {0} u - \beta_ {1} u - \dots - \beta_ {n - 2} \dot {u} - \beta_ {n - 1} u = \dot {x} _ {n - 1} - \beta_ {n - 1} u \\ \end{array}
$$

(2–34)

where $\beta _ { 0 } , \beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { n - 1 }$ are determined from

$$\beta_ {0} = b _ {0}\beta_ {1} = b _ {1} - a _ {1} \beta_ {0}\beta_ {2} = b _ {2} - a _ {1} \beta_ {1} - a _ {2} \beta_ {0}\beta_ {3} = b _ {3} - a _ {1} \beta_ {2} - a _ {2} \beta_ {1} - a _ {3} \beta_ {0} \tag {2-35}\beta_ {n - 1} = b _ {n - 1} - a _ {1} \beta_ {n - 2} - \dots - a _ {n - 2} \beta_ {1} - a _ {n - 1} \beta_ {0}$$

With this choice of state variables the existence and uniqueness of the solution of the state equation is guaranteed. (Note that this is not the only choice of a set of state variables.) With the present choice of state variables, we obtain
