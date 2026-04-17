import pkgutil, importlib, sys, json
import alphagenome
print('alphagenome path:', alphagenome.__path__)
mods = []
for finder, name, ispkg in pkgutil.iter_modules(alphagenome.__path__):
    mods.append(name)
print('submodules:', mods)
for name in mods:
    try:
        mod = importlib.import_module(f'alphagenome.{name}')
        print('module', name, 'has attrs', [a for a in dir(mod) if not a.startswith('_')][:5])
    except Exception as e:
        print('error importing', name, e)
