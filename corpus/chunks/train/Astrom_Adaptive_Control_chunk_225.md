# THEOREM 4.2 Asymptotic properties 2

Assume that Algorithm 4.1 with least-squares estimation is applied to Eq. (4.1) and that

$$\min (k, l) \geq n - 1 \tag {4.27}$$

If the asymptotic estimates of $R^{*}$ and $S^{*}$ are relatively prime, the equilibrium solution is such that

$$\overline {{y (t + \tau) y (t)}} = 0 \quad \tau = d, d + 1, \dots \tag {4.28}$$

that is, the output is a moving-average process of order d - 1.

Proof: The closed-loop system is described by

$$R ^ {*} u (t) = - S ^ {*} y (t)A ^ {*} y (t) = B ^ {*} u \left(t - d _ {0}\right) + C ^ {*} e (t)$$

Hence

$$\left(A ^ {*} R ^ {*} + q ^ {- d _ {0}} B ^ {*} S ^ {*}\right) y = R ^ {*} C ^ {*} e\left(A ^ {*} R ^ {*} + q ^ {- d _ {0}} B ^ {*} S ^ {*}\right) u = - S ^ {*} C ^ {*} e$$

Introduce the signal w defined by

$$\left(A ^ {*} R ^ {*} + q ^ {- d _ {0}} B ^ {*} S ^ {*}\right) w = C ^ {*} e \tag {4.29}$$

Hence

$$y = R ^ {*} w \quad \text { and } \quad u = - S ^ {*} w \tag {4.30}$$

The condition of Eq. (4.25) then implies that

$$\overline {{{R ^ {*}}}} \overline {{{w (t)}}} \overline {{{y (t + \tau)}}} = 0 \quad \tau = d, d + 1, \dots , d + l\overline {{{S ^ {*} w (t) y (t + \tau)}}} = 0 \quad \tau = d, d + 1, \dots , d + k$$

If we introduce

$$C _ {w y} (\tau) = \overline {{w (t) y (t + \tau)}}$$

the preceding equations can be written as

$$
\left( \begin{array}{c c c c c c c c} r _ {0} & r _ {1} & r _ {2} & \dots & r _ {k} & 0 & \dots & 0 \\ 0 & r _ {0} & r _ {1} & r _ {2} & \dots & r _ {k} \\ \vdots & \ddots & \ddots & \ddots & \ddots & & \ddots \\ 0 & \dots & 0 & r _ {0} & r _ {1} & r _ {2} & \dots & r _ {k} \\ s _ {0} & s _ {1} & s _ {2} & \dots & s _ {l} & 0 & \dots & 0 \\ 0 & s _ {0} & s _ {1} & s _ {2} & \dots & s _ {l} \\ \vdots & \ddots & \ddots & \ddots & \ddots & & \ddots \\ 0 & \dots & 0 & s _ {0} & s _ {1} & s _ {2} & \dots & s _ {l} \end{array} \right) \left( \begin{array}{c} C _ {w y} (d) \\ \vdots \\ C _ {w y} (d + k - l) \end{array} \right) = 0
$$

Since the Sylvester matrix on the left is nonsingular when $R^*$ and $S^*$ are relatively prime (compare Section 11.4), it follows that

$$C _ {w y} (\tau) = 0 \quad \tau = d, d + 1, \dots , d + k + l$$

The covariance function satisfies the equation

$$F ^ {*} (q ^ {- 1}) C _ {w y} (\tau) = 0 \quad \tau \geq 0$$

The system of Eq. (4.29) has the order

$$n + k = n + \max (k, l)$$

If

$$k + l + 1 \geq n + \max (k, l)$$

or, equivalently,

$$\min (k, l) \geq n - 1$$

it follows that

$$C _ {w y} (\tau) = 0 \quad \tau = d, d + 1, \dots$$

It also follows from Eq. (4.30) that

$$C _ {y} (\tau) = 0 \quad \tau = d, d + 1, \dots$$

which completes the proof.

□
