import configparser

# Initialize the config parser
config_object = configparser.RawConfigParser()

# Read the configuration file
config_object.read(r'C:\Users\Rafi Ornob\PycharmProjects\PeopleAPI-FrameWork\Configuration\config.ini')


class ReadConfig:
    @staticmethod
    def get_admin_url():
        # Fetch the admin URL from the 'admin login value' section
        adminurl = config_object.get('admin login value', 'adminURL')
        return adminurl

    @staticmethod
    def get_user_name():
        # Fetch the username from the 'admin login value' section
        username = config_object.get('admin login value', 'username')
        return username

    @staticmethod
    def get_password():
        # Fetch the password from the 'admin login value' section
        password = config_object.get('admin login value', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        # Fetch the invalid username from the 'admin login value' section
        invalid_username = config_object.get('admin login value', 'invalid_username')
        return invalid_username
