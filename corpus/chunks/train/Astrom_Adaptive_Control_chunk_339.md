# The Augmented Error

Some progress has now been made to construct stable parameter adjustment rules for the problem of adjusting a feedforward gain. Passivity theory gave good insight and led to the idea of filtering the model error so that $GG_{c}$ is SPR. However, we have not solved the problem in which G has a pole excess larger than 1. To do this, we first factor the transfer function G as

$$G = G _ {1} G _ {2}$$

where the transfer function $G_{1}$ is SPR. The error $e = y - y_{m}$ can then be written as

$$
\begin{array}{l} e = G \left(\theta - \theta^ {0}\right) u _ {c} = \left(G _ {1} G _ {2}\right) \left(\theta - \theta^ {0}\right) u _ {c} \\ = G _ {1} \left(G _ {2} \left(\theta - \theta^ {0}\right) u _ {c} + \left(\theta - \theta^ {0}\right) G _ {2} u _ {c} - \left(\theta - \theta^ {0}\right) G _ {2} u _ {c}\right) \\ = G _ {1} \left(\left(\theta - \theta^ {0}\right) G _ {2} u _ {c}\right) - G _ {1} \left(\left(\theta - \theta^ {0}\right) G _ {2} u _ {c} - G _ {2} \left(\theta - \theta^ {0}\right) u _ {c}\right) \\ \end{array}
$$

Introduce the augmented error $\varepsilon$ defined by

$$\varepsilon = e + \eta$$

where $\eta$ is the error augmentation defined by

$$
\begin{array}{l} \eta = G _ {1} \left(\theta - \theta^ {0}\right) G _ {2} u _ {c} - G \left(\theta - \theta^ {0}\right) u _ {c} \\ = G _ {1} \left(\theta G _ {2} u _ {c}\right) - G \theta u _ {c} \\ \end{array}
$$

The second equality follows because $G\theta^{0}u = \theta^{0}Gu$ when $\theta^{0}$ is constant. The augmented error is thus obtained by adding a correction term $\eta$ to the error. The correction term vanishes when the parameter $\theta$ is constant. It follows that

$$\varepsilon = G _ {1} \left(\left(\theta - \theta^ {0}\right) G _ {2} u _ {c}\right) = G _ {1} \left(\theta - \theta^ {0}\right) \bar {u} _ {c} \tag {5.58}$$

where $\bar{u}_{c}$ is the reference signal filtered through $G_{2}$ . Equation (5.58) is an error model similar to the ones used previously, and we have the following theorem.
