# Stability of Stochastic Self-Tuners

Averaging methods can be used for stability analysis of stochastic self-tuning regulators. Consider a simple self-tuner based on least-squares estimation and minimum-variance control (Algorithm 4.1 with $Q^{*} = P^{*} = 1$ ). Let the algorithm be applied to a system described by Eq. (6.71). The self-tuner is assumed to be compatible with the model in the sense that the time delay and the model orders are the same. The closed-loop system is globally stable if the pulse transfer function

$$G (z) = \frac {1}{C (z)} - \frac {1}{2}$$

is SPR (see Ljung (1977b)). The filter $P^{*}$ that is used to filter the regressors can be interpreted as an estimate of the observer polynomial $C^{*}$ . The condition for global stability is then that the transfer function

$$G (z) = \frac {P (z)}{C (z)} - \frac {1}{2}$$

is SPR. The local stability condition is that the real part of polynomial $C(z)$ is positive at all zeros of the polynomial $B(z)$ (see Holst (1979)). The method with stochastic averaging is illustrated with three examples.
