def movie_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.name, filename)