from GUI.login_window import LoginWindow
from Database.database import init_pool

if __name__ == "__main__":
    try:
        init_pool()
        print("Baza de date pornita!")
    except ConnectionError as e:
        print("Conexiunea nu se realizeaza")
        exit(1)

    app = LoginWindow()
    app.run()