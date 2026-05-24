import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def convert_to_exe():
    file_path = filedialog.askopenfilename(
        title="اختر ملف بايثون لإخفاء كوده",
        filetypes=[("Python Files", "*.py")]
    )
    
    if not file_path:
        return
        
    status_label.config(text="جاري معالجة الملف وإخفاء الكود... يرجى الانتظار", fg="#d35400")
    root.update()
    
    try:
        # التأكد من تثبيت مكتبة التحويل
        subprocess.check_call(["pip", "install", "pyinstaller"])
        
        # تحويل الملف إلى ملف تنفيذي واحد وإخفاء الكود المصدري
        # خيار --noconsole يخفي شاشة سطر الأوامر السوداء عند تشغيل تطبيقك لاحقاً
        command = f'pyinstaller --onefile --noconsole "{file_path}"'
        subprocess.run(command, shell=True, check=True)
        
        status_label.config(text="تم الحماية والتحويل بنجاح!", fg="#27ae60")
        messagebox.showinfo("نجاح", "تم إخفاء الكود بنجاح. ستجد التطبيق الجديد داخل مجلد اسمه 'dist' في نفس مسار هذا السكريبت.")
    except Exception as e:
        status_label.config(text="فشلت العملية", fg="#c0392b")
        messagebox.showerror("خطأ", f"حدث خطأ أثناء التشفير:\n{str(e)}")

# إعداد واجهة البرنامج
root = tk.Tk()
root.title("أداة إخفاء وحماية كود بايثون")
root.geometry("450x250")
root.configure(bg="#2c3e50")

# نصوص الواجهة
title_label = tk.Label(root, text="محول الملفات إلى تطبيق مخفي المصدر", font=("Arial", 14, "bold"), fg="white", bg="#2c3e50")
title_label.pack(pady=20)

btn_select = tk.Button(root, text="اختر ملف Python (.py)", font=("Arial", 12), bg="#3498db", fg="white", command=convert_to_exe, bd=0, padx=10, pady=5)
btn_select.pack(pady=15)

status_label = tk.Label(root, text="جاهز للاستخدام", font=("Arial", 10), fg="#bdc3c7", bg="#2c3e50")
status_label.pack(pady=20)

root.mainloop()
