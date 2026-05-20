$$
\mathbf {x} (t) = e ^ {- 2 t} \beta \left[ \begin{array}{c} 1 \\ - 1 \end{array} \right].
$$

(The reader is invited to check this by calculating $\mathbf{x}(t)$ as $e^{At}\mathbf{x}_0$ .)

In terms of the circuit, the first modal vector corresponds to equal voltages on the capacitances. With $i_{s}=0$ , the voltages remain equal and there is no current through the two top resistances, so both voltages decay according to the RC=1 time constant.

The second modal vector corresponds to an initial state where the two voltages are equal but of opposite signs. The symmetry of the network forces them to remain so. Since $x_{2}(t) = -x_{1}(t)$ , the current leaving node 1 through the two top resistances is $(2x_{1}) / 2R = (x_{1}) / R$ . The total current drawn from the capacitance at node 1 is thus $(2x_{1}) / R$ , for an effective time constant of $\frac{R}{2} C = \frac{1}{2}$ ; this explains the mode -2.
