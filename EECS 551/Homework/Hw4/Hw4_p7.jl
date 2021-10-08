using LinearAlgebra
using Plots
using Random: seed!
seed!(3); e = randn(length(T))
T = LinRange(0, 2, 16)
t = LinRange(0, 2, 501)
f = 0.5 * exp.(0.8 * T) 
y = 0.5 * exp.(0.8 * t)

A15 = [TT'j for TT in T, j = 0:length(T) -1]
A2 = A15[:, 1:3]
x15 = pinv(A15)*f 
x2 = pinv(A2)*f

plot(t, y; lable="y(t)", ylim = (-1, 4))
scatter!(T, f, label = "T")

a15 = [tt^j for tt in t, j =0:length(T)-1]
a2 = a15[:,1:3]
plot!(t, (a15*x15), label = "a polynomial of degree 15")
plot!(t, (a2*x2), label = "a polynomial of degree 2",xaxis= "t", yaxis = "f(t)")
