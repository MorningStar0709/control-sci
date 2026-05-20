# 1.3.2 Optimizing Multistage Functions

We next provide a brief introduction to methods for solving multistage optimization problems like (1.6). Consider the set of variables w, x, y, and z, and the following function to be optimized

$$f (w, x) + g (x, y) + h (y, z)$$

Notice that the objective function has a special structure in which each stage’s cost function in the sum depends only on adjacent variable pairs. For the first version of this problem, we consider w to be a fixed parameter, and we would like to solve the problem

$$\min _ {x, y, z} f (w, x) + g (x, y) + h (y, z) \quad w \text { fixed }$$

One option is to optimize simultaneously over all three decision variables. Because of the objective function’s special structure, however, we can obtain the solution by optimizing a sequence of three singlevariable problems defined as follows

$$\min _ {x} \left[ f (w, x) + \min _ {y} \left[ g (x, y) + \min _ {z} h (y, z) \right] \right]$$

We solve the inner problem over z first, and denote the optimal value and solution as follows

$$\underline {{h}} ^ {0} (y) = \min _ {z} h (y, z) \quad \underline {{z}} ^ {0} (y) = \arg \min _ {z} h (y, z)$$

Notice that the optimal z and value function for this problem are both expressed as a function of the y variable. We then move to the next optimization problem and solve for the y variable

$$\min _ {y} g (x, y) + \underline {{h}} ^ {0} (y)$$

and denote the solution and value function as

$$\underline {{g}} ^ {0} (x) = \min _ {y} g (x, y) + \underline {{h}} ^ {0} (y) \quad \underline {{y}} ^ {0} (x) = \arg \min _ {y} g (x, y) + \underline {{h}} ^ {0} (y)$$

The optimal solution for y is a function of x, the remaining variable to be optimized. The third and final optimization is

$$\min _ {x} f (w, x) + \underline {{g}} ^ {0} (x)$$

with solution and value function

$$\underline {{f}} ^ {0} (w) = \min _ {x} f (w, x) + \underline {{g}} ^ {0} (x) \quad \underline {{x}} ^ {0} (w) = \arg \min _ {x} f (w, x) + \underline {{g}} ^ {0} (x)$$

We summarize the recursion with the following annotated equation

$$\underbrace {\min _ {x} \left[ f (w , x) + \overbrace {\min _ {y} \left[ g (x , y) + \underbrace {\min _ {z} h (y , z)} _ {\underline {{h}} ^ {0} (y) , \underline {{z}} ^ {0} (y)} \right]} ^ {\underline {{g}} ^ {0} (x) , \underline {{y}} ^ {0} (x)} \right]} _ {\underline {{f}} ^ {0} (w), \underline {{x}} ^ {0} (w)}$$
