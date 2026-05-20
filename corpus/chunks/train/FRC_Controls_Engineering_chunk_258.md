# 9. Stochastic control theory

Stochastic control theory is a subfield of control theory that deals with the existence of uncertainty either in observations or in noise that drives the evolution of a system. We assign probability distributions to this random noise and aim to achieve a desired control task despite the presence of this uncertainty.

Stochastic optimal control is concerned with doing this with minimum cost defined by some cost functional, like we did with LQR earlier. First, we’ll cover the basics of probability and how we represent linear stochastic systems in state-space representation. Then, we’ll derive an optimal estimator using this knowledge, the Kalman filter, and demonstrate creative applications of the Kalman filter theory.

This will be a math-heavy introduction, so read Kalman and Bayesian Filters in Python by Roger Labbe[1] first.
