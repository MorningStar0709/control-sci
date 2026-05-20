# 9.6.11 Modeling other noise colors

The Kalman filter assumes a model with zero-mean white noise. If the model is incomplete in some way, whether it’s missing dynamics or assumes an incorrect noise model, the residual $\widetilde { \mathbf { y } } = \mathbf { y } - \mathbf { C } \hat { \mathbf { x } }$ over time will have probability characteristics not indicative eof white noise (e.g., it isn’t zero-mean).

To handle other colors of noise in a Kalman filter, define that color of noise in terms of white noise and augment the model with it.
