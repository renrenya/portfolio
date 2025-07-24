import tkinter as tk
import random
import time

sentences = [
    "夏に食べるアイスは格別です。",
    "私は毎日プログラミングの勉強をしています。",
    "新しい本の発売日が今から楽しみです。",
    "私は文字を素早く正確に入力するためにタイピング練習をする。",
]

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("タイピングゲーム")
        self.start_time = None

        self.sentence = random.choice(sentences)

        self.label = tk.Label(root, text=self.sentence, font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 14), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.button = tk.Button(root, text="判定する", command=self.check_input)
        self.button.pack()

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_input(self):
        end_time = time.time()
        user_input = self.entry.get()
        if user_input == self.sentence:
            elapsed = end_time - self.start_time
            speed = len(self.sentence) / elapsed
            self.result_label.config(
                text=f" 正解\n時間: {elapsed:.2f}秒\n速度: {speed:.2f}文字/秒", fg="green"
            )
        else:
            self.result_label.config(text="❌ 間違いがあります。", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
