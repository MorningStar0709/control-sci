# 6.8 AVERAGING IN STOCHASTIC SYSTEMS

The importance of averaging was illustrated in the previous sections. However, the excitation has been restricted to constant or sinusoidal inputs. In this section averaging is used on discrete-time systems with stochastic inputs. Assume that the system is described by

$$A ^ {*} (q ^ {- 1}) y (t) = B ^ {*} (q ^ {- 1}) u (t - d) + C ^ {*} (q ^ {- 1}) e (t) \tag {6.71}$$

where $e(t)$ is a zero-mean Gaussian stochastic process. Depending on the specifications, different self-tuning regulators can be used to control the system (compare Chapter 4). For simplicity it is assumed that the basic direct self-tuning algorithm (Algorithm 4.1) is used. The controller parameters are then estimated from a model of the form

$$y (t) = R ^ {*} \left(q ^ {- 1}\right) u (t - d) + S ^ {*} \left(q ^ {- 1}\right) y (t - d) \tag {6.72}$$

or

$$y (t) = \varphi (t - d) ^ {T} \theta \tag {6.73}$$

The parameters $\theta$ are estimated by using the recursive least-squares method. In applying averaging, it is appropriate to use the form

$$\hat {\theta} (t) = \hat {\theta} (t - 1) + \gamma (t) R (t) ^ {- 1} \varphi (t - d) \left(y (t) - \varphi^ {T} (t - d) \hat {\theta} (t - 1)\right) \tag {6.74}R (t) = R (t - 1) + \gamma (t) (\varphi (t - d) \varphi^ {T} (t - d) - R (t - 1))$$

where the covariance matrix $P(t)$ is related to $R(t)$ through

$$P (t) = \gamma (t) R (t) ^ {- 1}$$

and $\gamma(t) = 1/t$ . In some cases it is convenient to replace the matrix $R(t)$ by a scalar $r(t)$ . This gives shorter computation times and requires less storage, but it gives slower convergence. For stochastic approximation we obtain

$$r (t) = r (t - 1) + \gamma (t) (\varphi (t - d) ^ {T} \varphi (t - d) - r (t - 1)) \tag {6.75}$$

The controller is

$$u (t) = - \frac {\hat {S} ^ {*} \left(q ^ {- 1}\right)}{\hat {R} ^ {*} \left(q ^ {- 1}\right)} y (t) \tag {6.76}$$

or

$$\varphi (t) ^ {T} \hat {\theta} (t) = 0$$
