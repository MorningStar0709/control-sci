# 5.1.1 Extremization of a Functional

In this section, we obtain the necessary conditions for optimization of cost functionals which are summations such as

$$J (x (k _ {0}), k _ {0}) = J = \sum_ {k = k _ {0}} ^ {k _ {f} - 1} V (x (k), x (k + 1), k) \tag {5.1.1}$$

where, the discrete instant $k = k_{0}, k_{1}, \cdots, k_{f} - 1$ . Note the following points.

1. For a given interval $k \in [k_0, k_f]$ and a given function $V(x(k), x(k + 1), k)$ , the summation interval in (5.1.1) needs to be $[k_0, k_f - 1]$ .

2. We consider first a scalar case for simplicity and then we generalize for the vector case.

3. We are also given the initial condition $x(k = k_0) = x(k_0)$ .

4. Consider the case of a free-final point system, such that $k$ is fixed or specified and $x(k_{f})$ is free or unspecified.

5. Also, if $T$ is the sampling period, then $x(k) = x(kT)$ .

6. Let us note that if we are directly considering the discrete-time version of the continuous-time cost functionals (such as (2.3.1) addressed in Chapter 2), we have the sampling period $T$ multiplying the cost functional (5.1.1).

For extremization (maximization or minimization) of functionals, analogous to the case of continuous-time systems addressed in Chapter 2, we use the fundamental theorem of the calculus of variations (CoV) which states that the first variation must be equal to zero. The methodology for this simple case of optimization of a functional is carried out briefly under the following steps.

- Step 1: Variations   
- Step 2: Increment   
- Step 3: First Variation   
- Step 4: Euler-Lagrange Equation
