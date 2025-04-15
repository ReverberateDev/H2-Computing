import jupytext

# Load the .py file as a notebook
nb = jupytext.read("temp.py")

# Save it as .ipynb
jupytext.write(nb, "temp.ipynb")