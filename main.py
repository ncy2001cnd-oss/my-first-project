def greet(name: str) -> str:
    """Return a friendly greeting message."""
    return f"안녕하세요, {name}님! 연습 프로젝트에 오신 것을 환영합니다."


def main() -> None:
    """Run a simple interactive greeting program."""
    print("간단한 인사 프로그램입니다.")
    name = input("이름을 입력해주세요: ").strip()
    if not name:
        name = "친구"
    print(greet(name))


if __name__ == "__main__":
    main()
