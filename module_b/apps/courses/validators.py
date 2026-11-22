from django.core.exceptions import ValidationError
from django.db.models.fields.files import ImageFieldFile

def validate_image_size(image: ImageFieldFile) -> None:
  max_size_kb = 2000
  
  if (image.size > max_size_kb * 1024):
    raise ValidationError(f"Максимальный размер картинки - {max_size_kb} Кб")