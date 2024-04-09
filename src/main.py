import random


def secret_to_int(secret: str) -> int:
    return int.from_bytes(secret.encode(), "big")


def int_to_secret(secret: int) -> str:
    return secret.to_bytes((secret.bit_length() + 7) // 8, "big").decode()


def generate_polynomial(degree: int, secret: int) -> list[int]:
    return [random.randint(0, 100) for _ in range(degree)] + [secret]


def shamir_secret_sharing(total_n: int, threshold: int, secret: int):
    pass


if __name__ == "__main__":
    secret = secret_to_int("hello threshold secret sharing")
    print(generate_polynomial(3, secret))
