from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'

    def ready(self):
        #импортируем файл с описанной функцией-подписщиком на сигнал
        import images.signals
