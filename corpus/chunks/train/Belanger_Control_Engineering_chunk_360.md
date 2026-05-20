6.8 Drum speed control In Problem 3.46 (Chapter 3), the drum speed control system is divided into two independent subsystems: one with a common-mode input $u_{c}$ and an output $\omega_0$ , and the other with a differential-mode input $u_{d}$ and an output $\omega_1 - \omega_2$ . Each system is characterized by a pair of underdamped poles.

In line with the idea outlined in Problem 6.7 for dealing with underdamped poles, the following compensators are proposed:

$$F _ {1} (s) = k _ {1} \frac {(- s + 2 5 0 \pm j 2 5 0)}{(s + 8 0 0) ^ {2}}$$

for the subsystem with $u_{c}$ as input, and

$$F _ {2} (s) = k _ {2} \frac {(s + 2 5 0 \pm j 2 5 0)}{(s + 8 0 0) ^ {2}}$$

for the other subsystems. For each subsystem:

a. Obtain the Root Locus.   
b. Select the value of $k_{i}, i = 1$ or 2, for which the lowest of the damping factors associated with any pair of complex poles is maximized (approximately).   
c. Sketch the block diagram for the complete (multivariable) control system.   
d. Obtain (closed-loop) responses for unit-step changes in the references to $\omega_0$ and $\omega_{1} - \omega_{2}$ .

6.9 Maglev In Problem 3.22 (Chapter 3), the inputs to the Maglev vehicle were redefined in terms of three new inputs: the levitation common-mode $(\Delta u_{LC})$ and differential-mode $(\Delta u_{LD})$ inputs, and the guidance differential-mode $(\Delta u_{GD})$ input. It was shown that the heave mode is affected only by $\Delta u_{LC}$ , and that the transfer function has two real poles located symmetrically with respect to the origin.

a. Use a compensator $k[(s + p) / (s + 2p)]$ of the plant, where $-p$ is the stable pole, and select $k$ so that the closed-loop poles have $\zeta = \sqrt{2/2}$ .   
b. For an initial state $\Delta z(0) = a$ , $\Delta v_z(0) = 0$ , what is the largest value of $a$ such that (i) $|\Delta u_{LC}| \leq 600$ and (ii) $|\Delta z(t)| \leq .014$ ?

6.10 Maglev Following upon Problem 6.9, we wish to control the other two degrees of freedom. It makes physical sense to control $\Delta y$ (lateral motion) with $\Delta u_{GD}$ and $\Delta \theta$ (roll) with $\Delta u_{LD}$ . This time, however, it is not true that $\Delta u_{GD}$ affects only $\Delta y$ and $\Delta u_{LD}$ affects only $\Delta \theta$ , but we ignore this cross-coupling in the first instance.
