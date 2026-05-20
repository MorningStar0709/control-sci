$$
\begin{array}{l} \alpha a _ {k} a _ {l} + \beta b _ {k} b _ {l} = \bar {\alpha} \tilde {a} _ {k} \tilde {a} _ {l} + \bar {\beta} \tilde {b} _ {k} \tilde {b} _ {!} \\ = \frac {(\alpha a _ {k} + \beta b _ {1} b _ {k}) (\alpha a _ {l} + \beta b _ {1} b _ {l})}{\tilde {\alpha}} + \tilde {\beta} \tilde {b} _ {k} \tilde {b} _ {l} \\ \end{array}
$$

where Eq. (11.37) has been used to eliminate $\tilde{a}_{k}\tilde{a}_{l}$ . Inserting the expression in Eq. (11.36) for $\tilde{\alpha}$ gives, after some calculations,

$$\left(b _ {k} - b _ {1} a _ {k}\right) \left(b _ {l} - b _ {1} a _ {l}\right) = \frac {\tilde {\alpha} \tilde {\beta}}{\alpha \tilde {\beta}} \tilde {b} _ {k} \tilde {b} _ {l}$$

```txt
PROCEDURE
DyadicReduction(VAR a,b:col; VAR alpha,beta:REAL;
    i0,i1,i2 :CARDINAL);
CONST
mzero = 1.0E-10;
VAR
i : CARDINAL;
w1,w2,b1,gam : REAL;
BEGIN
IF beta<mzero THEN beta:=0.0; END;
b1 := b[i0];
w1 := alpha;
w2 := beta*b1;
alpha := alpha + w2*b1;
IF alpha > mzero THEN
beta := w1*beta/alpha;
gam := w2/alpha;
FOR i:=i1 TO i2 DO
    b[i] := b[i] - b1*a[i];
    a[i] := a[i] + gam*b[i];
END;
END;
END DyadicReduction; 
```  
Figure 11.15 Dyadic decomposition.

These equations have several solutions. A simple one is

$$\tilde {b} _ {k} = b _ {k} - b _ {1} a _ {k}\bar {\beta} = \frac {\alpha \beta}{\bar {\alpha}}$$

A solution to the dyadic decomposition problem of Eq. (11.34) is given by the equations

$$
\begin{array}{l} \tilde {\alpha} = \alpha + \beta b _ {1} ^ {2} \\ \tilde {\beta} = \frac {\alpha \beta}{\tilde {\alpha}} \\ \gamma = \frac {\beta b _ {1}}{\bar {\alpha}} \\ \tilde {b} _ {k} = b _ {k} - b _ {1} a _ {k} \quad k = 2, \dots , n \\ \tilde {a} _ {k} = a _ {k} + \gamma \tilde {b} _ {k} \quad k = 2, \dots , n \\ \end{array}
$$

The algorithm in Fig. 11.15 is an implementation of the dyadic decomposition.

```txt
PROCEDURE
LDFilter(VAR theta,d:col; VAR l:matr; phi:col;
    lambda:REAL; n:CARDINAL);
VAR
i,j : CARDINAL;
e,w : REAL;
BEGIN
d[0] := lambda;
e := phi[0];
FOR i:=1 TO n DO
    e:=e-theta[i]*phi[i];
    w:=phi[i];
    FOR j:=i+1 TO n DO w:=w+phi[j]*l[i,j]; END;
    l[0,i]:=0.0;
    l[i,0]:=w;
END;
FOR i:=n TO 1 BY -1 DO (* Notice backward loop *)
    DyadicReduction(l[0],l[i],d[0],d[i],0,i,n);
END;

FOR i:=1 TO n DO
    theta[i]:=theta[i]+l[0,i]*e;
    d[i]:=d[i]/lambda;
END;
END LDFilter; 
```  
Figure 11.16 LD decomposition.

In this code, the type

$$\text { col } = \text { ARRAY } [ 0.. \text { maxindex } ] \text { OF REAL; }$$
