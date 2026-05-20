# Controllability and Reachability

Consider the system

$$
\begin{array}{l} \begin{array}{l} x (k + 1) = \Phi x (k) + \Gamma u (k) \\ (k) = C _ {0} (k) \end{array} \tag {3.15} \\ y (k) = C x (k) \\ \end{array}
$$

Assume that the initial state $x(0)$ is given. The state at time $n$ , where $n$ is the order of the system, is given by

$$
\begin{array}{l} x (n) = \Phi^ {n} x (0) + \Phi^ {n - 1} \Gamma u (0) + \dots + \Gamma u (n - 1) \tag {3.16} \\ = \Phi^ {n} x (0) + W _ {c} U \\ \end{array}
$$

where

$$
\begin{array}{l} W _ {c} = \left( \begin{array}{l l l l} \Gamma & \Phi \Gamma & \dots & \Phi^ {n - 1} \Gamma \end{array} \right) \\ U = \left( \begin{array}{l l l} u ^ {T} (n - 1) & \dots & u ^ {T} (0) \end{array} \right) ^ {T} \\ \end{array}
$$

[Compare with Eq. (2.17).] If $W_{c}$ has rank n, then it is possible to find n equations from which the control signals can be found such that the initial state is transferred to the desired final state $x(n)$ . Notice that the solution is not unique if there is more than one input signal. In the literature, controllability is defined in different ways; the following definition will be used in this text.

DEFINITION 3.7 CONTROLLABILITY The system (3.15) is controllable if it is possible to find a control sequence such that the origin can be reached from any initial state in finite time.

A concept related to controllability is reachability, which is defined as follows.

DEFINITION 3.8 REACHABILITY The system (3.15) is reachable if it is possible to find a control sequence such that an arbitrary state can be reached from any initial state in finite time.

The two concepts, however, are equivalent if $\Phi$ is invertible. Reachability will be discussed here primarily. Controllability does not imply reachability, which is seen from (3.16). If $\Phi^{n}x(0)=0$ , then the origin will be reached with zero input but the system is not necessarily reachable.

The following theorem follows from the preceding definition and calculations.

THEOREM 3.7 REACHABILITY The system (3.15) is reachable if and only if the matrix $W_{c}$ has rank $n$ .

Remark. The matrix $W_{c}$ is usually referred to as the controllability matrix because of its analogy with continuous-time systems.
