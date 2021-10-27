#
# Syntax: x = lsngd(A, b; mu, x0, nIters)
#
# Inputs: A is a m x n matrix
#
# b is a vector of length m
#
# mu is the step size to use, and must satisfy
# 0 < mu <= 1 / sigma_1(A)^2 to guarantee convergence
# where sigma_1(A) is the first (largest) singular value.
# A default value for mu will be explained in Ch.5.
#
# x0 is the initial starting vector (of length n) to use.
# Its default value is all zeros for simplicity.
#
# nIters is the number of iterations to perform (default 200)
#
# Outputs: x is a vector of length n containing the approximate solution
#
# Description: Performs Nesterov-accelerated gradient descent
# to solve the least squares problem
# \argmin_x \| b - A x \|_2
#
function lsngd(A, b; x0 = zeros(size(A,2)), nIters = 200, mu = 0)
    
    t_next = 0
    x_current = x0
    x_next = x0
    for i in 1:nIters

        t_current = t_next
        t_next = 0.5 * (1 + sqrt(1 + 4 * t_current^2))
         
        z = x_next + ( ((t_current - 1) / t_next) * (x_next - x_current) )

        x_current = x_next
        x_next = z - mu * (A' * (A * z - b))
    end
    return x_next
end