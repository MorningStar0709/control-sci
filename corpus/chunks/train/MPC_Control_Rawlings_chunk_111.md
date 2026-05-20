# Example 1.11: More measured outputs than inputs and zero offset

We consider a well-stirred chemical reactor depicted in Figure 1.6, as in Pannocchia and Rawlings (2003). An irreversible, first-order reaction A -→ B occurs in the liquid phase and the reactor temperature is regulated with external cooling. Mass and energy balances lead to the following nonlinear state space model:

$$
\begin{array}{l} \frac {d c}{d t} = \frac {F _ {0} c _ {0} - F c}{\pi r ^ {2} h} - k _ {0} \exp \left(- \frac {E}{R T}\right) c \\ \frac {d T}{d t} = \frac {F _ {0} (T _ {0} - T)}{\pi r ^ {2} h} + \frac {- \Delta H}{\rho C _ {p}} k _ {0} \exp \left(- \frac {E}{R T}\right) c + \frac {2 U}{r \rho C _ {p}} (T _ {c} - T) \\ \frac {d h}{d t} = \frac {F _ {0} - F}{\pi r ^ {2}} \\ \end{array}
$$

The controlled variables are h, the level of the tank, and c, the molar concentration of species A. The additional state variable is T , the reactor temperature; while the manipulated variables are $T _ { c }$ , the coolant liquid temperature, and F, the outlet flowrate. Moreover, it is assumed that the inlet flowrate acts as an unmeasured disturbance. The model parameters in nominal conditions are reported in Table 1.1. The openloop stable steady-state operating conditions are the following:

$$c ^ {s} = 0. 8 7 8 \mathrm{kmol} / \mathrm{m} ^ {3} \quad T ^ {s} = 3 2 4. 5 \mathrm{K} \quad h ^ {s} = 0. 6 5 9 \mathrm{m}T _ {c} ^ {s} = 3 0 0 \mathrm{K} \quad F ^ {s} = 0. 1 \mathrm{m} ^ {3} / \min$$

Using a sampling time of 1 min, a linearized discrete state space model is obtained and, assuming that all the states are measured, the state space variables are:

$$
x = \left[ \begin{array}{c} c - c ^ {s} \\ T - T ^ {s} \\ h - h ^ {s} \end{array} \right] \qquad u = \left[ \begin{array}{c} T _ {c} - T _ {c} ^ {s} \\ F - F ^ {s} \end{array} \right] \qquad y = \left[ \begin{array}{c} c - c ^ {s} \\ T - T ^ {s} \\ h - h ^ {s} \end{array} \right] \qquad p = F _ {0} - F _ {0} ^ {s}
$$

The corresponding linear model is:

$$x (k + 1) = A x (k) + B u (k) + B _ {p} py (k) = C x (k)$$

in which

$$
\begin{array}{l} A = \left[ \begin{array}{c c c} 0. 2 6 8 1 & - 0. 0 0 3 3 8 & - 0. 0 0 7 2 8 \\ 9. 7 0 3 & 0. 3 2 7 9 & - 2 5. 4 4 \\ 0 & 0 & 1 \end{array} \right] \qquad C = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \\ B = \left[ \begin{array}{c c} - 0. 0 0 5 3 7 & 0. 1 6 5 5 \\ 1. 2 9 7 & 9 7. 9 1 \\ 0 & - 6. 6 3 7 \end{array} \right] \qquad B _ {p} = \left[ \begin{array}{c} - 0. 1 1 7 5 \\ 6 9. 7 4 \\ 6. 6 3 7 \end{array} \right] \\ \end{array}
$$
