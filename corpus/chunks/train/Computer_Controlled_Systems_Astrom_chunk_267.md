Figure 4.14 Block diagram of a general controller that combines model following with feedback from estimated states, and disturbance states. Compare with Figs. 4.8 and 4.13.

Useful insight is obtained by introducing the difference between the estimated state $\hat{x}$ and the state of the model $x_{m}$ . Assume that the systems are given in reachable canonical forms and that the model and the process have the same zeros. We can then choose $C_{m} = C$ and $\Gamma_{m} = \lambda\Gamma$ . We now introduce

$$\hat {e} = x _ {m} - \hat {x} \tag {4.62}$$

It follows from Eqs. (4.23) and (4.61) that

$$
\begin{array}{l} \hat {e} (k + 1) = \Phi_ {m} x _ {m} (k) + \Gamma_ {m} u _ {c} (k) - \Phi \hat {x} (k) - \Phi_ {x w} \hat {w} (k) - \Gamma u (k) - K \varepsilon (k) \\ = \Phi \hat {e} (k) - \Phi_ {x w} \hat {w} (k) + (\Phi_ {m} - \Phi) x _ {m} (k) + \lambda \Gamma u _ {c} (k) - \Gamma u (k) - K \varepsilon (k) \\ \end{array}
$$

Only the first element of the vector $(\Phi_{m}-\Phi)x_{m}(k)+\lambda\Gamma u_{c}(k)$ is different from zero. This element is given by

$$\left(a _ {1} - a _ {1} ^ {m}\right) x _ {m 1} + \left(a _ {2} - a _ {2} ^ {m}\right) x _ {m 2} + \dots + \left(a _ {n} - a _ {1} ^ {m}\right) x _ {m n} + \lambda u _ {c} = \lambda \left(C _ {f f} x _ {m} + u _ {c}\right)$$

Furthermore we have

$$
\begin{array}{l} \varepsilon (k) = y (k) - C \hat {x} (k) \\ = y (k) - C \hat {x} (k) + C x _ {m} (k) - C x _ {m} (k) \\ = y (k) - y _ {m} (k) + C \hat {e} (k) \\ \end{array}
$$

We now introduce

$$u (k) = u _ {f b} (k) + u _ {f f} (k)$$

where

$$u _ {f f} (k) = \lambda \left(C _ {f f} x _ {m} (k) + u _ {c} (k)\right)$$

and the controller (4.61) becomes

$$
\begin{array}{l} u (k) = u _ {f b} (k) + u _ {f f} (k) \\ u _ {f f} (k) = \lambda \left(C _ {f f} x _ {m} (k) + u _ {c} (k)\right) \\ u _ {f b} (k) = L \hat {e} (k) - L _ {w} \hat {w} (k) \\ \hat {e} (k + 1) = \Phi \hat {e} (k) - \Phi_ {x w} \hat {w} (k) - \Gamma u _ {f b} (k) + K \left(y _ {m} (k) - y (k) - C \hat {e} (k)\right) \tag {4.63} \\ \end{array}
\hat {w} (k + 1) = \Phi_ {w} \hat {w} (k) - K _ {w} \left(y _ {m} (k) - y (k) - C \hat {e} (k)\right)x _ {m} (k + 1) = \Phi_ {m} x _ {m} (k) + \Gamma_ {m} u _ {c} (k)
$$

In the special case of a constant input disturbance we have $w = v$ , $\Phi_w = 1$ , $\Phi_{xw} = \Gamma$ . In this case the controller will have integral action. To see this clearly we will reqrite Eq. (4.63) for the controller.

![](image/5097786b53775bac1127b4135c97a538404d0b306a3a199307cd6345831a6d88.jpg)

<details>
<summary>flowchart</summary>
