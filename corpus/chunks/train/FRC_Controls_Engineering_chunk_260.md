# 9.2 State observers

State observers are used to estimate states which cannot be measured directly. This can be due to noisy measurements or the state not being measurable (a hidden state). This information can be used for localization, which is the process of using external measurements to determine an agent’s pose,[2] or orientation in the world.

One type of state estimator is LQE. “LQE” stands for “Linear-Quadratic Estimator”. Similar to LQR, it places the estimator poles such that it minimizes the sum of squares of the estimation error. The Luenberger observer and Kalman filter are examples of these, where the latter chooses the pole locations optimally based on the model and measurement uncertainties.

Computer vision can also be used for localization. By extracting features from an image taken by the agent’s camera, like a retroreflective target in FRC, and comparing them to known dimensions, one can determine where the agent’s camera would have to be to see that image. This can be used to correct our state estimate in the same way we do with an encoder or gyroscope.
