import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    st.title("Plot your graph with Graphify")
    st.subheader('Solve your graph-based assignments with ease')

    # Input fields for x and y values
    x_values = st.text_input("Enter x values (separated by comma):")
    y_values = st.text_input("Enter y values (separated by comma):")

    # Convert input strings to lists of floats
    x_values_list = [float(x.strip()) for x in x_values.split(',')] if x_values else []
    y_values_list = [float(y.strip()) for y in y_values.split(',')] if y_values else []

    if x_values_list and y_values_list:
        data = {'X axis': x_values_list, 'Y axis': y_values_list}
        df = pd.DataFrame(data) #dataframe is a streamlit component
        st.write(df)

    if st.button("Plot Graph"):
        try:
            # Plot the graph
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.plot(x_values_list, y_values_list, 'o-', color='#2563eb', label="Data Points")
            ax.set_xlabel("$x$ $axis$", fontsize=14)
            ax.set_ylabel("$y$ $axis$", fontsize=14)
            ax.set_title("Your Graph")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

        except ValueError:
            st.error("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
