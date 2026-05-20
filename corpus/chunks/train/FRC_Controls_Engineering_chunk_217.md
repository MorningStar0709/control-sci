$$
\mathbf {k} _ {1} = f (\mathbf {x} _ {k}, \mathbf {u} _ {k})\mathbf {k} _ {2} = f (\mathbf {x} _ {k} + h \frac {1}{2} \mathbf {k} _ {1}, \mathbf {u} _ {k})\mathbf {k} _ {3} = f (\mathbf {x} _ {k} + h \frac {1}{2} \mathbf {k} _ {2}, \mathbf {u} _ {k})\mathbf {k} _ {4} = f (\mathbf {x} _ {k} + h \mathbf {k} _ {3}, \mathbf {u} _ {k})\mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h \frac {1}{6} (\mathbf {k} _ {1} + 2 \mathbf {k} _ {2} + 2 \mathbf {k} _ {3} + \mathbf {k} _ {4})
\begin{array}{c c c c c} 0 & & & \\ \frac {1}{2} & \frac {1}{2} & & \\ \frac {1}{2} & 0 & \frac {1}{2} & & \\ 1 & 0 & 0 & 1 & \\ \hline & \frac {1}{6} & \frac {1}{3} & \frac {1}{3} & \frac {1}{6} \end{array}
$$

Here’s a reference implementation.

#include <Eigen/Core>

/// Performs 4th order Runge-Kutta integration of dx/dt = f(x, u) for dt.   
///   
/// @param f The function to integrate. It must take two arguments x and u.   
/// @param x The initial value of x.   
/// @param u The value u held constant over the integration period.

```cpp
/// @param dt The time over which to integrate.
template <typename F, typename T, typename U>
T rk4(F&& f, T x, U u, double dt) {
    const auto& h = dt;

T k1 = f(x, u);
    T k2 = f(x + h * 0.5 * k1, u);
    T k3 = f(x + h * 0.5 * k2, u);
    T k4 = f(x + h * k3, u);

return x + h / 6.0 * (k1 + 2.0 * k2 + 2.0 * k3 + k4);
} 
```  
Snippet 7.1. RK4 implementation in C++

Other methods of Runge-Kutta integration exist with various properties,[11] but the one presented here is popular for its high accuracy relative to the amount of floating point operations (FLOPs) it requires.
