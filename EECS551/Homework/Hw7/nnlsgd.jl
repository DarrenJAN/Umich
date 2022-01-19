"""
`x = nnlsgd(A, b ; mu=0, x0=zeros(size(A,2)), nIters::Int=200)`
Performs projected gradient descent to solve the least squares problem:
``\\argmin_{x \\geq 0} 0.5 \\| b 鈭� A x \\|_2`` with nonnegativity constraint.
In:
鈭� `A` `m x n` matrix
鈭� `b` vector of length `m`
Option:
鈭� `mu` step size to use, and must satisfy ``0 < mu < 2 / \\sigma_1(A)^2``
to guarantee convergence,
where ``\\sigma_1(A)`` is the first (largest) singular value.
Ch.5 will explain a default value for `mu`
鈭� `x0` is the initial starting vector (of length `n`) to use.
Its default value is all zeros for simplicity.
鈭� `nIters` is the number of iterations to perform (default 200)
Out:
`x` vector of length `n` containing the approximate LS solution
"""
function nnlsgd(A, b ; mu::Real=0, x0=zeros(size(A,2)), nIters::Int=200)
    
    if (mu == 0) # use the following default value:
        mu = 1. / (maximum(sum(abs.(A),dims=1)) * maximum(sum(abs.(A),dims=2)))
    end

    x = vec(x0)
    b = vec(b)
    
    for _ in 1:nIters
        z = x - mu * (A' * (A * x - b))
        x = max.(0,z)
    end
    
    return x
end