from flask_lib import FlaskLib


backend = FlaskLib()

@backend.api('/bhens_sum_of_sonu')
def A(d):
    print(d)
    return 'Mera Nam Sonu Hai'

@backend.api('/sum2')
def A(d):
    print(d)
    return 'PPP'

@backend.api('/api/sum2')
def sum2(d):
    print(d)
    return d['x'] + d['y']

backend.run(port=5502)
