If we are mainly interested in the first variable x, then the function $\underline { { x } } ^ { 0 } ( \boldsymbol { w } )$ is of primary interest and we have obtained this function quite efficiently. This nested solution approach is an example of a class of techniques known as dynamic programming (DP). DP was developed by Bellman (Bellman, 1957; Bellman and Dreyfus, 1962) as an efficient means for solving these kinds of multistage optimization problems. Bertsekas (1987) provides an overview of DP.

The version of the method we just used is called backward DP because we find the variables in reverse order: first z, then y, and finally x. Notice we find the optimal solutions as functions of the variables to be optimized at the next stage. If we wish to find the other variables y and z as a function of the known parameter w, then we nest the optimal solutions found by the backward DP recursion

$$\underset {\sim} {y} ^ {0} (w) = \underline {{y}} ^ {0} (\underline {{x}} ^ {0} (w)) \quad \underset {\sim} {z} ^ {0} (w) = \underline {{z}} ^ {0} (\underset {\sim} {y} ^ {0} (w)) = \underline {{z}} ^ {0} (\underline {{y}} ^ {0} (\underline {{x}} ^ {0} (w)))$$

As we see shortly, backward DP is the method of choice for the regulator problem.

In the state estimation problem to be considered later in this chapter, w becomes a variable to be optimized, and z plays the role of a parameter. We wish to solve the problem

$$\min _ {w, x, y} f (w, x) + g (x, y) + h (y, z) \quad z \text { fixed }$$

We can still break the problem into three smaller nested problems, but

the order is reversed

$$\underbrace {\min _ {y} \left[ h (y , z) + \overbrace {\min _ {x} [ g (x , y) + \underbrace {\min _ {w} f (w , x)} ]} ^ {\overline {{g}} ^ {0} (y) , \overline {{x}} ^ {0} (y)} \right]} _ {\overline {{h}} ^ {0} (z), \overline {{y}} ^ {0} (z)} \tag {1.7}$$

This form is called forward DP because we find the variables in the order given: first w, then x, and finally y. The optimal value functions and optimal solutions at each of the three stages are shown in (1.7). This version is preferable if we are primarily interested in finding the final variable y as a function of the parameter z. As before, if we need the other optimized variables x and w as a function of the parameter z, we must insert the optimal functions found by the forward DP recursion
