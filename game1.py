import random
import re
import tkinter as tk
import tkinter.messagebox as tmsg

def ButtonClick():
    # 取得使用者輸入的數字  
    guess = editbox.get()
    if len(guess) != 4:
        tmsg.showerror('提示', '請輸入四位數字!')    
        return
    if not re.match(r'^\d\d\d\d$', guess):
        tmsg.showerror('提示', '請輸入數字!')      
        return
    if len(set(guess)) != 4:
        tmsg.showerror('提示', '請輸入不重複的數字!')
        return
    # 檢查答案
    hit = 0
    blow = 0
    for i in range(4):
        if int(guess[i]) == num[i]:
            hit += 1 
        elif int(guess[i]) in num:
            blow += 1
    if hit == 4:
            tmsg.showinfo('猜測結果', '恭喜你答對了!')
            root.destroy()
    else:
        memorybox.insert(tk.END, '猜測結果 : ' + '數字正確，位置正確 : ' + str(hit) + '\n' + '                ' + '數字正確，位置錯誤 : ' + str(blow) + '\n')
    
def generate_numbers():
    # 生成四個不重複的隨機數字
    while True:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)
        d = random.randint(1, 9)
        num = [a, b, c, d]
        if len(set(num)) == 4:
            return num
   
num = generate_numbers()

# 製作視窗
root = tk.Tk()
root.title('猜數字遊戲')
root.geometry('600x400')

# 製作標籤
label1 = tk.Label(root, text='請輸入四個不重複的數字', font=('Arial', 15))
label1.place(x = 20, y = 20)

# 製作文字框
editbox = tk.Entry(root, width = 6, font=('Arial', 20))
editbox.place(x = 50, y = 70)

# 製作按鈕
button = tk.Button(root,width = 6, text='確認', font=('Arial', 15), command = ButtonClick)
button.place(x = 150, y = 70)

memorybox = tk.Text(root, font=('Arial', 15))
memorybox.place(x = 250, y = 0, width = 350 , height = 400)

# 啟動視窗
root.mainloop()



