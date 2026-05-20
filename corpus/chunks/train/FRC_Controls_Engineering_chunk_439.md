# 17.1 Solving optimization problems with Sleipnir

Sleipnir is a C++ library that facilitates the specification of constrained nonlinear optimization problems with natural mathematical notation, then efficiently solves them.

Sleipnir supports problems of the form:

$$\min _ {x} f (x)$$

$\mathrm { s u b j e c t } \mathrm { t o } c _ { e } ( x ) = 0$

$$c _ {i} (x) \geq 0$$

where $f ( x )$ is the scalar cost function, x is the vector of decision variables (variables the solver can tweak to minimize the cost function), $c _ { e } ( x )$ is the vector-valued function whose rows are equality constraints, and $c _ { i } ( x )$ is the vector-valued function whose rows are inequality constraints. Constraints are equations or inequalities of the decision variables that constrain what values the solver is allowed to use when searching for an optimal solution.

The nice thing about Sleipnir is users don’t have to put their system in the form shown above manually; they can write it in natural mathematical form and it’ll be converted for them. We’ll cover some examples next.
