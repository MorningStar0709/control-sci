# 2.11 Notes and References

The early texts on sampled-data systems dealt exclusively with input-output models and transform theory Jury (1958), Ragazzimi and Franklin (1958), and Tsypkin (1958). The state-space approach used in this chapter offers significant simplifications. With a zero-order hold, the control signal is constant over the sampling period and the discrete-time model is obtained simply by integrating the state equations over one sampling period. This problem formulation was introduced in Kalman and Bertram (1958). It took some time before this approach found its way into textbooks. Because of its simplicity it is now the predominant approach.

Transformation of state variables and canonical forms is standard material in state-space theory. These results are very similar to the corresponding results for continuous-time systems. A more detailed treatment is given in Kailath (1980). Historically, the input-output approach preceded the state-space approach. A direct treatment from this point of view is given in the classic texts just mentioned. The multivariable case is discussed in Rosenbrock (1970) and Kučera (1979, 1991).

The z-transform is extensively discussed in Jury (1958, 1982) and Doetsch (1971). These references contain large tables of z-transform pairs. A table of zero-order-hold equivalent transfer functions (compare with Table 2.1) is given in Neuman and Baradello (1979).

The relationship between the zeros of continuous and sampled systems is discussed in Åström, Hagander, and Sternby (1984). The theorems for the limiting zeros for large and small sampling periods are given in this paper.

Theorem 2.1 is proved in Wittenmark (1985b). A generalization to the sampling of a system with several time delays is found in Bernhardsson (1993).

Programs for computer algebra such as Maple $^{®}$ and Mathematica $^{®}$ are discussed, for instance, in Char (1992) and Wolfram (1988). For MATLAB $^{®}$ and MATRIX $_{X}^{®}$ we refer to the manuals for the programs.

Properties of matrices and transformations are found, for instance, in Gantmacher (1960), Bellman (1970), and Golub and Van Loan (1989).
