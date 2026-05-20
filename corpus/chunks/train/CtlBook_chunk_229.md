# 1.) Polynomial Vectors

Here, python.control requires multiplying out zeros and poles and encoding the resuling polynomials as vectors such as

$$s ^ {3} + 3 7 s ^ {2} + 1 2 3. 4 s + 2 5 9. 5 \quad \rightarrow \quad [ 1, 3 7, 1 2 3. 4, 2 5 9. 5 ]$$

Not too hard. Once this is done we give them to python directly e.g.

```txt
num = [1 5]
den = [1,37,123.4,259.5]
syst = ctl.TransferFunction(num,den) # note two separate parameters 
```
