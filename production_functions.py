# Cobb-Douglas Production Function
def cobb_douglas(x1, x2, gamma1, gamma2, a):
    """Calculate the output of a Cobb-Douglas production function.

    The Cobb-Douglas production function models output as a product of input factors, 
    each raised to an exponent that indicates their contribution to the output.

    Args:
        x1 (float): Quantity of the first input factor.
        x2 (float): Quantity of the second input factor.
        gamma1 (float): Output elasticity of the first input factor.
        gamma2 (float): Output elasticity of the second input factor.
        a (float): Total factor productivity (scaling factor).

    Returns:
        float: The calculated output from the Cobb-Douglas production function.
    """
    y = a * (x1 ** gamma1 * x2 ** gamma2)
    return y


# Leontief Production Function
def leontief(x1, x2, a):
    """Calculate the output of a Leontief production function.

    The Leontief production function models output as being limited by the scarcest input, 
    implying a fixed proportion of inputs required to produce output.

    Args:
        x1 (float): Quantity of the first input factor.
        x2 (float): Quantity of the second input factor.
        a (float): Scaling factor for production.

    Returns:
        float: The calculated output from the Leontief production function.
    """
    y = a * min(x1, x2)
    return y


# Constant Elasticity of Substitution (CES) Production Function
def ces(x1, x2, gamma1, gamma2, a, rho):
    """Calculate the output of a Constant Elasticity of Substitution (CES) production function.

    The CES production function models output as a weighted sum of inputs, 
    allowing for varying degrees of substitutability between them, controlled by the elasticity parameter rho.

    Args:
        x1 (float): Quantity of the first input factor.
        x2 (float): Quantity of the second input factor.
        gamma1 (float): Weight for the first input factor.
        gamma2 (float): Weight for the second input factor.
        a (float): Scaling factor for production.
        rho (float): Substitution parameter, where lower values indicate less substitutability between inputs.

    Returns:
        float: The calculated output from the CES production function.
    """
    y = a * (gamma1 * x1 ** (-rho) + gamma2 * x2 ** (-rho)) ** -(1 / rho)
    return y


# General Constant Elasticity of Substitution (CES) Production Function
def general_ces(factors, gammas, rho, a):
    """Calculate the output of a generalized CES (Constant Elasticity of Substitution) production function.

    This generalized CES production function allows for an arbitrary number of input factors,
    each with a corresponding weight, controlled by the elasticity parameter `rho`.

    Args:
        factors (list of float): Quantities of input factors.
        gammas (list of float): Weights for each input factor.
        rho (float): Substitution parameter; higher values indicate greater substitutability.
        a (float): Scaling factor for production.

    Returns:
        float: The calculated output from the generalized CES production function.
    """
    ces_sum = sum(gamma * (factor ** -rho) for gamma, factor in zip(gammas, factors))
    y = a * (ces_sum ** (-1 / rho))
    return y

 