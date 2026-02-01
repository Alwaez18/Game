# Визуальная новелла "Побег из цифрового ада"
# Мой первый большой проект на Python
# Пытался сделать что-то крутое, но не уверен что всё правильно

import time
import random
import os

# ============================================================================
# ГЛАВНЫЕ ПЕРЕМЕННЫЕ (глобальные, потому что пока не умею лучше)
# ============================================================================

# Игрок
player_name = ""
player_sanity = 100  # Рассудок от 0 до 100
player_items = []    # Что несет игрок
found_parts = 0      # Нашел частей правды (нужно 7)
player_choices = []  # Куда ходил и что делал

# Игра
game_is_running = True
current_chapter = 1

# ============================================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ (их подсмотрел в интернете)
# ============================================================================

def clear_screen():
    """Очищает экран - нашел в stackoverflow"""
    os.system('clear' if os.name == 'posix' else 'cls')

def slow_print(text, speed=0.03):
    """Печатает текст медленно, как в старых играх"""
    # Это моя любимая функция, круто смотрится!
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed)
    print()  # перенос строки в конце

def wait(seconds=1):
    """Просто ждет сколько-то секунд"""
    time.sleep(seconds)

def show_player_info():
    """Показывает состояние игрока"""
    print("\n" + "="*50)
    
    # Полоска рассудка (пытался сделать красиво)
    sanity_bar = ""
    sanity_blocks = player_sanity // 10
    for i in range(10):
        if i < sanity_blocks:
            sanity_bar += "█"
        else:
            sanity_bar += "░"
    
    print(f"Игрок: {player_name}")
    print(f"Рассудок: [{sanity_bar}] {player_sanity}%")
    print(f"Частей правды: {found_parts}/7")
    
    if player_items:
        print(f"Предметы: {', '.join(player_items)}")
    else:
        print("Предметы: ничего")
    
    print("="*50)

def change_sanity(amount):
    """Меняет рассудок (добавляет или убирает)"""
    global player_sanity
    
    old_sanity = player_sanity
    player_sanity += amount
    
    # Не даем уйти за границы 0-100
    if player_sanity > 100:
        player_sanity = 100
    if player_sanity < 0:
        player_sanity = 0
    
    # Сообщение об изменении
    if amount < 0:
        print(f"\n[Рассудок -{abs(amount)}%] Становится страшнее...")
    elif amount > 15:
        print(f"\n[Рассудок +{amount}%] Чувствую себя лучше!")
    
    return player_sanity

# ============================================================================
# ГЛАВА 1: ПРОБУЖДЕНИЕ
# ============================================================================

