from app.service import UserService


def main() -> None:
    service = UserService()
    user = service.create_user("alice", 30)
    print(service.describe_user(user))


if __name__ == "__main__":
    main()