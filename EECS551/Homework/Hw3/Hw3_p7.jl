using LinearAlgebra: svdvals
using Plots
using LaTeXStrings
n = 100
x = randn(n); y = randn(n); A = x*y'
s = svdvals(A)
scatter(s, yscale = :log10, label= "", title = "singular values: log scale", xlabel="i", ylabel=L"\sigma_i") # to make ?i