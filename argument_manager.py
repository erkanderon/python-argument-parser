
class ArgumentManager:

    def __init__(self, parser):
        self.parser = parser
        self.parser.add_argument("--environment",
                                 help="Deployment environment",
                                 choices=['dev', 'qa', 'stg', 'prod'])
        self.parser.add_argument("--packages",
                                 help="will be deployed wars",
                                 nargs="+")

    def get_arguments(self):
        args = self.parser.parse_args()
        return args