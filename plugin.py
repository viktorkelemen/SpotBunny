import urllib

def results(fields, original_query):
    q = fields.get('~query')
    url = u"https://our.intern.facebook.com/intern/bunny/?" + urllib.urlencode([('q', q)])
    return {
        "title": "Open spotbunny {}".format(q),
        "run_args": [url]
	}

def run(url):
	import os, pipes
	os.system('open {0}'.format(pipes.quote(url.encode('utf8'))))
