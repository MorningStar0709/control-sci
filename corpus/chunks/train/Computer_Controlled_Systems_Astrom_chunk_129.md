# Example 2.13 Double integrator with time delay

Use h = 1 for the double integrator and introduce a time delay of 0.5 s. Then from (2.10) and Example 2.7,

$$
\begin{array}{l} H (q) = C (q I - \Phi) ^ {- 1} (\Gamma_ {0} + \Gamma_ {1} q ^ {- 1}) \\ = \left( \begin{array}{l l} 1 & 0 \end{array} \right) \frac {\left( \begin{array}{c c} q - 1 & - 1 \\ 0 & q - 1 \end{array} \right)}{(q - 1) ^ {2}} \binom{0. 1 2 5 + 0. 3 7 5 q ^ {- 1}}{0. 5 + 0. 5 q ^ {- 1}} \\ = \frac {0 . 1 2 5 (q ^ {2} + 6 q + 1)}{q (q ^ {2} - 2 q + 1)} = \frac {0 . 1 2 5 (q ^ {1} + 6 q ^ {- 2} + q ^ {- 3})}{1 - 2 q ^ {- 1} + q ^ {- 2}} \\ \end{array}
$$

Section 2.5 shows that different state-space representations can be used. Of course, this does not change the input-output model.

THEOREM 2.4 INVARIANCE OF THE PULSE-TRANSFER OPERATOR The pulse-transfer operator $H(q)$ for the state-space model (2.16) is independent of the state-space representation.

Proof. Given the pulse-transfer operator

$$H (q) = C (q I - \Phi) ^ {- 1} \Gamma + D$$

and a transformation matrix T. In the new coordinates

$$
\begin{array}{l} \tilde {H} (q) = \tilde {C} (q I - \tilde {\Phi}) ^ {- 1} \tilde {\Gamma} + \tilde {D} = C T ^ {- 1} (q T T ^ {- 1} - T \Phi T ^ {- 1}) ^ {- 1} T \Gamma + D \\ = C T ^ {- 1} \left(T (q I - \Phi) T ^ {- 1}\right) ^ {- 1} T \Gamma + D = C T ^ {- 1} T (q I - \Phi) ^ {- 1} T ^ {- 1} T \Gamma + D \\ = C (q I - \Phi) ^ {- 1} \Gamma + D = H (q) \\ \end{array}
$$

The input-output models of a system with a zero-order hold can be obtained by using (2.5) and (2.26). In order to simplify the computation of the pulse-transfer operator $H(q)$ , it is convenient to use Table 2.1, which gives $H(q)$ for some standard systems.

Programs for computer algebra such as Maple $^{®}$ and Mathematica $^{®}$ are very convenient for performing sampling because the result is obtained in algebraic form and it can easily be converted to computer code. This approach makes tables obsolete and it also reduces the potential sources of mistakes in manual calculations.
