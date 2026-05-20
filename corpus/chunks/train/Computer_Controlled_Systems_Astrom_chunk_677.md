# Prediction, Filtering, and Smoothing

Different estimators for the states in (11.3) can be derived depending on the available measurements. Assume that the data

$$Y _ {k} = \{y (i), u (i) \mid i \leq k \}$$

is known. Using $Y_{k}$ we want to estimate $x(k + m)$ . We have three cases:

- Smoothing $(m < 0)$   
• Filtering (m = 0)   
- Prediction $(m > 0)$

Figure 11.6 illustrates the different cases. In this section the prediction and filtering problems are discussed. The resulting dynamic system is called a filter regardless of which of the problems is solved.
