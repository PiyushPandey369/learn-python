'''
    try-except-finally implementation Example
'''
def division(a,b):
    try:
        print(a/b)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("Finally......")

division(2,0)