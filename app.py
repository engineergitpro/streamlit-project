import streamlit as st

# Set the title of the app
st.title("Simple Data Filtering")

# Display a header
st.header("Filter Items by Keyword")

# Create a list of items
items = ["apple", "banana", "grape", "orange", "kiwi", "strawberry", "blueberry", "mango"]

# Text input for the keyword
keyword = st.text_input("Enter a keyword to filter items:")

# Filter the items based on the keyword (case-insensitive)
filtered_items = [item for item in items if keyword.lower() in item.lower()]

# Display the filtered list
if filtered_items:
    st.subheader("Filtered Items:")
    st.write(filtered_items)
else:
    st.write("No items found with that keyword.")
