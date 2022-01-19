"""
out = shrink_p_1_2(v, reg::Real)
Compute minimizer of ``1/2 |v 鈭� x|^2 + reg |x|^p``
for `p=1/2` when `v` is real and nonnegative.
In:
* `v` scalar, vector, or array of (real, nonnegative) input values
* `reg` regularization parameter
Out:
* `xh` solution to minimization problem for each element of `v`
(same size as `v`)
"""
function shrink_p_1_2(v, reg::Real)
    (m,n)  = size(v)
    xhat = zeros(m,n)
    compute_xhat = (v) -> 4 / 3. * v * cos( 1 ./3 * acos(-(3^(3/2)*reg) / (4*v^(3/2))))^2
    compare_result = v .> 3/2. * reg^(2/3.)
    xhat[compare_result] = compute_xhat.(v[compare_result])
    return xhat
end 