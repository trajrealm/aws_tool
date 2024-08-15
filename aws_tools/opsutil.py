def gen_dict_extract(key, var):
    for k, v in var.items():
        if k == key:
            yield v
        if isinstance(v, dict):
            for result in gen_dict_extract(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in gen_dict_extract(key, d):
                    yield result


def get_system_status_dict(var):
    for st in gen_dict_extract('SystemStatus', var):
        return st


def get_db_instance_status_dict(var):
    for st in gen_dict_extract('DBInstanceStatus', var):
        return st
