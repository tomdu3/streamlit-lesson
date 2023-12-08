import streamlit as st

def calculator_body():
	st.write('---')
	col1, col2, col3 = st.beta_columns(3)
	with col1:
		num1 = st.number_input(label = 'Enter first integer', step = 1)
	with col2:
		num2 = st.number_input(label = 'Enter second integer', step = 2)
	with col3:
		operator = st.selectbox(label = 'Select an operator',
								 options = ['Add', 'Subtract', 'Multiply', 'Divide'])
	if st.button('Click to calculate!'):
		if num2 == 0 and operator == 'Divide':
			st.error('Division by zero error. Enter a non-zero integer.')
		else:
			calculator_function(num1, num2, operator)

def calculator_function(num1, num2, operator):
	if operator == 'Add': result = num1 + num2
	elif operator == 'Subtract': result = num - num2
	elif operator == 'Multiply': result = num1 * num2
	elif operator == 'Divide': result = num1 / num2

	st.success(f'The result is: **{result}**')


    
