def check_parentheses_balance(s):
    stack = []
    parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if stack == [] or parentheses[char] != stack.pop():
                return "Несиметрично"
        # Ігноруємо всі інші символи, які не є розділювачами
        else:
            continue
            
    if stack == []:
        return "Симетрично"
    else:
        return "Несиметрично"

# Приклади використання
print(check_parentheses_balance("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Поверне "Симетрично"
print(check_parentheses_balance("( 23 ( 2 - 3);"))  # Поверне "Несиметрично"
print(check_parentheses_balance("( 11 }"))  # Поверне "Несиметрично"
