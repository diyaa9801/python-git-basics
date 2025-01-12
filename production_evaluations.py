import production_functions

# Adding formatted variables for better visual representation
gamma1_f = ('\u03B3' + '\u2081')  
gamma2_f = ('\u03B3' + '\u2082')
a_f = ('\u03B1')
x1_f= ("x" + "\u2081")
x2_f=("x"+"\u2082")
rho_f = ('\u2212' + '\u03C1')
gammas_f =('\u03B3\u2C7C')
factors_f = ('x\u2C7C')

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
cob = production_functions.cobb_douglas(x1, x2, gamma1, gamma2, a)
leo = production_functions.leontief(x1, x2, a)
ces1 = production_functions.ces(x1, x2, gamma1, gamma2, a, rho)

# Print statements with detailed inputs and results, matching to two decimal places
print(f"The production according to the Cobb-Douglas production function is {cob}, "
      f"when the inputs are {x1_f}={x1}, {x2_f}={x2}, {gamma1_f}={gamma1}, {gamma2_f}={gamma2}, and {a_f}={a}. "
      f"Expected output: {expected_cob}. Match: {'Yes' if round(cob, 2) == round(expected_cob, 2) else 'No'}.\n")

print(f"The production according to the Leontief production function is {leo}, "
      f"when the inputs are {x1_f}={x1}, {x2_f}={x2}, and {a_f}={a}. "
      f"Expected output: {expected_leo}. Match: {'Yes' if round(leo, 2) == round(expected_leo, 2) else 'No'}.\n")

print(f"The production according to the CES production function is {ces1:.2f}, "
      f"when the inputs are {x1_f}={x1}, {x2_f}={x2}, {gamma1_f}={gamma1}, {gamma2_f}={gamma2}, {a_f}={a}, and {rho_f}={rho}. "
      f"Expected output: {expected_ces}. Match: {'Yes' if round(ces1, 2) == round(expected_ces, 2) else 'No'}.\n")

#Testoutput
factors=[1,2,3]
gammas=[3,2,1]
a=1
rho=3
expected_general_ces=0.6682


general_ces= production_functions.general_ces(factors, gammas, rho, a)
print("Generalized CES output:", general_ces)

print(f"The production according to the General CES production function is {general_ces:.2f}, "
      f"when the inputs are {factors_f}={factors}, {gammas_f}={gammas}, {a_f}={a}, and {rho_f}={rho}. "
      f"Expected output: {expected_general_ces}. Match: {'Yes' if round(general_ces, 2) == round(expected_general_ces, 2) else 'No'}.\n")
