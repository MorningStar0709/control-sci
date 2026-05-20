The last term is zero because $e(k+m), e(k+m-1), \ldots$ , and $e(k+1)$ have zero mean values and are independent of $y(k), y(k-1), \ldots$ . The predictor that minimizes the mean-square prediction error is thus given by (12.16) and the prediction error by (12.18). The proof is completed by taking the mean value of the square of the prediction error (12.18). This gives (12.19).

Remark 1. Notice that the best predictor is linear. The linearity does not depend critically on the minimum-variance criterion. If the probability density of $y(k)$ is symmetric, the predictor of (12.16) is optimal for all criteria of the form $\mathbf{E}g\left((y(k+m)-\hat{y})^{2}\right)$ for symmetric g.

Remark 2. The assumption that $e(i)$ and $e(j)$ are independent for $i \neq j$ is essential for the last term in (12.21) to vanish. If the variables are uncorrelated, the term will still vanish if the predictor $\hat{y}$ is restricted to being linear.

Remark 3. It follows from (12.18) that

$$\tilde {y} (k + 1 \mid k) = y (k + 1) - \hat {y} (k + 1 \mid k) = e (k + 1)$$

The random variables $e(k)$ can thus be interpreted as the innovations of the process $y(k)$ (compare with Sec. 10.4).

Remark 4. Notice that the function

$$J (m) = \sigma^ {2} \left(1 + f _ {1} ^ {2} + \dots + f _ {m - 1} ^ {2}\right)$$

is the variance of the prediction error over the time interval $mh$ . The function $J(m)$ approaches the variance of $y$ as $m \to \infty$ . A graph of the function $J$ shows how well the process may be predicted over different horizons. See Example 12.3.

Remark 5. The predictor discussed in this section is equivalent to the steady-state predictor obtained using the Kalman filter in Sec.11.3 (see Example 11.6).