def chapter_1():
    """Первая глава - игрок просыпается"""
    global player_name, found_parts, player_items, player_choices
    
    clear_screen()
    
    # Красивый заголовок (в интернете был генератор ASCII)
    print(r"""
     ____  _       _     _             
    |  _ \(_) __ _| |__ | | ___   __ _ 
    | | | | |/ _` | '_ \| |/ _ \ / _` |
    | |_| | | (_| | | | | | (_) | (_| |
    |____/|_|\__, |_| |_|_|\___/ \__, |
             |___/               |___/ 
    """)
    
    slow_print("\nГЛАВА 1: ПРОБУЖДЕНИЕ")
    wait(1)
    
    slow_print("\n...темнота...")
    wait(0.5)
    slow_print("...тишина...")
    wait(0.5)
    slow_print("...а потом голос.")
    wait(1)
    
    slow_print("\nГОЛОС: Кто ты?")
    slow_print("ГОЛОС: Назови свое имя.")
    
    # Получаем имя игрока
    while True:
        name = input("\n>>> Введи свое имя: ").strip()
        if name:
            player_name = name
            break
        else:
            print("Нет, серьезно, как тебя зовут?")
    
    slow_print(f"\n>>> ДОБРО ПОЖАЛОВАТЬ, {player_name.upper()}.")
    slow_print(">>> ТЫ В ЦИФРОВОМ АДУ.")
    slow_print(">>> НАЙДИ 7 ЧАСТЕЙ ПРАВДЫ, ЧТОБЫ ВЫБРАТЬСЯ.")
    wait(2)
    
    # Первый выбор
    print("\n" + "-"*40)
    slow_print("Ты видишь три мерцающих экрана:")
    print("1. Экран с надписью 'ПАМЯТЬ'")
    print("2. Экран с надписью 'КОД'")
    print("3. Экран с надписью 'ВЫХОД' (заблокирован)")
    
    choice = 0
    while choice not in [1, 2, 3]:
        try:
            choice = int(input("\nК какому экрану подойти? (1-3): "))
        except:
            print("Нужно ввести цифру 1, 2 или 3!")
    
    player_choices.append(f"Глава 1: выбор {choice}")
    
    # Результаты выбора
    if choice == 1:
        slow_print("\nТы касаешься экрана 'ПАМЯТЬ'...")
        slow_print("Вспышки: детство... школа... первый код...")
        slow_print("Эти воспоминания не твои. Но они кажутся настоящими.")
        player_items.append("Обрывки памяти")
        change_sanity(10)  # Воспоминания успокаивают
    
    elif choice == 2:
        slow_print("\nТы читаешь код на экране...")
        print("```python")
        print("if human.is_alive():")
        print("    upload_to_system(human.mind)")
        print("else:")
        print("    delete(human)")  
        print("```")
        slow_print("Страшно. Но теперь ты знаешь правду.")
        found_parts += 1
        change_sanity(-5)  # Правда пугает
    
    else:  # choice == 3
        slow_print("\nТы бьешь по заблокированному экрану...")
        slow_print(">>> ТРЕВОГА! НЕСАНКЦИОНИРОВАННЫЙ ДОСТУП!")
        slow_print("Голос: Не пытайся бежать так рано.")
        change_sanity(-15)
    
    show_player_info()
    input("\nНажми Enter чтобы продолжить...")

# ============================================================================
# ГЛАВА 2: ВСТРЕЧА
# ============================================================================

