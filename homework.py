class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories: float) -> None:    
    
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; Длительность: '
                f'{self.duration:.3f} ч.; Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; Потрачено ккал: '
                f'{self.calories:.3f}.'
                )


class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65
    M_IN_KM = 1000
    def __init__(self,
                action: int,
                duration: float,
                weight: float,
                ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dist = self.action * self.LEN_STEP / self.M_IN_KM 
# в км
        return dist

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mspeed = self.get_distance() / self.duration 
#dist or self.distance()???
        return mspeed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                            self.duration,
                            self.get_distance(),
                            self.get_mean_speed(),
                            self.get_spent_calories()
                            )


class Running(Training):
    """Тренировка: бег."""

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    min_in_hour = 60

    def __init__(self, 
                action: int,
                duration: float,
                weight: float):

#get_spent_calories()) методы не наследуются
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """ Расчет калорий"""
        cal_Run = ((self.coeff_calorie_1 * self.get_mean_speed() - self.coeff_calorie_2) * self.weight / self.M_IN_KM * self.duration * self.min_in_hour)
        return cal_Run


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    
    coeff_calorie_3 = 0.035
    coeff_calorie_4 = 2
    coeff_calorie_5 = 0.029
    MIN_IN_HOUR = 60

    def __init__(self, 
                action: int,
                duration: float,
                weight: float,
                height: float):
#get_distance,get_mean_speed,show_training_info,get_spent_calories):
        self.height = height 
        super().__init__(action, duration, weight)
#,get_distance(),get_mean_speed(),show_training_info())

    def get_spent_calories(self) -> float:
        """ Расчет калорий"""
        cal_walk = (self. coeff_calorie_3 * self.weight + (self.get_mean_speed()**self. coeff_calorie_4 // self.height) * self. coeff_calorie_5 * self.weight) * self.duration*self.MIN_IN_HOUR 
        return cal_walk


class Swimming(Training):
    """Тренировка: плавание."""
    coeff_calorie_6 = 1.1
    coeff_calorie_7 = 2
    LEN_STEP = 1.38
    M_IN_KM = 1000

    def __init__(self,
                action:int,
                duration:float,
                weight:float,
                length_pool:float,
                count_pool:int):
        self.length_pool = length_pool
        self.count_pool = count_pool
#get_distance(),get_mean_speed(),show_training_info(),get_spent_calories()):
        super().__init__(action, duration, weight)
#get_distance(),get_mean_speed(),show_training_info())

    def get_mean_speed(self) -> float:
        mswim = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return mswim

    def get_spent_calories(self) -> float:
        cal_Swim = (self.get_mean_speed() + self.coeff_calorie_6) * self.coeff_calorie_7 * self.weight 
        return cal_Swim

    def get_distance(self) -> float:
        sw_distance = self.action * self.LEN_STEP / self.M_IN_KM
        return sw_distance

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    training_class = training_type[workout_type]
    training_obj = training_class(*data)
    return training_obj



def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)