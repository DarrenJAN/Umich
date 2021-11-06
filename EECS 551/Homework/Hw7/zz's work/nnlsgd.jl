"""
`x = nnlsgd(A, b ; mu=0, x0=zeros(size(A,2)), nIters::Int=200)`
Performs projected gradient descent to solve the least squares problem:
``\\argmin_{x \\geq 0} 0.5 \\| b − A x \\|_2`` with nonnegativity constraint.
In:
− `A` `m x n` matrix
− `b` vector of length `m`
Option:
− `mu` step size to use, and must satisfy ``0 < mu < 2 / \\sigma_1(A)^2``
to guarantee convergence,
where ``\\sigma_1(A)`` is the first (largest) singular value.
Ch.5 will explain a default value for `mu`
− `x0` is the initial starting vector (of length `n`) to use.
Its default value is all zeros for simplicity.
− `nIters` is the number of iterations to perform (default 200)
Out:
`x` vector of length `n` containing the approximate LS solution
"""
function nnlsgd(A, b ; mu::Real=0, x0=zeros(size(A,2)), nIters::Int=200)
    
    if (mu == 0) 
        mu = 1. / (maximum(sum(abs.(A),dims=1)) * maximum(sum(abs.(A),dims=2)))
    end
    
    x_next = x0
    
    for i in 1:nIters
        z = x_next - mu * (A' * (A * x_next - b ))
        x_next = max.(0, z)
    end 
    
    return x_next
end 