$$
\left[ \begin{array}{c} \dot {\hat {x}} _ {1} \\ \dot {\hat {x}} _ {2} \\ \cdot \\ \cdot \\ \cdot \\ \dot {\hat {x}} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c c} - p _ {1} & & & & & 0 \\ & - p _ {2} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & - p _ {n} \end{array} \right] \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \\ \cdot \\ \cdot \\ \cdot \\ \hat {x} _ {n} \end{array} \right] + \left[ \begin{array}{c} c _ {1} \\ c _ {2} \\ \cdot \\ \cdot \\ \cdot \\ c _ {n} \end{array} \right] u

y = \left[ \begin{array}{c c c c} 1 & 1 & \dots & 1 \end{array} \right] \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \\ \cdot \\ \cdot \\ \cdot \\ \hat {x} _ {n} \end{array} \right] + b _ {0} u
$$

A–9–4. Consider the system defined by

$$\frac {Y (s)}{U (s)} = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n - 1} s + b _ {n}}{(s + p _ {1}) ^ {3} (s + p _ {4}) (s + p _ {5}) \cdots (s + p _ {n})} \tag {9-91}$$

where the system involves a triple pole at $s = - p _ { 1 }$ . (We assume that, except for the first three $\boldsymbol { p _ { i } } ^ { \prime }$ ’s being equal, the $\vec { p _ { i } } ^ { \prime } \mathbf { \dot { \dot { \mathbf { \delta } } } }$ s are different from one another.) Obtain the Jordan canonical form of the state-space representation for this system.

Solution. The partial-fraction expansion of Equation (9–91) becomes

$$\frac {Y (s)}{U (s)} = b _ {0} + \frac {c _ {1}}{(s + p _ {1}) ^ {3}} + \frac {c _ {2}}{(s + p _ {1}) ^ {2}} + \frac {c _ {3}}{s + p _ {1}} + \frac {c _ {4}}{s + p _ {4}} + \dots + \frac {c _ {n}}{s + p _ {n}}$$

which may be written as

$$
\begin{array}{l} Y (s) = b _ {0} U (s) + \frac {c _ {1}}{(s + p _ {1}) ^ {3}} U (s) + \frac {c _ {2}}{(s + p _ {1}) ^ {2}} U (s) \\ + \frac {c _ {3}}{s + p _ {1}} U (s) + \frac {c _ {4}}{s + p _ {4}} U (s) + \dots + \frac {c _ {n}}{s + p _ {n}} U (s) \tag {9-92} \\ \end{array}
$$

Define

$$X _ {1} (s) = \frac {1}{(s + p _ {1}) ^ {3}} U (s)X _ {2} (s) = \frac {1}{(s + p _ {1}) ^ {2}} U (s)X _ {3} (s) = \frac {1}{s + p _ {1}} U (s)X _ {4} (s) = \frac {1}{s + p _ {4}} U (s)X _ {n} (s) = \frac {1}{s + p _ {n}} U (s)$$

Notice that the following relationships exist among $X _ { 1 } ( s ) , X _ { 2 } ( s )$ , and $X _ { 3 } ( s )$ :

$$\frac {X _ {1} (s)}{X _ {2} (s)} = \frac {1}{s + p _ {1}}\frac {X _ {2} (s)}{X _ {3} (s)} = \frac {1}{s + p _ {1}}$$

Then, from the preceding definition of the state variables and the preceding relationships, we obtain
