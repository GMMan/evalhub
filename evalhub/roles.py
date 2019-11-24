from rolepermissions.roles import AbstractUserRole


class Evaluator(AbstractUserRole):
    available_permissions = {}


class DaycareUser(AbstractUserRole):
    available_permissions = {}
