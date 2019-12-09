import argparse
from argument_manager import ArgumentManager


class MainManager:
    def __init__(self):

        self.workflow()

    def workflow(self):
        parser = argparse.ArgumentParser()
        manager = ArgumentManager(parser)
        args = manager.get_arguments()

        print(args.environment)
        print(args.packages)


if __name__ == "__main__":
    mng = MainManager()


