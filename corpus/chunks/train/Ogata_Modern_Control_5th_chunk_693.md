Now define state variables as follows:

$$
X _ {n} (s) = \frac {1}{s} \left[ b _ {1} U (s) - a _ {1} Y (s) + X _ {n - 1} (s) \right]X _ {n - 1} (s) = \frac {1}{s} \left[ b _ {2} U (s) - a _ {2} Y (s) + X _ {n - 2} (s) \right]
\begin{array}{l} \cdot \\ \cdot \\ \cdot \end{array} \tag {9-81}
X _ {2} (s) = \frac {1}{s} \left[ b _ {n - 1} U (s) - a _ {n - 1} Y (s) + X _ {1} (s) \right]X _ {1} (s) = \frac {1}{s} \left[ b _ {n} U (s) - a _ {n} Y (s) \right]
$$

Then Equation (9–80) can be written as

$$Y (s) = b _ {0} U (s) + X _ {n} (s) \tag {9-82}$$

By substituting Equation (9–82) into Equation (9–81) and multiplying both sides of the equations by s, we obtain

$$
\begin{array}{l} s X _ {n} (s) = X _ {n - 1} (s) - a _ {1} X _ {n} (s) + \left(b _ {1} - a _ {1} b _ {0}\right) U (s) \\ s X _ {n - 1} (s) = X _ {n - 2} (s) - a _ {2} X _ {n} (s) + \left(b _ {2} - a _ {2} b _ {0}\right) U (s) \\ s X _ {2} (s) = X _ {1} (s) - a _ {n - 1} X _ {n} (s) + \left(b _ {n - 1} - a _ {n - 1} b _ {0}\right) U (s) \\ s X _ {1} (s) = - a _ {n} X _ {n} (s) + \left(b _ {n} - a _ {n} b _ {0}\right) U (s) \\ \end{array}
$$

Taking the inverse Laplace transforms of the preceding n equations and writing them in the reverse order, we get

$$
\begin{array}{l} \dot {x} _ {1} = - a _ {n} x _ {n} + \left(b _ {n} - a _ {n} b _ {0}\right) u \\ \dot {x} _ {2} = x _ {1} - a _ {n - 1} x _ {n} + \left(b _ {n - 1} - a _ {n - 1} b _ {0}\right) u \\ \dot {x} _ {n - 1} = x _ {n - 2} - a _ {2} x _ {n} + (b _ {2} - a _ {2} b _ {0}) u \\ \dot {x} _ {n} = x _ {n - 1} - a _ {1} x _ {n} + \left(b _ {1} - a _ {1} b _ {0}\right) u \\ \end{array}
$$

Also, the inverse Laplace transform of Equation (9–82) gives

$$y = x _ {n} + b _ {0} u$$

Rewriting the state and output equations in the standard vector-matrix forms gives Equations (9–78) and (9–79). Figure 9–2 shows a block diagram representation of the system defined by Equations (9–78) and (9–79).

Figure 9–2 Block diagram representation of the system defined by Equations (9–78) and (9–79) (observable canonical form).   
![](image/8f54a9a0117e85ced9be0db5b47a529d57cdcbb777cfbefa60ae8c5598214014.jpg)

<details>
<summary>flowchart</summary>
