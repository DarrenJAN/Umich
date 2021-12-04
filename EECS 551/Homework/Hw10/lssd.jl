using LinearAlgebra

"""
x = lssd(A, b ; x0=zeros(size(A,2)), nIters::Int=10)
Perform steepest descent to solve the least squares problem
`\\hat{x} = \\arg\\min_x f(x), f(x) = 1/2 \\| b − A x \\|_2`
In:
* `A` : `m × n` matrix
* `b` : vector of length `m`
Option:
* `x0` : initial vector (of length `n`); default `zeros`
* `nIters` : number of iterations to perform; default `10`
Out:
* `x` a vector of length `n` containing the approximate solution
Notes:
Because this is a quadratic cost function, there is a closed−form solution
for the step size each iteration, so no "line search" procedure is needed.
A full−credit solution uses only *one* multiply by `A` and one by `A'` per iteration.
"""
function lssd(A, b ; x0=zeros(size(A,2)), nIters::Int=10)
    
    x_current = x0
    Ax = A * x_current
    for _ in 1:nIters
        gradient = A' * (Ax - b)
        direction = - gradient
        Ad = A * direction
        Ad_norm = norm(Ad)
        
        if(Ad_norm == 0)
            return x_crrent
        else 
            step = - direction' * gradient / (Ad_norm.^2)
        end
        
        x_current = x_current + step * direction 
        Ax = Ax + step * Ad 
    end
    
    return x_current
        
end