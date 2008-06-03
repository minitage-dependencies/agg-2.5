import os
def lt(options, buildout):
    """Custom pre-make hook for building libgd"""
    import pdb;pdb.set_trace()  ## Breakpoint ##
    #relibtoolize project"
    os.system("""cd %s;
            chmod +x autogen.sh
              """ % (
                  options['compile-directory']
              )
             )

