# PROBLEMS

3.1 In sampling a continuous-time process model with h = 1 the following pulse transfer function is obtained:

$$H (z) = \frac {z + 1 . 2}{z ^ {2} - z + 0 . 2 5}$$

The design specification states that the discrete-time closed-loop poles should correspond to the continuous-time characteristic polynomial

$$s ^ {2} + 2 s: 1$$

(a) Design a minimal-order discrete-time indirect self-tuning regulator. The controller should have integral action and give a closed-loop system having unit gain in stationary. Determine the Diophantine equation that solves the design problem.

(b) Suggest a design that includes direct estimation of the controller parameters. Discuss why a well-working direct self-tuning regulator is more difficult to design for this process than is an indirect self-tuning regulator.

3.2 Consider the process

$$G (s) = \frac {1}{s (s + a)}$$

where $\alpha$ is an unknown parameter. Assume that the desired closed-loop system is

$$G _ {m} (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

Construct continuous- and discrete-time indirect self-tuning algorithms for the system.

3.3 Consider the system

$$G (s) = G _ {1} (s) G _ {2} (s)$$

where

$$G _ {1} (s) = \frac {b}{s + a}G _ {2} (s) = \frac {c}{s + d}$$

where a and b are unknown parameters and c and d are known. Construct discrete-time direct and indirect self-tuning algorithms for the partially known system.

3.4 A process has the transfer function

$$G (s) = \frac {b}{s (s + 1)}$$

where b is a time-varying parameter. The system is controlled by a proportional controller

$$u (t) = k \left(u _ {c} (t) - y (t)\right)$$

It is desirable to choose the feedback gain so that the closed-loop system has the transfer function

$$G (s) = \frac {1}{s ^ {2} + s + 1}$$

Construct a continuous-time indirect self-tuning algorithm for the system.

3.5 The code for simulating Examples 3.4 and 3.5 is listed below. Study the code and try to understand the details.

DISCRETE SYSTEM reg

"Indirect Self-Tuning Regulator based on the model

“ H(q) = (b0\*q + b1) / (q^2 + a1\*q + a2)

"using standard RLS estimation and pole placement design

"Polynomial B is canceled if cancel>0.5

INPUT ysp y "set point and process output

OUTPUT u "control variable

STATE ysp1 y1 u1 v1 "controller states

STATE th1 th2 th3 th4 "parameter estimates

STATE f1 f2 f3 f4 "regression variables

STATE p11 p12 p13 p14 "covariance matrix

STATE p22 p23 p24

STATE p33 p34

STATE p44

NEW nysp1 ny1 nu1 nv1
