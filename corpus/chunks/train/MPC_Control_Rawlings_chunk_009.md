# Chapter 6. Distributed Model Predictive Control

The recent paper (Stewart, Venkat, Rawlings, Wright, and Pannocchia, 2010) provides a compact treatment of many of the issues and results discussed in Chapter 6. Also, for plants with sparsely coupled input constraints, it provides an extension that achieves centralized optimality on convergence of the controllers’ iterations.

Suboptimal MPC and inherent robustness. The recent paper (Pannocchia, Rawlings, and Wright, 2011) takes the suboptimal MPC formulation in Section 6.1.2, also discussed in Section 2.8, and establishes its inherent robustness to bounded process and measurement disturbances. See also the paper by Lazar and Heemels (2009), which first addressed inherent robustness of suboptimal MPC to process disturbances by (i) specifying a degree of suboptimality and (ii) using the timevarying state constraint tightening approach of Lim´on Marruedo, Alamo, and Ca- ´ macho (2002) to achieve recursive feasibility under disturbances.

The key assumption in (Pannocchia et al., 2011) is the following.

Assumption 8. For any $x , x ^ { \prime } \in \mathcal { X } _ { N }$ and $\mathbf { u } \in \mathcal { U } _ { N } ( x )$ , there exists ${ \bf u } ^ { \prime } \in { \mathcal { U } } _ { N } ( x ^ { \prime } )$ such that $\vert \mathbf { u } - \mathbf { u } ^ { \prime } \vert \leq \sigma ( \vert x - x ^ { \prime } \vert )$ for some K-function $\sigma ( \cdot )$ .

This assumption also implies that $V _ { N } ^ { 0 } ( \cdot )$ is continuous by applying Theorem C.28 in Rawlings and Mayne (2009). If state constraints are softened and the terminal stability constrained is removed by choosing a suitably increased terminal penalty, then this assumption is automatically satisfied. The conclusion of (Pannocchia et al., 2011) is that suboptimal MPC has the same inherent robustness properties as optimal MPC.

Nonlinear distributed MPC. A recent paper (Stewart, Wright, and Rawlings, 2011) proposes a method for handling the nonconvex optimization resulting from nonlinear plant models. The basic difficulty is that taking the convex step of the local controllers’ optimizations may not decrease the plantwide cost. To overcome this problem, the following procedure is proposed.

After all suboptimizers finish an iteration, they exchange steps. Each suboptimizer forms a candidate step

$$u _ {i} ^ {p + 1} = u _ {i} ^ {p} + w _ {i} \alpha_ {i} ^ {p} v _ {i} ^ {p} \quad \forall i \in \mathbb {I} _ {1: M} \tag {4}$$
