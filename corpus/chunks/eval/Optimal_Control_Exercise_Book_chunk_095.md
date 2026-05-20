3 2 5 2 3 2 1 1 \right] \tag {394}$$ By comparison with the previous gain, we notice that the absolute value of the parameters is higher;
this will result in a more ”aggressive” control.
The plot are the following, in the same order as the experiment before in the below plots.
![](image/7505dc58be837f10d5cb9485ca9a40cc095f438d96ba90eb9b2e6337bbdaf887.jpg) <details> <summary>line</summary> | Time [s] | x(t) [m] | x(t) [m/s] | Setpoint | | -------- | -------- | ---------- | -------- | | 0 | -1.2 | -1.2 | 0.0 | | 1 | -0.8 | 1.2 | 0.0 | | 2 | -0.4 | 0.5 | 0.0 | | 3 | -0.2 | 0.3 | 0.0 | | 4 | -0.1 | 0.1 | 0.0 | | 5 | -0.05 | 0.05 | 0.0 | | 6 | -0.02 | 0.02 | 0.0 | | 7 | -0.01 | 0.01 | 0.0 | | 8 | -0.005 | 0.005 | 0.0 | | 9 | -0.002 | 0.002 | 0.0 | | 10 | -0.001 | 0.001 | 0.0 | </details> Figure 5: New position and velocity plot These results confirm our hypothesis: the position and velocity stabilize faster, at the cost of a higher variation for the angular position and velocity.
Moreover, since the weight for the control input was chosen as 0.1, its absolute value is much larger than before;
the first was in the range of $u ( t ) \in ( - 4 , 2 )$ while the new control input has a much wider range around $u ( t ) \in ( - 4 0 , 2 0 )$ .
Thus, a more aggressive controller results in using more energy for a faster stabilization.
