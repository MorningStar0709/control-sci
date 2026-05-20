Alternate Form: An alternate form for the ARE (5.4.4) is obtained by considering steady-state form of the DRE (5.3.20) as

$$\bar {\mathbf {P}} = \mathbf {A} ^ {\prime} \{\bar {\mathbf {P}} - \bar {\mathbf {P}} \mathbf {B} [ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} ] ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \} \mathbf {A} + \mathbf {Q}. \tag {5.4.7}$$

The optimal feedback control (5.3.24) becomes

$$\mathbf {u} ^ {*} (k) = - \bar {\mathbf {L}} _ {a} \mathbf {x} ^ {*} (k) \tag {5.4.8}$$

where, the alternate optimal-feedback gain matrix (5.3.25) becomes

$$\bar {\mathbf {L}} _ {a} = \left[ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} \right] ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {A}. \tag {5.4.9}$$

The optimal control (5.4.9) with the state (5.4.1) gives us the optimal system

$$\mathbf {x} ^ {*} (k + 1) = \left[ \mathbf {A} - \mathbf {B} \bar {\mathbf {L}} _ {a} \right] \mathbf {x} ^ {*} (k). \tag {5.4.10}$$

Table 5.4 Procedure Summary of Discrete-Time, Linear Quadratic Regulator System: Steady-State Condition
