$$u (t) + r _ {1} u (t - 1) = t _ {0} u _ {c} (t) - s _ {0} y (t) - s _ {1} y (t - 1)$$

The controller parameters were expressed as functions of the model parameters and the specifications. Figure 3.4 shows the process output and the control signal in a simulation of the process with the self-tuner when the command signal is a square wave. The output converges to the model output after an initial transient. The control signal has a severe oscillation ("ringing") with a period of two sampling periods. This is due to the cancellation of the process zero at $z = -b_{1} / b_{0} = -0.84$ . This oscillation is a consequence of a bad choice of the underlying design methodology. The initial transient depends critically on the initial values of the estimator. In this particular case these values were $\hat{a}_1(0) = \hat{a}_2(0) = 0$ , $\hat{b}_0(0) = 0.01$ , and $\hat{b}_1(0) = 0.2$ . Notice that it is necessary that $\hat{b}_0 \neq 0$ . (Compare with Example 3.1.) The initial covariance matrix was diagonal with $P(1,1) = P(2,2) = 100$ and $P(3,3) = P(4,4) = 1$ . The reason for using different values for parameters $\hat{a}_i$ and $\hat{b}_i$ is that these parameters differ by an order of magnitude.

The parameter estimates are shown in Fig. 3.5. The behavior of the estimates depends critically on the initial values of the estimator. Notice that the estimates converge quickly. They are close to their correct values already at time t = 5. The estimates obtained at time t = 100 are

$$\hat {a} _ {1} (1 0 0) = - 1. 6 0 \quad (- 1. 6 0 6 5) \quad \hat {b} _ {0} (1 0 0) = 0. 1 0 7 \quad (0. 1 0 6 5)\hat {a} _ {2} (1 0 0) = 0. 6 0 \quad (0. 6 0 6 5) \quad \hat {b} _ {1} (1 0 0) = 0. 0 9 2 \quad (0. 0 9 0 2)$$

These values are quite close to the true values, which are given in parentheses. The controller parameters obtained at time t = 100 are

$$r _ {1} (1 0 0) = 0. 8 5 \quad (0. 8 4 6 7) \quad t _ {0} (1 0 0) = 1. 6 5 \tag {1.6531}s _ {0} (1 0 0) = 2. 6 4 \quad (2. 6 8 5 2) \quad s _ {1} (1 0 0) = - 0. 9 9 \quad (- 1. 0 3 2 1)$$

B

The system in Example 3.4 behaves quite well, apart from the “ringing” control signal. This can be avoided by using a design in which the process zero is not canceled. The consequences of this are illustrated in the next example.
