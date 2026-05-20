Using the small gain theorem, the design procedure here boils down to the determination of the controller $K ( s )$ such that the inequality

$$\left\| \frac {W (s)}{1 + K (s) G (s)} \right\| _ {\infty} < 1$$

is satisfied, where $G ( s )$ is the transfer function of the model used in the design process, $K ( s )$ is the transfer function of the controller, and $W ( s )$ is the chosen transfer function to approximate $\Delta ( s )$ . In most practical cases, we must satisfy more than one such inequality that involves $G ( s ) , K ( s )$ , and $W ( s ) { \mathrm { ' s } } .$ For example, to guarantee robust stability and robust performance we may require two inequalities, such as

$$
\begin{array}{l} \left\| \frac {W _ {m} (s) K (s) G (s)}{1 + K (s) G (s)} \right\| _ {\infty} <   1 \quad \text { for   robust   stability } \\ \left\| \frac {W _ {s} (s)}{1 + K (s) G (s)} \right\| _ {\infty} <   1 \quad \text { for   robust   performance } \\ \end{array}
$$

be satisfied. (These inequalities are derived in Section 10–9.) There are many different such inequalities that need to be satisfied in many different robust control systems. (Robust stability means that the controller $K ( s )$ guarantees internal stability of all systems that belong to a group of systems that include the system with the actual plant. Robust performance means the specified performance is satisfied in all systems that belong to the group.) In this book all the plants of control systems we discuss are assumed to be known precisely, except the plants we discuss in Section 10–9 where an introductory aspect of robust control theory is presented.
