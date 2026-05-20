$$
\begin{array}{l} X _ {1} (s) = Q (s) \\ X _ {2} (s) = s Q (s) \\ X _ {n - 1} (s) = s ^ {n - 2} Q (s) \\ X _ {n} (s) = s ^ {n - 1} Q (s) \\ \end{array}
$$

Then, clearly,

$$
\begin{array}{l} s X _ {1} (s) = X _ {2} (s) \\ s X _ {2} (s) = X _ {3} (s) \\ s X _ {n - 1} (s) = X _ {n} (s) \\ \end{array}
$$

which may be rewritten as

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = x _ {3}\dot {x} _ {n - 1} = x _ {n}$$

Noting that $s ^ { n } Q ( s ) = s X _ { n } ( s )$ we can rewrite Equation (9–72) as,

$$s X _ {n} (s) = - a _ {1} X _ {n} (s) - \dots - a _ {n - 1} X _ {2} (s) - a _ {n} X _ {1} (s) + U (s)$$

or

$$\dot {x} _ {n} = - a _ {n} x _ {1} - a _ {n - 1} x _ {2} - \dots - a _ {1} x _ {n} + u \tag {9-75}$$

Also, from Equations (9–71) and (9–73), we obtain

$$Y (s) = b _ {0} U (s) + \left(b _ {1} - a _ {1} b _ {0}\right) s ^ {n - 1} Q (s) + \dots + \left(b _ {n - 1} - a _ {n - 1} b _ {0}\right) s Q (s)+ \left(b _ {n} - a _ {n} b _ {0}\right) Q (s)= b _ {0} U (s) + \left(b _ {1} - a _ {1} b _ {0}\right) X _ {n} (s) + \dots + \left(b _ {n - 1} - a _ {n - 1} b _ {0}\right) X _ {2} (s)+ \left(b _ {n} - a _ {n} b _ {0}\right) X _ {1} (s)$$

The inverse Laplace transform of this output equation becomes

$$y = \left(b _ {n} - a _ {n} b _ {0}\right) x _ {1} + \left(b _ {n - 1} - a _ {n - 1} b _ {0}\right) x _ {2} + \dots + \left(b _ {1} - a _ {1} b _ {0}\right) x _ {n} + b _ {0} u \tag {9-76}$$

Combining Equations (9–74) and (9–75) into one vector–matrix differential equation, we obtain Equation (9–69). Equation (9–76) can be rewritten as given by Equation (9–70). Equations (9–69) and (9–70) are said to be in the controllable canonical form. Figure 9–1 shows the block diagram representation of the system defined by Equations (9–69) and (9–70).

Figure 9–1 Block diagram representation of the system defined by Equations (9–69) and (9–70) (controllable canonical form).   
![](image/4d0c99ceace35699d8a7d4334c0b2f3ed4df943654f76ddfa50bdfbdaa90b85d.jpg)

<details>
<summary>flowchart</summary>
