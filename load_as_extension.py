from stevedore import extension


mgr = extension.ExtensionManager(
    namespace='stevedore_testplugins.database',
    invoke_on_load=True,
    invoke_args=(),
)

def func1(ext, data):
    return (ext.name, ext.obj.format(data))

results = mgr.map(func1, "")

for ext , result in results:
    print(f"return value from extension ({ext}) is ({result})")



'''
from pkg_resources import iter_entry_points

_plugins = {}

def load_register_plugins(group='general'):

    group=f"stevedore_testplugins.{group}"

    if group not in _plugins:
        _plugins[group] = []

    end_points = iter_entry_points(group=group)
    
    for end_point in end_points:
        if end_point.name in _plugins[group]:
            raise ValueError(f"The plugin {end_point.name} already registered!")
        _plugins[group].append(end_point)

    print(f"\nEntry points of group {group} are:")
    for plugin in _plugins[group]:
        function = plugin.load()
        function()


load_register_plugins(group = "database")
'''
