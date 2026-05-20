\- Step 4: Closed-Loop Optimal Control: The state space representation shown in Figure 3.1 prompts us to think that we can obtain the optimal control $\mathbf{u}^{*}(t)$ as a function (negative feedback) of the optimal state $\mathbf{x}^{*}(t)$ . Now to formulate a closed-loop optimal control, that is, to obtain the optimal control $\mathbf{u}^{*}(t)$ which is a function of the costate $\boldsymbol{\lambda}^{*}(t)$ as seen from (3.2.5), as a function of the state $\mathbf{x}^{*}(t)$ , let us examine the final condition on $\boldsymbol{\lambda}^{*}(t)$ given by (3.2.10). This in fact relates the costate in terms of the state at the final time $t_{f}$ . Similarly, we may like to connect the costate with the state for the complete interval of time $[t_{0}, t_{f}]$ . Thus, let us assume a transformation [113, 102]

$$\boldsymbol {\lambda} ^ {*} (t) = \mathbf {P} (t) \mathbf {x} ^ {*} (t) \tag {3.2.11}$$

where, $\mathbf{P}(t)$ is yet to be determined. Then, we can easily see that with (3.2.11), the optimal control (3.2.5) becomes

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t) \tag {3.2.12}$$

which is now a negative feedback of the state $\mathbf{x}^{*}(t)$ . Note that this negative feedback resulted from our “theoretical development” or “mathematics” of optimal control procedure and not introduced intentionally [6].

Differentiating (3.2.11) w.r.t. time $t$ , we get

$$\dot {\boldsymbol {\lambda}} ^ {*} (t) = \dot {\mathbf {P}} (t) \mathbf {x} ^ {*} (t) + \mathbf {P} (t) \dot {\mathbf {x}} ^ {*} (t). \tag {3.2.13}$$

Using the transformation (3.2.11) in the control, state and costate system of equations (3.2.5), (3.2.6) and (3.2.7), respectively, we get

$$\dot {\mathbf {x}} ^ {*} (t) = \mathbf {A} (t) \mathbf {x} ^ {*} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t), \tag {3.2.14}\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \mathbf {Q} (t) \mathbf {x} ^ {*} (t) - \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t). \tag {3.2.15}$$

Now, substituting state and costate relations (3.2.14) and (3.2.15) in (3.2.13), we have
