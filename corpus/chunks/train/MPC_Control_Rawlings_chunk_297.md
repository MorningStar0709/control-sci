# Example 2.43: Unreachable setpoint MPC

An example is presented to illustrate the advantages of the proposed setpoint tracking MPC (sp-MPC) compared to traditional target tracking MPC (targ-MPC). The regulator cost function for the proposed sp-MPC, is

$$V _ {N} ^ {\mathrm{sp}} (x, \mathbf {u}) = \frac {1}{2} \sum_ {j = 0} ^ {N - 1} | x (j) - x _ {\mathrm{sp}} | _ {Q} ^ {2} + | u (j) - u _ {\mathrm{sp}} | _ {R} ^ {2} + | u (j + 1) - u (j) | _ {S} ^ {2}$$

<table><tr><td>Performance measure</td><td>targ-MPC (a=targ)</td><td>sp-MPC (a=sp)</td><td> $\Delta$  index (%)</td></tr><tr><td> $V_{u}^{a}$ </td><td>0.016</td><td> $2.2 \times 10^{-6}$ </td><td>99.98</td></tr><tr><td> $V_{y}^{a}$ </td><td>3.65</td><td>1.71</td><td>53</td></tr><tr><td> $V^{a}$ </td><td>3.67</td><td>1.71</td><td>54</td></tr></table>

Table 2.3: Comparison of controller performance for Example 2.43.

in which $Q > 0 , R , S \geq 0$ , at least one of $R , S > 0 $ , and $x ( j ) = \phi ( j ; x , { \bf u } )$ . This system can be put in the standard form defined for terminal constraint MPC by using the augmented state ${ \widetilde { x } } ( k ) \ : = \ ( x ( k ) , u ( k - 1 ) )$ discussed in Section 1.2.5. The regulator cost function in traditional targ-MPC is

$$V _ {N} ^ {\text {targ}} (x, \mathbf {u}) = \frac {1}{2} \sum_ {j = 0} ^ {N - 1} | x (j) - x _ {s} | _ {Q} ^ {2} + | u (j) - u _ {s} | _ {R} ^ {2} + | u (j + 1) - u (j) | _ {S} ^ {2}$$

The controller performance is assessed using the following three closedloop control performance measures

$$
\begin{array}{l} V _ {u} ^ {a} = \frac {1}{2 k \Delta} \sum_ {j = 0} ^ {k - 1} | u (j) - u _ {\mathrm{sp}} | _ {R} ^ {2} + | u (j + 1) - u (j) | _ {S} ^ {2} \\ V _ {y} ^ {a} = \frac {1}{2 k \Delta} \sum_ {j = 0} ^ {k - 1} \left| x (j) - x _ {\mathrm{sp}} \right| _ {Q} ^ {2} \\ V ^ {a} = V _ {u} ^ {a} + V _ {y} ^ {a} \qquad a = (\mathrm{sp}, \mathrm{targ}) \\ \end{array}
$$

in which $\Delta$ is the process sample time, and $x ( j )$ and $u ( j )$ are the state and control at time j of the controlled system using either target (a=targ) or setpoint (a=sp) tracking MPC for a specified initial state. For each of the indices defined previously, we define the percentage improvement of sp-MPC compared with targ-MPC by

$$\Delta \text { index } (\%) = \frac {V ^ {\mathrm{targ}} - V ^ {\mathrm{sp}}}{V ^ {\mathrm{targ}}} \times 1 0 0$$

Consider the single-input, single-output system with transfer function

![](image/b5217c0330cbf51a2af53e919b51fa7c48f3892ddd1e8ecfbda6785028c16527.jpg)
