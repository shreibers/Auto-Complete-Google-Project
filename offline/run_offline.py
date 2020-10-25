from offline.init_data import Init


def main():
    init = Init()

    print("loading the files and preparing the system...")
    init.init_data()


if __name__ == '__main__':
    main()