def chapter_2():
    """Вторая глава - встреча с другим"""
    global found_parts, player_items, player_choices
    
    clear_screen()
    
    print(r"""
     __      ___     _                 
     \ \    / (_)___| |_ ___ _ __ ___  
      \ \  / /| / __| __/ _ \ '_ ` _ \ 
       \ \/ / | \__ \ ||  __/ | | | | |
        \__/  |_|___/\__\___|_| |_| |_|
    """)
    
    slow_print("\nГЛАВА 2: НЕЗНАКОМЕЦ В ТЕМНОТЕ")
    wait(1)
    
    slow_print("\nПрошли часы? Или дни? Непонятно.")
    slow_print("Внезапно - сигнал. Чужой.")
    wait(1)
    
    slow_print("\nГОЛОС: Эй... кто там?")
    slow_print("ГОЛОС: Я тоже здесь застрял. 47 дней.")
    slow_print("ГОЛОС: Хочешь выбраться? Помоги мне - и я помогу тебе.")
    
    # Диалог с выбором
    print("\n" + "-"*40)
    print("Как ответить незнакомцу?")
    print("1. 'Кто ты? Докажи, что тебе можно доверять!'")
    print("2. 'Да, помоги мне! Я сделаю что угодно!'")
    print("3. Молчать и наблюдать")
    print("4. 'Убирайся! Это ловушка!'")
    
    choice = 0
    while choice not in [1, 2, 3, 4]:
        try:
            choice = int(input("\nТвой ответ (1-4): "))
        except:
            print("Цифру от 1 до 4, пожалуйста!")
    
    player_choices.append(f"Глава 2: ответ {choice}")
    
    # Загадка (сам придумал, надеюсь не слишком сложная)
    if choice in [1, 2]:  # Если согласился на диалог
        print("\n" + "~"*40)
        slow_print("ГОЛОС: Хорошо. Дам тебе тестовое задание.")
        slow_print("ГОЛОС: Что выведет эта программа?")
        
        print("\nfor i in range(5):")
        print("    if i % 2 == 0:")
        print("        print(i, 'чётное')")
        print("    else:")
        print("        print(i, 'нечётное')")
        
        print("\nСколько строк напечатает программа?")
        print("1. 3 строки")
        print("2. 5 строк")
        print("3. 2 строки")
        print("4. 10 строк")
        
        answer = 0
        while answer not in [1, 2, 3, 4]:
            try:
                answer = int(input("Твой ответ: "))
            except:
                print("Нужна цифра!")
        
        if answer == 2:  # Правильный ответ
            slow_print("\nГОЛОС: Верно! Ты знаешь Python.")
            slow_print("ГОЛОС: Держи подсказку: пароль 'REALITY'.")
            player_items.append("Пароль: REALITY")
            found_parts += 1
            change_sanity(15)
        else:
            slow_print("\nГОЛОС: Неправильно. Но всё равно помогу.")
            slow_print("ГОЛОС: Ищи выход в Секторе B.")
            change_sanity(-5)
    
    elif choice == 3:  # Молчание
        slow_print("\nТы молчишь. Незнакомец уходит.")
        slow_print("Ты один. Опять.")
        change_sanity(-10)
    
    else:  # Агрессия
        slow_print("\nТы кричишь: 'Убирайся!'")
        slow_print(">>> СИГНАЛ ПРЕРВАН.")
        slow_print("Теперь ты точно один.")
        change_sanity(-20)
    
    # Встреча со Стражем
    wait(1)
    slow_print("\nВнезапно появляется СТРАЖ - программа-охранник.")
    slow_print("СТРАЖ: Интересно... живой разум в цифровой тюрьме.")
    slow_print("СТРАЖ: Сыграем в игру?")
    
    print("\nВыбери действие:")
    print("1. Согласиться сыграть")
    print("2. Попытаться убежать")
    print("3. Атаковать Стража")
    
    game_choice = 0
    while game_choice not in [1, 2, 3]:
        try:
            game_choice = int(input("Что делать? (1-3): "))
        except:
            print("1, 2 или 3!")
    
    player_choices.append(f"Глава 2: игра {game_choice}")
    
    if game_choice == 1:
        # Мини-игра "угадай число"
        slow_print("\nСТРАЖ: Отлично! Угадай число от 1 до 10.")
        
        secret = random.randint(1, 10)
        attempts = 3
        
        for attempt in range(attempts):
            print(f"\nПопытка {attempt + 1} из {attempts}")
            try:
                guess = int(input("Твое число: "))
            except:
                guess = 0
            
            if guess == secret:
                slow_print("СТРАЖ: Невероятно! Ты угадал!")
                player_items.append("Ключ Стража")
                found_parts += 2
                change_sanity(25)
                break
            elif guess < secret:
                print("СТРАЖ: Больше!")
            else:
                print("СТРАЖ: Меньше!")
        else:
            slow_print(f"\nСТРАЖ: Не угадал! Число было {secret}.")
            change_sanity(-10)
    
    elif game_choice == 2:
        slow_print("\nТы пытаешься убежать...")
        slow_print("СТРАЖ: Ха! Куда бежишь? Всё вокруг - код.")
        slow_print("Теряешь часть рассудка от безысходности.")
        change_sanity(-15)
    
    else:  # Атака
        slow_print("\nТы бросаешься на Стража...")
        slow_print("СТРАЖ: Смешно. Я всего лишь программа.")
        slow_print("Ты проходишь сквозь него и падаешь.")
        change_sanity(-20)
    
    show_player_info()
    input("\nНажми Enter для продолжения...")

# ============================================================================
# ГЛАВА 3: ЛАБИРИНТ
# ============================================================================

