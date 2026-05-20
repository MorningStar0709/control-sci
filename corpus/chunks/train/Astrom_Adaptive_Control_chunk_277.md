# EXAMPLE 5.3 Lack of parameter convergence

Consider the simple system for updating a feedforward gain, discussed in Example 5.1. Assume that $G(s) = 1$ . The process model is $y = ku$ , the control law is $u = \theta u_{c}$ , and the desired response is given by $y_{m} = k_{0}u_{c}$ . The error is

$$e = (k \theta - k _ {0}) u _ {c} = k (\theta - \theta^ {0}) u _ {c}$$

where $\theta^{0} = k_{0}/k$ . The MIT rule gives the following differential equation for the parameter:

$$\frac {d \theta}{d t} = - \gamma k ^ {2} u _ {c} ^ {2} (\theta - \theta^ {0})$$

This equation has the solution

$$\theta (t) = \theta^ {0} + (\theta (0) - \theta^ {0}) e ^ {- \gamma k ^ {2} I _ {c}} \tag {5.10}$$

where

$$I _ {t} = \int_ {0} ^ {t} u _ {c} ^ {2} (\tau) d \tau$$

and $\theta(0)$ is the initial value of the parameter $\theta$ . The estimate converges toward its correct value only if the integral $I_{t}$ diverges as $t \to \infty$ . The convergence is exponential if the input signal is persistently exciting. (Compare with Section 2.4.) The error is given by

$$e (t) = k u _ {c} (t) (\theta (0) - \theta^ {0}) e ^ {- \gamma h ^ {2} I _ {t}}$$

Notice that the error will always go to zero as $t \rightarrow \infty$ because either the integral $I_{t}$ diverges or else $u_{c}(t) \rightarrow 0$ . However, the limiting value of the parameter $\theta$ will depend on the properties of the input signal. ☐

Example 5.3 illustrates the fact that the error e goes to zero but that the parameters do not necessarily converge to their correct values. This is a characteristic feature of all adaptive systems. The input signal must have certain properties for the parameters to converge. The conditions required were discussed in Chapter 2; compare with the notion of persistent excitation, which was introduced in Section 2.4.
