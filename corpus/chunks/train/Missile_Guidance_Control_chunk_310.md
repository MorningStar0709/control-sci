# 4.6 Augmented Proportional Navigation

We have seen in the previous section that the basic proportional navigation law is expressed as

$$a _ {n} = N V _ {c} \left(\frac {d \lambda}{d t}\right), \tag {4.24}$$

where N is the navigation constant, $V _ { c }$ is the interceptor missile’s closing velocity, and $d \lambda / d t$ is the line-of-sight angle rate measured by the onboard radar or other sensor. The missile’s lateral (or normal) acceleration $a _ { n }$ (note that here we use the subscript n instead of l to indicate the missile’s lateral or normal acceleration) history is in general invariant. This lateral acceleration is desired to be normal to the LOS. For aerodynamically maneuvering missiles, this acceleration occurs normal to the instantaneous velocity vector. Moreover, the effective navigation ratio takes several values. For instance, for $N \geq 3$ , a nearly straight-line missile trajectory results. Guidance accuracy decreases as N increases. Next, we note that the line of sight is given by

$$\lambda = y / R _ {M T} = y / V _ {c} (t _ {f} - t), \tag {4.71}$$

where y is the relative missile–target separation, $R _ { M T }$ is the range from the missile to the target, $t _ { f }$ is the final intercept time, and t is the present time (note that as discussed earlier in this chapter, $t _ { f } - t = t _ { g o } )$ . Taking the derivative of (4.71) results in [17], [35]

$$\frac {d \lambda}{d t} = (1 / V _ {c} t _ {g o} ^ {2}) [ y + \dot {y} t _ {g o} ]. \tag {4.72}$$

Making use of (4.72), (4.24) can now be written in the form

$$a _ {n} = N V _ {c} \left(\frac {d \lambda}{d t}\right) = (N / t _ {g o} ^ {2}) \left[ y + \left(\frac {d y}{d t}\right) t _ {g o} \right], \tag {4.73}$$

where the navigation constant N is given by (4.32a).

The expression in the brackets represents the miss distance that would occur, assuming no target maneuver and if the missile underwent no further corrective acceleration. This miss distance is called zero effort miss and is perpendicular to the $L O S .$ . However, if the target undergoes, say, a constant maneuver, the zero effort miss term in (4.72) or (4.73) must be augmented by an additional term as follows [35]:

$$a _ {n} = (N / t _ {g o} ^ {2}) \left[ y + \left(\frac {d y}{d t}\right) t _ {g o} + (1 / 2) a _ {T} t _ {g o} ^ {2} \right], \tag {4.74}$$

where $a _ { T }$ represents the additional term due to the target maneuver. Thus, in the presence of target maneuver, and using (4.73), we have
