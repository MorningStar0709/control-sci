# Longer Time Delays

If the time delay is longer than h, then the previous analysis has to be modified a little. If

$$\tau = (d - 1) h + \tau^ {\prime} \quad 0 < \tau^ {\prime} \leq h$$

where d is an integer, the following equation is obtained:

$$x (k h + h) = \Phi x (k h) + \Gamma_ {0} u (k h - (d - 1) h) + \Gamma_ {1} u (k h - d h)$$

where $\Gamma_{0}$ and $\Gamma_{1}$ are given by (2.11) with $\tau$ replaced by $\tau'$ . The corresponding state-space description is

$$
\left( \begin{array}{c} x (k h + h) \\ u (k h - (d - 1) h) \\ \vdots \\ u (k h - h) \\ u (k h) \end{array} \right) = \left( \begin{array}{c c c c c} \Phi & \Gamma_ {1} & \Gamma_ {0} & \dots & 0 \\ 0 & 0 & I & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & I \\ 0 & 0 & 0 & \dots & 0 \end{array} \right) \left( \begin{array}{c} x (k h) \\ u (k h - d h) \\ \vdots \\ u (k h - 2 h) \\ u (k h - h) \end{array} \right) + \left( \begin{array}{c} 0 \\ 0 \\ \vdots \\ 0 \\ I \end{array} \right) u (k h) \tag {2.12}
$$

Notice that if $\tau > 0$ , then $d \cdot r$ extra state variables are used to describe the delay, where r is the number of inputs. The characteristic polynomial of the state-space description is $\lambda^{dr}A(\lambda)$ , where $A(\lambda)$ is the characteristic polynomial of $\Phi$ .

An example illustrates use of the general formula.
