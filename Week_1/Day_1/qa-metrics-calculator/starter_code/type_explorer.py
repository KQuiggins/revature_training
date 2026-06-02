


def main():
    age = 47
    price = 19.99
    name = "Kenneth"
    is_active = True
    result = None

    print(f"Variable Exploration:")
    print(f"{'age':<12} = {age:<10} (type: {type(age).__name__})")
    print(f"{'price':<12} = {price:<10} (type: {type(price).__name__})")
    print(f"{'name':<12} = {name:<10} (type: {type(name).__name__})")
    print(f"{'is_active':<12} = {is_active:<10} (type: {type(is_active).__name__})")
    print(f"{'result':<12} = {str(result):<10} (type: {type(result).__name__})")
    print()
    print()
    
    print(f"Operators Demo:")
    print(f"{'17 // 5':<12} = {str(17 // 5):<10} (floor division)")
    print(f"{'17 / 5':<12} = {str(17 / 5):<10} (true division)")
    print(f'"QA " * 3 = {("QA " * 3)}')
    print(f"{'True + True':<12} = {True + True}")
    print()
    print()
    
    print(f"Precision Gotcha:")
    print(f"0.1 + 0.2 = {0.1 + 0.2} (not exactly 0.3!)")








if __name__ == "__main__":
    main()