# 2–5 STATE-SPACE REPRESENTATION OF SCALAR DIFFERENTIAL EQUATION SYSTEMS

A dynamic system consisting of a finite number of lumped elements may be described by ordinary differential equations in which time is the independent variable. By use of vector-matrix notation, an nth-order differential equation may be expressed by a firstorder vector-matrix differential equation. If n elements of the vector are a set of state variables, then the vector-matrix differential equation is a state equation. In this section we shall present methods for obtaining state-space representations of continuous-time systems.

State-Space Representation of nth-Order Systems of Linear Differential Equations in which the Forcing Function Does Not Involve Derivative Terms. Consider the following nth-order system:

$$y ^ {(n)} + a _ {1} y ^ {(n - 1)} + \dots + a _ {n - 1} \dot {y} + a _ {n} y = u \tag {2-30}$$

Noting that the knowledge of $y ( 0 ) , { \dot { y } } ( 0 ) , \dots , { \overset { ( n - 1 ) } { y } } ( 0 )$ together with the input, $u ( t )$ for $t \geq 0$ , determines completely the future behavior of the system, we may take (n - 1) $y ( t ) , \dot { y } ( t ) , \dot { \ldots } , \dot { y } ^ { \prime } ( t )$ as a set of n state variables. (Mathematically, such a choice of state variables is quite convenient. Practically, however, because higher-order derivative terms are inaccurate, due to the noise effects inherent in any practical situations, such a choice of the state variables may not be desirable.)

Let us define

$$
\begin{array}{l} x _ {1} = y \\ x _ {2} = \dot {y} \\ x _ {n} = \begin{array}{c} (n - 1) \\ y \end{array} \\ \end{array}
$$

Then Equation (2–30) can be written as

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {n - 1} = x _ {n} \\ \dot {x} _ {n} = - a _ {n} x _ {1} - \dots - a _ {1} x _ {n} + u \\ \end{array}
$$

or

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {2-31}$$

where

$$
\begin{array}{l} \mathbf {x} = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right], \\ \mathbf {A} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right], \\ \mathbf {B} = \left[ \begin{array}{c} 0 \\ 0 \\ \cdot \\ \cdot \\ \cdot \\ 0 \\ 1 \end{array} \right] \\ \end{array}
$$

The output can be given by
