# PD / ED Mathematics

## Extension Determinacy

For
F=<K,S,Phi>
with Phi_b subseteq P(S_b):

LD_F(b) iff |Phi_b|=1

ED(F) iff for all b in K, |Phi_b|=1.

Define:
EX(F) iff for all b in K, Phi_b != emptyset
UN(F) iff for all b in K, |Phi_b| <= 1

Therefore:
ED(F) iff EX(F) and UN(F).

The same formal target admits typed instantiations only when the bridge is licensed.

## Characterization regime

t=<X_t,sigma_t,approx_t,C_t>

sigma_t:X_t -> F_ED

Sufficiency:
for all x in X_t,
[[c]]_t(x) -> ED(sigma_t(x))

Necessity:
for all x in X_t,
ED(sigma_t(x)) -> [[c]]_t(x)

These are regime-relative.

## PDAudit 1.1

Frozen frame:
F=<C,T,B,Gamma_0,A,rho,approx_T,Pi,gamma,Lambda>

rho:A -> Y

Result quotient:
R_T=rho[A]/approx_T

Fiber:
Fib_rho(r)={a in A : [rho(a)]_approx_T=r}

Coordinate sensitivity:
Sens_lambda =
{J subseteq I_lambda :
 exists a,a' with
 lambda(a)_{-J}=lambda(a')_{-J}
 and rho(a) not approx_T rho(a')}

MinSens_lambda=min_subseteq Sens_lambda

Working object:
PDAudit_1.1(F)=
<R_T,Fib_rho,
 {<lambda,MinSens_lambda>:lambda in Lambda},
 kappa_A,kappa_Lambda>

Pair-difference relation:
Delta_rho={(a,a') : rho(a) not approx_T rho(a')}

## Core interpretation

PD identifies result-relevant distinctions inside an admissible frame.
General PD can additionally challenge whether the frame itself is adequate.

This supplies both:
- DIFFERENTIATE as a primitive research job;
- G_PD as a candidate generator for other jobs.
