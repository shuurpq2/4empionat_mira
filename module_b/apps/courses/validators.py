from django.core.exceptions import ValidationError
from django.db.models.fields.files import ImageFieldFile

def validate_image_size(image: ImageFieldFile) -> None:
  max_size_kb = 2000

  if (image.size > max_size_kb * 1024):
    raise ValidationError(f"Максимальный размер картинки - {max_size_kb} Кб")

def validate_supertube_link(link: str) -> None:
  prefix = "https://super-tube.cc/video/v"

  if not (link.startswith(prefix) and link.removeprefix(prefix).isdigit()):
    raise ValidationError(f"Видеоссылка не валидна")