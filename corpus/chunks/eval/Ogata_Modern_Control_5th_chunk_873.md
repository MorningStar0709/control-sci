# PROBLEMS

B–10–1. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

where

$$
\mathbf {A} = \left[ \begin{array}{r r r} - 1 & 0 & 1 \\ 1 & - 2 & 0 \\ 0 & 0 & - 3 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{l l l} 1 & 1 & 0 \end{array} \right]
$$

Transform the system equations into (a) controllable canonical form and (b) observable canonical form.

B–10–2. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

where

$$
\mathbf {A} = \left[ \begin{array}{r r r} - 1 & 0 & 1 \\ 1 & - 2 & 0 \\ 0 & 0 & - 3 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 1 \\ 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{l l l} 1 & 1 & 1 \end{array} \right]
$$

Transform the system equations into the observable canonical form.

B–10–3. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & - 5 & - 6 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 1 \\ 1 \end{array} \right]
$$

By using the state-feedback control it is desired tou = -Kx, have the closed-loop poles at Deter-s = -2 ; j4, s = -10. mine the state-feedback gain matrix K.

B–10–4. Solve Problem B–10–3 with MATLAB.

B–10–5. Consider the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] u
$$

Show that this system cannot be stabilized by the statefeedback control whatever matrix K is chosen.u = -Kx,

B–10–6. A regulator system has a plant

$$\frac {Y (s)}{U (s)} = \frac {1 0}{(s + 1) (s + 2) (s + 3)}$$

Define state variables as

$$x _ {1} = yx _ {2} = \dot {x} _ {1}x _ {3} = \dot {x} _ {2}$$

By use of the state-feedback control it is desiredu = -Kx, to place the closed-loop poles at

$$s = - 2 + j 2 \sqrt {3}, \quad s = - 2 - j 2 \sqrt {3}, \quad s = - 1 0$$

Determine the necessary state-feedback gain matrix K.

B–10–7. Solve Problem B–10–6 with MATLAB.

B–10–8. Consider the type 1 servo system shown in Figure 10–58. Matrices A, B, and C in Figure 10–58 are given by
