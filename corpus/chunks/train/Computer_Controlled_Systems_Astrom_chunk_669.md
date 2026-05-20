# Properties of the LQ-Controller

The pole-placement controller in Sec. 4.3 and the stationary LQ-controller have the same structure. However, they are obtained differently, so there are some differences in their properties.

The linear state-feedback controller of (11.18) has n parameters in the single-input case. It is, in general, difficult to tune the parameters directly such that a good performance of the closed-loop system is obtained. Instead, the tuning procedure can be to choose the n eigenvalues of the closed-loop system and use the design procedure in Sec. 4.3. This procedure is well suited for single-input-single-output systems. It is, however, difficult to compromise between the speed of the system and the magnitude of the control signal.

The LQ-controller has several good properties. It is applicable to multivariable and time-varying systems. Also, changing the relative magnitude between the elements in the weighting matrices means a compromise between the speed of the recovery and the magnitudes of the control signals. The following two theorems give properties of the closed-loop system when using the LQ-controller.

THEOREM 11.3 STABILITY OF THE CLOSED-LOOP SYSTEM Let the system of (11.16) be time-invariant and let the loss function of (11.9) be such that Q in (11.10) is positive definite. Assume that a positive-definite steady-state solution, $\bar{S}$ , to (11.33) exists. Then the steady-state optimal-control strategy

![](image/f348f966cc82fea61b1c3bc8a53e229f65707f6ad0411c3bb00ea3d79c5ae705.jpg)  
Figure 11.4 Simulation of the process in Example 11.2 for different values of the weighting at the end point; $q_{0} = 10$ (dashed), $q_{0} = 3.70$ (solid), and $q_{0} = 0$ (dashed-dotted).

$$u (k) = - L x (k) = - \left(Q _ {2} + \Gamma^ {T} \bar {S} \Gamma\right) ^ {- 1} (\Gamma^ {T} \bar {S} \Phi + Q _ {1 2} ^ {T}) x (k)$$

gives an asymptotically stable closed-loop system

$$x (k + 1) = (\Phi - \Gamma L) x (k)$$

Proof. Theorem 3.4 can be used to show that the closed-loop system is asymptotically stable. It is to be shown that the function

$$V (x (k)) = x ^ {T} (k) \bar {S} x (k)$$

is a Lyapunov function. V is positive definite and
