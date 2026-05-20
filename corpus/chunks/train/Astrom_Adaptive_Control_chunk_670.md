output settle to constant values after a transient. The regression vector then becomes

$$
\varphi (t) = \left( \begin{array}{c c} - u _ {c} & a u _ {c} / b \end{array} \right)
$$

This vector lies in a one-dimensional subspace of $R^{2}$ and is thus not persistently exciting. The simulation shown in Fig. 11.12 illustrates the behavior of the system. The process output tracks the command signal quite well, and the control signal is also quite reasonable. Figure 11.12 shows that the element $p_{11}$ of the P-matrix grows approximately exponentially during the periods when the command signal is constant. The deviations are due to the measurement noise that gives some excitation. The other elements of the P-matrix behave similarly. The estimator gains also grow significantly. Exponential growth of the P-matrix and the associated increase in the estimator gains are clearly noticeable in Fig. 11.12. The parameter estimates will change significantly, as shown in Fig. 11.13. The estimates are very inaccurate at the end of the periods when the command signal has been constant. In Fig. 11.13 we also show the estimate of process gain calculated from

$$\hat {k} = \frac {\hat {b}}{1 + \hat {a}}$$

This estimate is very good for the whole period because this variable is well excited. This is why the controller behaves reasonably well in spite of the poor estimates of a and b. □

To get further insight into the windup phenomenon, we make a simplified analysis of the behavior shown in Example 11.7. For this purpose we assume that the regression vector is constant, that is, $\varphi(t) = \varphi_{0}$ . The inverse of the P-matrix is given by

$$P ^ {- 1} (t + 1) = \lambda^ {t} P _ {0} ^ {- 1} + \sum_ {k = 1} ^ {t} \lambda^ {t - k} \varphi_ {0} \varphi_ {0} ^ {T} = \lambda^ {t} P _ {0} ^ {- 1} + \frac {1 - \lambda^ {t}}{1 - \lambda} \varphi_ {0} \varphi_ {0} ^ {T}$$

Using the matrix inversion lemma (Lemma 2.1), we find after some calculations that the covariance matrix can be written as

$$P (t + 1) = \frac {1}{\lambda^ {t}} \left(P _ {0} - \frac {P _ {0} \varphi_ {0}}{\lambda^ {t} \alpha (t)} + \frac {\varphi_ {0} ^ {T} P _ {0}}{\varphi_ {0} ^ {T} P _ {0} \varphi_ {0}}\right)$$

where

$$\alpha (t) = \frac {1 - \lambda}{1 - \lambda^ {t}}$$

Furthermore, we find that

$$P (t + 1) \varphi_ {0} = a (t) \frac {P _ {0} \varphi_ {0}}{\lambda^ {t} a (t) + \varphi_ {0} ^ {T} P _ {0} \varphi_ {0}} \tag {11.20}$$

The $P$ -matrix can be decomposed as
