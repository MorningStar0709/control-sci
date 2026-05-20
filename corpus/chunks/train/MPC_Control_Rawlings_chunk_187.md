# Exercise 1.60: Disturbance models and offset

Consider the following two-input, three-output plant discussed in Example 1.11

$$x ^ {+} = A x + B u + B _ {p} py = C x$$

in which

$$
A = \left[ \begin{array}{c c c} 0. 2 6 8 1 & - 0. 0 0 3 3 8 & - 0. 0 0 7 2 8 \\ 9. 7 0 3 & 0. 3 2 7 9 & - 2 5. 4 4 \\ 0 & 0 & 1 \end{array} \right] \quad C = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right]

B = \left[ \begin{array}{c c} - 0. 0 0 5 3 7 & 0. 1 6 5 5 \\ 1. 2 9 7 & 9 7. 9 1 \\ 0 & - 6. 6 3 7 \end{array} \right] \quad B _ {p} = \left[ \begin{array}{c} - 0. 1 1 7 5 \\ 6 9. 7 4 \\ 6. 6 3 7 \end{array} \right]
$$

The input disturbance p results from a reactor inlet flowrate disturbance.

(a) Since there are two inputs, choose two outputs in which to remove steady-state offset. Build an output disturbance model with two integrators. Is your augmented model detectable?

(b) Implement your controller using $p = 0 . 0 1$ as a step disturbance at $k = 0 ,$ . Do you remove offset in your chosen outputs? Do you remove offset in any outputs?

(c) Can you find any two-integrator disturbance model that removes offset in two outputs? If so, which disturbance model do you use? If not, why not?
