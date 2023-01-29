import re 


MIN_SIZE = 8
MAX_SIZE = 64

BAN_LIST = []


password  = 'LolaPalooza@3223'

result = {
    'maiuscula': bool(re.search('([A-Z])', password)),
    'miuscula': bool(re.search('([a-z])', password)),
    'numero': bool(re.search('([0-9])', password)),
    'special': bool(re.search('([!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?\]*$])', password)),
    'sequence': not bool(re.search('([0-9]1{3,})', password))
}
print(re.search('([&.\-])', password))
print(result)