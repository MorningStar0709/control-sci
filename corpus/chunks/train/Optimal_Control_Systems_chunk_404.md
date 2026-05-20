We call such a control $\epsilon$ fuel-optimal. Similarly, for the region $R_{3}$ , we have the $\epsilon$ fuel-optimal control sequence given as $\{+1,0,-1\}$ . Note that the control sequence $\{-1,+1\}$ through $A_{1}BCEO$ is not an allowable optimal control sequence (7.3.17) and also consumes more fuel than the $\epsilon$ -fuel optimal through $A_{1}BCDO$ . Also, we like to make $\epsilon$ as small as possible and apply the control $\{0\}$ as soon as the trajectory enters the region $R_{4}$ .

\- Step 8: Control Law: The fuel-optimal control law for driving the system from any initial state $(x_{1}, x_{2})$ to the origin, can be stated as follows:

$$
u ^ {*} (t) = \left\{ \begin{array}{c c c} + 1 & \forall & \left(x _ {1}, x _ {2}\right) \in \gamma_ {+} \\ - 1 & \forall & \left(x _ {1}, x _ {2}\right) \in \gamma_ {-} \\ 0 & \forall & \left(x _ {1}, x _ {2}\right) \in R _ {2} \cup R _ {4}. \end{array} \right. \tag {7.3.27}
$$

If $(x_{1}, x_{2}) \in R_{1} \cup R_{3}$ , there is no fuel-optimal control. However, there is $\epsilon-$ fuel-optimal control as described above.
