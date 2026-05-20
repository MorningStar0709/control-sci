# Example 6.12 (dc Servo)

Design a PID controller for the dc servo that satisfies the crossover-frequency and phase-margin specifications of Example 6.10.

Solution We begin with a PD controller. As in Example 6.10, we must provide $34.2^{\circ}$ of phase lead at $\omega = 3$ .

$$\neq (j 3 T _ {2} + 1) = \tan^ {- 1} 3 T _ {2} = 3 4. 2 ^ {\circ}T _ {2} = 0. 2 2 6 \mathrm{s}.$$

The PI term is such that $\frac{1}{j\omega T_1} + 1 \approx 1$ at crossover, i.e.,

$$\frac {1}{3 T _ {1}} = \alpha \ll 1.$$

Take $\alpha = 0.1$ , so that $T_{1} = 3.33$ s.

We need a loop gain of unit magnitude at $\omega = 3$ ; since $|L(j3)| = -12.6$ db, the controller must contribute 12.6 db, or 4.26, at $\omega = 3$ . Thus,

$$k \left| \frac {1}{j (3 . 3 3) (3)} + 1 \right| | j (3) (. 2 2 6) + 1 | = 4. 2 6$$

or

$$k = \frac {4 . 2 6}{(1 . 0 0 5) (1 . 2 0 8)} = 3. 5 1.$$

Therefore,

$$
\begin{array}{l} G _ {c} (s) = 3. 5 1 \left(\frac {1}{3 . 3 3 s} + 1\right) (0. 2 2 6 s + 1) \\ = 3. 7 5 \left(1 + \frac {1}{3 . 5 5 6 s} + 0. 2 1 1 s\right). \\ \end{array}
$$
