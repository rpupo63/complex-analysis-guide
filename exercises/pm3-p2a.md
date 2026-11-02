---
label: ex:a-bound-on-the-derivative
source: Practice midterm 3, Problem 2(a)
title: a bound on the derivative
placement: f6
order: 1
---
Let $f$ be entire with $|f'(z)|\le1+|z|$ for all $z$. Show that $f$ is a polynomial of degree at most $2$.
<details class="sol"><summary>Hint</summary>
$f'$ is entire (@cor:holomorphic-functions-are-smooth). Apply Cauchy's estimate to $f'$.
</details>
<details class="sol"><summary>Solution</summary>
$f'$ is entire (@cor:holomorphic-functions-are-smooth), and Cauchy's estimate (@cor:cauchys-estimate) on $|z|=R$ gives its Taylor coefficients $|c_n|\le(1+R)R^{-n}\to0$ for $n\ge2$. So $f'(z)=\alpha+\beta z$. The coefficients of $f$ are $a_{n+1}=\frac{c_n}{n+1}$ (@thm:cauchys-formula-for-derivatives: $a_n=f^{(n)}(0)/n!$), so $f(z)=a_0+\alpha z+\frac\beta2z^2$.
</details>
