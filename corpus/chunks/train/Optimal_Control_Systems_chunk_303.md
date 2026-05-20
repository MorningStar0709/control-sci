# 5.5 Discrete-Time Linear Quadratic Tracking System

and substituting for the state from (5.5.6) in (5.5.20),

$$\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {P} (k + 1) [ \mathbf {A x} ^ {*} (k) + \mathbf {B u} ^ {*} (k) ] + \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {g} (k + 1). \tag {5.5.21}$$

Now premultiplying by $\mathbf{R}$ and solving for the optimal control $\mathbf{u}^{*}(k)$ we have

$$\boxed {\mathbf {u} ^ {*} (k) = - \mathbf {L} (k) \mathbf {x} ^ {*} (k) + \mathbf {L} _ {g} (k) \mathbf {g} (k + 1)} \tag {5.5.22}$$

where, the feedback gain $\mathbf{L}(k)$ and the feed forward gain $\mathbf{L}_{g}(k)$ are given by

$$\mathbf {L} (k) = \left[ \mathbf {R} + \mathbf {B} ^ {\prime} \mathbf {P} (k + 1) \mathbf {B} \right] ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {P} (k + 1) \mathbf {A} \tag {5.5.23}\mathbf {L} _ {g} (k) = \left[ \mathbf {R} + \mathbf {B} ^ {\prime} \mathbf {P} (k + 1) \mathbf {B} \right] ^ {- 1} \mathbf {B} ^ {\prime} \tag {5.5.24}$$

The optimal state trajectory is now given from (5.5.6) and (5.5.22) as

$$\mathbf {x} ^ {*} (k + 1) = [ \mathbf {A} - \mathbf {B L} (k) ] \mathbf {x} (k) + \mathbf {B L} _ {g} (k) \mathbf {g} (k + 1). \tag {5.5.25}$$

The implementation of the discrete-time optimal tracker is shown in Figure 5.12. The complete procedure for the linear quadratic tracking system is summarized in Table 5.5.
