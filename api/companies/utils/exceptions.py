from rest_framework.exceptions import APIException


class NotFoundEmployee(APIException):
    status_code = 404
    default_detail = "Funcionário não encontrado"
    default_code = "not_found_employee"


class NotFoundGroup(APIException):
    status_code = 404
    default_detail = "O grupo não foi encontrado"
    default_code = "not_found_group"


class RequiredFields(APIException):
    status_code = 400
    default_detail = "Os campos obrigatórios não foram preenchidos"
    default_code = "error_required_fields"


class NotFoundTaskStatus(APIException):
    status_code = 404
    default_detail = "Status da tarefa não foi encontrado"
    default_code = "not_found_task_status"


class NotFoundTask(APIException):
    status_code = 404
    default_detail = "Tarefa não foi encontrada"
    default_code = "not_found_task"
