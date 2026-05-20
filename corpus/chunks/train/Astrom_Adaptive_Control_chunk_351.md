# 5.9 RELATIONS BETWEEN MRAS AND STR

For a long time, model-reference adaptive systems and self-tuning regulators were regarded as two quite different approaches to adaptive control. In this section we will show that the methods are closely related. The key observation is that the direct self-tuner in which process zeros are canceled (Algorithm 3.3) can be interpreted as a MRAS.

An MRAS for a general continuous-time linear system was derived in Section 5.8. In the derivation it was assumed that the process was minimum-phase and that all its zeros were canceled in the design. We showed that the adjustment law for updating the parameters can be written as

$$\frac {d \theta}{d t} = \gamma \varphi_ {f} \varepsilon \tag {5.81}$$

where $\varphi_{f}$ is a filtered regression vector and $\varepsilon$ is the augmented error given by Eq. (5.77), that is,

$$\varepsilon = \frac {Q}{P} (y - y _ {m}) + \frac {b _ {o} Q}{A _ {o} A _ {m}} \eta \tag {5.82}$$

Now consider a discrete-time direct self-tuner. When all process zeros are canceled, polynomial $B^{-}$ is a constant and we get the process model

$$y (t) = \varphi_ {f} ^ {T} (t - d _ {0}) \theta$$

In the direct algorithm the estimated parameters are equal to the controller parameters. The least-squares method can be used for the estimation by using the residual

$$\varepsilon (t) = y (t) - \hat {y} (t) = y (t) - \varphi_ {f} ^ {T} (t - d _ {0}) \hat {\theta} (t - 1)$$

The parameter update can be written as

$$\hat {\theta} (t) = \hat {\theta} (t - 1) + P (t) \varphi_ {f} ^ {T} \left(t - d _ {0}\right) c (t) \tag {5.83}$$

The residual is given by

$$\varepsilon (t) = y (t) - \hat {y} (t) = y (t) - y _ {m} (t) + y _ {m} (t) - \hat {y} (t) = e (t) + \eta (t) \tag {5.84}$$

A comparison of Eqs. (5.81) and (5.83) show that Eq. (5.83) can be interpreted as a discrete-time version of Eq. (5.81). Notice that the gain $\gamma$ in the MRAS is replaced by the matrix $P(t)$ . This matrix changes the gradient direction $\varphi_{f}$ and gives an appropriate step length. Also notice that it follows from Eq. (5.84) that the error augmentation is simply $y - \hat{y}$ . The augmented error that required a significant ingenuity to derive in the MRAS context is thus obtained directly from the least-squares equations in the STR. More filtering is required in the MRAS because of the continuous time formulation. Notice that it follows from Eq. (5.83) that

$$\varphi_ {f} ^ {T} (t - d _ {0}) = - \operatorname{grad} _ {\theta} \varepsilon (t)$$
