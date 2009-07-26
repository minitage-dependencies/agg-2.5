import os, sys

def which(program, environ=None, key = 'PATH', split = ':'):
    if not environ:
        environ = os.environ
    PATH=environ.get(key, '').split(split)
    fp = None
    if '/' in program:
        fp = os.path.abspath(program)
    if not fp:
        for entry in PATH:
            fp = os.path.abspath(os.path.join(entry, program))
            if os.path.exists(fp):
                break
    if os.path.exists(fp):
        return fp
    raise IOError('Program not fond: %s in %s ' % (program, PATH))

def h(o, b):
    try:
        os.environ['GNUMAKE'] = which('gmake')
    except:
        pass

sed =  'sed'
try:
    sed = which('gsed')
except:
    sed = 'sed'

def lt(options, buildout):
    """Custom pre-make hook for building libgd"""
    #relibtoolize project"
    os.system("""cd %s;
            chmod +x autogen.sh
            %s -e "s/--ignore-deps//g" -i autogen.sh
            %s -e "s|aclocal|aclocal -I %s|g" -i autogen.sh
              """ % (
                  options['compile-directory'],
                  sed, sed,
                  os.path.join( 
                      buildout['libsdl']['location'], 
                      'share',
                      'aclocal')
              )
             )

