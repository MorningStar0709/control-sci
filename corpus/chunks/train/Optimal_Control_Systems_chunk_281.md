# 5.3.2 Optimal Cost Function

For finding the optimal cost function $J^{*}(k_{0})$ , we can follow the same procedure as the one used for the continuous-time systems in Chapter 3 to get

$$\boxed {J ^ {*} = \frac {1}{2} \mathbf {x} ^ {* \prime} \left(k _ {0}\right) \mathbf {P} \left(k _ {0}\right) \mathbf {x} \left(k _ {0}\right).} \tag {5.3.28}$$

Let us note that the Riccati function $\mathbf{P}(k)$ is generated off-line before we obtain the optimal control $\mathbf{u}^{*}(k)$ to be applied to the system. Thus, in general for any initial state k, we have the optimal cost as

$$\boxed {J ^ {*} (k) = \frac {1}{2} \mathbf {x} ^ {* \prime} (k) \mathbf {P} (k) \mathbf {x} ^ {*} (k).} \tag {5.3.29}$$

The entire procedure is now summarized in Table 5.3. The actual implementation of this control law is shown in Figure 5.2. We now illustrate the previous procedure by considering a second order system with a general cost function.
