import tasks as T

menu = {
        "1. distance": T.one.get_distance(),
        "2. circle": T.two.solve(),
        "3. operations": T.three.solve(),
        "4. favorite_movies": T.four.solve(),
        "5. my_family": T.five.solve(),
        "6. zoo": T.six.solve(),
        "7. songs_list": T.six.solve(),
        "8. secret": T.eight.solve(),
        "9. garden": T.nine.solve(),
        "10. shopping": T.ten.solve(),
        "11. store": T.eleven.solve(),
    }

def main():
    while True:
        print("choose task:")
        for key in menu:
            value = menu[key]
            print(f'{key:<30}')
        choice = int(input("\nchoose task: "))
        if 0<=choice <=len(menu):
            solution = menu[list(menu)[choice - 1]]
        else:
            print("there is no such task")
            break

        print(solution)


if __name__ == "__main__":
    main()