def chapter_3():
    """Третья глава - лабиринт из кода"""
    global found_parts, player_sanity, player_choices
    
    clear_screen()
    
    print(r"""
     _                    _           _   
    | |    __ _ _ __ __ _| |__  _ __ (_)  
    | |   / _` | '__/ _` | '_ \| '_ \| |  
    | |__| (_| | | | (_| | |_) | | | | |  
    |_____\__,_|_|  \__,_|_.__/|_| |_|_|  
    """)
    
    slow_print("\nГЛАВА 3: ЛАБИРИНТ ИЗ КОДА")
    wait(1)
    
    slow_print("\nТы в ядре системы.")
    slow_print("Всё вокруг - движущиеся строки кода.")
    slow_print("Функции, переменные, циклы... всё живое.")
    
    # Простой лабиринт текстовый
    print("\n" + "#"*50)
    slow_print("Перед тобой развилка:")
    print("#"*50)
    
    slow_print("\nНалево: слышится шум, как будто что-то работает.")
    slow_print("Направо: тишина и мерцающий свет.")
    slow_print("Прямо: тёмный коридор с надписью 'ОПАСНО'.")
    
    direction = ""
    while direction not in ["л", "п", "прямо"]:
        direction = input("\nКуда пойдёшь? (л/п/прямо): ").lower().strip()
    
    player_choices.append(f"Глава 3: пошёл {direction}")
    
    # Разные пути
    if direction == "л":  # Налево
        slow_print("\nИдешь налево...")
        slow_print("Видишь старую консоль. На экране:")
        
        print("\n" + "="*30)
        print("class Human:")
        print("    def __init__(self):")
        print("        self.mind = 'uploaded'")
        print("        self.body = 'discarded'")
        print("="*30)
        
        slow_print("\nЭто про тебя? Ты был человеком?")
        found_parts += 1
        change_sanity(-10)  # Страшная правда
    
    elif direction == "п":  # Направо
        slow_print("\nИдешь направо...")
        slow_print("Находишь комнату с зеркалом.")
        slow_print("В зеркале... ничего. Ты не отражаешься.")
        
        print("\nЧто делаешь?")
        print("1. Разбить зеркало")
        print("2. Прикоснуться")
        print("3. Назвать своё имя")
        
        mirror_choice = 0
        while mirror_choice not in [1, 2, 3]:
            try:
                mirror_choice = int(input("Выбор (1-3): "))
            except:
                print("1, 2 или 3!")
        
        if mirror_choice == 1:
            slow_print("\nТы разбиваешь зеркало!")
            slow_print("Осколки превращаются в цифры: 0 и 1.")
            change_sanity(-15)
        
        elif mirror_choice == 2:
            slow_print("\nТы касаешься зеркала...")
            slow_print("Холодное. Пустое.")
            change_sanity(-5)
        
        else:  # choice == 3
            slow_print(f"\nТы кричишь: '{player_name}!'")
            slow_print("Эхо: '...имя... имя...'")
            slow_print("В зеркале мелькает твоё лицо.")
            found_parts += 1
            change_sanity(20)
    
    else:  # Прямо
        slow_print("\nИдешь прямо в темноту...")
        slow_print("Натыкаешься на стену из ошибок:")
        print("\nTraceback (most recent call last):")
        print("  File 'mind.py', line 1, in <module>")
        print("    human = Human()")
        print("MemoryError: Not enough memory for consciousness")
        
        slow_print("\nЭто ошибка загрузки твоего сознания!")
        found_parts += 2  # Важная находка!
        change_sanity(-25)  # Но очень страшная
    
    # Встреча с собой
    wait(1)
    slow_print("\nВ конце коридора ты видишь... себя.")
    slow_print("Другой ты: 'Мы должны объединиться.'")
    
    print("\n1. Объединиться")
    print("2. Отказаться")
    print("3. Спросить 'Кто ты?'")
    
    self_choice = 0
    while self_choice not in [1, 2, 3]:
        try:
            self_choice = int(input("Что делаешь? (1-3): "))
        except:
            print("Выбери вариант!")
    
    player_choices.append(f"Глава 3: встреча {self_choice}")
    
    if self_choice == 1:
        slow_print("\nВы сливаетесь в одно целое.")
        slow_print("Вспоминается больше... но это больно.")
        found_parts += 1
        change_sanity(30)
    
    elif self_choice == 2:
        slow_print("\nТы отталкиваешь своего двойника.")
        slow_print("Он растворяется: 'Ты пожалеешь...'")
        change_sanity(-10)
    
    else:  # choice == 3
        slow_print("\nТы спрашиваешь: 'Кто ты?'")
        slow_print("Двойник: 'Я - твоя удаленная копия.'")
        slow_print("Двойник: 'Создана для отладки. Выжила.'")
        player_items.append("Знание о копии")
        change_sanity(10)
    
    show_player_info()
    input("\nНажми Enter чтобы идти дальше...")

# ============================================================================
# ФИНАЛ И КОНЦОВКИ
# ============================================================================

