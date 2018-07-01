import memcache
mc =memcache.Client(['127.0.0.1:11211'])
mc.set('name','jack')
mc.set('name')
mc.delete('name')
mc.get('name')
mc.set('name','jack',10)