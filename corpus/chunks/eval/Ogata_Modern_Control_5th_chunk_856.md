$$
\left[ \begin{array}{c} \dot {\mathbf {x}} \\ \hline \dot {\mathbf {e}} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B K F} \\ \hline \mathbf {0} & \mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \hline \mathbf {e} \end{array} \right]
$$

The state matrix here is a $6 \times 6$ matrix. The response of the system to the given initial condition can be obtained easily with MATLAB. (See MATLAB Program 10–27.) The resulting response curves are shown in Figure 10–50. The response curves seem to be acceptable.

![](image/b367d6507429be6dcd67cd27c21797f3f815d5d8b821499a33156f6d648adcf3.jpg)  
Figure 10–50 Response curves to initial condition.
