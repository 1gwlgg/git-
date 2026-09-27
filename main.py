"""主程序入口 - Git 协同开发实验示例"""


def greet(name: str) -> str:
    """打招呼"""
    return f"Hello, {name}!"


def add(a: int | float, b: int | float) -> int | float:
    """两数相加（master 版本：支持浮点数）"""
    return a + b


def main():
    print(greet("World"))
    print(f"1 + 2 = {add(1, 2)}")
    print(f"0.1 + 0.2 = {add(0.1, 0.2)}")


if __name__ == "__main__":
    main()
