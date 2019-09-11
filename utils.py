from subprocess import check_call


def call(command):
    print(f"calling: \"{command}\"")
    return check_call(command, shell=True)
