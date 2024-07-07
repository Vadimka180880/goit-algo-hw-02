from collections import deque

def is_palindrome(s):
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    s = s.replace(' ', '').lower()
    
    # Створюємо двосторонню чергу
    dq = deque(s)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# Приклади використання
print(is_palindrome("A man a plan a canal Panama"))  # Поверне True
print(is_palindrome("РОТОР"))                        # Поверне True
print(is_palindrome("Hello"))                        # Поверне False
