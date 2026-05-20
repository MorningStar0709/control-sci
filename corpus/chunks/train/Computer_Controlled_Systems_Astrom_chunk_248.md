# An Alternative Observer

There are many variations of the observer given by Eq. (4.28). The observer has a delay, because $\hat{x}(k \mid k - 1)$ depends only on measurements up to time k - 1. The following observer can be used to avoid the delay:

$$\hat {x} (k \mid k) = \Phi \hat {x} (k - 1 \mid k - 1) + \Gamma u (k - 1)+ K \left[ y (k) - C \left(\Phi \hat {x} (k - 1 \mid k - 1) + \Gamma u (k - 1)\right) \right] \tag {4.32}= (I - K C) \left(\Phi \hat {x} (k - 1 \mid k - 1) + \Gamma u (k - 1)\right) + K y (k)$$

The reconstruction error when using this observer is given by

$$\bar {x} (k \mid k) = x (k) - \hat {x} (k \mid k) = (\Phi - K C \Phi) \bar {x} (k - 1 \mid k - 1)$$

This equation is similar to (4.30), and from the definition of the observability matrix $W_{o}$ , it is found that the pair $(\Phi, C\Phi)$ is observable if the pair $(\Phi, C)$ is observable. This implies that $\Phi - KC\Phi$ can be given arbitrary eigenvalues by selecting K. Further,

$$y (k) - C \hat {x} (k \mid k) = C \tilde {x} (k \mid k) = (I - C K) C \Phi \bar {x} (k - 1 \mid k - 1)$$

If the system has p outputs, then I - CK is a $p \times p$ matrix; K may be chosen such that CK = I if rank (C) = p. This implies that $C\hat{x}(k \mid k) = y(k)$ , which means that the output of the system is estimated without error. This will make it possible to eliminate p equations from (4.32), and the order of the observer will be reduced. Reduced-order observers of this type are called Luenberger observers.
