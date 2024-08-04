class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.next_movie_id = 1
        self.next_user_id = 1
        self.next_ticket_id = 1

    def addMovie(self, movieName):
        movie_id = self.next_movie_id
        self.movies[movie_id] = movieName
        self.next_movie_id += 1
        return movie_id

    def showAllMovies(self):
        return self.movies

    def addUser(self, userName):
        user_id = self.next_user_id
        self.users[user_id] = userName
        self.next_user_id += 1
        return user_id

    def buyTicket(self, userId, movieId):
        if userId in self.users and movieId in self.movies:
            ticket_id = self.next_ticket_id
            self.tickets[ticket_id] = (userId, movieId)
            self.next_ticket_id += 1
            return ticket_id
        return None

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True
        return False


def main():
    cinemaSystem = CinemaTicketSystem()

    while True:
        print("\nЗдравствуйте, у вас есть следующие доступные функции:")
        print("1. Добавить новый фильм")
        print("2. Показать все доступные фильмы")
        print("3. Добавить нового пользователя")
        print("4. Купить билет")
        print("5. Отменить покупку билета")
        print("6. Выйти")

        choice = input("Введите номер функции: ")

        if choice == '1':
            movieName = input("Введите название фильма: ")
            movie_id = cinemaSystem.addMovie(movieName)
            print(f"Фильм '{movieName}' добавлен с идентификатором {movie_id}.")

        elif choice == '2':
            movies = cinemaSystem.showAllMovies()
            if movies:
                print("Доступные фильмы:")
                for movie_id, movieName in movies.items():
                    print(f"{movie_id}: {movieName}")
            else:
                print("Нет доступных фильмов.")

        elif choice == '3':
            userName = input("Введите имя пользователя: ")
            user_id = cinemaSystem.addUser(userName)
            print(f"Пользователь '{userName}' добавлен с идентификатором {user_id}.")

        elif choice == '4':
            try:
                userId = int(input("Введите идентификатор пользователя: "))
                movieId = int(input("Введите идентификатор фильма: "))
                ticket_id = cinemaSystem.buyTicket(userId, movieId)
                if ticket_id:
                    print(f"Билет куплен с идентификатором {ticket_id}.")
                else:
                    print("Не удалось купить билет. Проверьте идентификаторы пользователя и фильма.")
            except ValueError:
                print("Ошибка ввода. Пожалуйста, введите числовые идентификаторы.")

        elif choice == '5':
            try:
                ticketId = int(input("Введите идентификатор билета: "))
                if cinemaSystem.cancelTicket(ticketId):
                    print("Билет успешно отменен.")
                else:
                    print("Билет с таким идентификатором не найден.")
            except ValueError:
                print("Ошибка ввода. Пожалуйста, введите числовой идентификатор билета.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите номер функции от 1 до 6.")


if __name__ == "__main__":
    main()
