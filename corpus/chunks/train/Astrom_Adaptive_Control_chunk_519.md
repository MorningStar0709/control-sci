# Cautious Controllers

Minimization over only one step leads to the one-step or cautious controller of Eq. (7.15). This controller takes the parameter uncertainties into account, in contrast to the certainty equivalence controller of Eq. (7.13). However, the gain of Eq. (7.15) will decrease if the variance of $\hat{b}_{0}$ increases. This will give less information about $b_{0}$ in the next step, and the variance will increase further. The controller is then caught in a vicious circle, and the magnitude of the control signal becomes very small. This is called the turn-off phenomenon.
