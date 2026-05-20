# PROBLEMS

B–7–1. Consider the unity-feedback system with the openloop transfer function:

$$G (s) = \frac {1 0}{s + 1}$$

Obtain the steady-state output of the system when it is subjected to each of the following inputs:

(a) $r ( t ) = \sin \left( t + 3 0 ^ { \circ } \right)$   
(b) $r ( t ) = 2 \cos ( 2 t - 4 5 ^ { \circ } )$   
$\begin{array} { r l } { \mathbf { ( c ) } } & { { } r ( t ) = \sin { \left( t + 3 0 ^ { \circ } \right) } - 2 \cos { \left( 2 t - 4 5 ^ { \circ } \right) } } \end{array}$

B–7–2. Consider the system whose closed-loop transfer function is

$$\frac {C (s)}{R (s)} = \frac {K \left(T _ {2} s + 1\right)}{T _ {1} s + 1}$$

Obtain the steady-state output of the system when it is subjected to the input r(t)=R sin vt.

B–7–3. Using MATLAB, plot Bode diagrams of $G _ { 1 } ( s )$ and $G _ { 2 } ( s )$ given below.

$$G _ {1} (s) = \frac {1 + s}{1 + 2 s}G _ {2} (s) = \frac {1 - s}{1 + 2 s}$$

$G _ { 1 } ( s )$ is a minimum-phase system and $G _ { 2 } ( s )$ is a nonminimum-phase system.

B–7–4. Plot the Bode diagram of

$$G (s) = \frac {1 0 (s ^ {2} + 0 . 4 s + 1)}{s (s ^ {2} + 0 . 8 s + 9)}$$

B–7–5. Given

$$G (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

show that

$$\left| G (j \omega_ {n}) \right| = \frac {1}{2 \zeta}$$

B–7–6. Consider a unity-feedback control system with the following open-loop transfer function:

$$G (s) = \frac {s + 0 . 5}{s ^ {3} + s ^ {2} + 1}$$

This is a nonminimum-phase system. Two of the three open-loop poles are located in the right-half s plane as follows:

Open-loop poles at s = -1.4656

$$s = 0. 2 3 2 8 + j 0. 7 9 2 6s = 0. 2 3 2 8 - j 0. 7 9 2 6$$

Plot the Bode diagram of G(s) with MATLAB. Explain why the phase-angle curve starts from $0 ^ { \circ }$ and approaches ±180°. B–7–7. Sketch the polar plots of the open-loop transfer function

$$G (s) H (s) = \frac {K \left(T _ {a} s + 1\right) \left(T _ {b} s + 1\right)}{s ^ {2} (T s + 1)}$$

for the following two cases:

(a)

(b)

B–7–8. Draw a Nyquist locus for the unity-feedback control system with the open-loop transfer function

$$G (s) = \frac {K (1 - s)}{s + 1}$$

Using the Nyquist stability criterion, determine the stability of the closed-loop system.

B–7–9. A system with the open-loop transfer function

$$G (s) H (s) = \frac {K}{s ^ {2} \left(T _ {1} s + 1\right)}$$

is inherently unstable.This system can be stabilized by adding derivative control. Sketch the polar plots for the open-loop transfer function with and without derivative control.

B–7–10. Consider the closed-loop system with the following open-loop transfer function:
