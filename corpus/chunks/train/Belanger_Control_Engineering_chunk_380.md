# Example 7.2 (dc Servo)

For the dc servo of Example 2.1 (Chapter 2), compute the state feedback gain that places the closed-loop poles at $-3 \pm 3j$ and -24. Give the control law for regulation to a set $\theta = \theta_{d}$ , and write the closed-loop transfer function $\theta/\theta_{d}$ .

Solution The state equation is Equation 2.19, where

$$
A = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 4. 4 3 8 \\ 0 & - 1 2 & - 2 4 \end{array} \right]; \quad \mathbf {b} = \left[ \begin{array}{c} 0 \\ 0 \\ 2 0 \end{array} \right].
$$

The open-loop eigenvalues are 0, -2.424, and -21.576, so the open-loop characteristic polynomial is

$$\det (s I - A) = s (s + 2. 4 2 4) (s + 2 1. 5 7 6)= s ^ {3} + 2 4 s ^ {2} + 5 3. 3 7 s.$$

To apply Equation 7.18, we must calculate

$$
\begin{array}{l} A d j (s I - A) \mathbf {b} = A d j \left[ \begin{array}{c c c} s & - 1 & 0 \\ 0 & s & - 4. 4 3 8 \\ 0 & 1 2 & s + 2 4 \end{array} \right] \left[ \begin{array}{l} 0 \\ 0 \\ 2 0 \end{array} \right] \\ = \left[ \begin{array}{c c c} x & x & 4. 4 3 8 \\ x & x & 4. 4 3 8 s \\ x & x & s ^ {2} \end{array} \right] \left[ \begin{array}{c} 0 \\ 0 \\ 2 0 \end{array} \right] \\ = \left[ \begin{array}{c} 8 8. 7 6 \\ 8 8. 7 6 s \\ 2 0 s ^ {2} \end{array} \right]. \\ \end{array}
$$

(Note that, by exploiting the structure of $\mathbf{b}$ , we save work by not calculating elements of the adjoint that will be multiplied by 0.)

We are now ready to apply Equation 7.18. The desired characteristic polynomial is

$$
\begin{array}{l} p (s) = (s + 2 4) (s + 3 + 3 j) (s + 3 - 3 j) \\ = (s ^ {3} + 3 0 s ^ {2} + 1 6 2 s + 4 3 2). \\ \end{array}
$$

We write Equation 7.18 as

$$
\begin{array}{l} s ^ {3} + 3 0 s ^ {2} + 1 6 2 s + 4 3 2 = s ^ {3} + 2 4 s ^ {2} + 5 3. 3 7 s + \left[ \begin{array}{c c c} k _ {1} & k _ {2} & k _ {3} \end{array} \right] \left[ \begin{array}{c} 8 8. 7 6 \\ 8 8. 7 6 s \\ 2 0 s ^ {2} \end{array} \right] \\ = s ^ {3} + (2 4 + 2 0 k _ {3}) s ^ {2} + (5 2. 0 5 8 + 8 8. 7 6 k _ {2}) s + 8 8. 7 6 k _ {1}. \\ \end{array}
$$

Equating coefficients yields

$$2 4 + 2 0 k _ {3} = 3 0 \quad \text { or } \quad k _ {3} = 0. 3 0 05 3. 3 7 + 8 8. 7 6 k _ {2} = 1 6 2 \quad \text { or } \quad k _ {2} = 1. 2 38 8. 7 6 k _ {1} = 4 3 2 \quad \text { or } \quad k _ {1} = 4. 8 6.$$

To calculate the control law, we need to compute the dc steady state corresponding to $\theta = \theta_{d}$ . Applying Equation 7.4,
