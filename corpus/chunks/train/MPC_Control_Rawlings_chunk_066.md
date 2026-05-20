# 1.2 Models and Modeling

in which

$$
\widetilde {A} = \left[ \begin{array}{c c} A & 0 \\ 0 & 0 \end{array} \right] \qquad \widetilde {B} = \left[ \begin{array}{c} B \\ I \end{array} \right] \qquad \widetilde {C} = \left[ \begin{array}{c c} C & 0 \end{array} \right]
$$

A rate of change constraint such as

$$\underline {{\Delta}} \leq u (k) - u (k - 1) \leq \overline {{\Delta}} \quad k \in \mathbb {I} _ {\geq 0}$$

is then stated as

$$
F \widetilde {x} (k) + E u (k) \leq e \qquad F = \left[ \begin{array}{c c} 0 & - I \\ 0 & I \end{array} \right] \qquad E = \left[ \begin{array}{c} I \\ - I \end{array} \right] \qquad e = \left[ \begin{array}{c} \overline {{\Delta}} \\ - \underline {{\Delta}} \end{array} \right]
$$

To simplify analysis, it pays to maintain linear constraints when using linear dynamic models. So if we want to consider fairly general constraints for a linear system, we choose the form

$$F x (k) + E u (k) \leq e \quad k \in \mathbb {I} _ {\geq 0}$$

which subsumes all the forms listed previously.

When we consider nonlinear systems, analysis of the controller is not significantly simplified by maintaining linear inequalities, and we generalize the constraints to set membership

$$x (k) \in \mathbb {X} \quad u (k) \in \mathbb {U} \quad k \in \mathbb {I} _ {\geq 0}$$

or, more generally,

$$(x (k), u (k)) \in \mathbb {Z} \quad k \in \mathbb {I} _ {\geq 0}$$

We should bear in mind one general distinction between input constraints, and output or state constraints. The input constraints often represent physical limits. In these cases, if the controller does not respect the input constraints, the physical system enforces them. In contrast, the output or state constraints are usually desirables. They may not be achievable depending on the disturbances affecting the system. It is often the function of an MPC controller to determine in real time that the output or state constraints are not achievable, and relax them in some satisfactory manner. As we discuss in Chapter 2, these considerations lead implementers of MPC often to set up the optimization problem using hard constraints for the input constraints and some form of soft constraints for the output or state constraints.

![](image/a2efa44beb2bf316a7d7377e6403b0749475be1ce570968489a10f9054a3fa1b.jpg)

<details>
<summary>line</summary>

| time | y |
| --- | --- |
| 0 | -3.0 |
| 5 | -1.5 |
| 10 | -2.0 |
| 15 | -4.0 |
| 20 | -5.5 |
| 25 | -2.5 |
| 30 | -1.0 |
| 35 | 0.5 |
| 40 | 2.0 |
| 45 | 3.5 |
| 50 | 4.0 |
| 55 | 5.0 |
| 60 | 6.0 |
| 65 | 7.5 |
| 70 | 8.0 |
| 75 | 9.0 |
| 80 | 10.0 |
| 85 | 9.5 |
| 90 | 8.5 |
| 95 | 7.5 |
| 100 | 6.5 |
| 105 | 5.5 |
| 110 | 4.5 |
| 115 | 3.5 |
| 120 | 2.5 |
| 125 | 1.5 |
| 130 | 0.5 |
| 135 | -0.5 |
| 140 | -1.5 |
| 145 | -2.5 |
| 150 | -3.5 |
| 155 | -4.5 |
| 160 | -3.0 |
| 165 | -2.0 |
| 170 | -1.0 |
| 175 | -0.5 |
| 180 | -1.5 |
| 185 | -2.5 |
| 190 | -3.5 |
| 195 | -4.5 |
| 200 | -5.5 |
</details>

Figure 1.2: Output of a stochastic system versus time.
