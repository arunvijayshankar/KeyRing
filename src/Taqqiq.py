import IO


def entry():
    print("Taqqiq: A Credentials Management System")

    print("1. New Key")
    print("2. Retrieve Key")
    print("3. Edit Key")
    print("4. Delete Key")
    print("5. Delete all Keys")
    print("6. Retrieve All")

    func = input("Choose between [1 - 6] or exit: ")
    while func not in ['1', '2', '3', '4', '5', '6', 'exit']:
        func = str(input("Choose between [1 - 6] or exit: "))

    call_Taqqiq(func)


def call_Taqqiq(func):
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
        IO.Taqqiq_exit()
