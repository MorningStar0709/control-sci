The inverse Laplace transform of $\mathbf { X } ( s )$ gives the solution ${ \bf x } ( t )$ Thus,.

$$\mathbf {x} (t) = \mathscr {L} ^ {- 1} \left[ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \right] \mathbf {x} (0) \tag {9-35}$$

Note that

$$(s \mathbf {I} - \mathbf {A}) ^ {- 1} = \frac {\mathbf {I}}{s} + \frac {\mathbf {A}}{s ^ {2}} + \frac {\mathbf {A} ^ {2}}{s ^ {3}} + \dots$$

Hence, the inverse Laplace transform of $( s \mathbf { I } - \mathbf { A } ) ^ { - 1 }$ gives

$$\mathcal {L} ^ {- 1} \left[ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \right] = \mathbf {I} + \mathbf {A} t + \frac {\mathbf {A} ^ {2} t ^ {2}}{2 !} + \frac {\mathbf {A} ^ {3} t ^ {3}}{3 !} + \dots = e ^ {\mathbf {A} t} \tag {9-36}$$

(The inverse Laplace transform of a matrix is the matrix consisting of the inverse Laplace transforms of all elements.) From Equations (9–35) and (9–36), the solution of Equation (9–34) is obtained as

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0)$$

The importance of Equation (9–36) lies in the fact that it provides a convenient means for finding the closed solution for the matrix exponential.

State-Transition Matrix. We can write the solution of the homogeneous state equation

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} \tag {9-37}$$

as

$$\mathbf {x} (t) = \boldsymbol {\Phi} (t) \mathbf {x} (0) \tag {9-38}$$

where $\Phi ( t )$ is an $n \times n$ matrix and is the unique solution of

$$\dot {\boldsymbol {\Phi}} (t) = \mathbf {A} \boldsymbol {\Phi} (t), \quad \boldsymbol {\Phi} (0) = \mathbf {I}$$

To verify this, note that

$$\mathbf {x} (0) = \boldsymbol {\Phi} (0) \mathbf {x} (0) = \mathbf {x} (0)$$

and

$$\dot {\mathbf {x}} (t) = \dot {\boldsymbol {\Phi}} (t) \mathbf {x} (0) = \mathbf {A} \boldsymbol {\Phi} (t) \mathbf {x} (0) = \mathbf {A} \mathbf {x} (t)$$

We thus confirm that Equation (9–38) is the solution of Equation (9–37).

From Equations (9–31), (9–35), and (9–38), we obtain

$$\boldsymbol {\Phi} (t) = e ^ {\mathbf {A} t} = \mathscr {L} ^ {- 1} \left[ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \right]$$

Note that

$$\boldsymbol {\Phi} ^ {- 1} (t) = e ^ {- \mathbf {A} t} = \boldsymbol {\Phi} (- t)$$

From Equation (9–38), we see that the solution of Equation (9–37) is simply a transformation of the initial condition. Hence, the unique matrix is called the state-(t) transition matrix. The state-transition matrix contains all the information about the free motions of the system defined by Equation (9–37).
