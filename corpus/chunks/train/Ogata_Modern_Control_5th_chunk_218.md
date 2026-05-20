Figure 5–21 Unit-step response curve.

Obtaining Three-Dimensional Plot of Unit-Step Response Curves with MATLAB. MATLAB enables us to plot three-dimensional plots easily.The commands to obtain three-dimensional plots are “mesh” and “surf.” The difference between the “mesh” plot and “surf” plot is that in the former only the lines are drawn and in the latter the spaces between the lines are filled in by colors. In this book we use only the “mesh” command.

EXAMPLE 5–4 Consider the closed-loop system defined by

$$\frac {C (s)}{R (s)} = \frac {1}{s ^ {2} + 2 \zeta s + 1}$$

(The undamped natural frequency $\omega _ { n }$ is normalized to 1.) Plot unit-step response curves c(t) when z assumes the following values:

$$\zeta = 0, 0. 2, 0. 4, 0. 6. 0. 8, 1. 0$$

Also plot a three-dimensional plot.

An illustrative MATLAB Program for plotting a two-dimensional diagram and a threedimensional diagram of unit-step response curves of this second-order system is given in MATLAB Program 5–6. The resulting plots are shown in Figures 5–22(a) and (b), respectively. Notice that we used the command mesh(t,zeta,y') to plot the three-dimensional plot.We may use a command mesh(y') to get the same result. [Note that command mesh(t,zeta,y) or mesh(y) will produce a three-dimensional plot the same as Figure 5–22(b), except that x axis and y axis are interchanged. See Problem A–5–15.]

When we want to solve a problem using MATLAB and if the solution process involves many repetitive computations, various approaches may be conceived to simplify the MATLAB program.A frequently used approach to simplify the computation is to use “for loops.” MATLAB Program 5–6 uses such a “for loop.” In this book many MATLAB programs using “for loops” are presented for solving a variety of problems. Readers are advised to study all those problems carefully to familiarize themselves with the approach.
