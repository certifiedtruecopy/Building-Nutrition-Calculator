import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox

def calculate_nutrient_intake(age, gender, weight, height, activity_level, goal):
    # محاسبه BMR
    if gender == "زن":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:  # فرض بر اینکه جنسیت "مرد" است
        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    # ضریب فعالیت
    activity_factors = {
        "فوق العاده فعال": 1.9,
        "خیلی فعال": 1.725,
        "متوسط فعال": 1.55,
        "کمی فعال": 1.375,
        "بی تحرک": 1.2
    }
    tdee = bmr * activity_factors[activity_level]

  
    protein_percentage = 0.15  
    carbs_percentage = 0.50  
    fat_percentage = 0.35  

    protein = (tdee * protein_percentage) / 4  
    carbs = (tdee * carbs_percentage) / 4  
    fat = (tdee * fat_percentage) / 9  

    # تنظیم مقادیر بر اساس هدف وزنی
    if goal == "افزایش وزن":
        carbs *= 1.1
        fat *= 1.1
    elif goal == "کاهش وزن":
        carbs *= 0.9
        fat *= 0.9

    return protein, carbs, fat

def on_calculate():
    try:
        age = int(age_entry.get())  
        gender = gender_combobox.get()  
        weight = float(weight_entry.get())
        height = float(height_entry.get())  
        activity_level = activity_combobox.get()
        goal = goal_combobox.get()
        
        protein, carbs, fat = calculate_nutrient_intake(age, gender, weight, height, activity_level, goal)
        messagebox.showinfo("نتایج", f"پروتئین: {protein:.2f} گرم\nکربوهیدرات: {carbs:.2f} گرم\nچربی: {fat:.2f} گرم")
    except ValueError:
        messagebox.showerror("خطا", "لطفا اطلاعات صحیح وارد کنید")

# ایجاد یک نمونه از کلاس 
root = tk.Tk()

# تعیین عنوان پنجره
root.title("محاسبه‌گر")

# تعیین اندازه پنجره
root.geometry("320x660")

# بارگذاری عکس
image = PhotoImage(file="C:/Users/anaja/OneDrive/Desktop/App/Fitness/photo.PNG")

# ایجاد یک برچسب (لیبل) با استفاده از تی تی کا و قرار دادن عکس در آن
image_label = ttk.Label(root, image=image)
image_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# ایجاد بخش‌های ورودی
age_label = ttk.Label(root, text="سن")
age_label.grid(row=1, column=1, padx=10, pady=10)
age_entry = ttk.Entry(root, width=24)
age_entry.grid(row=1, column=0, padx=10, pady=10)

gender_label = ttk.Label(root, text="جنسیت")
gender_label.grid(row=2, column=1, padx=10, pady=10)
gender_combobox = ttk.Combobox(root, values=["مرد", "زن"])
gender_combobox.grid(row=2, column=0, padx=10, pady=10)

weight_label = ttk.Label(root, text="وزن")
weight_label.grid(row=3, column=1, padx=10, pady=10)
weight_entry = ttk.Entry(root, width=24)
weight_entry.grid(row=3, column=0, padx=10, pady=10)

height_label = ttk.Label(root, text="قد")
height_label.grid(row=4, column=1, padx=10, pady=10)
height_entry = ttk.Entry(root, width=24)
height_entry.grid(row=4, column=0, padx=10, pady=10)

activity_label = ttk.Label(root, text="فعالیت روزانه")
activity_label.grid(row=5, column=1, padx=10, pady=10)
activity_combobox = ttk.Combobox(root, values=["فوق العاده فعال", "خیلی فعال", "متوسط فعال", "کمی فعال", "بی تحرک"])
activity_combobox.grid(row=5, column=0, padx=10, pady=10)

goal_label = ttk.Label(root, text="هدف")
goal_label.grid(row=6, column=1, padx=10, pady=10)
goal_combobox = ttk.Combobox(root, values=["افزایش وزن", "کاهش وزن", "ثبات وزن"])
goal_combobox.grid(row=6, column=0, padx=10, pady=10)

# ایجاد دکمه محاسبه
calculate_button = ttk.Button(root, text="محاسبه", width=24, command=on_calculate)
calculate_button.grid(row=8, column=0, padx=10, pady=10)

# نمایش پنجره تا زمانی که کاربر آن را ببندد
root.mainloop()