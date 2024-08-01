import tkinter as tk
from tkinter import messagebox

# Görevleri yükleme fonksiyonu
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                tasks_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        open("tasks.txt", "w").close()

"""
Uygulama başlatıldığında daha önce kaydedilmiş görevleri "tasks.txt" dosyasından okur ve liste kutusuna ekler.
Dosya bulunmazsa yeni bir "tasks.txt" dosyası oluşturur.
"""

# Görevleri kaydetme fonksiyonu
def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

"""
Bu fonksiyon mevcut görevleri "tasks.txt" dosyasına kaydeder.
Liste kutusundaki tüm görevleri alır ve her birini dosyaya yazar.
"""

# Görev ekleme fonksiyonu
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")

"""
Bu fonksiyon kullanıcıdan alınan yeni görevi liste kutusuna ekler.
Görev kutusuna girilen metni alır ve liste kutusunun sonuna ekler.
Görev eklendikten sonra giriş kutusunu temizler.
Görev eklenmezse uyarı mesajı gösterir.
"""

# Görev silme fonksiyonu
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen silmek için bir görev seçin")

"""
Bu fonksiyon seçilen görevi liste kutusundan siler.
Kullanıcının seçtiği görevin indeksini alır ve bu görevi listeden siler.
Hiçbir görev seçilmezse uyarı mesajı gösterir.
"""

# Ana pencereyi oluşturma
root = tk.Tk()
root.title("To-Do List Uygulaması")

# Görev giriş alanı
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Görev ekleme butonu
add_button = tk.Button(root, text="Görev Ekle", command=add_task)
add_button.pack(pady=5)

"""
Kullanıcı görev eklemek için butona tıklaması "add_task" fonksiyonunu çağırır.
"""

# Görevleri listeleme alanı
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

"""
Kullanıcının eklediği görevlerin listeleneceği liste kutusunu oluşturur.
"""

# Görev silme butonu
delete_button = tk.Button(root, text="Görev Sil", command=delete_task)
delete_button.pack(pady=5)

"""
Kullanıcı bir görevi silmek için butona tıkladığında "delete_task" fonksiyonunu çağırır.
"""

# Uygulama başlatıldığında görevleri yükleme
load_tasks()

"""
Uygulama başlatıldığında "load_tasks" fonksiyonu çağrılarak daha önce kaydedilmiş görevler yüklenir.
"""

# Ana döngüyü çalıştırma
root.mainloop()
