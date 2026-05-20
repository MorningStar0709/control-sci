$$
\begin{array}{l} \min _ {x _ {1 s}, u _ {1 s}} \frac {1}{2} \left[ \begin{array}{c} y _ {1 s} - y _ {1 s p} \\ y _ {2 s} - y _ {2 s p} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} Q _ {1 s} & \\ & Q _ {2 s} \end{array} \right] \left[ \begin{array}{c} y _ {1 s} - y _ {1 s p} \\ y _ {2 s} - y _ {2 s p} \end{array} \right] + \\ \frac {1}{2} \left[ \begin{array}{c} u _ {1 s} - u _ {1 s p} \\ u _ {2 s} - u _ {2 s p} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} R _ {1 s} & \\ & R _ {2 s} \end{array} \right] \left[ \begin{array}{c} u _ {1 s} - u _ {1 s p} \\ u _ {2 s} - u _ {2 s p} \end{array} \right] \\ \end{array}
$$

subject to

$$
\left[ \begin{array}{c c c c} I - A _ {1} & & - \overline {{B}} _ {1 1} & - \overline {{B}} _ {1 2} \\ & I - A _ {2} & - \overline {{B}} _ {2 1} & - \overline {{B}} _ {2 2} \\ H _ {1} C _ {1} & & & \\ & H _ {2} C _ {2} & & \end{array} \right] \left[ \begin{array}{c} x _ {1 s} \\ x _ {2 s} \\ u _ {1 s} \\ u _ {2 s} \end{array} \right] = \left[ \begin{array}{c} B _ {d 1} \hat {d} _ {1} (k) \\ B _ {d 2} \hat {d} _ {2} (k) \\ r _ {1 s p} - H _ {1} C _ {d 1} \hat {d} _ {1} (k) \\ r _ {2 s p} - H _ {2} C _ {d 2} \hat {d} _ {2} (k) \end{array} \right]
E _ {1} u _ {1 s} \leq e _ {1}
$$

in which

$$y _ {1 s} = C _ {1} x _ {1 s} + C _ {d 1} \hat {d} _ {1} (k) \quad y _ {2 s} = C _ {2} x _ {2 s} + C _ {d 2} \hat {d} _ {2} (k) \tag {6.27}$$

But here we run into several problems. First, the constraints to ensure zero offset in both players’ controlled variables are not feasible with only the $u _ { 1 s }$ decision variables. We require also $u _ { 2 s }$ , which is not available to player one. We can consider deleting the zero offset condition for player two’s controlled variables, the last equality constraint. But if we do that for both players, then the two players have different and coupled equality constraints. That is a path to instability as we have seen in the noncooperative target problem. To resolve this issue, we move the controlled variables to the objective function, and player one solves instead the following

$$
\min _ {x _ {1 s}, u _ {1 s}} \frac {1}{2} \left[ \begin{array}{c} H _ {1} y _ {1 s} - r _ {1 s p} \\ H _ {2} y _ {2 s} - r _ {2 s p} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} T _ {1 s} & \\ & T _ {2 s} \end{array} \right] \left[ \begin{array}{c} H _ {1} y _ {1 s} - r _ {1 s p} \\ H _ {2} y _ {2 s} - r _ {2 s p} \end{array} \right]
$$

subject to (6.27) and
