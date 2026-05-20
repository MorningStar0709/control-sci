# Integral Action

To obtain a controller with integral action we use the same idea as in Sec. 4.5 and introduce a constant disturbance v at the process input. The controller then becomes

$$u (k) = - L \hat {x} (k) - \hat {v} (k) + L _ {c} u _ {r} (k)\hat {x} (k + 1) = \Phi \hat {x} (k) + \Gamma (\hat {v} (k) + u (k)) + K (y (k) - C \hat {x} (k)) \tag {4.52}\hat {v} (k + 1) = \hat {v} (k) + K _ {w} (y (k) - C \hat {x} (k))$$

These equations can also be written as

$$u (k) = - L \hat {x} (k) - \hat {v} (k) + L _ {c} u _ {c} (k)\hat {x} (k + 1) = (\Phi - \Gamma L) \hat {x} (k) + \Gamma L _ {c} u _ {c} (k) + K (y (k) - C \hat {x} (k)) \tag {4.53}\hat {v} (k + 1) = \hat {v} (k) + K _ {w} \left(y (k) - C \hat {x} (k)\right)$$

A comparison with Eq. (4.44) shows that command signal following is obtained by a very simple modification of the systems discussed previously.
