has been introduced. By using the procedure DyadicReduction it is now straightforward to write a procedure that implements Algorithm 11.1. Such a procedure is given in Fig. 11.16. The algorithm performs one step of a recursive least-squares estimation. Starting from the current estimate $\theta$ , the covariance represented by its LD decomposition, and the regression vector, the procedure generates updated values of the estimate and its covariance. The data type

$$\text { matr } = \text { ARRAY } [ 0.. \text { maxindex } ] \text { OF col; }$$

is used in the program. The starting values can be chosen to be $L = I$ and $d = [\beta_0, \beta_0, \ldots, \beta_0]$ . This gives $LD = \beta_0I$ .
