# The General Problem

In the general least-squares problem, it is assumed that "the computed variable," y, in Gauss' terminology is given by the model

$$\hat {y} = \theta_ {1} \varphi_ {1} (x) + \theta_ {2} \varphi_ {2} (x) + \dots + \theta_ {n} \varphi_ {n} (x) \tag {13.2}$$

where $\varphi_{1},\varphi_{2},\ldots ,\varphi_{n}$ are known functions, and $\theta_{1},\theta_{2},\ldots ,\theta_{n}$ are unknown parameters. Pairs of observations $\{(x_i,y_i),i = 1,2,\dots ,N\}$ are obtained from an experiment. The problem is to determine the parameters in such a way that the variables $\hat{y}$ , computed from the model of (13.2) and the experimental values $x_{i}$ agree as closely as possible with the measured variables $y_{i}$ . Assuming that all measurements have the same precision, the principle of least squares says that the parameters should be selected in such a way that the loss function

$$J (\theta) = \frac {1}{2} \sum_ {i = 1} ^ {N} \varepsilon_ {i} ^ {2}$$

is minimal where

$$\varepsilon_ {i} = y _ {i} - \hat {y} _ {i} = y _ {i} - \theta_ {1} \varphi_ {1} (x _ {i}) - \dots - \theta_ {n} \varphi_ {n} (x _ {i}) \quad i = 1, 2, \dots , N$$

Compare with Fig. 13.1. To simplify the calculations, the following vector nota-

tions are introduced:

$$
\varphi = \left( \begin{array}{l l l l} \varphi_ {1} & \varphi_ {2} & \dots & \varphi_ {n} \end{array} \right) ^ {T}

\theta = \left( \begin{array}{l l l l} \theta_ {1} & \theta_ {2} & \dots & \theta_ {n} \end{array} \right) ^ {T}

y = \left( \begin{array}{l l l l} y _ {1} & y _ {2} & \dots & y _ {N} \end{array} \right) ^ {T}

\varepsilon = \left( \begin{array}{c c c c} \varepsilon_ {1} & \varepsilon_ {2} & \dots & \varepsilon_ {N} \end{array} \right) ^ {T}

\Phi = \left( \begin{array}{c} \varphi^ {T} (x _ {1}) \\ \vdots \\ \varphi^ {T} (x _ {N}) \end{array} \right)
$$

The least-squares problem can now be formulated in a compact form. The loss function J can be written as

$$J (\theta) = \frac {1}{2} \varepsilon^ {T} \varepsilon = \frac {1}{2} \| \varepsilon \| ^ {2} \tag {13.3}$$

where

$$\varepsilon = y - \hat {y}$$

and

$$\hat {\mathbf {y}} = \Phi \theta$$

Determine the parameter $\theta$ in such a way that $\|\varepsilon\|^{2}$ is minimal. The solution to the least-squares problem is given by the following theorem.

THEOREM 13.1 LEAST-SQUARES SOLUTION The function of (13.3) is minimal for parameters $\hat{\theta}$ such that
