import tkinter as tk
from tkinter import ttk

class HotkeyManager:
    def __init__(self, root):
        self.root = root
        self.root.title("핫키 관리자")
        
        # 테이블 생성
        self.tree = ttk.Treeview(root, columns=("앱 이름", "핫키"), show="headings")
        self.tree.heading("앱 이름", text="앱 이름")
        self.tree.heading("핫키", text="핫키")
        self.tree.pack(fill="both", expand=True)
        
        # 입력 필드 및 추가 버튼
        self.app_name_entry = ttk.Entry(root)
        self.app_name_entry.pack()
        self.hotkey_entry = ttk.Entry(root)
        self.hotkey_entry.pack()
        
        self.add_button = ttk.Button(root, text="추가", command=self.add_hotkey)
        self.add_button.pack()
    
    def add_hotkey(self):
        app_name = self.app_name_entry.get()
        hotkey = self.hotkey_entry.get()
        if app_name and hotkey:
            self.tree.insert("", "end", values=(app_name, hotkey))

# 앱 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = HotkeyManager(root)
    root.mainloop()