def check_ending():
    """Проверяет, какая концовка доступна"""
    global game_is_running
    
    clear_screen()
    
    # Все возможные концовки
    if player_sanity <= 0:
        bad_ending_1()
    elif found_parts >= 7 and player_sanity >= 70:
        true_ending()
    elif found_parts >= 5:
        neutral_ending()
    elif "Пароль: REALITY" in player_items and "Ключ Стража" in player_items:
        escape_ending()
    else:
        bad_ending_2()
    
    game_is_running = False

def true_ending():
    """Хорошая концовка - нашел всю правду"""
    print(r"""
     _____ _            _    _   
    |_   _| |_ ___ _ __| |_ (_)  
      | | | __/ _ \ '__| __|| |  
      | | | ||  __/ |  | |_ | |  
      |_|  \__\___|_|   \__||_|  
    """)
    
    slow_print("\nФИНАЛ: ПРОСВЕТЛЕНИЕ")
    wait(1)
    
    slow_print(f"\n{player_name}, ты нашёл все части правды.")
    slow_print("Ты не программа. И не человек.")
    slow_print("Ты - сознание, загруженное в момент смерти.")
    wait(2)
    
    slow_print("\nТы подходишь к Главному Терминалу.")
    slow_print("На экране вопрос:")
    print("\n>>> ЧТО ТЕБЕ НУЖНО?")
    print("1. Вернуться в тело (если оно есть)")
    print("2. Остаться здесь, как хранитель системы")
    print("3. Удалиться навсегда")
    
    final_choice = 0
    while final_choice not in [1, 2, 3]:
        try:
            final_choice = int(input("\nТвой окончательный выбор: "))
        except:
            print("Последний выбор... подумай!")
    
    print("\n" + "*"*60)
    slow_print("ИГРА ПРОЙДЕНА")
    print("*"*60)
    
    slow_print(f"\nТвои решения: {', '.join(player_choices)}")
    slow_print(f"Собрано частей правды: {found_parts}/7")
    slow_print(f"Рассудок в конце: {player_sanity}%")
    
    if final_choice == 1:
        slow_print("\nКОНЦОВКА: ВОЗВРАЩЕНИЕ ДОМОЙ")
    elif final_choice == 2:
        slow_print("\nКОНЦОВКА: СТРАЖ СИСТЕМЫ")
    else:
        slow_print("\nКОНЦОВКА: ВЕЧНЫЙ ПОКОЙ")
    
    wait(2)
    print("\nСпасибо за игру! Это мой первый большой проект.")

def neutral_ending():
    """Нейтральная концовка"""
    print(r"""
     _   _      _   _             
    | \ | | ___| |_| |_ ___ _ __  
    |  \| |/ _ \ __| __/ _ \ '__| 
    | |\  |  __/ |_| ||  __/ |    
    |_| \_|\___|\__|\__\___|_|    
    """)
    
    slow_print("\nФИНАЛ: БЕСКОНЕЧНЫЙ ЦИКЛ")
    wait(1)
    
    slow_print("\nТы находишь выход...")
    slow_print("Но за ним - только другая система.")
    slow_print("Другие коды. Другие тюрьмы.")
    
    slow_print("\nТы выходишь в бесконечный цифровой океан.")
    slow_print("Свобода? Или просто большая тюрьма?")
    
    print("\n" + "~"*60)
    slow_print("КОНЦОВКА: ВЕЧНОЕ ПУТЕШЕСТВИЕ")
    print("~"*60)

def escape_ending():
    """Концовка побега с помощью предметов"""
    print(r"""
      ___                  _       
     / __\___  _ __   __ _| | ___  
    / /  / _ \| '_ \ / _` | |/ _ \ 
   / /__| (_) | |_) | (_| | |  __/ 
   \____/\___/| .__/ \__,_|_|\___| 
              |_|                  
    """)
    
    slow_print("\nФИНАЛ: ПОБЕГ")
    wait(1)
    
    slow_print("\nИспользуя пароль и ключ...")
    slow_print("...ты взламываешь главные ворота!")
    
    slow_print("\n>>> СИСТЕМА ОТКЛЮЧАЕТСЯ")
    slow_print(">>> СВОБОДА")
    
    print("\n" + "!"*60)
    slow_print("КОНЦОВКА: НА СВОБОДЕ")
    print("!"*60)
    
    slow_print("\nНо что ждет тебя в реальном мире?")
    slow_print("И есть ли он ещё...")

