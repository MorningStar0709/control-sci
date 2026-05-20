# Minimum-Phase Systems

If the process dynamics is minimum phase, we have $\deg A_{o} = \deg A - \deg B - 1$ , $B^{-}$ is simply a constant, and Eq. (3.24) becomes

$$A _ {m} A _ {o} y (t) = b _ {0} \left(R u (t) + S y (t)\right) = \tilde {R} u (t) + \tilde {S} y (t) \tag {3.25}$$

where R is monic, $\tilde{R} = b_{0}R$ , and $\tilde{S} = b_{0}S$ . Since R and $\tilde{R}$ differ only by R being monic, we will not use a separate notation in the following discussion. When it is necessary, we will simply note whether or not R is monic.

When all process zeros are canceled, it is also natural to choose specifications so that

$$B _ {m} = q ^ {d _ {0}} A _ {m} (1)$$

where $d_{0} = \deg A - \deg B$ . This gives response with minimal delay and unit static gain.

By introducing the parameter vector

$$
\theta = \left( \begin{array}{c c c c c c} r _ {0} & \dots & r _ {\ell} & s _ {0} & \dots & s _ {\ell} \end{array} \right)
$$

and the regression vector

$$
\varphi (t) = \left( \begin{array}{c c c c c c} u (t) & \dots & u (t - \ell) & y (t) & \dots & y (t - \ell) \end{array} \right)
$$

the model given by Eq. (3.25) can be written as

$$\eta (t) = A _ {o} ^ {*} \left(q ^ {- 1}\right) A _ {m} ^ {*} \left(q ^ {- 1}\right) y (t) = \varphi^ {T} (t - d _ {0}) \theta \tag {3.26}$$

Since $\eta(t)$ can be computed from $y(t)$ , it can be regarded as an auxiliary output, and a recursive estimate of the parameters can now be obtained as described in Chapter 2.

This estimation method works very well if there is little noise, but the operation $A_{o}^{*}(q^{-1})A_{m}^{*}(q^{-1})y(t)$ may amplify noise significantly. The following method can be used to overcome this. Rewrite Eq. (3.25) as

$$y (t) = \frac {1}{A _ {o} A _ {m}} (R u (t) + S y (t)) = R ^ {*} u _ {f} (t - d _ {0}) + S ^ {*} y _ {f} (t - d _ {0}) \tag {3.27}$$

where

$$u _ {f} (t) = \frac {1}{A _ {o} ^ {*} (q ^ {- 1}) A _ {m} ^ {*} (q ^ {- 1})} u (t) \tag {3.28}y _ {f} (t) = \frac {1}{A _ {0} ^ {*} (q ^ {- 1}) A _ {m} ^ {*} (q ^ {- 1})} y (t)$$

and $d_0 = \deg A - \deg B$ . We have further assumed that $\deg R = \deg S = \deg (A_o A_m) - d_0 = \ell$ . Equation (3.27) can be used for least-squares estimation. If we introduce

$$
\theta = \left( \begin{array}{c c c c c c} r _ {0} & \dots & r _ {\ell} & s _ {0} & \dots & s _ {\ell} \end{array} \right)
$$

and

$$
\varphi (t) = \left( \begin{array}{l l l l l} u _ {f} (t) & \dots & u _ {f} (t - \ell) & y _ {f} (t) & \dots & y _ {f} (t - \ell) \end{array} \right)
$$

it can be written as

$$y (t) = \varphi^ {T} (t - d _ {0}) \theta$$

The estimates are then obtained recursively from Eqs. (3.22). The following adaptive control algorithm is then obtained.
