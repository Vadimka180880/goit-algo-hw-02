import queue
import threading
import time
import random

# Створюємо чергу заявок
service_queue = queue.Queue()

# Унікальний номер заявки
request_id = 0
total_requests = 30

def generate_request():
    global request_id
    for _ in range(total_requests):
        request_id += 1
        request_data = f"Заявка {request_id}"
        service_queue.put(request_data)
        print(f"Згенеровано: {request_data}")
        # Імітуємо випадковий час між генерацією нових заявок
        time.sleep(random.uniform(0.5, 2.0))

def process_request():
    processed_count = 0
    while processed_count < total_requests:
        if not service_queue.empty():
            current_request = service_queue.get()
            print(f"Обробляється: {current_request}")
            # Імітація обробки заявки (затримка) 
            time.sleep(random.uniform(0.5, 2.0))
            print(f"Оброблено: {current_request}")
            service_queue.task_done()
            processed_count += 1
        else:
            time.sleep(0.5)  # Очікуємо появу нових заявок

def main():
    # Запускаємо потік для генерації заявок
    generating_thread = threading.Thread(target=generate_request)
    generating_thread.start()

    # Запускаємо обробку заявок
    processing_thread = threading.Thread(target=process_request)
    processing_thread.start()

    # Чекаємо завершення обох потоків
    generating_thread.join()
    processing_thread.join()

    print("Усі заявки оброблені.")

if __name__ == "__main__":
    main()