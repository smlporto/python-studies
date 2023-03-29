import tkinter

window = tkinter.Tk()

window.title("Miles to Km Converter")
window.config(padx=60, pady=20)


def button_clicked():
    new_text = float(input.get())
    km_value["text"] = round(new_text * 1.609344, 2)


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_value = tkinter.Label(text="0", width=10)
km_value.grid(column=1, row=1)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()