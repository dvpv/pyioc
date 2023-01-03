from pyioc import YAMLContext


def main():
    context = YAMLContext("config.yaml")
    lister = context.get_nut("MovieLister")
    lister.list_movies()


if __name__ == "__main__":
    main()
