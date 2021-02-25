from datetime import datetime


def draw_game(k):
    print('+-+-+-+')
    print('|' + k[0] + '|' + k[1] + '|' + k[2] + '|')
    print('+-+-+-+')
    print('|' + k[3] + '|' + k[4] + '|' + k[5] + '|')
    print('+-+-+-+')
    print('|' + k[6] + '|' + k[7] + '|' + k[8] + '|')
    print('+-+-+-+')
    print('=======')


def find_victory_line(k):
    if k[0] == k[1] == k[2] and k[0] != ' ':
        return "верхня лінія"
    if k[3] == k[4] == k[5] and k[3] != ' ':
        return "середня лінія"
    if k[6] == k[7] == k[8] and k[6] != ' ':
        return "нижня лінія"
    if k[0] == k[3] == k[6] and k[0] != ' ':
        return "ліва лінія"
    if k[1] == k[4] == k[7] and k[1] != ' ':
        return "середня вертикальна лінія"
    if k[2] == k[5] == k[8] and k[2] != ' ':
        return "права лінія"
    if k[0] == k[4] == k[8] and k[0] != ' ':
        return "діагональ зліва направо"
    if k[2] == k[4] == k[6] and k[2] != ' ':
        return "діагональ справа наліво"
    return None


kletki = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def player_turn(player, symbol):
    while True:
        number = input("У яку клітинку поставити " + player + "?")
        if number.isdigit():
            number = int(number)
            if number >= 0 and number <= 8:
                if kletki[number] == ' ':
                    break
                else:
                    print("Ця клітинка не порожня")
            else:
                print("Число має бути від 0 до 8")
        else:
            print("Введіть число")
    kletki[number] = symbol
    draw_game(kletki)


def game():
    player_name_f = input("Як тебе звуть?\n")
    player_name_c = input("Як тебе звуть?\n")
    print("Хай переможе сильніший!\nХрестиками ходить " + player_name_f + ", а ноликами - " + player_name_c + ".")
    for i in range(5):
        player_turn("хрестик", "x")
        victory_line = find_victory_line(kletki)
        if victory_line != None:
            print("Гравець хрестиками захопив ", victory_line, "і переміг " + player_name_f)
            with open("winers.txt", mode='a') as file:
                file.write('Переміг ' + player_name_f + str(datetime.now()))
            break

        if ' ' not in kletki:
            print("Не залишилось порожніх клітинок! Нічия!")
            with open("winers.txt", mode='a') as file:
                file.write("Нічия." + str(datetime.now()))
            break

        player_turn("нолик", "o")
        victory_line = find_victory_line(kletki)
        if victory_line != None:
            print("Гравець хрестиками захопив ", victory_line, "і переміг " + player_name_c)
            with open("winers.txt", mode='a') as file:
                file.write('Переміг ' + player_name_c + str(datetime.now()))
            break


def menu():
    a = int(input("Хай! Якщо хочеш зараз зіграти зі своїм другом у хрестики-нолики, пиши 1.\n"
                  "Якщо хочеш подивитися список перемог - 2\n"
                  "Очистити список перемог - 3\n"
                  "Вийти з гри - 4\n"))

    if a == 1:
        draw_game(kletki)
        game()
    elif a == 2:
        print("А ось і список перемог:\n")
        file_w = open("winers.txt")
        read = file_w.read()
        print(read)
        file_w.close()
    elif a == 3:
        open('winers.txt', 'w').close()
        print("Перемоги очищені, дивись:\n")
        file_w = open("winers.txt")
        read = file_w.read()
        print(read)
    else:
        print("Гейм овер!")


menu()
