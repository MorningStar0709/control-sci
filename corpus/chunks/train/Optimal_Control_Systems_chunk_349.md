$$J _ {k _ {f} - 1} ^ {*} = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f} - 1) \left[ \left\{\mathbf {A} - \mathbf {B L} (k _ {f} - 1) \right\} ^ {\prime} \mathbf {F} \left\{\mathbf {A} - \mathbf {B L} (k _ {f} - 1) \right\} \right.\left. + \mathbf {L} ^ {\prime} \left(k _ {f} - 1\right) \mathbf {R L} \left(k _ {f} - 1\right) + \mathbf {Q} \right] \mathbf {x} \left(k _ {f} - 1\right)= \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f} - 1) \mathbf {P} (k _ {f} - 1) \mathbf {x} (k _ {f} - 1) \tag {6.3.23}$$

where,

$$\mathbf {P} \left(k _ {f} - 1\right) = \left\{\mathbf {A} - \mathbf {B L} \left(k _ {f} - 1\right) \right\} ^ {\prime} \mathbf {F} \left\{\mathbf {A} - \mathbf {B L} \left(k _ {f} - 1\right) \right\}+ \mathbf {L} ^ {\prime} (k _ {f} - 1) \mathbf {R L} (k _ {f} - 1) + \mathbf {Q} \tag {6.3.24}$$

Stage: $k_{f} - 2$

Using $i = k_{f} - 2$ in the cost function (6.3.16), we have

$$J _ {k _ {f} - 2} = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f}) \mathbf {F x} (k _ {f}) + \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f} - 2) \mathbf {Q x} (k _ {f} - 2)+ \frac {1}{2} \mathbf {u} ^ {\prime} \left(k _ {f} - 2\right) \mathbf {R u} \left(k _ {f} - 2\right) + \frac {1}{2} \mathbf {x} ^ {\prime} \left(k _ {f} - 1\right) \mathbf {Q x} \left(k _ {f} - 1\right)+ \frac {1}{2} \mathbf {u} ^ {\prime} (k _ {f} - 1) \mathbf {R u} (k _ {f} - 1). \tag {6.3.25}$$

Now, using (6.3.15) to replace $k_{f}$ , (6.3.21) to replace $u(k_{f} - 1)$ and (6.3.24) in (6.3.25), we get

$$J _ {k _ {f} - 2} = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f} - 2) \mathbf {Q x} (k _ {f} - 2) + \frac {1}{2} \mathbf {u} ^ {\prime} (k _ {f} - 2) \mathbf {R u} (k _ {f} - 2)+ \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f} - 1) \mathbf {P} (k _ {f} - 1) \mathbf {x} (k _ {f} - 1) \tag {6.3.26}$$

where, $\mathbf{P}(k_{f}-1)$ is given by (6.3.24). At this stage, we need to express all functions at stage $k_{f}-2$ . Then, once again, for this stage, to determine $\mathbf{u}^{*}(k_{f}-2)$ according to the optimality principle (6.3.4), we minimize $J_{k_{f}-2}$ in (6.3.26) w.r.t. $\mathbf{u}(k_{f}-2)$ and get relations similar to (6.3.21), (6.3.22), (6.3.23), and (6.3.24). For example, the optimal cost function becomes

$$J _ {k _ {f} - 2} ^ {*} = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f} - 2) \mathbf {P} (k _ {f} - 2) \mathbf {x} (k _ {f} - 2) \tag {6.3.27}$$
