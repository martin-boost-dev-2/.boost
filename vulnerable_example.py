"""Example file with vulnerabilities that trigger custom Semgrep rules."""

import subprocess


def run_user_code(user_input: str) -> None:
    # Triggers: no-eval
    result = eval(user_input)
    print(result)


def connect_to_database() -> None:
    # Triggers: no-hardcoded-password
    password = "super_secret_123"
    print(f"Connecting with {password}")


def run_command(cmd: str) -> None:
    # Triggers: no-shell-true
    subprocess.run(cmd, shell=True)
    subprocess.call(cmd, shell=True)
