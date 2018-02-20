import responses as res

response_mapper = {'/': res.resp_root,
                   '/login': res.resp_auth,
                   '/image': res.resp_image,
                   '/register': res.resp_register}


def get_response(path, environ):
    return response_mapper.get(path, res.resp_not_found)(environ)


def application(environ, start_response):
    # uwsgi --http :9090 --wsgi-file server.py
    path = environ['PATH_INFO']

    response_code, response_mime, response = get_response(path, environ)
    start_response(response_code, [response_mime])
    return response
