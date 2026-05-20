$$
\begin{array}{l} \overbrace {\min _ {x (T) , \dots , x (1)} \min _ {x (0)} \underbrace {\frac {1}{2} \left(| x (0) - \bar {x} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + | y (0) - C x (0) | _ {R ^ {- 1}} ^ {2} + | x (1) - A x (0) | _ {Q ^ {- 1}} ^ {2} + \right.} _ {\text { combine } V _ {0} (x (0))}} ^ {\text { arrival cost } V _ {1} ^ {-} (x (1))} \\ \left| y (1) - C x (1) \right| _ {R ^ {- 1}} ^ {2} + \left| x (2) - A x (1) \right| _ {Q ^ {- 1}} ^ {2} + \dots + \\ \left. \left| x (T) - A x (T - 1) \right| _ {Q ^ {- 1}} ^ {2} + \left| y (T) - C x (T) \right| _ {R ^ {- 1}} ^ {2}\right) \\ \end{array}
$$

Then we optimize over the first state, $x ( 0 )$ . This produces the arrival cost for the first stage, $V _ { 1 } ^ { - } ( x ( 1 ) )$ , which we will show is also quadratic

$$V _ {1} ^ {-} (x (1)) = \frac {1}{2} | x (1) - \hat {x} ^ {-} (1) | _ {(P ^ {-} (1)) ^ {- 1}} ^ {2}$$

Next we combine the arrival cost of the first stage with the next measurement $y ( 1 )$ to obtain $V _ { 1 } ( x ( 1 ) ) ,$ )

$$
\begin{array}{l} \overbrace {\min _ {x (T) , \dots , x (2)} \min _ {x (1)} \underbrace {\frac {1}{2} \left(\left| x (1) - \hat {x} ^ {-} (1) \right| _ {(P ^ {-} (1)) ^ {- 1}} ^ {2} + \left| y (1) - C x (1) \right| _ {R ^ {- 1}} ^ {2} + | x (2) - A x (1) | _ {Q ^ {- 1}} ^ {2} + \right.} _ {\text { combine } V _ {1} (x (1))}} ^ {\text { arrival cost } V _ {2} ^ {-} (x (2))} \\ \left| y (2) - C x (2) \right| _ {R ^ {- 1}} ^ {2} + \left| x (3) - A x (2) \right| _ {Q ^ {- 1}} ^ {2} + \dots + \\ \left. \left| x (T) - A x (T - 1) \right| _ {Q ^ {- 1}} ^ {2} + \left| y (T) - C x (T) \right| _ {R ^ {- 1}} ^ {2}\right) \tag {1.30} \\ \end{array}
$$

We optimize over the second state, $x ( 1 )$ , which defines arrival cost for the first two stages, $V _ { 2 } ^ { - } ( x ( 2 ) )$ . We continue in this fashion until we have optimized finally over $x ( T )$ and have solved (1.29). Now that we have in mind an overall game plan for solving the problem, we look at each step in detail and develop the recursion formulas of forward DP.

Combine prior and measurement. Combining the prior and measurement defines $V _ { 0 }$

$$V _ {0} (x (0)) = \frac {1}{2} \left(\underbrace {| x (0) - \overline {{x}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2}} _ {\text { prior }} + \underbrace {| y (0) - C x (0) | _ {R ^ {- 1}} ^ {2}} _ {\text { measurement }}\right) \tag {1.31}$$

which can be expressed also as

$$
\begin{array}{l} V _ {0} (x (0)) = \frac {1}{2} \left(| x (0) - \overline {{x}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + \right. \\ \left. \left| (y (0) - C \overline {{x}} (0)) - C (x (0) - \overline {{x}} (0)) \right| _ {R ^ {- 1}} ^ {2}\right) \\ \end{array}
$$
