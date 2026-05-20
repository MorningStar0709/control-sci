# ALGORITHM 4.1 Basic direct self-tuning algorithm

Data: Given the prediction horizon d, let k and l be the degrees of the $R^{*}$ and $S^{*}$ polynomials, respectively. Let $Q^{*}/P^{*}$ be a stable filter.

Step 1: Estimate the coefficients of the polynomials $R^{*}$ and $S^{*}$ of the model

$$y (t + d) = R ^ {*} \left(q ^ {- 1}\right) u _ {f} (t) + S ^ {*} \left(q ^ {- 1}\right) y _ {f} (t) + \varepsilon (t + d) \tag {4.23}$$

where

$$
\begin{array}{l} R ^ {*} (q ^ {- 1}) = r _ {0} + r _ {1} q ^ {- 1} + \dots + r _ {k} q ^ {- k} \\ S ^ {*} (q ^ {- 1}) - s _ {0} + s _ {1} q ^ {- 1} + \dots + s _ {l} q ^ {- l} \\ \end{array}
$$

and

$$
\begin{array}{l} u _ {f} (t) = \frac {Q ^ {*} (q ^ {- 1})}{P ^ {*} (q ^ {- 1})} u (t) \\ y _ {f} (t) = \frac {Q ^ {*} (q ^ {- 1})}{P ^ {*} (q ^ {- 1})} y (t) \\ \end{array}
$$

using Eq. (2.21) with

$$
\begin{array}{l} \varepsilon (t) = y (t) - R ^ {*} u _ {f} (t - d) - S ^ {*} y _ {f} (t - d) = y (t) - \varphi^ {T} (t - d) \hat {\theta} (t - 1) \\ \varphi^ {T} (t) = \frac {Q ^ {*} (q ^ {- 1})}{P ^ {*} (q ^ {- 1})} \left( \begin{array}{l l l l l l} u (t) & \dots & u (t - k) & y (t) & \dots & y (t - l) \end{array} \right) \\ \theta^ {T} = \left( \begin{array}{c c c c c c} r _ {0} & \dots & r _ {k} & s _ {0} & \dots & s _ {l} \end{array} \right) \\ \end{array}
$$

Step 2: Calculate the control signal from

$$R ^ {*} (q ^ {- 1}) u (t) = - S ^ {*} (q ^ {- 1}) y (t) \tag {4.24}$$

with $R^*$ and $S^*$ given by the estimates obtained in Step 1.

Repeat Steps 1 and 2 at each sampling period.

Remark 1. Notice that this algorithm is the same as Algorithm 3.3 when $u_{c} = 0$ , but with different filters.

Remark 2. The parameter $r_0$ can either be estimated or be assumed to be known. In the latter case it is convenient to write $R^*$ as

$$R ^ {*} (q ^ {- 1}) = r _ {0} \left(1 + r _ {1} ^ {\prime} q ^ {- 1} + \dots + r _ {k} ^ {\prime} q ^ {- k}\right)$$

and use

$$
\begin{array}{l} \varepsilon (t) = y (t) - r _ {0} u _ {f} (t - d) - \varphi^ {T} (t - d) \hat {\theta} (t - 1) \\ \varphi^ {T} (t) = \frac {Q ^ {*} (q ^ {- 1})}{P ^ {*} (q ^ {- 1})} \left( \begin{array}{l l l l l l} r _ {0} u (t - 1) & \dots & r _ {0} u (t = k) & y (t) & \dots & y (t - l) \end{array} \right) \\ \theta^ {T} = \left( \begin{array}{c c c c c c} r _ {1} ^ {\prime} & \dots & r _ {k} ^ {\prime} & s _ {0} & \dots & s _ {l} \end{array} \right) \\ \end{array}
$$
