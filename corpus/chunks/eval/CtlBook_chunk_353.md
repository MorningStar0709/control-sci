# 10.2.3 Gain Space Searching and Optimization

As an example, consider a controller having two parameters, $P _ { 1 } , P _ { 2 }$ . For each point $\{ P _ { 1 } , P _ { 2 } \}$ , there is a certain step response and a certain resulting cost. In Figure 10.1, the two values, $P _ { 1 } , P _ { 2 } ^ { \mathrm { ~ ~ } }$ form a plane, and we can represent the cost at each point in the third axis. In the illustration, the point $\{ m , n \}$ represents the lowest value of cost over the whole plane. A simple function like a parabola can usually be easily optimized, however the cost function for step responses is not so simple, and is not known analytically. Our strategy will be to

![](image/6f822e059ca19d67cdc0bdd96bf48406cfd36a23603f03513ebf90b72aedb9f9.jpg)

<details>
<summary>text_image</summary>

Cost
P₂
n
m
P₁
</details>

Figure 10.1: Idealized cost function which has a minimum (optimum) at $P _ { 1 } = m , P _ { 2 } = n$ .

1. Choose initial values for the three gains $K _ { P } , K _ { I } , K _ { D }$ .   
2. Dene a range of each value to search.   
3. Dene how many discrete values to search for each gain, Nvals

4. Try every combination of values and nd those which produce the best step response.

In our PID control design problem, the three parameters could be thought of as forming a 3 dimensional space. Each controller is a single point in that space.

The simplest optimization method is to discretize the parameters and search all of the possible combinations. When the space of all parameter values gets very large, it can be too computationally expensive to try all the possible points in parameter space. In this case special algorithms are used or mathematical assumptions are made to speed the process. In our PID control design however we have only a 3 dimensional parameter space and simulation of step responses is suciently fast that we can do the brute-force exhaustive search in a reasonable time:

for Kp in range(kmin, kmax + dk, dk):

for Ki in range(kimin, kimax + dki, dki):

for Kd in range(kdmin, kdmax + dkd, dkd):

\*\*\* simulation and optimization code here

The algorithm will loop through a set of values for each of the three gains and keep track of which one produced the highest performance by each of the weight schemes.

Search Range We will dene our search range in terms of the center value and a multiplicative range r. If our nominal value is $K _ { 0 } ,$ then

$$K _ {m i n} = K _ {0} / \sqrt {r} \qquad K _ {m a x} = \sqrt {r} \times K _ {0}$$

With this scheme,
