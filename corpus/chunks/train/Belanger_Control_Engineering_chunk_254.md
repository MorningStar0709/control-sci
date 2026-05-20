# Example 5.8 (Active Suspension)

To demonstrate the application of the Root Locus method to study the effect of a parameter other than the control gain, consider the suspension system of Example 2.2 (Chapter 2), without the active input force u. Calculate the spring constant $K_{1}$ such that a 30-kg increase in the mass M results in a 3-cm change in $x_{1}$ . For that value of $K_{1}$ and for the values of M, m, and $K_{2}$ given in the example, plot the Root Locus of the system poles as the damping factor D varies. Find the value of D for which the least damped complex poles have the minimum (most negative) real part.

Solution The steady-state calculation is performed in Example 2.7, where it is shown that

$$x _ {1} ^ {*} = x _ {1 0} + x _ {2 0} = \frac {M g}{K _ {1}} - \frac {m + M}{K _ {2}} g.$$

![](image/4bb36cd17bbb587d9bab93f1ca51c37c8c13571cf21bcbe1a1e865f55cd4b87e.jpg)

<details>
<summary>natural_image</summary>

Pure Cartesian coordinate system with arrows and circles, no text or symbols present
</details>

Figure 5.6 Root locus, pendulum on cart

The specifications require that

$$0. 0 3 m = \frac {(3 0 \mathrm{kg}) (9 . 8 \mathrm{m} / \mathrm{s} ^ {2})}{K _ {\mathrm{i}}}\text { or } \quad K _ {1} = 9 8 0 0 \mathrm{N/m}.$$

The study of the system natural frequencies requires only the homogeneous system, which is

$$
\frac {d}{d t} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ v _ {1} \\ v _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ \frac {- K _ {1}}{M} & \frac {K _ {1}}{M} & \frac {- D}{M} & \frac {D}{M} \\ \frac {K _ {1}}{m} & \frac {- (K _ {1} + K _ {2})}{m} & \frac {D}{m} & \frac {- D}{m} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ v _ {1} \\ v _ {2} \end{array} \right]
$$

Substitution of the known values yields

$$
\frac {d}{d t} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ v _ {1} \\ v _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ - 3 2. 6 6 7 & 3 2. 6 6 7 & \frac {- D}{3 0 0} & \frac {D}{3 0 0} \\ 1 9 6 & - 7 9 6 & \frac {D}{5 0} & \frac {- D}{5 0} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ v _ {1} \\ v _ {2} \end{array} \right]
$$

At this point, it is possible to calculate the characteristic polynomial $\det(sI-A)$ in the form $Q(s)+DN(s)$ . This is not too onerous in this $4\times4$ case, but a larger matrix would probably need a symbolic manipulation program. We choose to follow a different route and write the state equations in such a way as to make
