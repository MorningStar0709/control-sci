$$\tilde {\boldsymbol {\eta}} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \tilde {\boldsymbol {\eta}} + \left[ \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \mathbf {K} _ {e} + \mathbf {A} _ {b a} - \mathbf {K} _ {e} \mathbf {A} _ {a a} \right] y + \left(\mathbf {B} _ {b} - \mathbf {K} _ {e} B _ {a}\right) u$$

define, similar to the case of the derivation of Equation (10–90),

$$\hat {\mathbf {A}} = \mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\hat {\mathbf {B}} = \hat {\mathbf {A}} \mathbf {K} _ {e} + \mathbf {A} _ {b a} - \mathbf {K} _ {e} A _ {a a}\hat {\mathbf {F}} = \mathbf {B} _ {b} - \mathbf {K} _ {e} B _ {a}$$

Then, the following three equations define the minimum-order oberver:

$$\dot {\tilde {\boldsymbol {\eta}}} = \hat {\mathbf {A}} \tilde {\boldsymbol {\eta}} + \hat {\mathbf {B}} y + \hat {\mathbf {F}} u \tag {10-101}\widetilde {\boldsymbol {\eta}} = \widetilde {\mathbf {x}} _ {b} - \mathbf {K} _ {e} y \tag {10-102}u = - \mathbf {K} \widetilde {\mathbf {x}} \tag {10-103}$$

Since Equation (10–103) can be rewritten as

$$
u = - \mathbf {K} \widetilde {\mathbf {x}} = - \left[ \begin{array}{c c} K _ {a} & \mathbf {K} _ {b} \end{array} \right] \left[ \begin{array}{c} y \\ \widetilde {\mathbf {x}} _ {b} \end{array} \right] = - K _ {a} y - \mathbf {K} _ {b} \widetilde {\mathbf {x}} _ {b}
= - \mathbf {K} _ {b} \widetilde {\boldsymbol {\eta}} - \left(K _ {a} + \mathbf {K} _ {b} \mathbf {K} _ {e}\right) y \tag {10-104}
$$

by substituting Equation (10–104) into Equation (10–101), we obtain

$$\dot {\widetilde {\boldsymbol {\eta}}} = \hat {\mathbf {A}} \widetilde {\boldsymbol {\eta}} + \hat {\mathbf {B}} y + \hat {\mathbf {F}} \left[ - \mathbf {K} _ {b} \widetilde {\boldsymbol {\eta}} - \left(K _ {a} + \mathbf {K} _ {b} \mathbf {K} _ {e}\right) y \right]= \left(\hat {\mathbf {A}} - \hat {\mathbf {F}} \mathbf {K} _ {b}\right) \widetilde {\boldsymbol {\eta}} + \left[ \hat {\mathbf {B}} - \hat {\mathbf {F}} \left(K _ {a} + \mathbf {K} _ {b} \mathbf {K} _ {e}\right) \right] y \tag {10-105}$$

Define

$$\widetilde {\mathbf {A}} = \hat {\mathbf {A}} - \hat {\mathbf {F}} \mathbf {K} _ {b}\widetilde {\mathbf {B}} = \hat {\mathbf {B}} - \hat {\mathbf {F}} \left(K _ {a} + \mathbf {K} _ {b} \mathbf {K} _ {e}\right)\widetilde {\mathbf {C}} = - \mathbf {K} _ {b}\widetilde {D} = - \left(K _ {a} + \mathbf {K} _ {b} \mathbf {K} _ {e}\right)$$

Then Equations (10–105) and (10–104) can be written as
