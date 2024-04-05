from PyInstaller.__main__ import run

if __name__ == '__main__':
    options = ["--windowed",
               "--onedir",
               "--icon", 'views/settings.ico',
               "--name", '核容试验辅助工具V1.0-3.31',
               "--add-data", "views/1浪头220kV第一组蓄电池充放电记录.xlsx;views",
               "--add-data", "views/五龙背变蓄电池记录.xlsx;views",
               "--add-data", "views/团山66kV蓄电池充放电记录.xlsx;views",
               'main.py',  # 主程序
               ]
    run(options)
