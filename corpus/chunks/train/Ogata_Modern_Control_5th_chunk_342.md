text(-2.8,1.2,'Uncompensated system')

text(-2.8,0.58,'Original closed-loop pole')

text(-0.1,0.85,'New closed-')

text(-0.1,0.62,'loop pole')

title('Root-Locus Plots of Compensated and Uncompensated Systems')

hold

Current plot released

% **** Plot root loci of the compensated system near the origin ****

rlocus(numc,denc)

v = [-0.6 0.6 -0.6 0.6]; axis(v); axis('square')

grid

title('Root-Locus Plot of Compensated System near the Origin')

If the damping ratio of the new dominant closed-loop poles is kept the same, then these poles are obtained from the new root-locus plot as follows:

$$s _ {1} = - 0. 3 1 + j 0. 5 5, \quad s _ {2} = - 0. 3 1 - j 0. 5 5$$

The open-loop gain K is determined from the magnitude condition as follows:

$$
\begin{array}{l} K = \left| \frac {s (s + 0 . 0 0 5) (s + 1) (s + 2)}{s + 0 . 0 5} \right| _ {s = - 0. 3 1 + j 0. 5 5} \\ = 1. 0 2 3 5 \\ \end{array}
$$

Then the lag compensator gain $\hat { K } _ { c }$ is determined as

$$\hat {K} _ {c} = \frac {K}{1 . 0 6} = \frac {1 . 0 2 3 5}{1 . 0 6} = 0. 9 6 5 6$$

Thus the transfer function of the lag compensator designed is

$$G _ {c} (s) = 0. 9 6 5 6 \frac {s + 0 . 0 5}{s + 0 . 0 0 5} = 9. 6 5 6 \frac {2 0 s + 1}{2 0 0 s + 1} \tag {6-20}$$

Then the compensated system has the following open-loop transfer function:

$$
\begin{array}{l} G _ {1} (s) = \frac {1 . 0 2 3 5 (s + 0 . 0 5)}{s (s + 0 . 0 0 5) (s + 1) (s + 2)} \\ = \frac {5 . 1 2 (2 0 s + 1)}{s (2 0 0 s + 1) (s + 1) (0 . 5 s + 1)} \\ \end{array}
$$

The static velocity error constant $K _ { v }$ is

$$K _ {v} = \lim _ {s \rightarrow 0} s G _ {1} (s) = 5. 1 2 \sec^ {- 1}$$

In the compensated system, the static velocity error constant has increased to $5 . 1 2 \ \mathrm { s e c } ^ { - 1 }$ , or $5 . 1 2 / 0 . 5 3 = 9 . 6 6$ times the original value. (The steady-state error with ramp inputs has decreased to about 10% of that of the original system.) We have essentially accomplished the design objective of increasing the static velocity error constant to $5 \sec ^ { - 1 }$ .

Note that, since the pole and zero of the lag compensator are placed close together and are located very near the origin, their effect on the shape of the original root loci has been small. Except for the presence of a small closed root locus near the origin, the root loci of the compensated and the uncompensated systems are very similar to each other. However, the value of the static velocity error constant of the compensated system is 9.66 times greater than that of the uncompensated system.
