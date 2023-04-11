import typing as tp

import django.db.models
import django.utils.html
import sorl.thumbnail


class ImageModel(django.db.models.Model):
    image = django.db.models.ImageField(
        'image',
        upload_to='pictures/',
        help_text='Will be rendered at 300px',
    )

    class Meta:
        abstract = True

    def get_image_300x300(self) -> tp.Any:
        return sorl.thumbnail.get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=51,
        )

    def image_tmb(self) -> tp.AnyStr:
        if self.image:
            return django.utils.html.mark_safe(
                f'<img src="{self.get_image_300x300().url}">',
            )
        return 'No picture'

    image_tmb.short_description = 'Image'
