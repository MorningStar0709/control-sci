Integrating the preceding equation between 0 and t gives

$$e ^ {- \mathbf {A} t} \mathbf {x} (t) - \mathbf {x} (0) = \int_ {0} ^ {t} e ^ {- \mathbf {A} \tau} \mathbf {B u} (\tau) d \tau$$

or

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B u} (\tau) d \tau \tag {9-41}$$

Equation (9–41) can also be written as

$$\mathbf {x} (t) = \boldsymbol {\Phi} (t) \mathbf {x} (0) + \int_ {0} ^ {t} \boldsymbol {\Phi} (t - \tau) \mathbf {B u} (\tau) d \tau \tag {9-42}$$

where $\boldsymbol { \Phi } ( t ) = e ^ { \mathbf { A } t }$ Equation (9–41) or (9–42) is the solution of Equation (9–40). The. solution x(t) is clearly the sum of a term consisting of the transition of the initial state and a term arising from the input vector.

Laplace Transform Approach to the Solution of Nonhomogeneous State Equations. The solution of the nonhomogeneous state equation

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}$$

can also be obtained by the Laplace transform approach.The Laplace transform of this last equation yields

$$s \mathbf {X} (s) - \mathbf {x} (0) = \mathbf {A X} (s) + \mathbf {B U} (s)$$

or

$$(s \mathbf {I} - \mathbf {A}) \mathbf {X} (s) = \mathbf {x} (0) + \mathbf {B U} (s)$$

Premultiplying both sides of this last equation by $( s \mathbf { I } - \mathbf { A } ) ^ { - 1 }$ , we obtain

$$\mathbf {X} (s) = (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {x} (0) + (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B U} (s)$$

Using the relationship given by Equation (9–36) gives

$$\mathbf {X} (s) = \mathscr {L} \left[ e ^ {\mathbf {A} t} \right] \mathbf {x} (0) + \mathscr {L} \left[ e ^ {\mathbf {A} t} \right] \mathbf {B U} (s)$$

The inverse Laplace transform of this last equation can be obtained by use of the convolution integral as follows:

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B u} (\tau) d \tau$$

Solution in Terms of $\mathbf { x } \big ( t _ { 0 } \big ) .$ Thus far we have assumed the initial time to be zero.. If, however, the initial time is given by $t _ { 0 }$ instead of 0, then the solution to Equation (9–40) must be modified to

$$\mathbf {x} (t) = e ^ {\mathbf {A} \left(t - t _ {0}\right)} \mathbf {x} \left(t _ {0}\right) + \int_ {t _ {0}} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B u} (\tau) d \tau \tag {9-43}$$

EXAMPLE 9–6 Obtain the time response of the following system:
