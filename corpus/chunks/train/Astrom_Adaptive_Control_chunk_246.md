# 4.6 ADAPTIVE PREDICTIVE CONTROL

Algorithm 4.1 is one way to make a controller with a variable prediction horizon. The underlying control problem is the moving-average controller. The moving-average controller may also be used for nonminimum-phase systems, as was illustrated in Section 4.3.

In using the minimum-variance controller or the moving-average controller the output is predicted only at one future time. The prediction horizon d is then a design parameter. The predicted output can also be computed for different prediction horizons and then used in a loss function. Several ways to achieve predictive control have been suggested in the literature; we now discuss and analyze some of these. The case with known parameters is first analyzed before the adaptive versions are discussed.

Predictive control algorithms are based on an assumed model of the process and on an assumed scenario for the future control signals. This gives a sequence of control signals. Only the first one is applied to the process, and a new sequence of control signals is calculated when a new measurement is obtained. This is called a receding-horizon controller. There are many variants of predictive control, for instance, model predictive control, dynamic matrix control, generalized predictive control, and extended horizon control. The methodology has been used extensively in chemical process control.
