using LinearAlgebra

"""
lr_schatten(Y, reg::Real)
Compute the regularized low−rank matrix approximation as the minimizer over `X`
of `1/2 \\|Y − X\\|^2 + reg R(x)`
where `R(X)` is the Schatten p−norm of `X` raised to the pth power, for `p=1/2`,
i.e., `R(X) = \\sum_k (\\sigma_k(X))^{1/2}`
In:
− `Y` : `M × N` matrix
− `reg` regularization parameter
Out:
− `Xh` : `M × N` solution to above minimization problem
"""
function lr_schatten(Y, reg::Real)
    U, s, V = svd(Y)
    xhat = shrink_p_1_2(s, reg)
    Xh = U * Diagonal(xhat) * V'
    return Xh
end
    
function shrink_p_1_2(v, reg::Real)
    m  = size(v,1)
    xhat = zeros(m)
    compute_xhat = (v) -> 4 / 3. * v * cos( 1 ./3 * acos(-(3^(3/2)*reg) / (4*v^(3/2))))^2
    compare_result = v .> 3/2. * reg^(2/3.)
    xhat[compare_result] = compute_xhat.(v[compare_result])
    return xhat
end 