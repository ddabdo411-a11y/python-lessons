import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sys
import io
import contextlib

class PythonExplained:
    def __init__(self, root):
        self.root = root
        self.root.title("تعلم بايثون - Python Explained")
        self.root.geometry("1050x650")
        self.root.configure(bg="#1e1e2e")

        self.topics = self.get_topics()
        self.setup_ui()
        self.show_topic(0)

    def get_topics(self):
        return [
            {
                "title": "المتغيرات والبيانات",
                "icon": "\U0001f4e6",
                "content": (
                    "المتغيرات (Variables) هي أماكن في الذاكرة لتخزين البيانات.\n\n"
                    "أنواع البيانات الأساسية:\n"
                    "\u2022 int    : أعداد صحيحة  (1, 100, -5)\n"
                    "\u2022 float  : أعداد عشرية   (3.14, 2.5)\n"
                    "\u2022 str    : نصوص           (\"مرحبا\", \u2018Python\u2019)\n"
                    "\u2022 bool   : قيم منطقية     (True, False)\n"
                    "\u2022 list   : قوائم          ([1, 2, 3])\n"
                    "\u2022 dict   : قواميس         ({\"اسم\": \"أحمد\"})\n\n"
                    "القواعد:\n"
                    "\u2022 الأسماء تبدأ بحرف أو شرطة سفلية\n"
                    "\u2022 حساسة لحالة الأحرف (age \u2260 Age)\n"
                    "\u2022 لا تبدأ برقم"
                ),
                "code": (
                    "# تعريف المتغيرات\n"
                    'name = "أحمد"\n'
                    "age = 25\n"
                    "height = 1.75\n"
                    "is_student = True\n\n"
                    "# طباعة المتغيرات\n"
                    "print(f\"الاسم: {name}\")\n"
                    "print(f\"العمر: {age}\")\n"
                    "print(f\"الطول: {height}\")\n"
                    "print(f\"طالب: {is_student}\")\n\n"
                    "# معرفة نوع البيانات\n"
                    "print(type(name))\n"
                    "print(type(age))"
                ),
            },
            {
                "title": "الجمل الشرطية",
                "icon": "\U0001f504",
                "content": (
                    "الجمل الشرطية تتحكم في مسار تنفيذ البرنامج.\n\n"
                    "الأدوات:\n"
                    "\u2022 if      : شرط أساسي\n"
                    "\u2022 elif    : شرط إضافي\n"
                    "\u2022 else    : الحالة الافتراضية\n"
                    "\u2022 and / or: دمج الشروط\n"
                    "\u2022 not     : عكس الشرط\n\n"
                    "ملاحظة: Python تعتمد على المسافات البادئة (indentation) لتحديد الكتل البرمجية."
                ),
                "code": (
                    "score = 85\n\n"
                    "if score >= 90:\n"
                    '    print("ممتاز")\n'
                    "elif score >= 80:\n"
                    '    print("جيد جداً")\n'
                    "elif score >= 70:\n"
                    '    print("جيد")\n'
                    "else:\n"
                    '    print(" needs تحسين")\n\n'
                    "# شرط مركب\n"
                    "age = 20\n"
                    "has_id = True\n\n"
                    "if age >= 18 and has_id:\n"
                    '    print("يمكنك الدخول")\n'
                    "else:\n"
                    '    print("ممنوع الدخول")'
                ),
            },
            {
                "title": "الحلقات التكرارية",
                "icon": "\U0001f501",
                "content": (
                    "الحلقات تستخدم لتكرار تنفيذ الأوامر.\n\n"
                    "for loop:\n"
                    "\u2022 تستخدم لتكرار عدد محدد من المرات\n"
                    "\u2022 تعمل مع القوائم والنصوص والمدى (range)\n\n"
                    "while loop:\n"
                    "\u2022 تستمر طالما الشرط صحيح\n"
                    "\u2022 انتبه للحلقات اللانهائية!\n\n"
                    "كلمات مساعدة:\n"
                    "\u2022 break    : إيقاف الحلقة\n"
                    "\u2022 continue : تخطي التكرار الحالي"
                ),
                "code": (
                    "# For loop مع range\n"
                    "for i in range(5):\n"
                    '    print(f"التكرار رقم {i}")\n\n'
                    'print("---")\n\n'
                    "# For loop مع قائمة\n"
                    'fruits = ["تفاح", "موز", "برتقال"]\n'
                    "for fruit in fruits:\n"
                    '    print(f"الفاكهة: {fruit}")\n\n'
                    'print("---")\n\n'
                    "# While loop\n"
                    "count = 0\n"
                    "while count < 3:\n"
                    '    print(f"العداد: {count}")\n'
                    "    count += 1\n\n"
                    'print("---")\n\n'
                    "# break و continue\n"
                    "for i in range(10):\n"
                    "    if i == 3:\n"
                    "        continue\n"
                    "    if i == 7:\n"
                    "        break\n"
                    "    print(i)"
                ),
            },
            {
                "title": "القوائم (Lists)",
                "icon": "\U0001f4cb",
                "content": (
                    "القوائم هي مجموعات مرتبة وقابلة للتعديل.\n\n"
                    "العمليات الأساسية:\n"
                    "\u2022 إنشاء قائمة: my_list = [1, 2, 3]\n"
                    "\u2022 الإضافة: append(), insert(), extend()\n"
                    "\u2022 الحذف: remove(), pop(), del\n"
                    "\u2022 الترتيب: sort(), reverse()\n"
                    "\u2022 البحث: index(), count()\n"
                    "\u2022 الطول: len()\n"
                    "\u2022 التقطيع: list[start:end:step]\n\n"
                    "القوائم تقبل أي نوع بيانات ويمكن دمج الأنواع."
                ),
                "code": (
                    "# إنشاء قائمة\n"
                    "numbers = [3, 1, 4, 1, 5]\n"
                    'print(f"الأصلية: {numbers}")\n\n'
                    "# إضافة عناصر\n"
                    "numbers.append(9)\n"
                    'print(f"بعد الإضافة: {numbers}")\n\n'
                    "# ترتيب\n"
                    "numbers.sort()\n"
                    'print(f"بعد الترتيب: {numbers}")\n\n'
                    "# حذف\n"
                    "numbers.pop()\n"
                    'print(f"بعد حذف آخر عنصر: {numbers}")\n\n'
                    "# تقطيع\n"
                    'print(f"أول 3 عناصر: {numbers[:3]}")\n'
                    'print(f"الطول: {len(numbers)}")\n\n'
                    "# قائمة بأسماء\n"
                    'names = ["أحمد", "سارة", "علي"]\n'
                    "for i, name in enumerate(names):\n"
                    '    print(f"{i+1}. {name}")'
                ),
            },
            {
                "title": "القواميس (Dictionaries)",
                "icon": "\U0001f4d6",
                "content": (
                    "القواميس تخزن بيانات على شكل مفتاح:قيمة (key: value).\n\n"
                    "المميزات:\n"
                    "\u2022 وصول سريع للبيانات بواسطة المفتاح\n"
                    "\u2022 المفاتيح فريدة (لا يمكن تكرارها)\n"
                    "\u2022 القيم يمكن أن تكون أي نوع\n\n"
                    "العمليات:\n"
                    "\u2022 الوصول: dict[key] أو dict.get(key)\n"
                    "\u2022 الإضافة: dict[key] = value\n"
                    "\u2022 الحذف: del dict[key] أو pop()\n"
                    "\u2022 المفاتيح: keys()\n"
                    "\u2022 القيم: values()\n"
                    "\u2022 العناصر: items()"
                ),
                "code": (
                    "# إنشاء قاموس\n"
                    "student = {\n"
                    '    "name": "أحمد",\n'
                    "    \"age\": 20,\n"
                    "    \"grade\": 88,\n"
                    '    "subjects": ["رياضيات", "فيزياء"]\n'
                    "}\n\n"
                    "print(student)\n"
                    'print(f\'الاسم: {student["name"]}\')\n\n'
                    "# إضافة مفتاح جديد\n"
                    'student["city"] = "القاهرة"\n'
                    'print(f"بعد الإضافة: {student}")\n\n'
                    "# التكرار على القاموس\n"
                    "for key, value in student.items():\n"
                    '    print(f"{key}: {value}")\n\n'
                    "# استخدام get (آمن)\n"
                    'print(f\'الهاتف: {student.get("phone", "غير موجود")}\')'
                ),
            },
            {
                "title": "الدوال (Functions)",
                "icon": "\u2699\ufe0f",
                "content": (
                    "الدوال هي كتل برمجية قابلة لإعادة الاستخدام.\n\n"
                    "المكونات:\n"
                    "\u2022 التعريف: def\n"
                    "\u2022 المعاملات (parameters)\n"
                    "\u2022 القيمة المُرجعة: return\n"
                    "\u2022 النطاق: local vs global\n\n"
                    "أنواع المعاملات:\n"
                    "\u2022 Positional: العادية\n"
                    "\u2022 Default: لها قيمة افتراضية\n"
                    "\u2022 Keyword: تُسمى عند النداء\n"
                    "\u2022 *args: عدد متغير\n"
                    "\u2022 **kwargs: معاملات مسماة متغيرة"
                ),
                "code": (
                    "# دالة بسيطة\n"
                    "def greet(name):\n"
                    '    return f"مرحبا {name}!"\n\n'
                    'print(greet("سارة"))\n\n'
                    "# دالة بقيمة افتراضية\n"
                    "def power(base, exp=2):\n"
                    "    return base ** exp\n\n"
                    "print(f\"3^2 = {power(3)}\")\n"
                    "print(f\"3^4 = {power(3, 4)}\")\n\n"
                    "# *args\n"
                    "def sum_all(*numbers):\n"
                    "    return sum(numbers)\n\n"
                    'print(f"المجموع: {sum_all(1, 2, 3, 4, 5)}")\n\n'
                    "# دالة داخلية\n"
                    "def outer(x):\n"
                    "    def inner(y):\n"
                    "        return x + y\n"
                    "    return inner(5)\n\n"
                    "print(outer(10))"
                ),
            },
            {
                "title": "البرمجة كائنية التوجه",
                "icon": "\U0001f3db\ufe0f",
                "content": (
                    "OOP: تنظيم الكود باستخدام الكائنات (Objects) والكلاسات (Classes).\n\n"
                    "المفاهيم الأساسية:\n"
                    "\u2022 Class:  القالب أو المخطط\n"
                    "\u2022 Object: نسخة من الكلاس\n"
                    "\u2022 __init__: المُنشئ (constructor)\n"
                    "\u2022 self: مرجع للكائن الحالي\n\n"
                    "مبادئ OOP:\n"
                    "\u2022 Encapsulation: إخفاء البيانات\n"
                    "\u2022 Inheritance: الوراثة\n"
                    "\u2022 Polymorphism: تعدد الأشكال"
                ),
                "code": (
                    "class Student:\n"
                    "    def __init__(self, name, age):\n"
                    "        self.name = name\n"
                    "        self.age = age\n"
                    "        self.grades = []\n\n"
                    "    def add_grade(self, grade):\n"
                    "        self.grades.append(grade)\n\n"
                    "    def average(self):\n"
                    "        if not self.grades:\n"
                    "            return 0\n"
                    "        return sum(self.grades) / len(self.grades)\n\n"
                    "    def info(self):\n"
                    '        return f"{self.name}, {self.age} سنة - المعدل: {self.average():.1f}"\n\n'
                    "# وراثة\n"
                    "class GraduateStudent(Student):\n"
                    "    def __init__(self, name, age, thesis):\n"
                    "        super().__init__(name, age)\n"
                    "        self.thesis = thesis\n\n"
                    "    def info(self):\n"
                    '        return f"{super().info()} | بحث: {self.thesis}"\n\n\n'
                    's1 = Student("أحمد", 20)\n'
                    "s1.add_grade(85)\n"
                    "s1.add_grade(92)\n"
                    "print(s1.info())\n\n"
                    's1 = GraduateStudent("سارة", 24, "الذكاء الاصطناعي")\n'
                    "s1.add_grade(95)\n"
                    "print(s1.info())"
                ),
            },
            {
                "title": "التعامل مع الأخطاء",
                "icon": "\u26a0\ufe0f",
                "content": (
                    "Exceptions: التعامل مع الأخطاء بشكل أنيق.\n\n"
                    "البنية:\n"
                    "\u2022 try:      الكود المحتمل خطؤه\n"
                    "\u2022 except:   معالجة الخطأ\n"
                    "\u2022 else:     إذا لم يحدث خطأ\n"
                    "\u2022 finally:  ينفذ دائماً\n\n"
                    "أنواع الأخطاء الشائعة:\n"
                    "\u2022 ValueError: قيمة غير صحيحة\n"
                    "\u2022 TypeError: نوع غير مناسب\n"
                    "\u2022 FileNotFoundError: ملف غير موجود\n"
                    "\u2022 ZeroDivisionError: قسمة على صفر"
                ),
                "code": (
                    "def divide(a, b):\n"
                    "    try:\n"
                    "        result = a / b\n"
                    "    except ZeroDivisionError:\n"
                    '        return "خطأ: لا يمكن القسمة على صفر"\n'
                    "    except TypeError:\n"
                    '        return "خطأ: الرجاء إدخال أرقام"\n'
                    "    else:\n"
                    '        return f"النتيجة: {result}"\n'
                    "    finally:\n"
                    '        print("تمت محاولة القسمة")\n\n'
                    "print(divide(10, 2))\n"
                    "print(divide(10, 0))\n"
                    'print(divide("a", 2))\n\n'
                    'print("---")\n\n'
                    "# رفع استثناء يدويًا\n"
                    "def check_age(age):\n"
                    "    if age < 0:\n"
                    '        raise ValueError("العمر لا يمكن أن يكون سالباً!")\n'
                    '    print(f"العمر: {age}")\n\n'
                    "try:\n"
                    "    check_age(-5)\n"
                    "except ValueError as e:\n"
                    "    print(f\"تم التقاط: {e}\")"
                ),
            },
            {
                "title": "الملفات (File I/O)",
                "icon": "\U0001f4be",
                "content": (
                    "قراءة وكتابة الملفات في Python.\n\n"
                    "طرق الفتح:\n"
                    '\u2022 "r" : قراءة (افتراضي)\n'
                    '\u2022 "w" : كتابة (مسح المحتوى)\n'
                    '\u2022 "a" : إضافة لنهاية الملف\n'
                    '\u2022 "r+": قراءة وكتابة\n\n'
                    "ملاحظة: استخدم with لفتح الملفات - يغلقها تلقائياً حتى لو حدث خطأ!"
                ),
                "code": (
                    "# كتابة ملف\n"
                    'with open("example.txt", "w", encoding="utf-8") as f:\n'
                    '    f.write("مرحبا بالعالم!\\n")\n'
                    '    f.write("هذا سطر ثاني\\n")\n\n'
                    'print("تمت الكتابة!")\n\n'
                    "# قراءة الملف\n"
                    'with open("example.txt", "r", encoding="utf-8") as f:\n'
                    "    content = f.read()\n"
                    '    print("محتويات الملف:")\n'
                    "    print(content)\n\n"
                    "# قراءة سطر سطر\n"
                    'with open("example.txt", "r", encoding="utf-8") as f:\n'
                    "    for line in f:\n"
                    '        print(f"> {line.strip()}")'
                ),
            },
            {
                "title": "وحدات ومكتبات",
                "icon": "\U0001f9e9",
                "content": (
                    "الوحدات (Modules) تنظم الكود في ملفات منفصلة.\n\n"
                    "طرق الاستيراد:\n"
                    "\u2022 import math           : استيراد المكتبة كلها\n"
                    "\u2022 from math import sqrt : استيراد جزء منها\n"
                    "\u2022 import math as m      : اسم مختصر\n\n"
                    "مكتبات مدمجة مهمة:\n"
                    "\u2022 math     : عمليات رياضية\n"
                    "\u2022 random   : أرقام عشوائية\n"
                    "\u2022 datetime : التاريخ والوقت\n"
                    "\u2022 os       : نظام التشغيل\n"
                    "\u2022 json     : التعامل مع JSON"
                ),
                "code": (
                    "import math\n"
                    "import random\n"
                    "from datetime import datetime\n\n"
                    "# math\n"
                    "print(f\"PI = {math.pi}\")\n"
                    "print(f\"جذر 16 = {math.sqrt(16)}\")\n\n"
                    "# random\n"
                    "print(f\"رقم عشوائي: {random.randint(1, 100)}\")\n"
                    'print(f"اختيار: {random.choice([\'تفاح\', \'موز\', \'برتقال\'])}")\n\n'
                    "# datetime\n"
                    "now = datetime.now()\n"
                    'print(f"التاريخ: {now:%Y-%m-%d}")\n'
                    'print(f"الوقت: {now:%H:%M:%S}")\n\n'
                    "# قائمة عشوائية\n"
                    'items = ["أ", "ب", "ج", "د"]\n'
                    "random.shuffle(items)\n"
                    'print(f"بعد الخلط: {items}")'
                ),
            },
        ]

    def setup_ui(self):
        # الإطار الرئيسي
        main_frame = tk.Frame(self.root, bg="#1e1e2e")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # الشريط الجانبي
        sidebar = tk.Frame(main_frame, bg="#181825", width=280)
        sidebar.pack(side=tk.RIGHT, fill=tk.Y)
        sidebar.pack_propagate(False)

        # عنوان الشريط
        header = tk.Label(
            sidebar, text="\U0001f40d  دروس بايثون", font=("Arial", 18, "bold"),
            bg="#181825", fg="#cdd6f4", pady=20
        )
        header.pack(fill=tk.X)

        # قائمة الدروس
        self.topic_listbox = tk.Listbox(
            sidebar, bg="#1e1e2e", fg="#cdd6f4",
            selectbackground="#45475a", selectforeground="#cdd6f4",
            font=("Arial", 12), borderwidth=0, highlightthickness=0,
            activestyle="none", cursor="hand2"
        )
        self.topic_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        for i, topic in enumerate(self.topics):
            self.topic_listbox.insert(tk.END, f"  {topic['icon']}  {topic['title']}")

        self.topic_listbox.bind("<<ListboxSelect>>", self.on_topic_select)

        # الإطار الأيمن (المحتوى)
        content_frame = tk.Frame(main_frame, bg="#1e1e2e")
        content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        # عنوان الدرس
        self.title_label = tk.Label(
            content_frame, text="", font=("Arial", 22, "bold"),
            bg="#1e1e2e", fg="#cdd6f4", anchor="w"
        )
        self.title_label.pack(fill=tk.X, pady=(0, 15))

        # إطار المحتوى والكود
        paned = tk.PanedWindow(content_frame, orient=tk.VERTICAL, bg="#1e1e2e", sashrelief=tk.RAISED, sashwidth=4)
        paned.pack(fill=tk.BOTH, expand=True)

        # منطقة الشرح
        top_frame = tk.Frame(paned, bg="#1e1e2e")
        paned.add(top_frame, height=200)

        self.content_text = tk.Text(
            top_frame, font=("Arial", 12), bg="#1e1e2e", fg="#cdd6f4",
            wrap=tk.WORD, padx=15, pady=15, borderwidth=0, highlightthickness=0,
            relief=tk.FLAT, spacing1=4, spacing2=2
        )
        self.content_text.pack(fill=tk.BOTH, expand=True)
        self.content_text.config(state=tk.DISABLED)

        # إطار الكود
        bottom_frame = tk.Frame(paned, bg="#1e1e2e")
        paned.add(bottom_frame, height=250)

        # شريط أدوات الكود
        code_toolbar = tk.Frame(bottom_frame, bg="#181825", height=40)
        code_toolbar.pack(fill=tk.X)
        code_toolbar.pack_propagate(False)

        code_label = tk.Label(
            code_toolbar, text="\U0001f4bb  مثال تطبيقي", font=("Arial", 11, "bold"),
            bg="#181825", fg="#a6e3a1", padx=15
        )
        code_label.pack(side=tk.RIGHT)

        self.run_btn = tk.Button(
            code_toolbar, text="\u25b6  تشغيل", font=("Arial", 10, "bold"),
            bg="#a6e3a1", fg="#1e1e2e", padx=15, pady=2,
            borderwidth=0, cursor="hand2", command=self.run_code
        )
        self.run_btn.pack(side=tk.LEFT, padx=10, pady=5)

        self.copy_btn = tk.Button(
            code_toolbar, text="\U0001f4cb  نسخ", font=("Arial", 10),
            bg="#45475a", fg="#cdd6f4", padx=15, pady=2,
            borderwidth=0, cursor="hand2", command=self.copy_code
        )
        self.copy_btn.pack(side=tk.LEFT, padx=(0, 5), pady=5)

        # محرر الكود
        self.code_editor = scrolledtext.ScrolledText(
            bottom_frame, font=("Consolas", 11), bg="#11111b", fg="#a6e3a1",
            insertbackground="#cdd6f4", wrap=tk.NONE, padx=10, pady=10,
            borderwidth=0, highlightthickness=0, relief=tk.FLAT
        )
        self.code_editor.pack(fill=tk.BOTH, expand=True)

        # منطقة المخرجات
        output_frame = tk.Frame(content_frame, bg="#181825", height=120)
        output_frame.pack(fill=tk.X, pady=(10, 0))
        output_frame.pack_propagate(False)

        output_header = tk.Label(
            output_frame, text="\U0001f4df  المخرجات", font=("Arial", 10, "bold"),
            bg="#181825", fg="#fab387", anchor="w", padx=10
        )
        output_header.pack(fill=tk.X, pady=(5, 0))

        self.output_text = scrolledtext.ScrolledText(
            output_frame, font=("Consolas", 10), bg="#181825", fg="#fab387",
            wrap=tk.WORD, padx=10, pady=5, borderwidth=0, highlightthickness=0,
            relief=tk.FLAT, height=4
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        self.output_text.config(state=tk.DISABLED)

    def show_topic(self, index):
        topic = self.topics[index]
        self.title_label.config(text=f"{topic['icon']}  {topic['title']}")

        self.content_text.config(state=tk.NORMAL)
        self.content_text.delete("1.0", tk.END)
        self.content_text.insert("1.0", topic["content"])
        self.content_text.config(state=tk.DISABLED)

        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert("1.0", topic["code"])

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)

    def on_topic_select(self, event):
        selection = self.topic_listbox.curselection()
        if selection:
            self.show_topic(selection[0])

    def run_code(self):
        code = self.code_editor.get("1.0", tk.END).strip()

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                exec(code)
            except Exception as e:
                print(f"خطأ: {e}")

        output = f.getvalue()
        if output:
            self.output_text.insert("1.0", output)
        else:
            self.output_text.insert("1.0", "(لا يوجد مخرجات)")

        self.output_text.config(state=tk.DISABLED)

    def copy_code(self):
        code = self.code_editor.get("1.0", tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(code)
        messagebox.showinfo("تم", "تم نسخ الكود إلى الحافظة!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PythonExplained(root)
    root.mainloop()
