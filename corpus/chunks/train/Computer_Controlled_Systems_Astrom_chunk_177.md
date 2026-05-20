$$
\begin{array}{l} \Delta V (x) = V (\Phi x) - V (x) = x ^ {T} \Phi^ {T} P \Phi x - x ^ {T} P x \\ = x ^ {T} \left(\Phi^ {T} P \Phi - P\right) x = - x ^ {T} Q x \\ \end{array}
$$

For $V$ to be a Lyapunov function, it is thus necessary and sufficient that there exists a positive definite matrix $P$ that satisfies the equation

$$\Phi^ {T} P \Phi - P = - Q \tag {3.9}$$

where Q is positive definite. Equation (3.9) is called the Lyapunov equation. It can be shown that there is always a solution to the Lyapunov equation when the linear system is stable. The matrix P is positive definite if Q is positive definite. One way of determining a Lyapunov function for a linear system is to choose a positive definite matrix Q and solve the Lyapunov equation. If the solution P is positive definite then the system is asymptotically stable.
