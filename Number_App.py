import streamlit as st

def main():
    st.title("Find the Largest Number")

    # Input from the user for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Find the largest number among the three
    largest_number = max(num1, num2, num3)

    # Display the result
    st.write("The largest number is:", largest_number)

if __name__ == "__main__":
    main()
