# Exercise 6.20: Time-varying controller iterations

We let $p _ { k } \ge 0$ be a time-varying integer-valued index representing the iterations applied in the controller at time k.

$$x _ {1} (k + 1) = A _ {1} x _ {1} (k) + \overline {{B}} _ {1 1} u _ {1} (0; k) + \overline {{B}} _ {1 2} u _ {2} (0; k)x _ {2} (k + 1) = A _ {2} x _ {2} (k) + \overline {{B}} _ {2 1} u _ {1} (0; k) + \overline {{B}} _ {2 2} u _ {2} (0; k)\mathbf {u} _ {1} (k + 1) = g _ {1} ^ {p _ {k}} \left(x _ {1} (k), x _ {2} (k), \mathbf {u} _ {1} (k), \mathbf {u} _ {2} (k)\right)\mathbf {u} _ {2} (k + 1) = g _ {2} ^ {p _ {k}} \left(x _ {1} (k), x _ {2} (k), \mathbf {u} _ {1} (k), \mathbf {u} _ {2} (k)\right)$$

Notice the system evolution is time-varying even though the models are time invariant because we allow a time-varying sequence of controller iterations.

Show that cooperative MPC is exponentially stabilizing for any $p _ { k } \ge 0$ sequence.
