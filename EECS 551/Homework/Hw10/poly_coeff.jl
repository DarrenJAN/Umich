using Polynomials
using LinearAlgebra
"""
g, h = poly_coeff(a, b, c, d)
Use Kronecker sums/products to construct polynomials with integer coefficients
with the given (algebraic) numbers as zeros.
In:
* `a, b, c, d` are integers
Out:
* `g` and `h` are Int vectors of length 5 with `p[5] = 1` and `q[5] = 1`
such that, in the notation defined below, `p3(x3) = 0` and `p4(x4) = 0`
Notation:
* `x1 = a + sqrt(b)`
* `x2 = c − sqrt(d)`
* `x3 = x1 + x2`
* `x4 = x1 * x2`
* `p1(x)` quadratic monic polynomial with integer−valued coefficients with a zero at `x1`
* `p2(x)` quadratic monic polynomial with integer−valued coefficients with a zero at `x2`
* `p3(x) = g[5] x^4 + g[4] x^3 + g[3] x^2 + g[2] x + g[1]` where `g[5] = 1`
* `p4(x) = h[5] x^4 + h[4] x^3 + h[3] x^2 + h[2] x + h[1]` where `h[5] = 1`
"""
function poly_coeff(a::Int, b::Int, c::Int, d::Int)
    g  = Vector{Int64}(zeros(5)) 
    h  = Vector{Int64}(zeros(5)) 
    g[5] = 1
    h[5] = 1
    
    #construct compan matrix of p1 and p2
    compan = e -> [-transpose(reverse(e)); [I zeros(length(e)-1)]]
    
    c1 = [a^2 - b ; -2 * a]
    c2 = [c^2 - d ; -2 * c]
    
    compan_p1 = compan(c1)
    compan_p2 = compan(c2)
    
    kron_sum = kron(compan_p1, I(2)) + kron(I(2), compan_p2)
    kron_product = kron(compan_p1, compan_p2)
    
    eigvals3 = eigvals(kron_sum)
    eigvals4 = eigvals(kron_product)

    p3 = fromroots(eigvals3)
    p4 = fromroots(eigvals4)
    
    g = convert.(Int64, round.(p3.coeffs, digits =0))
    h = convert.(Int64, round.(p4.coeffs, digits =0))
#     g[1] = convert(Int64, round(p3[0], digits = 0))
#     g[2] = convert(Int64, round(p3[1], digits = 0))
#     g[3] = convert(Int64, round(p3[2], digits = 0))
#     g[4] = convert(Int64, round(p3[3], digits = 0))
    
#     h[1] = convert(Int64, round(p4[0], digits = 0))
#     h[2] = convert(Int64, round(p4[1], digits = 0))
#     h[3] = convert(Int64, round(p4[2], digits = 0))
#     h[4] = convert(Int64, round(p4[3], digits = 0))
    
    
    return g, h
    
end
