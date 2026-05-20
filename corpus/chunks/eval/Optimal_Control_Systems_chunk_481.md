$$\boldsymbol {\Phi} (t, t _ {0}) = e ^ {\mathbf {A} (t - t _ {0})} \tag {B.1.7}$$

having the properties

$$\boldsymbol {\Phi} (t _ {0}, t _ {0}) = \mathbf {I}, \quad \boldsymbol {\Phi} (t _ {2}, t _ {1}) \boldsymbol {\Phi} (t _ {1}, t _ {0}) = \boldsymbol {\Phi} (t _ {2}, t _ {0}). \tag {B.1.8}$$

Similarly, the solution of the continuous-time LTV system (B.1.5) is given by

$$\mathbf {x} (t) = \boldsymbol {\Phi} (t, t _ {0}) \mathbf {x} (t _ {0}) + \int_ {t _ {0}} ^ {t} \boldsymbol {\Phi} (t, \tau) \mathbf {B} (\tau) \mathbf {u} (\tau) d \tau\mathbf {y} (t) = \mathbf {C} (t) \boldsymbol {\Phi} (t, t _ {0}) \mathbf {x} (t _ {0}) + \mathbf {C} (t) \int_ {t _ {0}} ^ {t} \boldsymbol {\Phi} (t, \tau) \mathbf {B} (\tau) \mathbf {u} (\tau) d \tau + \mathbf {D} (t) \mathbf {u} (t) \tag {B.1.9}$$

where, $\Phi(t, t_0)$ , still called the state transition matrix of the system (B.1.5), cannot be easily computed analytically, but does satisfy the properties (B.1.8). However, in terms of a fundamental matrix $\mathbf{X}(t)$ satisfying

$$\dot {\mathbf {X}} (t) = \mathbf {A} (t) \mathbf {X} (t) \tag {B.1.10}$$

it can be written as [35]

$$\boldsymbol {\Phi} (t, t _ {0}) = \mathbf {X} (t) \mathbf {X} ^ {- 1} (t _ {0}). \tag {B.1.11}$$
