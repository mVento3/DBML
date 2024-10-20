import tkinter as tk
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# password = 'zaq1@WSX'
# encoded_password = urllib.parse.quote(password)

# db_engine = create_engine(f"postgresql+psycopg://postgres:{encoded_password}@localhost")

# with db_engine.connect() as conn, conn.begin():
#     df_data = pd.read_sql_table("data", conn)



# Create the main Tkinter window
root = tk.Tk()
root.title("Matplotlib in Tkinter")

# Create a Matplotlib figure
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

# Embed the figure into the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

button = tk.Button(master=root, text="Update Plot")
button.pack(side=tk.BOTTOM)

root.mainloop()