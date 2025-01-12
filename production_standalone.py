# Adding formatted variables for better visual representation
gamma1_f = ('\u03B3' + '\u2081')  
gamma2_f = ('\u03B3' + '\u2082')
a_f = ('\u03B1')
x1_f= ("x" + "\u2081")
x2_f=("x"+"\u2082")
rho_f = ('\u2212' + '\u03C1')


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


#testoutput
x1=5
x2=3
gamma1=2
gamma2=2
a=1
rho=3

# Expected values for manual verification
expected_cob = 225
expected_leo = 3
expected_ces = 2.23

# Calculate function outputs
cob = cobb_douglas(x1, x2, gamma1, gamma2, a)
leo = leontief(x1, x2, a)
ces1 = ces(x1, x2, gamma1, gamma2, a, rho)

# Print statements with detailed inputs and results, matching to two decimal places
print(f"The production according to the Cobb-Douglas production function is {cob}, "
      f"when the inputs are {x1_f}={x1}, {x2_f}={x2}, {gamma1_f}={gamma1}, {gamma2_f}={gamma2}, and {a_f}={a}. "
      f"Expected output: {expected_cob}. Match: {'Yes' if round(cob, 2) == round(expected_cob, 2) else 'No'}.\n")

print(f"The production according to the Leontief production function is {leo}, "
      f"when the inputs are {x1_f}={x1}, {x2_f}={x2}, and {a_f}={a}. "
      f"Expected output: {expected_leo}. Match: {'Yes' if round(leo, 2) == round(expected_leo, 2) else 'No'}.\n")

print(f"The production according to the CES production function is {ces1:.2f}, "
      f"when the inputs are {x1_f}={x1}, {x2_f}={x2}, {gamma1_f}={gamma1}, {gamma2_f}={gamma2}, {a_f}={a}, and {rho_f}={rho}. "
      f"Expected output: {expected_ces}. Match: {'Yes' if round(ces1, 2) == round(expected_ces, 2) else 'No'}.")


