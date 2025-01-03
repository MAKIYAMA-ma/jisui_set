import os

start = 9
finish = 11
base = "(一般コミック) [藤本タツキ] チェンソーマン"
for i in range(start, finish+1):
    # 2桁のゼロパディングされた文字列を作成
    dir_name = base + " 第" + f"{i:02d}" + "巻"

    # ディレクトリが存在しない場合に作成
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"ディレクトリ '{dir_name}' を作成しました。")
    else:
        print(f"ディレクトリ '{dir_name}' は既に存在します。")
