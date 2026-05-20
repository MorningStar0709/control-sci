# THEOREM 8.1 Limit cycle period

Assume that the system defined in Fig. 8.3 and by Eqs. (8.9) and (8.10) has a symmetric limit cycle with period T. The period T is then the smallest value of T > 0 that satisfies the equation

$$C (I + \Phi) ^ {- 1} \Gamma = 0 \tag {8.11}$$

where

$$\Phi = e ^ {A T / 2}$$

and

$$\Gamma = \int_ {0} ^ {T / 2} e ^ {A s} d s B$$

Proof: Let $t_{k}$ denote the times when the relay switches. Since the limit cycle is symmetric, it follows that

$$t _ {k + 1} - t _ {k} = T / 2$$

Assume that the control signal $u$ is $d$ over the interval $(t_k, t_{k+1})$ . Integration of Eqs. (8.9) over the interval gives

$$x (t _ {k + 1}) = \Phi x (t _ {k}) + \Gamma d$$

Since the limit cycle is symmetric, it also follows that

$$x (t _ {k + 1}) = - x (t _ {k})$$

Hence

$$x (t _ {k}) = - (I + \Phi) ^ {- 1} \Gamma d$$

Since the output $y(t)$ must be zero at $t_k$ , it follows that

$$y (t _ {k}) = C x (t _ {k}) = - C (I + \Phi) ^ {- 1} \Gamma d = 0$$

which gives Eq. (8.11).

Remark 1. The condition of Eq. (8.11) can also be written as

$$H _ {T / 2} (- 1) = 0 \tag {8.12}$$

where $H_{T/2}(z)$ is the pulse transfer function obtained when sampling the system of Eqs. (8.9) with period T/2.

Remark 2. The result that the period is given by Eq. (8.12) also holds for linear systems with a time delay, provided that T/2 is larger than or equal to the delay.

Remark 3. Similar conditions can also be derived for relays with hysteresis.

□
