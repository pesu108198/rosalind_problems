def mendels_first_law(k, m, n):
    """
    Calculates the probability of a dominant phenotype offspring.
    k: number of homozygous dominant (AA)
    m: number of heterozygous (Aa)
    n: number of homozygous recessive (aa)
    """
    # Total population
    total = k + m + n
    
    # If population is less than 2, we can't select two parents
    if total < 2:
        return 0.0

    # Calculate the probability of selecting two parents that produce a RECESSIVE (aa) offspring.
    # We use the formula: (Count1 * Count2) / (Total * (Total - 1)) * P(aa | mating)
    
    # 1. Recessive x Recessive (aa x aa) -> 100% chance of aa
    # We pick one 'n', then another 'n' from the remaining (n-1)
    prob_recessive_recessive = (n / total) * ((n - 1) / (total - 1)) * 1.0
    print(prob_recessive_recessive)
    # 2. Heterozygous x Heterozygous (Aa x Aa) -> 25% chance of aa
    # We pick one 'm', then another 'm' from the remaining (m-1)
    prob_hetero_hetero = (m / total) * ((m - 1) / (total - 1)) * 0.25
    print(prob_hetero_hetero)
    # 3. Heterozygous x Recessive (Aa x aa) OR (aa x Aa) -> 50% chance of aa
    # Option A: Pick 'm' then 'n'
    # Option B: Pick 'n' then 'm'
    # Combined probability: 2 * (m * n)
    prob_hetero_recessive = 2 * (m / total) * (n / (total - 1)) * 0.5
    print(prob_hetero_recessive)
    # Sum of all probabilities producing 'aa'
    total_prob_recessive = prob_recessive_recessive + prob_hetero_hetero + prob_hetero_recessive
    
    # The result is the complement (1 - prob_recessive)
    return 1 - total_prob_recessive

# --- Sample Execution ---
# Sample Dataset from problem: 2 2 2
k_in, m_in, n_in = 2, 2, 2
result = mendels_first_law(k_in, m_in, n_in)

print(f"Given: k={k_in}, m={m_in}, n={n_in}")
print(f"Return: {result:.5f}")
