"""
Numerical verification script for generalized Collatz cycles
Validates modular congruence: x0 = c_{q-1} * m^{-(p - P_{q-1})} (mod A)
"""

def mod_inverse(a, m):
    # Extended Euclidean algorithm for modular inverse
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def verify_cycle(m, A, cycle_elements, v_list, c_list):
    x0 = cycle_elements[0]
    q = len(c_list)
    p = sum(v_list)
    
    # Cumulative division counts P_j
    P = [0]
    for v in v_list[:-1]:
        P.append(P[-1] + v)
        
    c_last = c_list[-1]
    P_last = P[-1]
    v_last = p - P_last
    
    # Theoretical remainder mod A
    m_pow_v_inv = mod_inverse(pow(m, v_last, A), A)
    theoretical_mod = (c_last * m_pow_v_inv) % A
    actual_mod = x0 % A
    
    print(f"--- Verification for Cycle starting at x0 = {x0} ---")
    print(f"Base m = {m}, Multiplier A = {A}, (p={p}, q={q})")
    print(f"Actual x0 mod A:       {actual_mod}")
    print(f"Theoretical Formula:   {theoretical_mod}")
    print(f"Match: {actual_mod == theoretical_mod}\n")

if __name__ == "__main__":
    # Test Base-3 System (m=3, A=5)
    # Cycle 1: {4, 7, 12} -> q=2, v=[1, 2], c=[2, 1]
    verify_cycle(m=3, A=5, cycle_elements=[4, 7, 12], v_list=[1, 2], c_list=[2, 1])
    
    # Cycle 2: {8, 14, 24} -> q=2, v=[1, 2], c=[1, 2]
    verify_cycle(m=3, A=5, cycle_elements=[8, 14, 24], v_list=[1, 2], c_list=[1, 2])
