"""主程序入口 - Git 协同开发实验示例"""


def greet(name: str) -> str:
    """打招呼"""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """两数相加"""
    return a + b


def main():
    print(greet("World"))
    print(f"1 + 2 = {add(1, 2)}")


if __name__ == "__main__":
    main()
