from modeltranslation.translator import register, TranslationOptions

from .models import New, Tag


@register(New)
class NewTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)
