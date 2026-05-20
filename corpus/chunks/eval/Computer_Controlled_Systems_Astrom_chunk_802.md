Listing 13.1 (Continued)   
```txt
{Calculate gain and covariance using the U-D method}
fj:=fi[1];
vj:=diag[1]*fj;
k[1]:=vj;
alphaj:=1.0+vj*fj;
diag[1]:=diag[1]/alphaj/lambda;
if n>1 then
begin
    kf:=0;
    ku:=0;
    for j:=2 to n do
    begin
    fj:fi[j];
    for i:=1 to j-1 do
    begin {f=fi*U}
    kf:=kf+1;
    fj:=fj+fi[i]*offdiag[kf]
    end; {i}
    vj:=fj*diag[j]; {v=D*f}
    k[j]:=vj;
    ajlast:=alphaj;
    alphaj:=ajlast+vj*fj;
    diag[j]:=diag[j]*ajlast/alphaj/lambda;
    pj:=-fj/ajlast;
    for i:=1 to j-1 do
    begin
    {kj+1:=kj+vj*uj}
    {uj:=uj+pj*kj}
    ku:=ku+1;
    w:=offdiag[ku]+k[i]*pj;
    k[i]:=k[i]+offdiag[ku]*vj;
    offdiag[ku]:=w
    end; {i}
    end; {j}
end; {if n>1 then}
{Update parameter estimates}
for i:=1 to n do theta[i]:=theta[i]+perr*k[i]/alphaj;
{Updatiag of fi}
for i:=1 to n-1 do fi[n+1-i]:=fi[n-i];
fi[1]:=-y;
fi[na+1]:=u
end {with eststate do}
end; {LS} 
```

![](image/f69c678167fd2b16ff439db4b8f02d7831b2247743c5ba4ffe6c72864f2945f3.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 1 |
| 500 | 10 | -1 |
| 500 | -10 | 1 |
| 500 | 10 | -1 |
| 500 | -10 | 1 |
| 500 | 10 | -1 |
| 500 | -10 | 1 |
| 500 | 10 | -1 |
| 500 | -10 | 18 |
</details>

Figure 13.2 Input and output when the system of (13.17) is simulated. The input is a PRBS sequence.
