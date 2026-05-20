# Exercise A.26: Controllability in continuous time

A linear, time-invariant, continuous time system

$$\frac {d x}{d t} = A x + B ux (0) = x _ {0} \tag {A.41}$$

is controllable if there exists an input $u ( t ) , 0 \leq t \leq t _ { 1 } , t _ { 1 } > 0$ that takes the system from any $x _ { 0 }$ at time zero to any $x _ { 1 }$ at some finite time $t _ { 1 }$ .

(a) Prove that the system in (A.41) is controllable if and only if

$$\operatorname{rank} (C) = n$$

in which C is, remarkably, the same controllability matrix that was defined for discrete time systems 1.17

$$
C = \left[ \begin{array}{c c c c} B & A B & \dots & A ^ {n - 1} B \end{array} \right]
$$

(b) Describe a calculational procedure for finding this required input.