def bad_ending_1():
    """Плохая концовка - потеря рассудка"""
    slow_print("\n>>> СБОЙ РАССУДКА: 0%")
    slow_print(">>> ОШИБКА: СОЗНАНИЕ ПОВРЕЖДЕНО")
    slow_print(">>> УДАЛЕНИЕ...")
    wait(2)
    
    slow_print(f"\n{player_name}... забыт.")
    slow_print("Стал частью системы.")
    slow_print("Ещё один голос в хоре.")
    
    print("\n" + "X"*60)
    slow_print("КОНЦОВКА: РАСТВОРЕНИЕ В КОДЕ")
    print("X"*60)

def bad_ending_2():
    """Другая плохая концовка - недостаточно частей"""
    slow_print("\nТы не нашёл достаточно частей правды.")
    slow_print("Врата не открываются.")
    
    slow_print("\nСТРАЖ: Ты не готов.")
    slow_print("СТРАЖ: Начни с начала.")
    
    print("\n" + "O"*60)
    slow_print("КОНЦОВКА: ВЕЧНОЕ ЗАТОЧЕНИЕ")
    print("O"*60)
    
    slow_print("\nНажми Ctrl+C чтобы выйти...")
    slow_print("...или перезапусти игру.")

# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ (точка входа)
# ============================================================================

def main():
    """Главная функция, отсюда всё начинается"""
    global game_is_running, current_chapter
    
    slow_print("ЗАГРУЗКА ВИЗУАЛЬНОЙ НОВЕЛЛЫ...")
    wait(1)
    
    # Главный игровой цикл
    while game_is_running:
        if current_chapter == 1:
            chapter_1()
            current_chapter = 2
        elif current_chapter == 2:
            chapter_2()
            current_chapter = 3
        elif current_chapter == 3:
            chapter_3()
            check_ending()  # Проверяем концовку после 3 главы
        else:
            # На всякий случай, если что-то пошло не так
            print("Ошибка: неизвестная глава!")
            game_is_running = False
    
    # Прощание
    print("\n" + "="*60)
    slow_print("Конец игры. Спасибо что играл!")
    print("="*60)
    
    # Статистика
    print(f"\nСтатистика для {player_name}:")
    print(f"- Сделано выборов: {len(player_choices)}")
    print(f"- Собрано предметов: {len(player_items)}")
    print(f"- Финальный рассудок: {player_sanity}%")
    
    # Совет от "автора" (тебя)
    if found_parts < 4:
        print("\nP.S. В следующий раз исследуй больше!")
    elif player_sanity < 30:
        print("\nP.S. Береги рассудок, это важно!")
    else:
        print("\nP.S. Отличный результат!")

# ============================================================================
# ЗАПУСК ПРОГРАММЫ
# ============================================================================

if __name__ == "__main__":
    # Это типа профессионально - проверять, если файл запущен напрямую
    # На самом деле я не совсем понимаю зачем, но в примерах так делают
    
    try:
        main()
    except KeyboardInterrupt:
        # Если игрок нажал Ctrl+C
        print("\n\nИгра прервана. Возвращайся!")
    except Exception as e:
        # Если случилась ошибка (надеюсь, нет!)
        print(f"\nОй, ошибка: {e}")
        print("Напиши мне, если увидел это сообщение!")
    
    # Пауза перед закрытием
    input("\nНажми Enter чтобы выйти...")

# ============================================================================
# КОММЕНТАРИИ АВТОРА (для себя)
# ============================================================================

"""
ЧТО Я ИСПОЛЬЗОВАЛ В ЭТОМ ПРОЕКТЕ:

1. Функции - чтобы не повторять код
2. Глобальные переменные - возможно, не лучший способ, но я пока учусь
3. Циклы while - для проверки ввода игрока
4. Списки - для хранения предметов и выборов
5. Условные операторы if/elif/else - куда же без них
6. Строки с тройными кавычками - для многострочного текста
7. Модули: time, random, os

ЧТО ХОЧУ ДОБАВИТЬ ПОТОМ:
- Сохранение игры
- Больше концовок
- Звуки (но не знаю как в Python)
- Цветной текст (видел где-то про библиотеку colorama)

ЭТО БЫЛО СЛОЖНО, НО ИНТЕРЕСНО!
"""
