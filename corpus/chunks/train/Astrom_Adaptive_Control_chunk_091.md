# Continuous-Time Models

In the recursive schemes the variables have so far been indexed by a discrete parameter t. The notation t was chosen because in many applications it denotes time. In some cases it is natural to use continuous-time observations. It is straightforward to generalize the results to this case. Equation (2.1) is still used, but i is now assumed to be a real variable. Assuming exponential forgetting, the parameter should be determined such that the criterion

$$V (\theta) = \int_ {0} ^ {t} e ^ {- \alpha (t - \tau)} (y (\tau) - \varphi^ {T} (\tau) \theta) ^ {2} d \tau \tag {2.27}$$

is minimized. The parameter $\alpha$ , where $\alpha \geq 0$ , corresponds to the forgetting factor $\lambda$ in Eq. (2.20). A straightforward calculation shows that the criterion is minimized if (see Problem 2.15 at the end of the chapter)

$$\left(\int_ {0} ^ {t} e ^ {- \alpha (t - \tau)} \varphi (\tau) \varphi^ {T} (\tau) d \tau\right) \hat {\theta} (t) = \int_ {0} ^ {t} e ^ {- \alpha (t - \tau)} \varphi (\tau) y (\tau) d \tau \tag {2.28}$$

which is the normal equation. The estimate is unique if the matrix

$$R (t) = \int_ {0} ^ {t} e ^ {- \alpha (t - \tau)} \varphi (\tau) \varphi^ {T} (\tau) d \tau \tag {2.29}$$

is invertible. It is also possible to obtain recursive equations by differentiating Eq. (2.28). The estimate is given by the following theorem.
