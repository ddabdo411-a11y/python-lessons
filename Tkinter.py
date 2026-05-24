import tkinter as tk

# دالة لتحديث النص في شاشة العرض عند الضغط على الأزرار
def press_button(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# دالة لحساب النتيجة النهائية عند الضغط على "="
def equal_press():
    global expression
    try:
        # حساب المعادلة النصية بأمان
        total = str(eval(expression))
        equation.set(total)
        expression = total # لحفظ النتيجة لإجراء عمليات أخرى عليها
    except:
        equation.set(" خطأ ")
        expression = ""

# دالة لمسح الشاشة "C"
def clear_screen():
    global expression
    expression = ""
    equation.set("")

# إعداد النافذة الرئيسية
root = tk.Tk()
root.title("حاسبة بايثون الذكية")
root.geometry("350x450")
root.configure(bg="#2c3e50")

expression = ""
equation = tk.StringVar()

# شاشة العرض العلوي
display = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=0, justify="right")
display.grid(columnspan=4, ipady=15, padx=10, pady=10, sticky="nsew")

# تصميم الأزرار وتوزيعها (النص، السطر، العمود)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# تخصيص أوزان الصفوف والأعمدة لتبدو متناسقة عند تكبير النافذة
for i in range(5):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

# إنشاء الأزرار برمجياً وإضافتها للواجهة
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, fg='white', bg='#27ae60', font=("Arial", 14, "bold"), command=equal_press, borderwidth=0)
    elif text == 'C':
        btn = tk.Button(root, text=text, fg='white', bg='#c0392b', font=("Arial", 14, "bold"), command=clear_screen, borderwidth=0)
    elif text in ['+', '-', '*', '/']:
        btn = tk.Button(root, text=text, fg='white', bg='#d35400', font=("Arial", 14, "bold"), command=lambda t=text: press_button(t), borderwidth=0)
    else:
        btn = tk.Button(root, text=text, fg='#2c3e50', bg='#ecf0f1', font=("Arial", 14), command=lambda t=text: press_button(t), borderwidth=0)
        
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# تشغيل التطبيق
root.mainloop()
