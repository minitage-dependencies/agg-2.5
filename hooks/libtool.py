import os
def lt(options, buildout):
    """Custom pre-make hook for building libgd"""
    #relibtoolize project"
    os.system("""cd %s;
            chmod +x autogen.sh
            sed -e "s/--ignore-deps//g" -i autogen.sh
            sed -e "s|aclocal|aclocal -I %s|g" -i autogen.sh
              """ % (
                  options['compile-directory'],
                  os.path.join( 
                      buildout['libsdl']['location'], 
                      'share',
                      'aclocal')
              )
             )

