from main.ui.Console import Console


class Main:

    @staticmethod
    def main():
        console = Console()
        console.run()
        print("bye")


main = Main()
main.main()
