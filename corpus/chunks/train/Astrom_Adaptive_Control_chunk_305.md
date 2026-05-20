# Adaptation of a Feedforward Gain

We now attempt to use Lyapunov theory to derive parameter adjustment laws for the problem of adjusting a feedforward gain. We consider the case in which the plant has transfer function $kG(s)$ , where $G(s)$ is known and k is unknown. The desired response is given by the transfer function $h_{0}G(s)$ . This problem was discussed previously in Examples 5.1 and 5.3. The error is given by

$$e = (k G (p) \theta - k _ {0} G (p)) u _ {c} = k G (p) (\theta - \theta^ {0}) u _ {c}$$

where $\theta^{0} = k_{0}/k$ . To use Lyapunov theory, we first introduce a state space representation of the transfer function G. The relation between the parameter $\theta$ and the error e can then be written as

$$\frac {d x}{d t} = A x + B \left(\theta - \theta^ {0}\right) u _ {c} \tag {5.36}e = C x$$

If the homogeneous system $\dot{x} = Ax$ is asymptotically stable, there exist positive definite matrices P and Q such that

$$\boldsymbol {A} ^ {T} \boldsymbol {P} + \boldsymbol {P A} = - \boldsymbol {Q} \tag {5.37}$$

Choose the following function as a candidate for a Lyapunov function:

$$V = \frac {1}{2} \left(\gamma x ^ {T} P x + (\theta - \theta^ {0}) ^ {2}\right)$$

The time derivative of V along the differential equation (Eqs. 5.36) is given by

$${\frac {d V}{d t}} = {\frac {\gamma}{2}} \left({\frac {d x ^ {T}}{d t}} P x + x ^ {T} P {\frac {d x}{d t}}\right) + (\theta - \theta^ {0}) {\frac {d \theta}{d t}}$$

Using Eqs. (5.36), we get

$$
\begin{array}{l} \frac {d V}{d t} = \frac {\gamma}{2} \left(\left(A x + B u _ {c} \left(\theta - \theta^ {0}\right)\right) ^ {T} P x + x ^ {T} P \left(A x + B u _ {c} \left(\theta - \theta^ {0}\right)\right)\right) \\ + \left(\theta - \theta^ {0}\right) \frac {d \theta}{d t} \\ = - \frac {\gamma}{2} x ^ {T} Q x + \left(\theta - \theta^ {0}\right) \left(\frac {d \theta}{d t} + \gamma u _ {c} B ^ {T} P x\right) \\ \end{array}
$$

If the parameter adjustment law is chosen to be

$$\frac {d \theta}{d t} = - \gamma u _ {v} B ^ {T} P x \tag {5.38}$$

we find that the derivative of the Lyapunov function will be negative as long as $x \neq 0$ . The static vector x and the error e = Cx will go to zero as t goes to infinity. Notice, however, that the parameter error $\theta - \theta^{0}$ will not necessarily go to zero.

Output feedback The result obtained is quite restrictive because it requires that all state variables are known. A parameter adjustment law that uses output feedback can be obtained if the Lyapunov function can be chosen so that

$$\boldsymbol {B} ^ {T} \boldsymbol {P} = C$$

where $C$ is the output matrix of the system in Eq. (5.34). With this choice of $P$ it follows that

$$B ^ {T} P x = C x = e$$

and the adjustment rule becomes

$$\frac {d \theta}{d t} = - \gamma u _ {c} e$$

The appropriate condition is given by the celebrated Kalman-Yakubovich lemma. The following definition is needed to state this lemma.
