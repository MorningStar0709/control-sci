$$
x (k + 1) = (\Phi - \Gamma L) x (k) + \left(\Phi_ {x w} - \Gamma L _ {w}\right) w - \Gamma L \tilde {x} (k) - \Gamma L _ {w} \tilde {w}
\begin{array}{l} w (k + 1) = \Phi_ {w} w (k) \\ \tilde {\tilde {x}} (k + 1) = (\Phi_ {w} - K C) \tilde {x} (k) + \Phi_ {w} \tilde {x} (k) \end{array} \tag {4.43}
\tilde {x} (k + 1) = (\Phi - K C) \tilde {x} (k) + \Phi_ {x w} \tilde {w} (k) \tag {4.43}\tilde {w} (k + 1) = \Phi_ {w} \tilde {w} (k) - K _ {w} C \bar {x} (k)
$$

Notice that the disturbance state w is observable but not reachable. The equations for the closed-loop system give useful insight into the behavior of the system. The matrix L ensures that the state x goes to zero at the desired rate after a disturbance. A proper choice of the gain $L_{w}$ reduces the effect of the disturbance v on the system by feedforward from the estimated disturbances $\hat{w}$ . This feedforward control action is particularly effective if the matrix $\Phi_{xw} - \Gamma L_{w}$ can be made equal to zero. The observer gains K and $K_{w}$ influence the rate at which the estimation errors go to zero. A block diagram of the system is shown in Fig. 4.8.
