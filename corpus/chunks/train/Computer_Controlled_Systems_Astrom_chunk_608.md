# Example 10.1 Predictor for a step signal

To predict the future value of a step signal, it seems natural to use the current value of the signal. For discrete-time signals, the predictor then becomes

$$\hat {y} ((k + m) h \mid k h) = y (k h)$$

The notation $\hat{y}(t \mid s)$ means the prediction of $y(t)$ based on data available at time s. This predictor has a prediction error at times $t = 0, h, 2h, \ldots, (m - 1)h$ , that is, m steps after the step change in y. It then predicts the signal without error.
