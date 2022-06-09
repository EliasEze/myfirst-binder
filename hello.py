print("Hello from Binder!")

import tkinter as tk


my_w = tk.Tk()
my_w.geometry("450x100")  # Size of the window
my_w.title("Experiment Selection")  # Adding a title

options = tk.StringVar(my_w)
options.set("")  # default value

l1 = tk.Label(my_w, text='Select An Experiment', width=18)
l1.grid(row=2, column=1)

om1 = tk.OptionMenu(my_w, options, "Exp1: Adjective Expression Sign", "Exp2: Noun Expression Sign",
                    "Exp3: Verb Expression Sign", "Exp4: Sentence Expression Sign")
om1.grid(row=2, column=2)

b1 = tk.Button(my_w, text='Start Experiment', command=lambda: start_experiment())
b1.grid(row=2, column=3)


# str_out=tk.StringVar(my_w)
# str_out.set("Output")

# l2 = tk.Label(my_w,  textvariable=str_out, width=10 )
# l2.grid(row=2,column=4)

def start_experiment():
    sel = str(options.get())
    print(sel)
    if 'Exp1' in sel:
        print("1")
    if 'Exp2' in sel:
        print("2")
    if 'Exp3' in sel:
        print("3")
    if 'Exp4' in sel:
        print("4")
    if 'Exp' not in sel:
        print("Please make a valid selection")


# my_w.mainloop()

if __name__ == '__main__':
    my_w.mainloop()
