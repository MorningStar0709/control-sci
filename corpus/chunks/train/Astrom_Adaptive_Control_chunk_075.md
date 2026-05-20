\mathcal {E} (t) = \left( \begin{array}{c c c c} \varepsilon (1) & \varepsilon (2) & \dots & \varepsilon (t) \end{array} \right) ^ {T}

\Phi (t) = \left( \begin{array}{c} \varphi^ {T} (1) \\ \vdots \\ \varphi^ {T} (t) \end{array} \right)
P (t) = \left(\Phi^ {T} (t) \Phi (t)\right) ^ {- 1} = \left(\sum_ {i = 1} ^ {t} \varphi (i) \varphi^ {T} (i)\right) ^ {- 1} \tag {2.3}
$$

where the residuals $\varepsilon(i)$ are defined by

$$\varepsilon (i) = y (i) - \hat {y} (i) = y (i) - \varphi^ {T} (i) \theta$$

With these notations the loss function (2.2) can be written as

$$V (\theta , t) = \frac {1}{2} \sum_ {i = 1} ^ {t} \varepsilon^ {2} (i) = \frac {1}{2} \mathcal {E} ^ {T} \mathcal {E} = \frac {1}{2} \| \mathcal {E} \| ^ {2}$$

where $\mathcal{E}$ can be written as

$$\mathcal {E} = Y - \hat {Y} = Y - \Phi \theta \tag {2.4}$$

The solution to the least-squares problem is given by the following theorem.
