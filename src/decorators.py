import time
import functools

def handle_db_errors(func):
    """Декоратор для централизованной обработки ошибок БД.
    Перехватывает FileNotFoundError, KeyError, ValueError и прочие исключения.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("Ошибка: Файл данных не найден. Возможно, база данных не инициализирована.")
        except KeyError as e:
            print(f"Ошибка: Таблица или столбец {e} не найден.")
        except ValueError as e:
            print(f"Ошибка валидации: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
    return wrapper

def confirm_action(action_name):
    """Фабрика декораторов: запрашивает подтверждение опасной операции.

    Args:
        action_name (str): Название действия для сообщения пользователю.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            answer = input(
                f'Вы уверены, что хотите выполнить "{action_name}"? [y/n]: '
            ).strip().lower()
            if answer != "y":
                print("Операция отменена.")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

def log_time(func):
    """Замеряет время выполнения функции и выводит его в консоль."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = func(*args, **kwargs)
        elapsed = time.monotonic() - start
        print(f"Функция {func.__name__} выполнилась за {elapsed:.3f} секунд")
        return result
    return wrapper

_cache_store = {"cache": {}}

def create_cacher():
    """Возвращает функцию cache_result с общим кэшем.

    Returns:
        callable: cache_result(key, value_func)
    """
    def cache_result(key, value_func):
        cache = _cache_store["cache"]
        if key in cache:
            return cache[key]
        result = value_func()
        cache[key] = result
        return result

    return cache_result

def clear_cache():
    """Очищает общий кэш.

    Так как все кэшеры, созданные через create_cacher,
    используют один и тот же словарь _cache_store["cache"],
    очистка затронет их все.
    """
    _cache_store["cache"].clear()