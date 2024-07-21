from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Movie(models.Model):
    _name = 'movies.movie'
    _rec_name = 'title'

    title = fields.Char(required=True, string="Título")
    punctuation = fields.Float(required=True, string="Puntuación")
    year = fields.Date(required=True, string="Año de publicación")
    director = fields.Integer(string="Director")
    genre = fields.Selection([
        ("accion", "Acción"),
        ("aventura", "Aventura"),
        ("ciencia-ficcion", "Ciencia ficción"),
        ("comedia", "Comedia"),
        ("drama", "Drama"),
        ("terror", "Terror"),
        ("suspenso", "Suspenso"),
        ("fantasia", "Fantasía"),
        ("animacion", "Animación"),
        ("documental", "Documental"),
        ("musical", "Musical"),
        ("romance", "Romance"),
        ("crimen", "Crimen"),
        ("misterio", "Misterio"),
        ("western", "Western"),
        ("belica", "Bélica"),
        ("biografica", "Biográfica"),
        ("historica", "Histórica"),
        ("deportiva", "Deportiva"),
        ("familiar", "Familiar")],
        required=True, string="Género")
    duration = fields.Char(string="Duración")
    review = fields.Text(string="Reseña")
    language = fields.Char(string="Lenguaje original")
    income = fields.Float(string="Recaudación")

    @api.constrains('punctuation')
    def valid_punctuation(self):
        for record in self:
            if not(0 <= record.punctuation <= 5.0):
                raise ValidationError("La puntuación debe ser de 0.0 a 5.0.")
            
    @api.constrains('duration')
    def valid_duration(self):
        for record in self:
            if record.duration:
                parts = record.duration.split(':')
                print(parts)
                if len(parts) != 3:
                    raise ValidationError("La duración debe estar en formato HH:MM:SS.")
                try:
                    hours = int(parts[0])
                    minutes = int(parts[1])
                    seconds = int(parts[2])
                    if (hours < 0) or not(0 < minutes < 60) or not(0 < seconds < 60):
                        raise ValidationError("Formato incorrecto de horas, minutos y segundos.")
                except ValidationError as exc:
                    raise ValidationError("La duración debe estar en formato numérico HH:MM:SS.") from exc
