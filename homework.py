class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type: str = training_type
        self.duration: float = duration
        self.distance: float = distance
        self.speed: float = speed
        self.calories: float = calories

    def get_message(self) -> str:
        text: str = (f'Тип тренировки: {self.training_type}; '
                     f'Длительность: {self.duration:.3f} ч.; '
                     f'Дистанция: {self.distance:.3f} км; '
                     f'Ср. скорость: {self.speed:.3f} км/ч; '
                     f'Потрачено ккал: {self.calories:.3f}.')
        return text


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65  # длина шага
    M_IN_KM: float = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action: float = action
        self.duration: float = duration
        self.weight: float = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dist = self.action * self.LEN_STEP / self.M_IN_KM
        return dist

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        avg_speed = self.get_distance() / self.duration
        return avg_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        training_info = InfoMessage(type(self).__name__,
                                    self.duration,
                                    self.get_distance(),
                                    self.get_mean_speed(),
                                    self.get_spent_calories())
        return training_info


class Running(Training):
    """Тренировка: бег."""

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:  # переопределяем калории
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        calorie = ((coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2)
                   * self.weight / self.M_IN_KM * self.duration * 60)
        return calorie


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height: float = height

    def get_spent_calories(self) -> float:  # переопределяем калории
        coeff_calorie_1: float = 0.035
        coeff_calorie_2: float = 0.029
        calorie_walk = (coeff_calorie_1 * self.weight
                        + (self.get_mean_speed()**2 // self.height)
                        * coeff_calorie_2 * self.weight) * (self.duration * 60)
        return calorie_walk


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38  # длина гребка

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool: float = length_pool
        self.count_pool: float = count_pool

    def get_mean_speed(self) -> float:  # переопределяем сред скорость плавания
        avg_speed = (self.length_pool * self.count_pool
                     / self.M_IN_KM / self.duration)
        return avg_speed

    def get_spent_calories(self) -> float:  # переопределяем калории
        coeff_calorie_1: float = 1.1
        coeff_calorie_2: float = 2
        calorie_swm = ((self.get_mean_speed() + coeff_calorie_1)
                       * coeff_calorie_2 * self.weight)
        return calorie_swm

    def get_distance(self) -> float:  # переопределяем гребок
        """Получить дистанцию в км."""
        dist = self.action * self.LEN_STEP / self.M_IN_KM
        return dist


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict = {'SWM': Swimming,
            'RUN': Running,
            'WLK': SportsWalking
            }
    return dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),  # action, dur, weigth, pool_l, pool_c)
        ('RUN', [15000, 1, 75]),        # action, dur, weight
        ('WLK', [9000, 1, 75, 180]),    # action, dur, weight, height
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
