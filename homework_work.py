class InfoMessage:
    """Информационное сообщение о тренировке."""
    #show_training_info(Training)
    training_type: str
    duration: float 
    distance: float
    speed: float
    calories: float
    text: str=(f'Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.')

    def get_message(self):
        
        return self.text


class Training:
    """Базовый класс тренировки."""
    LEN_STEP=0.65 # длина шага
    LEN_PADDLE= 1.38 # длина гребка
    M_IN_KM=1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration=duration
        self.weight=weight

        

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        LEN_STEP=0.65
        M_IN_KM=1000
        self.distance = self.action * LEN_STEP / M_IN_KM 
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        self.mean_speed = self.distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    def __init__(action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)

    def calories(self) -> float: # переопределяем калории
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        M_IN_KM=1000
        self.calorie_run=(coeff_calorie_1 * self.mean_speed - coeff_calorie_2) * self.weight / M_IN_KM * self.duration
    pass




def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict_training = {
                'SWM': Swimming,
                'RUN': Running,
                'WLK': SportsWalking
            }
    return dict_training[workout_type](*data)
   
    


def main(training: Training) -> None:
    """Главная функция."""
    info=training.show_training_info()
    print(info.get_message())
    


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),   # paddle, time(h), weigth, pool_lenth< pool_count)
        ('RUN', [15000, 1, 75]),         # steps, time, weight
        ('WLK', [9000, 1, 75, 180]),     # steps, time, weight, height
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

