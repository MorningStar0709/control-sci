# Example 7.12 (dc Servo)

The dc servo of Example 2.1 (Chapter 2) is provided with an angle sensor $(\theta)$ only—for example, a shaft encoder. We wish to estimate the states $\omega$ and $i$ and, in addition, the value of a load torque known to be constant. The eigenvalues of the error system are to be located at $-5 \pm j5$ , and $-7 \pm j7$ (somewhat faster than the system eigenvalues). Design an observer, and compute the state variables and their estimates for $v(t) = \sin t$ , $T_L = 1$ N, $\theta(0) = 1$ rad, $\omega(0) = 1$ rad/s, $i(0) = 0$ , and zero initial state for the observer.

Solution Including the (constant) disturbance state equation $\dot{z}=0$ , $T_{L}=z$ , the system is described by

$$
\frac {d}{d t} \left[ \begin{array}{c} \theta \\ \omega \\ i \\ z \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 4. 4 3 8 & - 7. 3 9 6 \\ 0 & - 1 2 & - 2 4 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \theta \\ \omega \\ i \\ z \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 2 0 \\ 0 \end{array} \right] v

y = \theta = \left[ \begin{array}{l l l l} 1 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \theta \\ \omega \\ i \\ z \end{array} \right].
$$

It can be verified that this system is observable.

The pole placement problem to be solved refers to the controllable system of Equation 7.62, resulting here in

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c c c} 0 & 0 & 0 & 0 \\ 1 & 0 & - 1 2 & 0 \\ 0 & 4. 4 3 8 & - 2 4 & 0 \\ 0 & - 7. 3 9 6 & 0 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} 1 \\ 0 \\ 0 \\ 0 \end{array} \right] u.
$$

This example is simple enough to yield to solution by hand. We have

$$
s I - A ^ {T} = \left[ \begin{array}{c c c c} s & 0 & 0 & 0 \\ - 1 & s & 1 2 & 0 \\ 0 & - 4. 4 3 8 & s + 2 4 & 0 \\ 0 & 7. 3 9 6 & 0 & s \end{array} \right]
\det (s I - A ^ {T}) = s ^ {2} (s ^ {2} + 2 4 s + 5 3. 2 5 6)
$$

and

$$
A d j (s I - A ^ {T}) = \left[ \begin{array}{c c c c} s (s ^ {2} + 2 4 s + 5 3. 2 5 6 & x & x & x \\ s (s + 2 4) & x & x & x \\ 4. 4 3 8 s & x & x & x \\ - 7. 3 9 6 (s + 2 4) & x & x & x \end{array} \right]
$$

Note that only the first column is needed, because the b vector's only nonzero entry is the first one.

Using Equation 7.18,

$$
\begin{array}{l} \det (s I - A ^ {T}) + k ^ {T} \operatorname{Adj} (s I - A ^ {T}) C = s ^ {4} + 2 4 s ^ {3} + 5 3. 2 5 6 s ^ {2} \\ + k _ {1} \left(s ^ {3} + 2 4 s ^ {2} + 5 3. 2 5 6 s\right) + k _ {2} \left(s ^ {2} + 2 4 s\right) + k _ {3} (4. 4 3 8 s) + k _ {4} (- 7. 3 9 6 s - 1 7 7. 5). \\ \end{array}
$$

The desired closed-loop polynomial is
