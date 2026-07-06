import subprocess
import time
import pyautogui

def draw_funny_art():
    # Запускаем Paint
    subprocess.Popen("mspaint.exe")
    time.sleep(1.5)  # Ждем, пока окно загрузится
    
    # Разворачиваем окно на весь экран, чтобы координаты не съехали
    pyautogui.hotkey('win', 'up')
    time.sleep(0.5)

    # Перемещаем курсор в центр холста для старта
    start_x, start_y = 500, 500
    pyautogui.moveTo(start_x, start_y)

    # Рисуем левую сферу (круг)
    pyautogui.dragTo(start_x + 50, start_y + 50, duration=0.3, button='left')
    pyautogui.dragTo(start_x + 100, start_y, duration=0.3, button='left')
    pyautogui.dragTo(start_x + 50, start_y - 50, duration=0.3, button='left')
    pyautogui.dragTo(start_x, start_y, duration=0.3, button='left')

    # Смещаемся к правой сфере
    pyautogui.moveTo(start_x + 100, start_y)

    # Рисуем правую сферу (круг)
    pyautogui.dragTo(start_x + 150, start_y + 50, duration=0.3, button='left')
    pyautogui.dragTo(start_x + 200, start_y, duration=0.3, button='left')
    pyautogui.dragTo(start_x + 150, start_y - 50, duration=0.3, button='left')
    pyautogui.dragTo(start_x + 100, start_y, duration=0.3, button='left')

    # Переходим к рисованию вертикального овала по центру вверх
    pyautogui.moveTo(start_x + 50, start_y - 30)
    
    # Линия вверх, закругление, линия вниз
    pyautogui.dragTo(start_x + 50, start_y - 250, duration=0.4, button='left')   # Вверх
    pyautogui.dragTo(start_x + 150, start_y - 250, duration=0.2, button='left')  # Шляпка (овал)
    pyautogui.dragTo(start_x + 150, start_y - 30, duration=0.4, button='left')   # Вниз

if __name__ == "__main__":
    draw_funny_art()