# 4.4 LQR with a Specified Degree of Stability

with the boundary condition (4.3.17) as $m(t_f) = 0$ . Solving (4.3.36) with this boundary condition, we get

$$m (t) = \frac {b ^ {2}}{r} \left[ \frac {e ^ {- \beta (t - t _ {f})} - e ^ {\beta (t - t _ {f})}}{(a + \beta) e ^ {- \beta (t - t _ {f})} - (a - \beta) e ^ {\beta (t - t _ {f})}} \right] \tag {4.3.37}$$

where, $\beta = \sqrt{a^2 + q\frac{b^2}{r}}$ . Then the optimal control (4.3.35) becomes

$$u ^ {*} (t) = \frac {1}{b} \left[ \frac {(a + \beta) e ^ {- \beta (t - t _ {f})} - (a - \beta) e ^ {\beta (t - t _ {f})}}{e ^ {- \beta (t - t _ {f})} - e ^ {\beta (t - t _ {f})}} \right] x ^ {*} (t). \tag {4.3.38}$$
