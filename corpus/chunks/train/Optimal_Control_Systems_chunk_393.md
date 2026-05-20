Figure 7.10 shows four possible control sequences (7.2.13) which drive the system from any initial condition to the origin.

1. If the system is initially anywhere (say a) on the $\gamma_{+}$ curve, the optimal control is u = +1 to drive the system to origin in minimum time $t_{f}$ .   
2. If the system is at rest anywhere (say b) on the $\gamma_{-}$ curve, the optimal control is u = -1 to drive the system to origin in minimum time $t_{f}$ .   
3. If the system is initially anywhere (say $c$ ) in the $R_{+}$ region, the optimal control sequence is $u = \{+1, -1\}$ to drive the system to origin in minimum time $t_f$ .   
4. If the system is initially anywhere (say $d$ ) in the $R_{-}$ region, the optimal control sequence is $u = \{-1, +1\}$ to drive the system to origin in minimum time $t_f$ .

If we start at $d$ and use the control $u = +1$ and use the optimal control sequence $u = \{-1, +1\}$ , we certainly drive the system to origin but

(a) we then have a control sequence $\{+1, -1, +1\}$ which is not a member of the optimal control sequence (7.2.13), and

(b) the time $t_f$ taken for the system using the control sequence $\{+1, -1, +1\}$ is higher than the corresponding time $t_f$ taken for the system with control sequence $\{-1, +1\}$ .

\- Step 9: Control Law: We now reintroduce \* to indicate the optimal values. The time-optimal control $u^*$ as a function of the state $[x_1, x_2]$ is given by

$$u ^ {*} = u ^ {*} \left(x _ {1}, x _ {2}\right) = + 1 \quad \text { for all } \quad \left(x _ {1}, x _ {2}\right) \in \gamma_ {+} \cup R _ {+}u ^ {*} = u ^ {*} (x _ {1}, x _ {2}) = - 1 \quad \text { for all } \quad (x _ {1}, x _ {2}) \in \gamma_ {-} \cup R _ {-}. \tag {7.2.26}$$

Alternatively, if we define $z = x_{1} + \frac{1}{2} x_{2}|x_{2}|$ , then if

$$z > 0, u ^ {*} = - 1, \quad \text { and }z < 0, u ^ {*} = + 1. \tag {7.2.27}$$

\- Step 10: Minimum Time: We can easily calculate the time taken for the system starting at any position in state space and ending at the origin. We use the set of equations (7.2.15) for each portion of the trajectory. It can be shown that the minimum time $t_f^*$ for the system starting from $(x_1, x_2)$ and arriving at $(0, 0)$ is given by [6]

$$
t _ {f} ^ {*} = \left\{ \begin{array}{l l} x _ {2} + \sqrt {4 x _ {1} + 2 x _ {2} ^ {2}} & \text { if } \quad (x _ {1}, x _ {2}) \in R _ {-} \text { or } x _ {1} > - \frac {1}{2} x _ {2} | x _ {2} | \\ - x _ {2} + \sqrt {- 4 x _ {1} + 2 x _ {2} ^ {2}} & \text { if } \quad (x _ {1}, x _ {2}) \in R _ {+} \text { or } x _ {1} <   - \frac {1}{2} x _ {2} | x _ {2} | \\ | x _ {2} | & \text { if } \quad (x _ {1}, x _ {2}) \in \gamma \text { or } x _ {1} = - \frac {1}{2} x _ {2} | x _ {2} | \end{array} \right. \tag {7.2.28}
$$
