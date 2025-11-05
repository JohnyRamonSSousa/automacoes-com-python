import tkinter as tk
from tkinter import ttk

#função para adicionar dados dos alunos
def adiciona_aluno():
    name = entry_name.get()
    email = entry_email.get()

    tree.insert("", tk.END, values=(name, email))
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Cadastro de Alunos")

tree = ttk.Treeview(root, columns=("Name", "Email"))
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.pack()

#configuração do campo nome
label_name = tk.Label(root, text="Name")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

#configuração do campo email
label_email = tk.Label(root, text="Email")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

#configuração do botão
button_add = tk.Button(root, text="Adicionar", command=adiciona_aluno)
button_add.pack()

root.mainloop()