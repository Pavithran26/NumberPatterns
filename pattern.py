import streamlit as st

def generate_pyramid(rows):
    pyramid = ""
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        pyramid += spaces + numbers + "\n"
    return pyramid

def generate_triangle(rows):
    triangle = ""
    for i in range(1, rows + 1):
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        triangle += numbers + "\n"
    return triangle

def generate_square(rows):
    square = ""
    for i in range(1, rows + 1):
        numbers = ' '.join(str(j) for j in range(1, rows + 1))
        square += numbers + "\n"
    return square

# Streamlit application
st.title("Number Pattern Generator")

# Input: Number of rows for the patterns
rows = st.number_input("Enter the number of rows:", min_value=1, value=5)

# Buttons for different patterns
if st.button("Generate Pyramid"):
    pattern = generate_pyramid(rows)
    st.text_area("Generated Pyramid Pattern:", value=pattern, height=300)

if st.button("Generate Triangle"):
    pattern = generate_triangle(rows)
    st.text_area("Generated Triangle Pattern:", value=pattern, height=300)

if st.button("Generate Square"):
    pattern = generate_square(rows)
    st.text_area("Generated Square Pattern:", value=pattern, height=300)