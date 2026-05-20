# Systems with Stable Inverses

By introducing the backward-shift operator $q^{-1}$ , the model in (12.5) can be written as

$$
\begin{array}{l} y (k) = \frac {B (q)}{A (q)} u (k) + \frac {C (q)}{A (q)} e (k) \\ = \frac {B ^ {*} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} q ^ {- d} u (k) + \frac {C ^ {*} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} e (k) \tag {12.23} \\ \end{array}
$$

where

$$d = \deg A - \deg B > 0$$

is the pole excess of the system (see Sec. 2.6). Further, $\deg A = \deg C = n$ . The reciprocal polynomials are introduced to make the discussion based on causality arguments more transparent.

It follows from (12.23) that

$$y (k + d) = \frac {C ^ {*} \left(q ^ {- 1}\right)}{A ^ {*} \left(q ^ {- 1}\right)} e (k + d) + \frac {B ^ {*} \left(q ^ {- 1}\right)}{A ^ {*} \left(q ^ {- 1}\right)} u (k) \tag {12.24}= F ^ {*} (q ^ {- 1}) e (k + d) + \frac {G ^ {*} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} e (k) + \frac {B ^ {*} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} u (k)$$

where Equation (12.20) with $m = d$ has been used to obtain the last equality. The first term of the right-hand side is independent of the data available at time $k$ and thus also of the second and third terms. The second term can be computed exactly in terms of data available at time $k$ . To do this, the variable $e(k)$ is given by (12.23); that is,

$$e (k) = \frac {A ^ {*}}{C ^ {*}} y (k) - q ^ {- d} \frac {B ^ {*}}{C ^ {*}} u (k)$$

where the arguments of the polynomials have been dropped to simplify the writing. Using this expression for e, Eq. (12.24) can be written as

$$
\begin{array}{l} y (k + d) = F ^ {*} e (k + d) + \frac {G ^ {*}}{C ^ {*}} y (k) - q ^ {- d} \frac {B ^ {*} G ^ {*}}{A ^ {*} C ^ {*}} u (k) + \frac {B ^ {*}}{A ^ {*}} u (k) \tag {12.25} \\ = F ^ {*} e (k + d) + \frac {G ^ {*}}{C ^ {*}} y (k) + \frac {B ^ {*} F ^ {*}}{C ^ {*}} u (k) \\ \end{array}
$$

Now let $u(k)$ be an arbitrary function of $y(k), y(k-1), \ldots$ and $u(k-1), u(k-2), \ldots$ . Then

$$\mathrm{E} y ^ {2} (k + d) = \mathrm{E} \left(F ^ {*} e (k + d)\right) ^ {2} + \mathrm{E} \left(\frac {G ^ {*}}{C ^ {*}} y (k) + \frac {B ^ {*} F ^ {*}}{C ^ {*}} u (k)\right) ^ {2} \tag {12.26}$$

The mixed terms vanish because $e(k + d), \ldots, e(k + 1)$ are independent of $y(k), y(k - 1), \ldots$ and $u(k), u(k - 1), \ldots$ . Because the last term in (12.26) is nonnegative, it follows that

$$\mathrm{E} y ^ {2} (k + d) \geq \left(1 + f _ {1} ^ {2} + \dots + f _ {d - 1} ^ {2}\right) \sigma^ {2}$$

where equality is obtained for

$$u (k) = - \frac {G ^ {*} (q ^ {- 1})}{B ^ {*} (q ^ {- 1}) F ^ {*} (q ^ {- 1})} y (k) = - \frac {G (q)}{B (q) F (q)} y (k) \tag {12.27}$$
