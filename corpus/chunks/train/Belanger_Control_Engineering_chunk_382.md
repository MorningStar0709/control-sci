# Example 7.3 (Pendulum on a Cart)

Design a state feedback gain to place the closed-loop poles of the inverted pendulum system of Example 2.9, with the numerical values used in Example 2.5 (Chapter 2) at the locations -4.43, -4.43, and $-2 \pm 2j$ . Give the control law for regulation to the vertical equilibrium state.

Solution The linearized state space representation is

$$
\frac {d}{d t} \left[ \begin{array}{c} x \\ v \\ \theta \\ \omega \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & - 9. 8 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 9. 6 & 0 \end{array} \right] \left[ \begin{array}{c} x \\ v \\ \theta \\ \omega \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \\ 0 \\ - 1 \end{array} \right] u.
$$

With

$$
s I - A = \left[ \begin{array}{c c c c} s & - 1 & 0 & 0 \\ 0 & s & 9. 8 & 0 \\ 0 & 0 & s & - 1 \\ 0 & 0 & - 1 9. 6 & s \end{array} \right]
$$

we compute

$$\det (s I - A) = s ^ {2} (s ^ {2} - 1 9. 6).$$

The open-loop poles are at 0, 0, and ±4.43. We now calculate

$$
A d j (s I - A) = \left[ \begin{array}{c c c c} x & s ^ {2} - 1 9. 6 & x & - 9. 8 \\ x & s (s ^ {2} - 1 9. 6) & x & - 9. 8 s \\ x & 0 & x & s ^ {2} \\ x & 0 & x & s ^ {3} \end{array} \right]
$$

and

$$
\begin{array}{l} \mathbf {k} ^ {T} A d j (s I - A) \mathbf {b} = [ k _ {1} \quad k _ {2} \quad k _ {3} \quad k _ {4} ] \left[ \begin{array}{c} s ^ {2} - 9. 8 \\ s ^ {3} - 9. 8 s \\ - s ^ {2} \\ - s ^ {3} \end{array} \right] \\ = k _ {1} \left(s ^ {2} - 9. 8\right) + k _ {2} \left(s ^ {3} - 9. 8 s\right) - k _ {3} s ^ {2} - k _ {4} s ^ {3}. \\ \end{array}
$$

The desired characteristic polynomial is

$$
\begin{array}{l} p (s) = (s + 4. 4 3) ^ {2} (s + 2 + 2 j) (s + 2 - 2 j) \\ = s ^ {4} + 1 2. 8 6 s ^ {3} + 6 3. 0 4 s ^ {2} + 1 4 9. 3 s + 1 5 7. 8. \\ \end{array}
$$

Applying Equation 7.18,

$$
\begin{array}{l} p (s) ^ {\cdot} = s ^ {4} - 1 9. 6 s ^ {2} + k _ {1} \left(s ^ {2} - 9. 8\right) + k _ {2} \left(s ^ {3} - 9. 8 s\right) - k _ {3} s ^ {2} - k _ {4} s ^ {3} \\ = s ^ {4} + \left(k _ {2} - k _ {4}\right) s ^ {3} + \left(- 1 9. 6 + k _ {1} - k _ {3}\right) s ^ {2} - 9. 8 k _ {2} s - 9. 8 k _ {1}. \\ \end{array}
$$

Matching coefficients yields

$$
\begin{array}{l} k _ {2} - k _ {4} = 1 2. 8 6 \\ - 1 9. 6 + k _ {1} - k _ {3} = 6 3. 0 4 \\ - 9. 8 k _ {2} = 1 4 9. 3 \\ - 9. 8 k _ {1} = 1 5 7. 8 \\ \end{array}
$$

which leads to

$$k _ {1} = - 1 6, \quad k _ {2} = - 1 5. 2, \quad k _ {3} = - 9 8. 6, \quad k _ {4} = - 2 8. 1.$$

Here, the desired dc steady state is the origin; i.e., $x^{*} = u^{*} = 0$ .

The control law is

$$u = 1 6 x + 1 5. 2 v + 9 8. 6 \theta + 2 8. 1 \omega .$$

Figure 7.4 shows the state and input response for an initial state $\theta(0) = 15^{\circ} = 0.26$ rad, $v(0) = x(0) = \omega(0) = 0$ .
