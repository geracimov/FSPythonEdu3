from urllib.parse import parse_qs
import templatehelper as th
import users.userhelper as uh


def get_params(environ):
    query = environ['QUERY_STRING']
    return parse_qs(query)


def resp_not_found(environ):
    return '404', ('Content-Type', 'text/html'), b'no_data_found'


def resp_root(environ):
    return '200', ('Content-Type', 'text/plain'), b'main page'


def resp_register(environ):
    str_template = th.get_register_page()

    return '200', ('Content-Type', 'text/html'), bytes(str_template, encoding='utf-8')


def resp_auth(environ):
    """todo здесь наверно нужно сделать что то вроде использования сессий,
    если уже прошел аутентификацию, то иметь в контексте имя пользователя например"""
    req_method = environ['REQUEST_METHOD']
    if req_method == 'GET':
        str_template = th.get_auth_page()
    elif req_method == 'POST':
        params = parse_qs(environ['wsgi.input'].read().decode('utf-8'))
        auth = uh.auth_user(''.join(params['uname']), ''.join(params['psw']))
        str_template = th.get_auth_page(auth)
    else:
        return resp_not_found(None)
    return '200', ('Content-Type', 'text/html'), bytes(str_template, encoding='utf-8')


def resp_image(environ):
    params = get_params(environ)
    try:
        filename = ''.join(params.get('filename', ''))
        relative_name = './images/' + filename
        with open(relative_name, 'rb') as file:
            return '200', ('Content-Type', 'image/jpeg'), file.read()
    except IndexError:
        return resp_not_found(params)
    except IOError:
        return resp_not_found(params)
