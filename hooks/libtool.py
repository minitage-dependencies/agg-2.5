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

def ch(options, buildout):
    for i in ['install-sh', 'ltmain.sh', 'configure', 'libtool', 'autogen.sh']:
        os.chmod(
            os.path.join(options['compile-directory'], i),
            0755,)

def lt(options, buildout):
    #relibtoolize project"
    try:
        sed = which('gsed')
    except:
        sed = 'sed'
    sed = sed + " -ie"
    if os.uname()[0] == "Darwin":
        sed = "sed -iE"
    """Custom pre-make hook for building libgd"""
    os.environ['AUTOMAKE'] = "automake --foreign --add-missing --ignore-deps"
    cmd = """cd %s;
            chmod +x autogen.sh
            %s  "s/--ignore-deps//g"  autogen.sh
            %s  "s|aclocal|aclocal -I %s|g"  autogen.sh
              """ % (
                  options['compile-directory'],
                  sed, sed,
                  os.path.join( 
                      buildout['libsdl']['location'], 
                      'share',
                      'aclocal')
              )

    print "Running %s"%cmd
    os.system(cmd)

