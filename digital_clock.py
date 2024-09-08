import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text="Thời gian hiện tại là: " + current_time)
    window.after(1000, update_clock)

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Đồng hồ")

# Tạo nhãn để hiển thị thời gian
clock_label = tk.Label(window, font=("Arial", 24), bg="black", fg="white")
clock_label.pack(padx=20, pady=20)

# Bắt đầu cập nhật đồng hồ
update_clock()

# Chạy vòng lặp chính của tkinter
window.mainloop()
