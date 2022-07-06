try:
    import pkg_resources
    version = pkg_resources.require("cabot")[0].version
except (Exception, ImportError) as e:
    version = 'unknown'
