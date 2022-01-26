import IO


def entry():
    print("KeyRing")

    print("1. New Key")
    print("2. Retrieve Key")
    print("3. Edit Key")
    print("4. Delete Key")
    print("5. Delete all Keys")
    print("6. Retrieve All")

    func = input("Choose between [1 - 6] or exit: ")
    while func not in ['1', '2', '3', '4', '5', '6', 'exit']:
        func = str(input("Choose between [1 - 6] or exit: "))

    call_keyring(func)


def call_keyring(func: object) -> object:
    if func == '1':
        IO.new_service()
    elif func == '2':
        IO.retrieve_service()
    elif func == '3':
        IO.edit_service()
    elif func == '4':
        IO.delete_service()
    elif func == '5':
        IO.delete_all()
    elif func == '6':
        IO.retrieve_all()
    elif func == 'exit':
        IO.keyring_exit()


if __name__ == '__main__':
    entry()
