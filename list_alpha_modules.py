import pkgutil, alphagenome, sys
for _, modname, ispkg in pkgutil.iter_modules(alphagenome.__path__):
    print('submodule:', modname)
